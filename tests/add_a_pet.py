import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        user = "test"
        pwd = "test111"
        driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(3)
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)

        time.sleep(3)
        # find 'Pets' and click it. Then find "Add Pet" and click it

        driver.find_element(By.XPATH, "//a[contains(., 'Pets')]").click()
        driver.find_element(By.LINK_TEXT, ('ADD PET')).click()

        name = 'Pet'
        date_of_birth = '01/01/2001'
        history = 'test'
        breed = 'test'
        size = 'test'
        # find the form and send the credentials above
        elem = driver.find_element(By.ID, "id_name")
        elem.send_keys(name)
        elem = driver.find_element(By.ID, "id_date_of_birth")
        elem.send_keys(date_of_birth)
        elem = driver.find_element(By.ID, "id_history")
        elem.send_keys(history)
        elem = driver.find_element(By.ID, "id_breed")
        elem.send_keys(breed)
        elem = driver.find_element(By.ID, "id_size")
        elem.send_keys(size)
        elem.send_keys(Keys.RETURN)

        # time.sleep(5)

        try:
            # verify that the new Pet's name (Pet) shows up on success part of page
            driver.find_element(By.PARTIAL_LINK_TEXT, ('Pet'))
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("New pet's name not found on page. Form did not save new pet.")

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()