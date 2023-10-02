# scanning_script: Esse script foi criado com o objetivo de executar varredura em arquivos de 
# configurações de aplicações em busca de detecção de palavras-chaves proibidas em seu conteudo.
# Um conjunto dessas palavras-chaves proibidas são denominados como black-list. 
# Durante a execução da varredura podem ocorrer detecção de falsos-positivos, ou seja, detecção 
# de palavras semelhantes a uma palavras da black-list que não compromete a varredura.
# Partindo dessa hipótese essas palavras poderão ser adicionada na white-list, uma lista de 
# palavras que podem ter by-pass (Permissão para passar pelo varredura sem ser detectada como um falso-positivo)

# Comando de execução do arquivo: python .\scanning_script.py .\config.json 'palavra0' 'palavra1' --white_list 'palavra 2' 'palavra 3' 

import argparse

def scan_white_list(white_list, linha):
    if(len(white_list) != 0): # tratar problema do len
        for word in white_list:
            if word in linha:
                linha = linha.replace(word, "")
    return linha


parser = argparse.ArgumentParser(description='Parser para criar argumentos recebidos pela cli.')

parser.add_argument('caminho_do_arquivo', type=str, help='Caminho do arquivo a ser processado')
parser.add_argument('--white_list', type=str, nargs='+', help='Palavras a receberem Bypass')
parser.add_argument('--black_list', type=str, nargs='+', help='Palavras proibidas a serem detectadas')

args = parser.parse_args()

caminho_arquivo = args.caminho_do_arquivo
white_list = args.white_list
black_list = args.black_list

found=[]

print(f'BLACK-LIST: {black_list}')
print(f'WHITE-LIST: {white_list}')

try:
    with open(caminho_arquivo, 'r') as arquivo:
        for i, linha in enumerate (arquivo, 1):

            print(f' {i}: {linha}', end='')

            linha = scan_white_list(white_list, linha)

            if(len(black_list) != 0):
                for w in black_list:
                    if w in linha:
                        print(f'key: {w} encontrada na linha {i}')
       
except FileNotFoundError:
    print(f'O arquivo "{caminho_arquivo}" não foi encontrado.')
except Exception as e:
    print(f"Ocorreu um erro ao acessar o arquivo: {e}")

print(f'Caminho do arquivo: {caminho_arquivo}')
