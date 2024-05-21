from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from csv import writer
from tkinter import *
import time





def cutNum():
    # list to store file lines
    lines = []
    # read file
    with open('Price.txt', 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()

    # Write file
    with open('Price.txt', 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            # delete line 1. or pass any Nth line you want to remove
            # note list index starts from 0
            if number not in [0]:
                fp.write(line)


#Search in each State
def bestDealer(driver):
    cutNum()

    with open('Price.txt', 'r') as address:
        address_final = address.readline()
        getToCategories(driver)
        address_input = driver.find_element(By.ID, 'textField-address_input')
        address_input.click()
        time.sleep(1)
        address_input.clear()
        address_input.send_keys(address_final + Keys.ENTER)
        categoriesSearch(driver)
        selectDealer(driver)

        address.close()

def priceRecorder(driver, id):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[1]/div/div[2]/div/div[1]/div[2]"))
    )
    time.sleep(4)
    content = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div/div[2]/div/div[1]/div[2]")
    price = content.text
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/header/div[3]/div[2]/div/div/section/section[2]/button[2]/div/div/p"))
    )
    time.sleep(4)
    content_address = driver.find_element(By.XPATH, "/html/body/header/div[3]/div[2]/div/div/section/section[2]/button[2]/div/div/p")
    address = content_address.text

    list = [price, address]

    if id == 0:
        with open('PRICEFILE.csv', 'w', newline='') as f_object:
            f_object.close()
    
    with open('PRICEFILE.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(list)
        f_object.close()

    price = price.replace('"', '')
    price = price.replace('$', '')
    price = price.replace(',', '')
    newPrice = float(price)

    if id == 0 or id == 1:
        with open('Price.txt', 'w') as f_object:
            f_object.close()
    
        with open('Price.txt', 'a') as f_object:
            f_object.write(str(price))
            f_object.write("\n" + address)
            f_object.close()
    else:
        with open('Price.txt', 'r') as file:
            file_read = file.readline()
            if newPrice < float(file_read):
                file.close()
                with open('Price.txt', 'w') as f_object:
                    f_object.close()
    
                with open('Price.txt', 'a') as f_object:
                    f_object.write(price + "\n")
                    f_object.write(address)
                    f_object.close()
    

def selectDealer(driver):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='select-dealer-button']"))
    )

    select_dealer = driver.find_element(By.XPATH, "//*[@id='select-dealer-button']")
    select_dealer.click()

def categoriesSearch(driver):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Agriculture')]"))
    )
    search_category = driver.find_element(By.XPATH, "//*[contains(text(), 'Agriculture')]")
    search_category.click()

#Algorithm that gets you to the categories part
def getToCategories(driver):

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption css-rjwcd0']"))
    )

    try:
        search_dealer = driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption css-rjwcd0']")
        search_dealer.click()
    except:
        driver.refresh()
        search_dealer = driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption css-rjwcd0']")
        search_dealer.click()

    try:
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1ctp0ih']"))
    )
        
        link = driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1ctp0ih']")
        link.click()
    except:
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'See More Dealers')]"))
    )
        
        link = driver.find_element(By.XPATH, "//*[contains(text(), 'See More Dealers')]")
        link.click()

#Search in each State
def state_search(driver, id):
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Minor Outlying Islands', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'U.S. Virgin Islands', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

    try:

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption css-n3ds9y']"))
        )

        try:
            search_dealer = driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption css-n3ds9y']")
            search_dealer.click()
        except:
            driver.refresh()
            search_dealer = driver.find_element(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption css-n3ds9y']")
            search_dealer.click()

        address_input = driver.find_element(By.ID, 'textField-address_input')
        address_input.click()
        time.sleep(2)
        address_input.clear()
        address_input.send_keys(states[id] + Keys.ENTER)
        time.sleep(2)
        categoriesSearch(driver)
        selectDealer(driver)
    except:
        priceRecorder(driver, id)
        getToCategories(driver)
        address_input = driver.find_element(By.ID, 'textField-address_input')
        address_input.click()
        time.sleep(2)
        address_input.clear()
        address_input.send_keys(states[id] + Keys.ENTER)
        time.sleep(2)
        categoriesSearch(driver)
        selectDealer(driver)

#Main search algorithm
def search(tag):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://shop.deere.com/us")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'searchTriggerInput'))
    )

    input_element = driver.find_element(By.ID, 'searchTriggerInput')
    input_element.click()

    input_element = driver.find_element(By.ID, 'search-box')
    input_element.send_keys(tag + Keys.ENTER)

    with open('PRICEFILE.csv', 'w', newline='') as f_object:
            f_object.close()

    for i in range(0, 50):
        state_search(driver, i)

    bestDealer(driver)


    time.sleep(480)

    driver.quit()

#Interface for input of the product ID
def interface():
    root = Tk()

    e = Entry(root, width=50)
    e.pack()

    #Click the button to launch the search algorithm
    def myClick():
        myLabel = Label(root, text="Search In Progress!")
        myLabel.pack()
        search(e.get())
        

    myButton = Button(root, text="Search", command=myClick)
    myButton.pack()

    root.mainloop()

interface()