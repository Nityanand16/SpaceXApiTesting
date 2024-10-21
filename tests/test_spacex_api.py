import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Import WebDriver Manager
from pages.spacex_api_page import SpaceXApiPage
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestSpaceXApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #Selenium WebDriver using WebDriver Manager
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver

        # Initialize the Page Object for SpaceX API
        cls.spacex_api = SpaceXApiPage()

    @classmethod
    def tearDownClass(cls):
        #Teardown Selenium WebDriver
        cls.driver.quit()

    # validate that the API returns a 200 status code
    def test_status_code(self):
        response = self.spacex_api.get_latest_launch()
        self.assertEqual(response.status_code, 200, f"Expected 200, but got {response.status_code}")

    # validate that the response contains required fields
    def test_response_data_structure(self):
        response = self.spacex_api.get_latest_launch()
        json_data = response.json()

        # Assert that required fields are in the response
        self.assertIn('name', json_data, "Field 'name' is missing in the response")
        self.assertIn('date_utc', json_data, "Field 'date_utc' is missing in the response")
        self.assertIn('rocket', json_data, "Field 'rocket' is missing in the response")
        self.assertIn('success', json_data, "Field 'success' is missing in the response")

        # Add an explicit wait before proceeding with any further actions
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))  # Example condition
        )

    """Validate data types of response fields"""
    def test_data_types_and_format(self):
        response = self.spacex_api.get_latest_launch()
        json_data = response.json()

        # Validate if 'name' is a string
        self.assertIsInstance(json_data['name'], str, "'name' is not a string")

        # Validate if 'date_utc' is in ISO 8601 format
        try:
            datetime.strptime(json_data['date_utc'], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            self.fail("'date_utc' is not in ISO 8601 format")

        # Validate if 'rocket' is a string
        self.assertIsInstance(json_data['rocket'], str, "'rocket' is not a string")

        # Validate if 'success' is a boolean
        self.assertIsInstance(json_data['success'], bool, "'success' is not a boolean")

        # Explicit wait before proceeding (you can change this condition based on your needs)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))  # Example condition
        )

if __name__ == "__main__":
    unittest.main()