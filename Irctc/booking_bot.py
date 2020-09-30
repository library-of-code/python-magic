import os, time, random, sys
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# Your credentiality
name = "YOUR_NAME"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
dob = "YOUR_DOB"
email = "YOUR_EMAIL"
phone =
address1 = "BUILDING NO. "
address2 = "rEMAINING_ADDRESS"
pincode = "PINCODE_YOUR_ADDRESS"
desti = "DESTINATION"
start = "START"
age = "YOUR_AGE"

website = "https://www.irctc.co.in/nget/train-search"
browser = webdriver.Chrome('driver/chromedriver.exe')
browser.maximize_window()
browser.get(website)
time.sleep(0.5)
browser.find_element_by_xpath("//button[@class=\"btn btn-primary\"]").click()#ng-star-inserted
time.sleep(2)
# browser.find_element_by_xpath("//a[@class=\"ng-star-inserted\"]").click() # Click on login ourself
try:
    browser.find_element_by_xpath("//input[@id=\"userId\"]").send_keys(username)
except:
    time.sleep(2)
    browser.find_element_by_xpath("//input[@id=\"userId\"]").send_keys(username)
browser.find_element_by_xpath("//input[@id=\"pwd\"]").send_keys(password)
# Capcha time
## ENTER CAPCHA ON YOUR OWN
time.sleep(5)

# We are logged in
print(browser.find_element_by_xpath("//input[@id=\"userId\"]"))
while(1):
    try:
        browser.find_element_by_xpath("//input[@id=\"userId\"]")
        print("Extending")
        print(browser.find_element_by_xpath("//input[@id=\"userId\"]"))
        time.sleep(2)
    except:
        print("Breaking.....")
        break

text = browser.find_element_by_xpath('/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/span[1]').get_attribute("innerHTML")

print(text)

browser.find_element_by_xpath('//*[@id="origin"]/span/input').send_keys(start)
browser.find_element_by_xpath('//*[@id="destination"]/span/input').send_keys(desti)
# Date Manually
browser.find_element_by_xpath("//button[@label=\"Find Trains\"]").click()
text = browser.find_element_by_xpath('/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/span[1]').get_attribute("innerHTML")
time.sleep(5)
# browser.find_element_by_xpath()
while(1):
    try:
        browser.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[1]/div/div[3]/p-footer/div/button[2]/span[2]').click()
    except:
        print("Extending due to loading thing")
        time.sleep(0.2)
        continue
    break

while(1):
    try:
        browser.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[2]/div/div[3]/p-footer/div/button[2]/span[2]').click()
    except:
        print("Extending due to loading thing")
        time.sleep(0.1)
        continue
    break

# Form filling

while(1):
    try:
        browser.find_element_by_xpath("//input[@placeholder=\" Name\"]").send_keys(name)
    except:
        print("Extending due to loading thing")
        time.sleep(0.01)
        continue
    break

# browser.find_element_by_xpath("//input[@placeholder=\"Name\"]").send_keys("Ayush Gupta")
browser.find_element_by_xpath("//input[@placeholder=\"Age\"]").send_keys(age)
# time.sleep(2)
browser.find_element_by_xpath("//select[@formcontrolname='passengerGender']/option[text()='Male']").click()
try:
    browser.find_element_by_xpath("//select[@formcontrolname='passengerBerthChoice']/option[text()='Upper']").click()
except:
    print("Option not available")
    browser.find_element_by_xpath("//select[@formcontrolname='passengerBerthChoice']/option[text()='Window Side']").click()

try:
    browser.find_element_by_xpath("//label[@for=\"confirmberths\"]").click() ##
except:
    print("Game Over")
try:
    browser.find_element_by_xpath("//label[@for=\"travelInsuranceOptedYes\"]").click() ##
except:
    print("Game Over")
try:
    browser.find_element_by_xpath("//label[@for=\"autoUpgradation\"]").click()  ##
except:
    print("Still a chance")

browser.find_element_by_xpath("//input[@placeholder=\"Correspondence 1 *\"]").send_keys(address1)
browser.find_element_by_xpath("//input[@placeholder=\"Correspondence 2 (Optional)\"]").send_keys(address2)
# browser.find_element_by_xpath("//input[@placeholder=\"Correspondence 3 (Optional)\"]").send_keys("Correspondence 2 (Optional)")
browser.find_element_by_xpath("//input[@placeholder=\"PIN *\"]").send_keys(pincode)
browser.find_element_by_xpath("//label[@for=\"2\"]").click()
time.sleep(1.5)
browser.find_element_by_xpath("//label[@for=\"2\"]").send_keys(Keys.ENTER)

while(1):
    try:
        text = browser.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/p-dialog/div/div[2]/p').get_attribute('innerHTML')
    except:
        print("Text not found")
        continue
        time.sleep(0.005)
    break

flag = 1
lst = text.split()
if lst[-2] == 'mobile':
    key = phone
    browser.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/p-dialog/div/div[2]/div/span/input').send_keys(key)
elif lst[-1] == 'ID':
    key = email
    browser.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/p-dialog/div/div[2]/div/span/input').send_keys(key)
elif lst[-2] == 'ddMMyyyy':
    key = dob
    browser.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/p-dialog/div/div[2]/div/span/input').send_keys(key)
elif lst[-2] == '':
    browser.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/p-dialog/div/div[2]/div/div[1]/button').click()
    flag = 0
else:
    print("We can't do anything")
    flag = 0

try:
    if flag:
        browser.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/p-dialog/div/div[2]/div/button').click()
except:
    print("There's some issue")

while(1):
    url = browser.current_url
    if (url.endswith('reviewBooking')):
        break
    # try:
    #     browser.find_element_by_xpath('//span[contain(text(), " Availability Status: ")]')
    # except:
    #     continue
    # browser.execute_script("window.scrollBy(0,window.innerHeight)")
    # break

# Going to the filled form verification page

browser.execute_script("window.scrollBy(0,1000)")
try:
    browser.find_element_by_xpath('//*[@id="recaptcha-anchor-label"]/span').click()
except:
    print("No Issues")

while(1):
    try:
        browser.find_element_by_xpath('//*[@id="divMain"]/div/app-review-booking/div/p-confirmdialog/div/div[3]/p-footer/div/button[2]/span[2]').click()
    except:
        print("Extending due to loading thing")
        time.sleep(0.05)
        continue
    break

#

while(1):
    try:
        browser.find_element_by_xpath('//*[@id="ui-tabpanel-1-label"]/span').click() #("//spam[contains(text(), 'BHIM/ UPI/ USSD')]").click()
    except:
        print("Extending due to loading thing")
        time.sleep(0.02)
        continue
    break

browser.find_element_by_xpath("//label[@for='bank_117']").click()
time.sleep(0.01)
browser.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/app-payment-options/div/div[4]/div/div[3]/div[2]/div[1]/app-payment/div[4]/div/form/p-tabview/div/div/p-tabpanel[2]/div/div[2]/div[1]/div/div/div/button').click()

# browser.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form').submit()
# Select the desired train

