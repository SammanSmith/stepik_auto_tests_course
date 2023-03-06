from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()
    # browser.switch_to.alert.accept()

    fw = browser.window_handles[0]
    sw = browser.window_handles[1]

    browser.switch_to.window(sw)
    x = browser.find_element(By.ID, 'input_value').text
    x = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(x)

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()