from selenium import webdriver
import time

link = "http://suninjuly.github.io/wait1.html"


browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5)

browser.find_element_by_id("verify").click()

mes = browser.find_element_by_id("verify_message")
assert "successful" in mes.text