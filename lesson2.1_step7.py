from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sunduk = browser.find_element_by_id("treasure")
    x = sunduk.get_attribute("valuex")
    y = calc(x)

    answ = browser.find_element_by_id("answer")
    answ.send_keys(y)

    rob = browser.find_element_by_id("robotCheckbox")
    rob.click()

    rob_rule = browser.find_element_by_id("robotsRule")
    rob_rule.click()

    button_sub = browser.find_element_by_class_name("btn.btn-default")
    button_sub.click()

finally:
    time.sleep(10)
    browser.quit()
    browser.close()

