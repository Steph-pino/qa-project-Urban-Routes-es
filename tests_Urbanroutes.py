import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Urbanroutes import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.routes_page = UrbanRoutesPage(cls.driver)
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_click_pedir_un_taxi(self):
        self.routes_page.click_pedir_un_taxi()

    def test_choose_comfort_tariff(self):
        self.routes_page.set_comfort_tariff()

    def test_set_phone_number(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_pedir_un_taxi()
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_phone_number(data.phone_number)

    def test_set_payment_method(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_pedir_un_taxi()
        self.routes_page.open_payment_method_popup()
        self.routes_page.click_agregar_tarjeta()
        self.routes_page.set_card_number(data.card_number)
        assert self.routes_page.get_card_field().get_property('value') == data.card_number
        self.routes_page.set_cvv_number(data.card_code)
        self.routes_page.get_cvv_field().send_keys(Keys.TAB)
        self.routes_page.click_agregar_button()
        self.routes_page.close_popup_payment_method()

    def test_set_mensaje_al_conductor(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_pedir_un_taxi()
        self.routes_page.set_mensaje_al_conductor(data.message_for_driver)
        assert self.routes_page.get_mensaje_al_conductor() == data.message_for_driver

    def test_order_manta_y_panuelos(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_pedir_un_taxi()
        self.routes_page.set_comfort_tariff()
        self.routes_page.click_requisitos_pedido()
        self.routes_page.set_manta_y_panuelos()

    def test_order_dos_helados(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_pedir_un_taxi()
        self.routes_page.set_comfort_tariff()
        self.routes_page.set_icecream()

    def test_click_pedir_taxi_final(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_pedir_un_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


