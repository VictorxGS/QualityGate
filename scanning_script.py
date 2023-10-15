# scanning_script: Esse script foi criado com o objetivo de executar varredura em arquivos de 
# configurações de aplicações em busca de detecção de palavras-chaves proibidas em seu conteudo.
# Um conjunto dessas palavras-chaves proibidas são denominados como black-list. 
# Durante a execução da varredura podem ocorrer detecção de falsos-positivos, ou seja, detecção 
# de palavras semelhantes a uma palavras da black-list que não compromete a varredura.
# Partindo dessa hipótese essas palavras poderão ser adicionada na white-list, uma lista de 
# palavras que podem ter by-pass (Permissão para passar pelo varredura sem ser detectada como um falso-positivo)

# Comando de execução do arquivo: python .\scanning_script.py .\config.json 'palavra0' 'palavra1' --white_list 'palavra 2' 'palavra 3' 

# TO DO:
# Testar filtragem da funcao separate (problema de falta de cobertura)

import argparse
from colorama import init, Fore

def scan_white_list(white_list, linha):
    if(white_list is not None):
        for word in white_list:
            if word in linha:
                linha = linha.replace(word, "")
    return linha

def scan_black_list(black_list, linha, i):
    if(black_list is not None):
        for word in black_list:
            if word in linha:
                founds.append(f'\'{word}\' encontrada - linha {i}')
                print(Fore.RED + f'ALERT: \'{word}\' encontrada - linha {i}' + Fore.RESET)

def separate_words(linha): #Testar essa funcao
    indesejados = ['\n', '\t', ',', '"', ' ']
    for item in indesejados:
        linha = linha.replace(item, '')
    return linha.split(':')

def resume(founds):
    print('########## SCAN RESUME ##########') # Imprimir no canal de erro
    for found in founds:
        print(f'\033[91m>>>  {found}\033[0m')


white_list = []
black_list = []
founds = []

parser = argparse.ArgumentParser(description='Parser para criar argumentos recebidos pela cli.')

parser.add_argument('caminho_do_arquivo', type=str, help='Path do arquivo a ser processado')
parser.add_argument('-wl', '--white_list', type=str, nargs='+', required=False, help='Lista de palavras a receberem Bypass')
parser.add_argument('-bl', '--black_list', type=str, nargs='+', required=True, help='Lista de palavras indesejadas a serem detectadas')

args = parser.parse_args()

caminho_arquivo = args.caminho_do_arquivo
white_list = args.white_list
black_list = args.black_list

print(white_list) # Teste
print(black_list) # Teste

try:
    with open(caminho_arquivo, 'r') as arquivo:
        for i, linha in enumerate (arquivo, 1):
        
            print(f' {i}: {linha}') 
            linha = scan_white_list(white_list, linha)
            scan_black_list(black_list, linha, i)

except FileNotFoundError:
    print(f'O arquivo "{caminho_arquivo}" não foi encontrado.')
except Exception as e:
    print(f'Ocorreu um erro ao acessar o arquivo: {e}')

resume(founds)
