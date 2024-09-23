# -*- coding: utf-8 -*-
from cliente import ClienteTarefa

cli = ClienteTarefa()
for t in cli.obterTarefas():
    print(f'{t.codigo} :: {t.titulo}');
    print(f'==>{t.descricao}');
    print();
