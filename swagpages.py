from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Swag:
    home_url = 'https://www.saucedemo.com'
    username_id = "user-name"
    password_id = "password"
    login_button_id = "login-button"
    close_error_message = "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg"
    error_message_selector = "#login_button_container > div > form > div.error-message-container.error > h3"
    sidebar_id = "react-burger-menu-btn"
    sidebar_close_id = "react-burger-cross-btn"
    logout_link_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.driver.get(self.home_url)

    def username(self, uname):
        name = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, self.username_id)))
        name.send_keys(uname)

    def password(self, pwd):
        pas = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, self.password_id)))
        pas.send_keys(pwd)

    def login(self):
        log = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, self.login_button_id)))
        log.click()

    def error_message(self):
        error_message = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.error_message_selector))).text
        return error_message

    def close_error(self):
        button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.close_error_message)))
        button.click()

    def verify_button(self, button):
        try:
            self.driver.find_element(By.CSS_SELECTOR, button)
            return False
        except NoSuchElementException:
            return True

    def open_sidebar(self):
        self.driver.find_element(By.ID, self.sidebar_id).click()

    def sidebar_close(self):
        self.driver.find_element(By.ID, self.sidebar_close_id)

    def logout(self):
        self.driver.find_element(By.ID, self.logout_link_id).click()

    def current_url(self):
        return self.driver.current_url
