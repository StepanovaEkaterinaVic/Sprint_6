import allure

from curl import dzen_page
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import helper as hp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    @allure.step("Заполнение данных на странице 'Для кого самокат'")
    def fill_form_1(self):
        name, last_name, street, phone_number = hp.generate_registration_data()
        self.send_keys_to_input(OrderPageLocators.NAME_FIELD, name)
        self.send_keys_to_input(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_FIELD, street)
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.click_on_element(OrderPageLocators.METRO_FIELD_STATION)
        self.send_keys_to_input(OrderPageLocators.PHONE_FIELD, phone_number)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение данных на странице 'Про аренду'")
    def fill_form_2(self):
        self.send_keys_to_input(OrderPageLocators.DELIVERY_DATE_FIELD, hp.generate_start_order_data())
        self.send_keys_to_input(OrderPageLocators.DELIVERY_DATE_FIELD, Keys.ENTER)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_2)

    @allure.step('Проверка отображения модального окна успешного заказа')
    def success_order_modal(self):
        return self.wait_for_element(OrderPageLocators.SUCCESS_MODAL)

    @allure.step('Посмотреть статус заказа через кнопку "Посмотреть статус"')
    def view_status_modal(self):
        self.click_on_element(OrderPageLocators.VIEW_STATUS_BUTTON)

    @allure.step('Нажать на кнопку "Заказать" на экране "Про аренду"')
    def click_on_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_FIN)

    @allure.step('Нажать на кнопку "Да" в окне "Вы хотите оформить заказ?"')
    def click_on_yes_button(self):
        self.click_on_element(OrderPageLocators.ORDER_YES_BUTTON)

    @allure.step('Переход на главную страницу при клике на логотип самоката')
    def go_to_the_main_page(self):
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Переход на страницу Я.Дзен при клике на логотип Яндекс")
    def go_to_the_dzen_page(self):
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)

    @allure.step("Сравнить текущий URL с ожидаемым")
    def check_url(self, expected_url):
        actual_url = self.driver.current_url
        return actual_url == expected_url

    @allure.step("Подождать URL страницы")
    def wait_url(self, expected_url):
        self.wait_for_url(expected_url)

    @allure.step("Получить URL страницы в новом окне")
    def get_new_window_url(self):
        self.wait_and_switch_to_new_window()
        self.wait_for_url(dzen_page)


