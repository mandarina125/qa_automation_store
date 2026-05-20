from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://automationexercise.com/login")

    def login(self, email, password):
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()

    def get_title(self):
        return self.driver.title