import requests
import json

class Tarefa:
    def __init__(self,dados):
        self.codigo = dados['codigo']
        self.titulo = dados['titulo']
        self.descricao = dados['descricao']
    def json(self):
        return {'codigo': self.codigo,
                'titulo': self.titulo,
                'descricao': self.descricao}

class ClienteTarefa:
    def __init__(self):
        self.baseURL = 'http://localhost:8080/tarefa'
    def obterTarefas(self):
        tarefas = []
        retorno = requests.get(self.baseURL)
        for t in json.loads(retorno.content):
            tarefas.append(Tarefa(t))
        return tarefas
    def incluirTarefa(self,tarefa):
        requests.post(self.baseURL,json=tarefa.json())
    def excluirTarefa(self,codigo):
        requests.delete(f'{self.baseURL}/{codigo}')
