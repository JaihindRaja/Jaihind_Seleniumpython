
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    # Used for setup "it runs before test cases"
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)

    # Used for teardown/close "it runs after test case"
    yield driver
    driver.quit()


@pytest.mark.parametrize("uname, pwd", [
    ("Jaihind Raja", "1234"),
    ("problem_user", "1234"),
    ("problem_user", "secret_sauce")
])
# WebDriverWait is good practice to use time.sleep is not good practice
def test_valid(driver, uname, pwd):
    driver.get("https://www.saucedemo.com")
    username = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "user-name")))
    username.send_keys(uname)
    password = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys(pwd)

    loginb = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "login-button")))
    loginb.click()

    error_message_element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#login_button_container > div > form > div.error-message-container.error > h3')))
    assert error_message_element.text is not None


# def test_valid1(driver):
#     driver.get("https://www.saucedemo.com")
#     time.sleep(5)
#     driver.find_element(By.ID, "user-name").send_keys("problem_user")
#     driver.find_element(By.ID, "password").send_keys("12345")
#     time.sleep(2)
#     driver.find_element(By.ID, "login-button").click()
#     time.sleep(3)
#
#     error_message_element = driver.find_element(By.CSS_SELECTOR, '#login_button_container > div > form > '
#                                                                  'div.error-message-container.error > h3')
#     time.sleep(2)
#     assert error_message_element.text == "Epic sadface: Username and password do not match any user in this service"
#

def test_valid2(driver):
    driver.get("https://www.saucedemo.com")
    username = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "user-name")))
    username.send_keys("standard_user")
    password = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")
    login = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "login-button")))
    login.click()

    # (WebDriverWait(driver, 2).until(EC.url_to_be(("https://www.saucedemo.com/inventory.html"))))
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
