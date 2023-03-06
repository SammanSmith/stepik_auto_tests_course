from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element(By.ID, 'treasure')
    val = img.get_attribute('valuex')

    funcX = calc(val)

    browser.find_element(By.ID, 'answer').send_keys(funcX)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()


except:
    pass

finally:
    time.sleep(10)
    browser.quit()

