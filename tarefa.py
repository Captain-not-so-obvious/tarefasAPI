from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Tarefa(Base):
    __tablename__ = "tarefa"
    codigo = Column(String(4), primary_key=True)
    titulo = Column(String(50))
    descricao = Column(String(255))
