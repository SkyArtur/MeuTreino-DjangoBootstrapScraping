import os.path

from django.test import LiveServerTestCase
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By


class ScrapingTestCase(LiveServerTestCase):

    def setUp(self):
        self.base_project = Path(__file__).parent.parent
        self.options = webdriver.EdgeOptions()
        self.options.add_argument(f'user_data_dir={self.base_project / "Profile"}')
        self.browser = webdriver.Edge(
            executable_path=self.base_project / 'msedgedriver.exe',
            options=self.options)

    def tearDown(self):
        self.browser.quit()

    def test_interface(self):
        self.browser.get(self.live_server_url + '/')
        sleep(2)
        input_scraping = self.browser.find_element(By.ID, 'url_scraping')
        btn_scraping = self.browser.find_element(By.ID, 'btn_scraping')
        sleep(1)
        input_scraping.send_keys('Batata')
        sleep(1)
        btn_scraping.click()
        sleep(5)

