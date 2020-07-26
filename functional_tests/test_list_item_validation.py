from unittest import skip
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    """тест - проверка элемента списка"""

    def test_cannot_add_empty_items(self):
        """тест - нельзя добавить пустые элементы списка"""
        # Эдит открывает домашнюю страницу и пытается отправить пустой элемент списка
        # Она нажимает Enter на пустом поле ввода
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        # Домашняя страница обновляется и она видит сообщение об ошибке Элемент списка не может быть пустым
        self.wait_for(lambda: self.assertEqual(self.browser.find_element_by_css_selector('.error').text,
                                               "You can't have an empty list item"))
        # Она пробует снова теперь с неким текстом и все проходит успешно
        self.browser.find_element_by_id('id_new_item').send_keys('Bay milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        # Она пробует снова отправить пустой элемент и вновь получает ошибку
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertEqual(self.browser.find_element_by_css_selector('.error').text,
                                               "You can't have an empty list item"))
        # Она может это исправить заполнив поле неким текстом
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Bay milk')
        self.wait_for_row_in_list_table('2: Make tea')

