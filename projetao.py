# -*- coding: utf-8 -*-
from conexao import cursorCmd

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        self.b = b = Gtk.Builder()
        b.add_from_file("projetao.glade")

        self.janela = b.get_object("janela")
        self.btn_gravar = b.get_object("btn_gravar")
        self.btn_excluir = b.get_object("btn_excluir")
        self.btn_atualizar = b.get_object("btn_atualizar")
        self.tabela = b.get_object("tabela")

        self.btn_gravar.connect("clicked",self.ao_gravar)
        self.btn_excluir.connect("clicked",self.ao_excluir)
        self.btn_atualizar.connect("clicked",self.ao_atualizar)

        self.janela.show_all()
        Gtk.main()

    def ao_gravar(self, comp=None, dados=None):
        print("oi")
        linhas = cursorCmd("SELECT nome, juros, periodo, tipo FROM interesse",(),"all")
        i = 0
        for nome,juros,periodo,tipo in linhas:
            i += 1
            novoNome = Gtk.Label(label = nome)
            novoJuros = Gtk.Label(label= f"{juros*100}% ao {periodo}")
            novoTipo = Gtk.Label(label=tipo)
            self.tabela.attach(novoNome, 0, i, 1,1)
            self.tabela.attach(novoJuros, 1, i, 1,1)
            self.tabela.attach(novoTipo, 2, i, 1,1)

        self.tabela.show_all()

    def ao_excluir(self):
        pass

    def ao_atualizar(self):
        pass



if __name__ == "__main__":
    App()
