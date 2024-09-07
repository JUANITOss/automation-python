from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the browser
browser = webdriver.Firefox()

# Opening the url
browser.get('https://automatetheboringstuff.com/')

# Click the selector
elem = browser.find_element(By.CSS_SELECTOR, '.main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(2) > a:nth-child(1)')

elem.click()