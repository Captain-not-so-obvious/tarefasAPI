from flask import Flask, jsonify, request
from tarefaDAO import TarefaDAO
from tarefa import Tarefa


app = Flask(__name__)
dao_tarefa = TarefaDAO()


@app.route('/tarefa')
def get_tarefas():
    tarefas = [];
    for t in dao_tarefa.obterTodos():
        tarefas.append({'codigo': t.codigo, 
                        'titulo': t.titulo,
                        'descricao': t.descricao})
    return jsonify(tarefas)

@app.route('/tarefa', methods=['POST'])
def add_tarefa():
    tarefa_json = request.get_json()
    tarefa = Tarefa(codigo=tarefa_json['codigo'], 
                    titulo=tarefa_json['titulo'],
                    descricao=tarefa_json['descricao'])
    dao_tarefa.incluir(tarefa)
    return '', 204

@app.route('/tarefa/<codigo>', methods=['DELETE'])
def del_tarefa(codigo):
    dao_tarefa.excluir(codigo)
    return '', 204
