
#This Bot was created by OBI.8045 on discord you can contact me there if you have any problems.
#If you want to get an item that isn't usually in stock use this script.
#Make sure to run this bot at least 5 minutes or more before the item comes in stock. 
#I hope you like it!

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#This is the sign in page for amazon
URL = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
#Put in the item you would like to buy in BUYURL
BUYURL = "https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-Tech-2-9-Slot/dp/B08J6F174Z"

#Put your email in here
email = "ralphobi2008@gmail.com"
#Put your password in here
password = "Grange2019"

driver.get(URL)

def login():
    #Finds the entry element on the page
    emailEntry = driver.find_element_by_id("ap_email")
    #Sends your email into the page
    emailEntry.send_keys(email)
    time.sleep(1)

    #Gets the continue button
    emailBtn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
    #Clicks on the continue button
    emailBtn.click()

    #Puts your password in
    passwordEntry = driver.find_element_by_id("ap_password")
    passwordEntry.send_keys(password)
    #Waits one second
    time.sleep(1)
    
    #Clicks password button
    passwordBtn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input")
    passwordBtn.click()
    #Calls the search function
    Search()

def Search():
    time.sleep(1)
    driver.get(BUYURL)
    while True:
        try:
            buyBtn = driver.find_element_by_id("buy-now-button")
            print("The item, {} is in stock.".format(driver.title))
            buyBtn.click()
            break
        except:
            driver.implicitly_wait(1.5)
            print("The item, {} is not in stock and I am refreshing the page.".format(driver.title))
            driver.refresh()

login()