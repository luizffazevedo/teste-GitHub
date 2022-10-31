import requests
import json
from datetime import date, datetime



class ListaRepo():
    def __init__(self,usuario):
        self.usuario = usuario


    def requisicao (self):
        '''Retorna a resposta da API em json .'''

        resposta = requests.get('https://api.github.com/users/luizffazevedo/repos')
        if resposta.status_code == 200 :
            return resposta.json()

        else :
            return resposta.status_code
    

    def filtro_repositorio (self):
        '''Essa função filtra todos os repositórios e diz se está ativo ou arquivado .'''
        dados_api = self.requisicao()
        for i in range(len(dados_api)):
            if dados_api[i]['archived'] == True:
                print(f'O portifólio {dados_api[i]["name"]} está arquivado.')

            else : 
                print(f'O portifólio {dados_api[i]["name"]} está ativo.')

    
    def ordenar_repositorio_nome (self):
        '''Ordena o repositório por ordem alfabética .'''
        dados_api = self.requisicao()
        dados_lista = []
        for dados in range(len(dados_api)):
            dados_lista.append(dados_api[dados]['name'])

        for d in dados_lista :
            print(d)


    def mostrar_data_repositorio(self):
        '''Mostra a data de modificação do último commit do repositório . '''
        dados_api = self.requisicao()
        datas = list()
        data_atual = date.today()
        for i in range(len(dados_api)):
            datas.append(dados_api[i]['pushed_at'][0:10])
        
        dic_tempo = {}

        for d in range(len(datas)):
            ano = int(datas[d][0:4]) 
            dia = int(datas[d][8:])
            mes = int(datas[d][5:7])
            data = date(ano,mes,dia)
            tempo_decorrido = abs((data_atual - data)).days
            dic_tempo[dados_api[d]['name']] = tempo_decorrido
        for i in sorted(dic_tempo,key=dic_tempo.get):
            print(f'Repositório : {i} ,último commit há {dic_tempo[i]} dias atrás .')

    
    def pesquisa_repositório(self):
        '''Pesquisa por itens no repositório'''
        lista_repos = []
        dados_api = self.requisicao()
        pesquisa = input('DIGITE PARA PESQUISAR NO REPOSITÓRIO :')
        elemento_encontrado = None
        for i in range(len(dados_api)):
            lista_repos.append(dados_api[i]['name'])
        for s in lista_repos:
            if pesquisa in s:
                elemento_encontrado = s

        if elemento_encontrado :
            print(elemento_encontrado)

    
    

    
    def print_do_repositorio(self):
        '''Essa Função lista os itens do repositório por nome .'''
        dados_api = self.requisicao()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)



repositorios = ListaRepo('luizffazevedo')


repositorios.mostrar_data_repositorio()
repositorios.filtro_repositorio()
repositorios.mostrar_data_repositorio()
repositorios.pesquisa_repositório()



