import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSignInForm(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver (in this case, Chrome)
        self.driver = webdriver.Chrome(executable_path='C://Users//Hp//Downloads//chromedriver_win32//chromedriver.exe')

    def test_sign_in_form(self):
        # Open the sign-in page
        self.driver.get("http://192.168.87.102:5000/signin")  # Replace with the actual URL

        # Find the email and password input fields by their HTML attributes
        email_input = self.driver.find_element_by_name("email")
        password_input = self.driver.find_element_by_name("password")

        # Simulate user input (replace "your_email" and "your_password" with actual test data)
        email_input.send_keys("test@gmail.com")
        password_input.send_keys("1234")

        # Submit the form
        submit_button = self.driver.find_element_by_css_selector("button.btn.btn-primary")
        submit_button.click()

        # Perform any assertions or verifications based on the expected behavior
        # For example, you might check if a success message is displayed or if the user is redirected

    def tearDown(self):
        # Close the browser window after the test is complete
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
