from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    print("x:", x)

try:
    value = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    print("y is - ", y)

    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("solve").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    answ = alert_text.split(': ')[-1]
    print("answ: ", answ)
    alert.accept()

    browser.get("https://stepik.org/catalog?auth=login")
    browser.find_element_by_id("id_login_email").send_keys('klimova.ek.ser@yandex.by')
    browser.find_element_by_id("id_login_password").send_keys('QWas12ed34')
    browser.find_element_by_class_name("sign-form__btn.button_with-loader").click()

    time.sleep(5)
    browser.get('https://stepik.org/lesson/181384/step/8?auth=login&unit=156009')
    time.sleep(15)
   # browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input = browser.find_element_by_id("ember364")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answ)
    but1 = browser.find_element_by_class_name("submit-submission")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", but1)
    but1.click()

finally:
    time.sleep(10)
    #browser.quit()

