#to open amazon and switch to multiple windows
from selenium import webdriver
import time

def Amazon():

    driver = webdriver.Chrome("C:/Users/Gopinath/Downloads/chromedriver_win32 (1)/chromedriver.exe")
    driver.get("http://www.amazon.in/")
    driver.maximize_window()
    #driver.implicitly_wait(6)

    search = driver.find_element("id","twotabsearchtextbox")
    search.send_keys("samsung galaxy m20")

    click = driver.find_element("id","nav-search-submit-button")
    click.click()

    element = driver.find_element("xpath","//span[text()='Samsung Galaxy M04 Light Green, 4GB RAM, 64GB Storage | Upto 8GB RAM with RAM Plus | MediaTek Helio P35 | 5000 mAh Battery']")
    element.click()


    driver.switch_to.default_content()

    search = driver.find_element("id","twotabsearchtextbox")
    search.clear()
    search.send_keys("iphone 14 pro")
    click = driver.find_element("id","nav-search-submit-button").click()
    time.sleep(3)

    iphoneelement = driver.find_element("xpath","//span[text()='Apple iPhone 14 Pro Max 128GB Silver']")
    iphoneelement.click()
    time.sleep(3)

    parent_handle = driver.current_window_handle
    window1 = driver.window_handles[0]
    window2 = driver.window_handles[1]

    driver.switch_to.window(window2)

    buy = driver.find_element("xpath", "//input[@id='add-to-cart-button']").click()

Amazon()