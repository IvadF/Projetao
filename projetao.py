# -*- coding: utf-8 -*-
from modelo import modelo
modelo = modelo()

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk


def negrito(texto, booleano):
    return booleano and ("<b>" + texto + "<b>") or texto


class App:
    def __init__(self):
        self.b = b = Gtk.Builder()
        b.add_from_file("projetao.glade")

        self.janela = b.get_object("janela")
        self.btn_gravar = b.get_object("btn_gravar")
        self.btn_excluir = b.get_object("btn_excluir")
        self.btn_atualizar = b.get_object("btn_atualizar")

        self.ent_nome = b.get_object("ent_nome")
        self.ent_juros = b.get_object("ent_juros")
        self.combobox = b.get_object("combobox")
        self.rad_simples = b.get_object("rad_simples")
        self.tabela = b.get_object("tabela")

        self.btn_gravar.connect("clicked",self.ao_gravar)
        self.btn_excluir.connect("clicked",self.ao_excluir)
        self.btn_atualizar.connect("clicked",self.ao_atualizar)

        self.janela.show_all()
        self.recarregar_tabela()
        Gtk.main()


    def recarregar_tabela(self):
        linhas = modelo.refresh()
        i = 0
        for nome,juros,periodo,tipo in linhas:
            i += 1
            novoNome = Gtk.Label()
            novoNome.set_markup(nome)
            novoJuros = Gtk.Label()
            novoJuros.set_markup(f"{juros*100}% ao {periodo}")
            novoTipo = Gtk.Label()
            novoTipo.set_markup(tipo)
            self.tabela.attach(novoNome, 0, i, 1,1)
            self.tabela.attach(novoJuros, 1, i, 1,1)
            self.tabela.attach(novoTipo, 2, i, 1,1)
        self.tabela.show_all()

    def ao_gravar(self, comp=None, dados=None):
        modelo.gravar(self.ent_nome.get_text().strip(),
                      self.ent_juros.get_text().strip(),
                      self.combobox.get_active_text(),
                      self.rad_simples.get_active() and "simples" or "composto")
        self.recarregar_tabela()

    def ao_excluir(self):
        pass

    def ao_atualizar(self):
        pass



if __name__ == "__main__":
    App()
