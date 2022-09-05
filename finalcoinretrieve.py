
# coding: utf-8

# In[ ]:


#from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import time

#running headless chrome canary
chrome_options = Options()
chrome_options.add_argument("--headless") 
#chrome_options.binary_location="C:\\Users\\admin\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"

#running chrome in background
driver=webdriver.Chrome('C:\\Users\\admin\\Desktop\\pyexe\\chromedriver.exe',chrome_options=chrome_options)


#general work
driver.implicitly_wait(3)
driver.get("https://info.binance.com/")
waitm=webdriver.support.ui.WebDriverWait
kys=webdriver.common.keys.Keys
x=driver.find_element_by_tag_name('input')






#///////////////function to get list of coin search results
def retrieve():
    
    #driver=webdriver.Chrome('C:\\Users\\admin\\Desktop\\pyexe\\chromedriver.exe')
    x.clear()
    ncoin=input(prompt="enter initials of coin")
    
    
    #sending keys little slower
    for c in ncoin:
        x.send_keys(c)
        time.sleep(0.6)
        
    #for seaarch lists to get accurately
    time.sleep(1.2)
    
    
    #exception if serach list not visible
    try:
        wait = waitm(driver,60)
        ret1=wait.until(EC.presence_of_element_located((By.ID,"search_list")))
    
    except TimeoutException:
        print("nosuchelement and closing driver session")
        driver.close()
    
    #saving links of coin related in list
    list1=[]
    listli=ret1.find_elements_by_tag_name("a")
    for item in listli:
        print(item.get_attribute('href'))
        list1.append(item.get_attribute('href'))

    return list1



#//////function to get coin details//////////////
def get_data(lists):
    list2=[]
    for count in lists:
        # This does not change focus to the new window for the driver.
        driver.execute_script("window.open('');")
        time.sleep(1.5)
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[1])
        driver.get(count)
        time.sleep(1.5)
        data=driver.find_element_by_class_name('media-info')
        list2.append(data.text.split('\n'))
        #cint=data.find_element_by_tag_name('h4')
        #coinint=cint.text
        # close the active tab
        driver.close()
        time.sleep(3)
        # Switch back to the first tab
        driver.switch_to.window(driver.window_handles[0])

    return list2



def print_coin_data(lists3):
    
    for item in lists3:
        print("COIN KEYWORD = " + item[0])
        print("COIN NAME = " + item[1])
        print("COIN PRICE = $ " + item[2])
        print("COIN 24 HOUR CHANGE = " + item[3])
        print('\n')

        
        
        
#///////////////// MAIN PROGRAMMING /////////////////

lists=retrieve()
lists3=get_data(lists)

#//printing data
print_coin_data(lists3)

ans=input("prompt=want another coin details")
ans=ans.lower()

#for recurring input
while ans != 'n' :
    lists=retrieve()
    lists3=get_data(lists)
    
    #//printing data
    print_coin_data(lists3)
    ans=input("prompt=want another coin details")
    ans=ans.lower()
    
driver.close()

#///////////// MAIN PROGRAMMING ENDS HERE ////////

