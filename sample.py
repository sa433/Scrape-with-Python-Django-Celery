from selenium import webdriver
import time
from selenium.webdriver.common.by import By

path = r'C:\Users\a\Desktop\Driver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=path)
time.sleep(2)
driver.maximize_window()

url = "https://books.toscrape.com/"
driver.get(url)
print("In driver")

try:
    page = 0
    while True:
        page += 1
        print("page = ",page)
        elements = driver.find_elements_by_xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']")
        time.sleep(2)
        for x in elements:
            a_tag = x.find_element_by_xpath(".//h3//a")
            print("href ",a_tag.get_attribute('href'))
            print("title ", a_tag.get_attribute('title'))
            print("price ",x.find_element_by_xpath(".//div[@class='product_price']/p[@class='price_color']").text)
        try:
            next_button = driver.find_element_by_xpath("//li[@class='next']/a")
            next_button.click()
            time.sleep(2)
        except Exception as e:
            print("No Next Button found, last page")
            break
except Exception as e:
    print("error ",e)
driver.quit()