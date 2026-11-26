# -*- coding: utf-8 -*-
from conexao import cursorCmd

class modelo:
    def refresh(self):
        return cursorCmd("SELECT nome, juros, periodo, tipo"
                 " FROM interesse", "all")

    def gravar(self, n,j,p,t):
        return cursorCmd("INSERT INTO interesse (nome, juros, periodo, tipo)"
                f" VALUES ('{n}', {int(j)*.01}, '{p}', '{t}')")
