from funções import verifica_arquivo,  adicionar, visualizar, excluir, atualizar, receber

sair = True
contatos = {}
nome_arquivo = 'arquivos(agenda).txt'

while sair:
    arquivo_existe = verifica_arquivo(nome_arquivo)
    
    if arquivo_existe:
        contatos = receber()
        print('[ 0 ] Adicionar contato\n[ 1 ] Visualizar a agenda telefônica\n[ 2 ] Excluir contato da agenda\n[ 3 ] Atualizar contato na agenda\n[ 4 ] Sair da interface da agenda telefônica')
        decisao = int(input('Digite o que deseja fazer na agenda telefônica: '))
        if decisao == 0:
            contatos = adicionar(contatos)
        elif decisao == 1:
            visualizar()
        elif decisao == 2:
            contatos = excluir(contatos)
        elif decisao == 3:
            contatos = atualizar(contatos)
        else:
            break
    else:
        print('A agenda telefônica ainda não foi criada. Vamos começar adicionando contatos: ')
        contatos = adicionar(contatos)