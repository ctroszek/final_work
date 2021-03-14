import psycopg2
import pytest
from pages.base_page import BasePage

# @pytest.fixture
# def create_base():
#     db = psycopg2.connect(user='postgres', password='postgres',
#                           host='localhost')
#     cursor = db.cursor()
#     cursor.execute('CREATE DATABASE postgres')
#     return db


class TestConnectToWebApp(BasePage):

    def test_connect(browser):
        base_page = BasePage(browser)
        base_page.open_base_page()

