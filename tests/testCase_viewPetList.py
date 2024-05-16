# it tests file to determine if the Pet List page is displayed when the user
# clicks the 'Adoptable Pets' button in the navigation pane of the local library
# application

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        user = "instructor"
        pwd = "mavericks"
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)
        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        # find 'All books' and click it – note this is all one Python statement
        #elem = driver.find_element(By.XPATH, "//a[contains(., 'All Books')]").click()
        #elem.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH, "//a[contains(., 'Adoptable Pets')]").click()

        time.sleep(5)
        try:
            # verify Pet List exists on new screen after clicking "Adoptable pets" button
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Pet List does not appear when Adoptable Pets clicked")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
