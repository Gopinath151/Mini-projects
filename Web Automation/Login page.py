from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Gopinath/Downloads/chromedriver_win32 (1)/chromedriver.exe")

driver.get("https://www.facebook.com")

#Auto login code for facebook

emailelement = driver.find_element("name","email")
emailelement.send_keys("**********")

passelement = driver.find_element("name","pass")
passelement.send_keys("**********")

login = driver.find_element("xpath","//button[@name='login']")
login.click()

# Auto Login code for instagram

driver.get("https://www.instagram.com")

email_element = driver.find_element("id","email")
email_element.send_keys("***********")

pass_element = driver.find_element("id","pass")
pass_element.send_keys("************")