from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webium import BasePage, Find

from object.user import User


class LoginPage(BasePage):

    email_field = Find(by=By.CSS_SELECTOR, value="input[type='email']")
    password_field = Find(by=By.CSS_SELECTOR, value="input[type='password']")
    next_button = Find(by=By.XPATH, value="//span[contains(text(), 'Далее')]")

    def __init__(self, driver):
        self.driver = driver
        self.user = User
        self.wait = WebDriverWait(self.driver, 10)
        super(LoginPage, self).__init__(url="https://gmail.com", driver=driver)

    def open(self):
        self.driver.get(self.url)
        return self

    def login_as(self, user):
        self.email_field.send_keys(user.email, Keys.ENTER)
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
        self.password_field.send_keys(user.password)
        self.next_button.click()
        return MainPage(self.driver)




class MainPage(BasePage):

    account_button = Find(by=By.XPATH, value="//*[@id='gb']/div[1]/div[1]/div[2]/div[5]/div[1]/a")
    logout_button = Find(by=By.XPATH, value="//*/a[contains(text(), 'Выйти')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        super(MainPage, self).__init__(url="https://mail.google.com/mail/#inbox", driver=driver)

    def logout(self):
        self.account_button.click()
        self.wait.until(expected_conditions.visibility_of(self.logout_button))
        self.logout_button.click()
