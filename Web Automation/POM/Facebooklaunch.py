from selenium import webdriver
from reusecode.seleniumheader import seleniumheader
from facebookresuse.HomePages import HomePages
from facebookresuse.HomePageText import HomePageText
import time
class facbook:

    def logintoFacebook(self):
        baseClass = seleniumheader()
        driver = baseClass.Driver()
        baseClass.URL("https://www.facebook.com/")

        home = HomePages(driver)

        baseClass.sendKeys(home.gettxtUser(),"*******")

        baseClass.sendKeys(home.gettxtpass(),"********")

        baseClass.click(home.getBtnLogin())

        time.sleep(20)

fbObj = facbook()
fbObj.logintoFacebook()


"""
Page Object Model, also known as POM, 
is a design pattern in Selenium that 
creates an object repository for storing all web elements. 

Rule 1: Locators maintained in seperate page(file)
Easy to identify
Reuse
Login-> logout
userName_id = "fbemail"

Login --> Reg --> logout
userName_id = "fbemail"

Login --> setting --> logout
userName_id = "fbemail"

Login --> post --> logout
userName_id = "fbemail"

Login --> friendss --> logout
userName_id = "fbemail"
Login --> logout --> logout
userName_id = "fbemail"

200 times
"""