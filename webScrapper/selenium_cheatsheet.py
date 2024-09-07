
# Selenium Cheat Sheet (Version 4.x)

# 1. Browser Initialization
# Initialize a browser (Firefox/Chrome/Edge)

from selenium import webdriver

# Firefox
browser = webdriver.Firefox()

# Chrome
# browser = webdriver.Chrome()

# Edge
# browser = webdriver.Edge()


# 2. Open a Webpage
# Open the target page using the .get() method

browser.get("https://example.com")


# 3. Locating Elements
# Various ways to locate elements on the page

from selenium.webdriver.common.by import By

# Find an element by ID
elem = browser.find_element(By.ID, 'element-id')

# Find an element by Name
elem = browser.find_element(By.NAME, 'element-name')

# Find an element by Class Name
elem = browser.find_element(By.CLASS_NAME, 'class-name')

# Find an element by CSS Selector
elem = browser.find_element(By.CSS_SELECTOR, '.css-class')

# Find an element by XPath
elem = browser.find_element(By.XPATH, '//div[@id="example"]')

# Find an element by Link Text
elem = browser.find_element(By.LINK_TEXT, 'Click here')

# Find an element by Partial Link Text
elem = browser.find_element(By.PARTIAL_LINK_TEXT, 'Click')


# 4. Interacting with Elements
# Perform actions like clicking or typing on the element

# Clicking an element
elem.click()

# Typing into a text field
elem.send_keys("Hello World")

# Clearing a text field
elem.clear()

# Submitting a form
form_element = browser.find_element(By.ID, 'form-id')
form_element.submit()


# 5. Waiting for Elements
# Use explicit or implicit waits to ensure the element is present

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Implicit wait (wait for 10 seconds for elements to appear)
browser.implicitly_wait(10)

# Explicit wait (wait up to 10 seconds for a specific element)
elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'element-id'))
)


# 6. Handling Alerts/Popups
# Switch to an alert and interact with it

alert = browser.switch_to.alert
alert.accept()  # Accepts the alert
alert.dismiss()  # Dismisses the alert


# 7. Handling Frames
# Switch to a frame, and switch back to the default content

browser.switch_to.frame('frame_name_or_id')
browser.switch_to.default_content()


# 8. Navigating Browser
# Perform browser actions like going back or forward in history

browser.back()   # Go back
browser.forward()  # Go forward

# Refresh the page
browser.refresh()


# 9. Taking Screenshots
# Capture a screenshot of the current page

browser.save_screenshot('screenshot.png')


# 10. Scrolling
# Scroll to a specific element

element = browser.find_element(By.ID, 'some_id')
browser.execute_script("arguments[0].scrollIntoView();", element)


# 11. Managing Cookies
# Add, get, or delete cookies

# Get all cookies
cookies = browser.get_cookies()

# Add a cookie
browser.add_cookie({'name': 'test_cookie', 'value': 'cookie_value'})

# Delete a cookie
browser.delete_cookie('test_cookie')


# 12. Closing the Browser
# Close the current tab or the entire browser

browser.close()  # Close current tab
browser.quit()   # Close all tabs and quit browser


# 13. Handling JavaScript Executions
# Execute JavaScript commands on the page

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# 14. Handling Dropdowns (Select)
# Interact with dropdown menus using the Select class

from selenium.webdriver.support.ui import Select

dropdown = Select(browser.find_element(By.ID, 'dropdown-id'))
dropdown.select_by_visible_text('Option Text')
dropdown.select_by_value('option_value')
dropdown.select_by_index(1)


# 15. Handling Multiple Windows
# Switch between multiple browser windows or tabs

browser.switch_to.window(browser.window_handles[1])  # Switch to new tab

# Close current window and switch back
browser.close()
browser.switch_to.window(browser.window_handles[0])


# 16. File Uploads
# Upload a file by sending the file path to an <input> element

upload_element = browser.find_element(By.ID, 'upload-id')
upload_element.send_keys('/path/to/file')


# 17. Debugging Tools
# Retrieve page source, current URL, or title

# Get the HTML source of the page
html = browser.page_source

# Get the current URL
current_url = browser.current_url

# Get the title of the page
title = browser.title
