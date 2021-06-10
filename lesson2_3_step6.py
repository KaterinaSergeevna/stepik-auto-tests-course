from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    browser.find_element_by_class_name("trollface.btn.btn-primary").click()
    
    first_win = browser.window_handles[0]
    new_win = browser.window_handles[1]

    browser.switch_to.window(new_win)

    x = browser.find_element_by_id("input_value").text
    print("x", x)
    y = calc(x)
    print("y", y)

    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_class_name("btn.btn-primary").click()

    alert = browser.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    answer = alert_text[-1]
    print("answer", answer)
 
    browser.get("https://stepik.org/catalog?auth=login&language=ru")   
    time.sleep(1)

    browser.find_element_by_id("id_login_email").send_keys("klimova.ek.ser@yandex.by")
    browser.find_element_by_id("id_login_password").send_keys("********")
    
    browser.find_element_by_class_name('sign-form__btn').click()  
    time.sleep(3)
    browser.get('https://stepik.org/lesson/184253/step/6?auth=login&unit=158843')
    time.sleep(3)  

    answer_input = browser.find_element_by_css_selector('textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)

    button = browser.find_element_by_class_name('submit-submission')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()

finally:
    time.sleep(1)

    