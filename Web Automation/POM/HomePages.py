from selenium.webdriver.common.by import By
from facebookresuse import LocatorMaintanece

class HomePages:
# Setter
#Constructor - it will call automatically when the class creates
    def __init__(self,driver):
        self.driver = driver
        self.userName = driver.find_element(By.ID,LocatorMaintanece.userName_id)
        self.passWord = driver.find_element(By.NAME,LocatorMaintanece.password_name)
        self.btnClick = driver.find_element(By.XPATH, LocatorMaintanece.btnlogin_xpath)

    def gettxtUser(self):
        return self.userName

    def gettxtpass(self):
        return self.passWord

    def getBtnLogin(self):
        return self.btnClick




