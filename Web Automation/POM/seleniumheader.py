from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


class seleniumheader():

    def Driver(self):
        self.driver = webdriver.Chrome("C:/Users/Gopinath/Downloads/chromedriver_win32 (1)/chromedriver.exe")
        

    def URL(self,Url):
        self.driver.get(Url)

    def maxwin(self):
        return self.driver.maximize_window()

    def sendKeys(self,selement,data):
        selement.send_keys(data)

    def PassendKeys(self,Pelement,data):
        Pelement.send_keys(data)

    def click(self,element):
        element.click()

    def acccount(self,element):
        element.click()

    def timesleep(self,sec):
        time.sleep(sec)

    def Month(self,a):
        self.a = Select(a)

    def xmonth(self,b):
        self.a.select_by_value(b)



