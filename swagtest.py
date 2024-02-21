import pytest
from pages.swagpages import Swag
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Error message set-up
error12 = "Epic sadface: Username and password do not match any user in this service"
error3 = "Epic sadface: Sorry, this user has been locked out."
error4 = "Epic sadface: Username is required"
error5 = "Epic sadface: Password is required"
error6 = "Epic sadface: Username is required"
inventory_page = "https://www.saucedemo.com/inventory.html"
home_url = 'https://www.saucedemo.com/'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("uname, pwd", [
    ("standard_user", "1234"),
    ("Jaihind Raja", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("", "1234"),
    ("standard_user", ""),
    ("", ""),
    ("standard_user", "secret_sauce")
])
def test_case(driver, uname, pwd):
    Swag(driver).home()
    if uname == "standard_user" and pwd == "1234":
        Swag(driver).username(uname)
        Swag(driver).password(pwd)
        Swag(driver).login()

        assert error12 == Swag(driver).error_message()
    elif uname == "Jaihind Raja" and pwd == "secret_sauce":
        Swag(driver).username(uname)
        Swag(driver).password(pwd)
        Swag(driver).login()

        assert error12 == Swag(driver).error_message()
    elif uname == "locked_out_user" and pwd == "secret_sauce":
        Swag(driver).username(uname)
        Swag(driver).password(pwd)
        Swag(driver).login()

        assert error3 == Swag(driver).error_message()
    elif uname == "" and pwd == "1234":
        Swag(driver).username(uname)
        Swag(driver).password(pwd)
        Swag(driver).login()

        assert error4 == Swag(driver).error_message()
    elif uname == "standard_user" and pwd == "":
        Swag(driver).username(uname)
        Swag(driver).password(pwd)
        Swag(driver).login()

        assert error5 == Swag(driver).error_message()
    elif uname == "" and pwd == "":
        Swag(driver).username(uname)
        Swag(driver).password(pwd)
        Swag(driver).login()

        assert error6 == Swag(driver).error_message()
    elif uname == "standard_user" and pwd == "secret_sauce":
        Swag(driver).username(uname)
        Swag(driver).password(pwd)
        Swag(driver).login()

        assert Swag(driver).current_url() == inventory_page


def test_close_error(driver):
    Swag(driver).home()
    Swag(driver).username("uname")
    Swag(driver).password("pwd")
    Swag(driver).login()

    Swag(driver).close_error()


def test_verify(driver):
    Swag(driver).home()
    Swag(driver).username("uname")
    Swag(driver).password("pwd")
    Swag(driver).login()
    Swag(driver).close_error()

    assert Swag(driver).verify_button(
        "#login_button_container > div > form > div.error-message-container.error > h3 > button > svg") is True


def test_side_bar(driver):
    Swag(driver).home()
    Swag(driver).username("standard_user")
    Swag(driver).password("secret_sauce")
    Swag(driver).login()
    Swag(driver).open_sidebar()

    assert Swag(driver).verify_button("react-burger-menu-btn") is True


def test_close_sidebar(driver):
    Swag(driver).home()
    Swag(driver).username("standard_user")
    Swag(driver).password("secret_sauce")
    Swag(driver).login()
    Swag(driver).open_sidebar()
    Swag(driver).sidebar_close()

    assert Swag(driver).verify_button("react-burger-cross-btn") is True


def test_logout(driver):
    Swag(driver).home()
    Swag(driver).username("standard_user")
    Swag(driver).password("secret_sauce")
    Swag(driver).login()
    Swag(driver).open_sidebar()
    Swag(driver).logout()

    assert Swag(driver).current_url() == home_url
