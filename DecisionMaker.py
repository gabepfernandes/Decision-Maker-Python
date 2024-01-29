from random import choice

def qualquer_filme(lista):
    filme_aleatorio = choice(lista)
    nome_filme_aleatorio = filme_aleatorio['nome']
    print('O filme de hoje vai ser: ' + nome_filme_aleatorio)
    print()
    

def remove_duplicados(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

def filme_filtrado_longo(genero, filmes):
    filmes_filtrados = []
    for filme in filmes:
        if filme['genero'] == genero and filme['duracao'] >= 120:
            filmes_filtrados.append(filme)
    return filmes_filtrados

def filme_filtrado_curto(genero, filmes):
    filmes_filtrados = []
    for filme in filmes:
        if filme['genero'] == genero and filme['duracao'] < 120:
            filmes_filtrados.append(filme)
    return filmes_filtrados   
    

                  
# lista de filmes Oscar 2024

filmes = [{'nome' : 'Killers of the Flower Moon', 'genero':'Crime','duracao' : 206},
          {'nome' : 'Poor Things', 'genero':'Romance', 'duracao' :141},
          {'nome' : 'Nyad', 'genero':'Drama', 'duracao' :121},
          {'nome' : 'Anatomy of a Fall', 'genero':'Misterio', 'duracao' :152},
          {'nome' : 'The Color Purple', 'genero':'Drama', 'duracao' :154},
          {'nome' : 'The Boy and the Heron', 'genero':'Aventura', 'duracao' :154},
          {'nome' : 'The Holdovers', 'genero':'Comedia', 'duracao' :117},
          {'nome' : 'Zone of Interest', 'genero':'Drama', 'duracao' :105},
          {'nome' : 'American Fiction', 'genero':'Comedia', 'duracao' :105},
          {'nome' : 'May December', 'genero':'Drama', 'duracao' :117},
          {'nome' : 'Perfect Days', 'genero':'Drama', 'duracao' :125} ]

lista_generos = []

for filme in filmes:
    lista_generos.append(filme['genero'])

lista_generos_sem_duplicatas = remove_duplicados(lista_generos)

escolha = int(input('Deseja me ajudar a escolher o filme de hoje?\n' +
                    '1 - Sim\n2 - Nao\nResposta: '))

if escolha == 1:
    print()
    print('Generos de filmes disponiveis:')
    for genero in lista_generos_sem_duplicatas:
        print('\t-' + genero)
    genero = input('\n -Escolha um: ')
    duracao = int(input('Desja ver um filme longo ou curto?\n' +
                    '1 - Longo\n2 - Curto\nResposta: ' ))
    if duracao == 1:
        filme_escolhido = filme_filtrado_longo(genero, filmes)
        qualquer_filme(filme_escolhido)
    if duracao == 2:
        filme_escolhido = filme_filtrado_curto(genero, filmes)
        qualquer_filme(filme_escolhido)


    
elif escolha == 2:
    qualquer_filme(filmes)
    print()


# Melhorias:
# - mostrar lista de filmes e perguntar se quer fazer alguma alteracao
# - tratamento de erros