from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path
def inputCredentials(nameOfElement, value):
    WebDriverWait(driver, waitMS).until(EC.presence_of_element_located((By.NAME, nameOfElement)))
    driver.find_element_by_name(nameOfElement).send_keys(value,Keys.ENTER)
def clickElement(selector):
    WebDriverWait(driver, waitMS).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    driver.find_element_by_css_selector(selector).click()
def getList(typeOfList):
    WebDriverWait(driver, waitMS).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"a[href='/{username}/{typeOfList}/'] > .g47SY ")))
    listSize=int(driver.find_element_by_css_selector(f"a[href='/{username}/{typeOfList}/'] > .g47SY ").text.replace(",",""))
    WebDriverWait(driver, waitMS).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"a[href='/{username}/{typeOfList}/']")))
    driver.find_element_by_css_selector(f"a[href='/{username}/{typeOfList}/']").click()
    textList=[]
    listOfPeople=[]
    while(True):
        try:
            WebDriverWait(driver, waitMS).until(EC.presence_of_element_located((By.CLASS_NAME, "FPmhX")))
            listOfPeople = driver.find_elements_by_class_name("FPmhX")
            if(len(listOfPeople)==listSize):
                break
            driver.execute_script('arguments[0].scrollIntoView()', listOfPeople[-1])
        except:
            pass
    for i in listOfPeople:
        textList.append(i.get_attribute("href"))
    return textList
driver = webdriver.Edge(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
driver.get("https://www.instagram.com/")
readCredentials = open(path.join(path.dirname(__file__), 'Credentials.txt'), "r")
fileLines=readCredentials.read().splitlines()
username=fileLines[0]
waitMS=10000
inputCredentials("username",username)
inputCredentials('password',fileLines[1])
readCredentials.close()
clickElement("img[data-testid='user-avatar']")
clickElement(f"a[href='/{username}/']")
following=getList('following')
clickElement("svg[aria-label='Close']")
followers=getList('followers')
with open(path.join(path.dirname(__file__), f'List Of {username}.txt'), "w+") as listOfNotFollowing:
    for i in following:
        if(not i in followers):
            listOfNotFollowing.write(i+"\n")
driver.quit()