# fixCurrency

Programa para corrigir problema de moedas estrangeiras na importação do GNUCASH.
Funciona para o extrato do cartão de crédito do Banco do Brasil, exportado no formato _OFX_.
Não testei com outros arquivos.

Como usar:

'''fix_curency.py <arquivo ofx de entrada> <arquivo ofx de saída>'''

Programa irá ler o arquivo OFX e identificar as linhas com informação de taxa de câmbio _<CURRATE>_. Em seguida irá multiplicar o valor da transação _<TRNAMT>_ pela taxa de câmbio. Por fim, reescreve o arquivo OFX, com o valor da transação convertido em Real e o valor da taxa de câmbio igual a 1.

Sugestões e melhorias são bem vindas
