import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from pyunitreport import HTMLTestRunner
import time
from selenium.webdriver.common.by import By


class FirstTest(unittest.TestCase):
    driver = None
    __id_button_login = "login-button"
    __xpath_input_user = '//*[@id="user-name"]'
    __id_input_password = "password"
    __xpath_error ='/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3'
    __id_validacion = '//*[@id="add-to-cart-sauce-labs-bike-light"]'

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test1_open_browser(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        element = driver.find_element(By.ID, self.__id_button_login).is_displayed()
        self.assertTrue(element)
        time.sleep(10)

    def test2_login_failed(self):
        driver = self.driver
        user = "standard_user"
        password = "secret_sauced"
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, self.__xpath_input_user).send_keys(user)
        driver.find_element(By.ID, self.__id_input_password).send_keys(password)
        driver.find_element(By.ID, self.__id_button_login).click()
        element = driver.find_element(By.XPATH, self.__xpath_error).is_displayed()
        self.assertTrue(element)

    def test3_login_success(self):
        driver = self.driver
        user = "standard_user"
        password = "secret_sauce"
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, self.__xpath_input_user).send_keys(user)
        driver.find_element(By.ID, self.__id_input_password).send_keys(password)
        driver.find_element(By.ID, self.__id_button_login).click()
        element = driver.find_element(By.XPATH, self.__id_validacion).is_displayed()
        self.assertTrue(element)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='Prueba'))

