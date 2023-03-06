from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x.text
    xx = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(xx)

    chkbtn = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    chkbtn.click()

    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()

    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()