from celery import shared_task
from selenium import webdriver
import time
from myapp.models import BookModel

@shared_task
def scrape(url):
    path = r'C:\Users\a\Desktop\Driver\chromedriver.exe'

    driver = webdriver.Chrome(executable_path=path)
    time.sleep(2)
    driver.maximize_window()

    driver.get(url)
    print("In driver")

    try:
        page = 0
        while True:
            page += 1
            print("page = ", page)
            elements = driver.find_elements_by_xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']")
            time.sleep(2)
            for x in elements:
                a_tag = x.find_element_by_xpath(".//h3//a")
                d_href = a_tag.get_attribute('href')
                # print("href ", a_tag.get_attribute('href'))
                d_title = a_tag.get_attribute('title')
                # print("title ", a_tag.get_attribute('title'))
                d_price = x.find_element_by_xpath(".//div[@class='product_price']/p[@class='price_color']").text
                # print("price ", x.find_element_by_xpath(".//div[@class='product_price']/p[@class='price_color']").text)

                book = BookModel(title=d_title, price=d_price, plink=d_href)
                book.save()
            try:
                next_button = driver.find_element_by_xpath("//li[@class='next']/a")
                next_button.click()
                print("Click execute")
                time.sleep(2)
            except Exception as e:
                print("No Next Button found, last page")
                break

    except Exception as e:
        print("error ", e)
    driver.quit()