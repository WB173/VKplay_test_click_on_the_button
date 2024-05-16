import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTextBox(unittest.TestCase):
    def setUp(self):
            # Создаем экземпляр Chrome WebDriver
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Remote(
               command_executor='http://127.0.0.1:4444/wd/hub',
               options=options
            )

    def test_click_on_the_button_positive(self):
        # Cоздаем локальную ссылку на объект драйвера, созданный в методе setUp
        driver = self.driver

        # Переход по заданному URL в WebDriver
        driver.get('https://demoqa.com/text-box')

        # Ищем поле Full Name и вводим данные
        elem_user_name = driver.find_element(By.ID, 'userName')
        elem_user_name.send_keys('Jon Smit')

        # Ищем поле Email и вводим данные
        elem_user_email = driver.find_element(By.ID, 'userEmail')
        elem_user_email.send_keys('test@test.te')

        # ID currentAddress существует для 2-х объектов, поля ввода и поля вывода. Поэтому ищем ID в поле ввода и только потом вводим данные
        elem_currentAddress_wrapper = driver.find_element(By.ID, 'currentAddress-wrapper')
        elem_user_current_address = elem_currentAddress_wrapper.find_element(By.ID, 'currentAddress')
        elem_user_current_address.send_keys('11 Brown Gateway Maisiebury B23 5RS')

        # Ищем кнопку Submit и нажимаем на нее
        elem_button_submit = driver.find_element(By.ID, 'submit')
        elem_button_submit.click()

        # Сравниваем введенные Full Name и Email с текстом в поле вывода
        self.assertIn("Jon Smit",  driver.find_element(By.ID, 'name').text)
        self.assertIn("test@test.te", driver.find_element(By.ID, 'email').text)

        # ID currentAddress существует для 2-х объектов, поля ввода и поля вывода. Поэтому ищем ID в поле вывода и только потом сравниваем
        elem_output = driver.find_element(By.ID, 'output')
        address_field_output = elem_output.find_element(By.ID, 'currentAddress')
        self.assertIn("11 Brown Gateway Maisiebury B23 5RS", address_field_output.text)

    def test_click_on_the_button_negative(self):
        # Cоздаем локальную ссылку на объект драйвера, созданный в методе setUp
        driver = self.driver

        # Переход по заданному URL в WebDriver
        driver.get('https://demoqa.com/text-box')

        # Ищем поле Email и вводим данные
        elem_user_email = driver.find_element(By.ID, 'userEmail')
        elem_user_email.send_keys('test')

        # Ищем кнопку Submit и нажимаем на нее
        elem_button_submit = driver.find_element(By.ID, 'submit')
        elem_button_submit.click()

        # Проверяем что поле ввода Email показало ошибку и сменило класс
        self.assertEqual(elem_user_email.get_attribute("class"), 'mr-sm-2 field-error form-control')

    # Закрываем Chrome WebDriver по окончанию теста
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":

    # Запускаем набор тестов
    unittest.main()