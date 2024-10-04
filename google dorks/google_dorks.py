import urllib.parse
import time
from termcolor import colored
from colorama import init, Fore

# Inicializa o colorama
init(autoreset=True)

def print_ascii_art():
    print(Fore.BLUE + '....................................')
    print(Fore.CYAN + "  ______ _            _            ")
    print(Fore.CYAN + " |  ____| |          | |           ")
    print(Fore.YELLOW + " | |__  | | ___   ___| | ___  ___   ")
    print(Fore.YELLOW + " |  __| | |/ _ \ / __| |/ _ \/ __|  ")
    print(Fore.RED + " | |    | | (_) | (__| |  __/\__ \  ")
    print(Fore.RED + " |_|    |_|\___/ \___|_|\___||___/  ")
    print()
    print(Fore.GREEN + "\nCanal Lima")
    print(Fore.MAGENTA + "\GOOGLE DORKS V1.0 TERMUX")
    print(Fore.BLUE + '...............................')
def main():
    print_ascii_art()

if __name__ == "__main__":
    main()
print(Fore.RED + '\nCanal Lima Sim, escrever ai')
def print_ascii_art():
    art = r"""
    Criador Samuel Rodrigues Silva Lima
     / ___| ___ _ __ _ __ _| |_ ___ _ __  
    | |  _ / _ \ '__| '__| | __/ _ \ '_ \ 
    | |_| |  __/ |  | |  | | ||  __/ | | |
     \____|\___|_|  |_|  |_|\__\___|_| |_|
    """
    
    # Exibindo a arte em verde
    print(colored(art, 'green'))
    print(colored("       Bot: Google Dorks", 'yellow'))

def main():
    print_ascii_art()
    print(colored("\nCarregando Google Dorks...", "yellow"))

if __name__ == "__main__":
    main()
    
    
def loading_animation():
    print(colored("\nCarregando Google Dorks...", 'red'), end="", flush=True)
    for _ in range(3):  # Número de "ciclos" de carregamento
        time.sleep(1)  # Espera 1 segundo
        print(".", end="", flush=True)
    print(colored("\n Pronto!", 'blue'))

def main():
    loading_animation()
    # Aqui você pode adicionar a lógica do seu script que utiliza Google Dorks
    print(colored("\nExecutando busca de Google Dorks...", 'yellow'))

if __name__ == "__main__":
    main()

def gerar_google_dork(termo_de_busca, categoria=None, estado=None, data_nascimento=None, palavras_remover=None, nome_mae=None, tipo_arquivo=None):
    dork = f'"{termo_de_busca}"'
    
    # Adiciona categoria se especificada
    if categoria:
        if categoria.lower() == "emails":
            dork = f'intext:"@{termo_de_busca}"'
        elif categoria.lower() == "senhas":
            dork = f'intitle:"index of" "{termo_de_busca}"'
        elif categoria.lower() == "cpf":
            dork = f'intext:"{termo_de_busca}" OR cpf OR "cadastro"'
        elif categoria.lower() == "rg":
            dork = f'intext:"{termo_de_busca}" OR rg OR "registro"'
        elif categoria.lower() == "banco de dados":
            dork = f'intext:"{termo_de_busca}" OR "banco de dados" OR "database"'
        elif categoria.lower() == "cartão de crédito":
            dork = f'intext:"{termo_de_busca}" OR "credit card" OR "cartão"'
        elif categoria.lower() == "arquivos de configuração":
            dork = f'intitle:"index of" AND ("{termo_de_busca}" OR "*.conf" OR "*.ini")'
        elif categoria.lower() == "diretórios expostos":
            dork = f'intitle:"index of" "{termo_de_busca}"'
        elif categoria.lower() == "informações sensíveis":
            dork = f'intext:"{termo_de_busca}" OR "senha" OR "senha123" OR "password"'
    
    if estado:
        dork += f' OR "{estado}"'
    
    if data_nascimento:
        dork += f' OR "{data_nascimento}"'

    if palavras_remover:
        dork += f' -{palavras_remover}'

    if nome_mae:
        dork += f' +"{nome_mae}"'

    if tipo_arquivo:
        dork += f' filetype:{tipo_arquivo}'
    
    return dork

def main():
    print(colored("BÉM VINDO AO GOOGLE DORKS V1.0 CANAL LIMA!", 'green'))
    print(colored("CATEREGORIAS DISPONIVEIS: emais, senhas, cpf, rg, banco de dados, cartão de crédito, arquivos de configuração, diretórios expostos, informações sensíveis.", 'red'))
    
    termo_de_busca = input(colored("\nDigite o que você deseja encontrar: ", 'green'))
    
    categoria = input(colored("\nEscolha uma categoria (deixe em branco para não usar): ",'green'))
    
    estado = input(colored("\nVocê deseja adicionar um estado (ex: Alagoas, ou pressione Enter para ignorar): ", 'green'))
    if estado.strip() == "":
        estado = None

    data_nascimento = input(colored("\nVocê deseja adicionar uma data de nascimento? (digite 'dd/mm/aaaa', ou pressione Enter para ignorar): ", 'green'))
    if data_nascimento.strip() == "":
        data_nascimento = None

    palavras_remover = input(colored("\nVocê deseja remover alguma palavra? (digite a palavra, ou pressione Enter para ignorar): ", 'green'))
    if palavras_remover.strip() == "":
        palavras_remover = None

    nome_mae = input(colored("\nVocê deseja adicionar o nome da mãe? (digite o nome, ou pressione Enter para ignorar): ",'green'))
    if nome_mae.strip() == "":
        nome_mae = None

    tipo_arquivo = input(colored("\nVocê deseja filtrar por tipo de arquivo? (digite 'pdf', 'docx', 'xlsx', etc., ou pressione Enter para ignorar): ", 'green'))
    if tipo_arquivo.strip() == "":
        tipo_arquivo = None

    dork = gerar_google_dork(termo_de_busca, categoria, estado, data_nascimento, palavras_remover, nome_mae, tipo_arquivo)
    
    # Codificando a URL
    dork_encoded = urllib.parse.quote(dork)
    
    print(Fore.RED +"\nAqui está o seu Google Dork gerado:")
    print(dork)
    print(Fore.BLUE +"\nVocê pode usá-lo aqui: https://www.google.com/search?q=" + dork_encoded)

if __name__ == "__main__":
    main()
