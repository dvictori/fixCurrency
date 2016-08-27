#!/usr/bin/env python
# -*- coding: utf-8 -*-

# programa para arrumar moeda nos arquivos OFX do cartão de crédito
# gerado pelo site do BB
# GnuCash não faz a conversão de moedas ao importar dados do cartão
# traz dolar como se fosse real

import argparse, re

def achaNumero(texto):
    '''Encontra o valor numérico na linha do OFX
    não estou querendo usar RE então uso substituicao
    e depois tento ler como valor float'''
    partes = texto.replace('>',';').replace('<',';').split(';')
    for p in partes:
        try:
            v = float(p)
            return v
        except ValueError:
            pass

def arrumaMoeda(linhas):
    '''Recebe o arquivo OFX, como uma lista, obtido pelo readlines
    encontra as linhas que contem o campo Currency, com a taxa de cambio
    multiplica o campo do valor pela taxa
    retorna a lista com as linhas alteradas'''
    
    # encontrando as linhas com transações em outra moeda
    # valor da transacao está 3 linhas antes
    p = re.compile('.*CURRENCY.*')
    taxas = [i for i,x in enumerate(linhas) if p.match(x)]
    
    for l in taxas:
        t = achaNumero(linhas[l])
        v = achaNumero(linhas[l-3])
        linhas[l] = '<CURRENCY><CURRATE>1.0000</CURRATE><CURSYM>USD</CURSYM></CURRENCY>\n'
        linhas[l-3] = '<TRNAMT>{:.2f}</TRNAMT>\n'.format(t*v)
    
    return linhas
    
def escreveSaida(linhas, saida):
    '''saida: nome do arquivo'''
    f = open(saida, 'w')
    [f.write(l) for l in linhas]
    f.close()

def main():
    parser = argparse.ArgumentParser(description='Corrige moeda no arquivo OFX do cartão do BB')
    parser.add_argument('entrada', help='Arquivo a ser convertido')
    parser.add_argument('saida', help='Nome do arquivo de saída')
    args = parser.parse_args()

    infile = open(args.entrada, 'r')
    linhas = infile.readlines()
    infile.close()
    
    convertido = arrumaMoeda(linhas)
    escreveSaida(convertido, args.saida)

if __name__ == '__main__':
    main()
    
