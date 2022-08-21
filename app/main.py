import requests
import sqlite3
from typing import List, Dict


def data_base(user: dict) -> None:
    """ Essa função trabalha com o banco de dados e persiste informações
    da função get_users() """

    # TODO: Abrir ou criar banco
    # TODO: Ler a doc do sqlite3 no python.org -> google: sqlite3 docs
    pass


def get_users() -> None:
    """ Essa função coleta dados de users humanos e vivos da API Rick And Morty """

    r = requests.get('https://rickandmortyapi.com/api/character?page=1')
    user = {"AQUI FICA A REQUISIÇÃO COM OS DADOS JÁ SANITIZADOS. r.json()": ''}
    # TODO: colete os dados da API com o json()
    # TODO: salve os dados coletados em um banco de dados com o nome de user.db

    # TODO: persistir os dados no db (user.db)
    data_base(user)
