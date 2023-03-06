from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.XPATH, '//h2/span[2]').text
    b = browser.find_element(By.XPATH, '//h2/span[4]').text

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(int(a) + int(b)))

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()
