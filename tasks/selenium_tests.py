from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class TaskDashSeleniumTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or specify path here
        self.driver.implicitly_wait(10)
        self.base_url = "http://127.0.0.1:8000/"

    def test_login_and_task_crud(self):
        driver = self.driver
        driver.get(self.base_url)

        # Login
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpass")
        password_input.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for redirect

        # Verify dashboard loaded by checking for some element, e.g., page title or heading
        self.assertIn("Dashboard", driver.title)

        # TODO: Add steps to create, update, delete tasks via UI

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
