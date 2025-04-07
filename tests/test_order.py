import allure

from curl import main_site, dzen_page
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages import order_page
from pages.order_page import OrderPage
from pages.main_page import MainPage


@allure.feature("Создание заказа")
class TestOrder:
    def test_create_order_with_hed_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_agree_cookie()
        main_page.agree_cookie()
        main_page.click_on_button_hed()

        order_page = OrderPage(driver)
        order_page.fill_form_1()
        order_page.fill_form_2()
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        assert order_page.success_order_modal()

        order_page.view_status_modal()
        order_page.go_to_the_main_page()
        assert order_page.check_url(main_site)

        order_page.go_to_the_dzen_page()
        order_page.get_new_window_url()
        assert order_page.check_url(dzen_page)
        
    def test_create_order_with_low_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_agree_cookie()
        main_page.agree_cookie()
        main_page.click_on_button_low()

        order_page = OrderPage(driver)
        order_page.fill_form_1()
        order_page.fill_form_2()
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        assert order_page.success_order_modal()

        order_page.view_status_modal()
        order_page.go_to_the_main_page()
        assert order_page.check_url(main_site)

        order_page.go_to_the_dzen_page()
        order_page.get_new_window_url()
        assert order_page.check_url(dzen_page)



