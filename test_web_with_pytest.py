# install pytest (pip instal pytest)
# Any pytest file should start with test_ or end with _test
# Any test method names should start with test
# Any code should be wrapped in method only
# Method name should make sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# you can run specific file with py-test <filename>
# -m stands for run test with mark (tag)
# you can skip testcase with @pytest.mark.skip
# you can ovid showing the result using @pytest.mark.xfail
# for get the html report install (pip install pytest-html)
# for run the test and get report open an comand prompt,
# cd to the folder where is this project
# run pytest --html=report.html

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_1():
    driver = webdriver.Chrome()  # .Firefox()
    driver.get("https://practicesoftwaretesting.com/")
    driver.implicitly_wait(5)  # 5 seconds max timeout for all process
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#search-query").send_keys("ham")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    hammer_products = driver.find_elements(By.XPATH, "//*[contains(text(), 'Hammer')]")
    hammer_number = len(hammer_products)
    assert hammer_number == 7


def test_2():
    driver = webdriver.Chrome()  # .Firefox()
    driver.get("https://practicesoftwaretesting.com/")
    driver.implicitly_wait(5)  # 5 seconds max timeout for all process
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#search-query").send_keys("wren")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    wrench_products = driver.find_elements(By.XPATH, "//*[contains(text(), 'Wrench')]")
    wrench_number = len(wrench_products)
    assert wrench_number == 3, "Number of Wrench products different than expected"
    driver.close()


def test_3():
    driver = webdriver.Chrome()  # .Firefox()
    driver.get("https://practicesoftwaretesting.com/")
    driver.implicitly_wait(5)  # 5 seconds max timeout for all process
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, ".card").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#btn-add-to-cart").click()
    price_1 = driver.find_element(By.CSS_SELECTOR, "span[aria-label='unit-price']").text
    time.sleep(2)
    driver.back()
    driver.find_element(By.CSS_SELECTOR, "img[alt='Pliers']").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#btn-add-to-cart").click()
    price_2 = driver.find_element(By.CSS_SELECTOR, "span[aria-label='unit-price']").text
    driver.back()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".ng-fa-icon.px-1").click()
    time.sleep(10)
    cart_price = driver.find_element(By.CSS_SELECTOR, "td[data-test='cart-total']").text
    assert float(cart_price[1:]) == float(price_1) + float(price_2), "Total cart price not correct"
    driver.close()