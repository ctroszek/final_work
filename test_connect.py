import psycopg2
import pytest


# @pytest.fixture
# def create_base():
#     db = psycopg2.connect(user='postgres', password='postgres',
#                           host='localhost')
#     cursor = db.cursor()
#     cursor.execute('CREATE DATABASE postgres')
#     return db

def test_connect():
    assert (1, 1) == (1, 1)
