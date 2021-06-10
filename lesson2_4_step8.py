from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_id("book")

WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button.click()