from sqlalchemy import select
from cursodb import postgresql_engine
from tarefa import Tarefa
from sqlalchemy.orm import Session

session = Session(postgresql_engine)

class TarefaDAO:
    def obterTodos(self):
        stmt = select(Tarefa)
        return session.scalars(stmt)
    def obter(self, codigo):
        tarefa = session.get(Tarefa, codigo)
        return tarefa        
    def incluir(self, tarefa):
        session.add(tarefa)
        session.commit()
    def excluir(self, codigo):
        session.delete(self.obter(codigo))
        session.commit()
    def alterar(self, tarefa):
        session.merge(tarefa)
        session.commit()
