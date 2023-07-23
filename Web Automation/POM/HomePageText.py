from selenium.webdriver.common.by import By
from facebookresuse import LocatorMaintanece

class HomePageText:

    def __init__(self,driver):
        self.driver = driver
        self.facebook_text = driver.find_element(By.XPATH,LocatorMaintanece.facebooktext_xpath)

    def gettxtfacebook(self):
        return self.facebook_text