# -*- coding: utf-8 -*-
import configparser
import certifi
import mysql.connector

def conectar():
    arq = configparser.ConfigParser()
    arq.read("config.ini", encoding="utf-8")

    banco = arq["Banco"]
    return mysql.connector.connect(
        host = banco["host"],
        user = banco["user"],
        password = banco["pass"],
        port = banco["port"],
        database = banco["name"],
        ssl_ca = certifi.where(),
        ssl_verify_cert = True,
        ssl_verify_identity = True,
    )


def cursorCmd(cmd, valueTuple=(), reading=False):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(cmd, valueTuple)
        if reading == "all":
            return cursor.fetchall()
        elif reading == "one":
            return cursor.fetchone()
        else:
            conexao.commit()


if __name__ == "__main__":
    #linhas = cursorCmd("SELECT id, nome, juros, periodo, tipo FROM interesse ORDER BY nome", (), "all")
    linhas = cursorCmd("DESCRIBE interesse")
    print("\n")
    for idd, nome, juros, periodo, tipo in linhas:
        print(f"id: {idd}, juros: {juros}, periodo: {periodo}, tipo: {tipo}")
