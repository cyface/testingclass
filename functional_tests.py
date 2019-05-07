import requests
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('bin/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)


class BrokenImageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('bin/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_home_page_for_broken_images(self):
        # Check for broken images on home page

        self.browser.get('http://localhost:8000')
        all_images = self.browser.find_elements_by_tag_name('img')
        for image in all_images:
            img_src = image.get_attribute('src')
            print(img_src)
            result = requests.get(img_src)
            self.assertEqual(result.status_code, requests.codes.ok)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
