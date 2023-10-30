import os

# Função que verifica se o arquivo existe
def verifica_arquivo(nome_arquivo):
    return os.path.isfile(nome_arquivo)

# Função para adicionar contatos à agenda
def adicionar(contatos):
    print('Se deseja parar digite "parar".')
    while True:
        nome = input('Digite o nome do contato: ')
        if nome == 'parar':
            break
        telefone = input('Digite o número de telefone do contato: ')
        if telefone == 'parar':
            break

        contatos[nome] = telefone

    with open('arquivos(agenda).txt', 'a') as arquivos:
        for nome, telefone in contatos.items():
            arquivos.write('Nome: {}, Telefone: {}\n'.format(nome, telefone))
    return contatos

# Função para visualizar os contatos da agenda
def visualizar():
    with open('arquivos(agenda).txt', 'r') as arquivo:
        conteudo = arquivo.read()
    print(conteudo)
    return conteudo

def receber():
    with open('arquivos(agenda).txt', 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

# Função para excluir os contatos da agenda
def excluir(contatos):
    parar = True
    print('Se deseja parar digite "parar".')
    while parar:
        nome = input('Digite o nome do contato que deseja excluir da agenda: ')
        if nome == 'parar':
            break
        elif nome in contatos:
            del contatos[nome]
        else:
            print('Esse contato não está na agenda.')

    with open('arquivos(agenda).txt', 'w') as arquivos:
        for nome, telefone in contatos.items():
            arquivos.write('Nome: {}, Telefone: {}\n'.format(nome, telefone))

    return contatos

# Função para atualizar os contatos da agenda
def atualizar(contatos):
    parar = True
    print('Se deseja parar digite "parar": ')
    while parar:    
        nome = str(input('Digite qual o nome que deseja alterar da agenda: '))
        if nome == 'parar':
            break
        if nome in contatos:
            nome_cha = str(input('Digite qual o novo nome de {} que deseja alterar: '.format(nome)))
            if nome_cha == 'parar':
                break
            telefone_cha = input('Digite qual o novo nuemro de {} que deseja alterar: '.format(nome))
            if telefone_cha == 'parar':
                break

            contatos[nome] = telefone_cha
            contatos[nome_cha] = contatos.pop(nome)
        else:
            print('O contato nao esta na agenda.')

    with open('arquivos(agenda).txt', 'w') as arquivos:
        for nome, telefone in contatos.items():
            arquivos.write('Nome: {}, Telefone: {}\n'.format(nome, telefone))

    return contatos