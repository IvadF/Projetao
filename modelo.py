# -*- coding: utf-8 -*-
from conexao import cursorCmd

class modelo:
    def refresh(self):
        return cursorCmd("SELECT nome, juros, periodo, tipo"
                 " FROM interesse", "all")

    def gravar(self, n,j,p,t):
        return cursorCmd("INSERT INTO interesse (nome, juros, periodo, tipo)"
                f" VALUES ('{n}', {float(j)*.01}, '{p}', '{t}')")

    def deletar(self, n=None,j=None,p=None,t=None):
        wholeText = "DELETE FROM interesse"
        if n!="" or j!="" or p!="" or t!="":
            wholeText += " WHERE"

        i = -1
        for desc,item in [["nome",n],["juros",j],["periodo",p],["tipo",t]]:
            if item!="":
                i += 1
                if i > 0:
                    wholeText += " AND"
                if desc == "juros":
                    wholeText += " " + desc + " - " + str(float(item)*.01) + " < .0001"
                else:
                    wholeText += " " + desc + " = '" + item + "'"
        print(wholeText)
        return cursorCmd(wholeText)
