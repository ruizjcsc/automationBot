import account

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


from selenium.webdriver.common.keys import Keys



class CheckOutBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://us.supreme.com/collections/shirts")
        self.access_Website()

    def access_Website(self):
        #wait is good so that all items load up
        wait = WebDriverWait(self.driver, 10)
        #use wait variable here 
        #EC is expected condition and presence of element is on of the conditions located element with class name
        #button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "display-flex.cursor-pointer.flexWrap-wrap.position-relative")))
        # located element with css selector more specific using the data-cy-title attribute in each a tag

        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-cy-title="Loose Fit Oxford Shirt"]')))

        #trying to see if element is available or not with the data-available attribute not quite working
        #dataAvailable = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-available="true"]')))
        #isEnabled = dataAvailable.get_attribute("boolean")
        #if(isEnabled):
        #    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "display-flex.cursor-pointer.flexWrap-wrap.position-relative")))
        #    button.click()
        
        #button is clicked here
        button.click()

        time.sleep(2)
        #working with select list elements find the selector/list with css locator or other
        #then make a select object (dont forget the import)
        #then use select by visible text which is literally what the user sees on page
        selectSize = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="size-selector"]')))
        selectObj = Select(selectSize)
        selectObj.select_by_visible_text('XLarge')

        

if __name__ == "__main__":
    bot = CheckOutBot()

    time.sleep(20)

    #bot.cleanup()