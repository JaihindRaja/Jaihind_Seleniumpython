from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/")
time.sleep(8)

# to find search area and enter search text
driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Mokka Commentary")
time.sleep(5)

# to click on the search button
# driver.find_element(By.ID, "search-icon-legacy").click()
# time.sleep(10)

# to click the enter button in keyboard for search
driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()
