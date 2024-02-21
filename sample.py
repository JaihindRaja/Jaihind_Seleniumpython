# Import the Selenium library
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Initialize a WebDriver instance (e.g., Chrome or Firefox)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to a web page
driver.get('https://www.saucedemo.com')
time.sleep(2)
# Find an HTML element using a locator (e.g., XPath or CSS selector)
element = driver.find_element(By.ID, "user-name")
time.sleep(3)
# Use get_attribute() to retrieve the value of a specific attribute (e.g., "value" for an input field)
attribute_value = element.get_attribute('value')

# Print the attribute value
print(attribute_value)

# Close the browser window
driver.quit()
