import account

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


from selenium.webdriver.common.keys import Keys



class CheckOutBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://us.supreme.com/collections/all")
        self.access_Website()

    def access_Website(self):
        #wait is good so that all items load up
        wait = WebDriverWait(self.driver, 10)
        #use wait variable here 
        #EC is expected condition and presence of element is on of the conditions located element with class name
        #button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "display-flex.cursor-pointer.flexWrap-wrap.position-relative")))
        #located element with css selector more specific using the data-cy-title attribute in each a tag
        item = account.item()
        print(item)
        #formula for finding item by title name works for all products 
        #aslong as you know the official title as presented on the website
        itemSearch = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-cy-title='+'"'+item+'"')))

        #trying to see if element is available or not with the data-available attribute not quite working
        #dataAvailable = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-available="true"]')))
        #isEnabled = dataAvailable.get_attribute("boolean")
        #if(isEnabled):
        #    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "display-flex.cursor-pointer.flexWrap-wrap.position-relative")))
        #    button.click()
        
        #button is clicked here
        itemSearch.click()

        time.sleep(2)

        #working with select list elements find the selector/list with css locator or other
        #then make a select object (dont forget the import)
        #then use select by visible text which is literally what the user sees on page
        size = account.size()
        selectSize = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="size-selector"]')))
        selectObj = Select(selectSize)
        selectObj.select_by_visible_text(''+size+'')

        #adds item to cart standard element locator using css selector and click function
        addToCart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]')))
        addToCart.click()

        
        time.sleep(2)


        # print statement comes out false 
        # so i cant click on it so i will just brute force go to checkout page
        #goToCheckOut = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[data-cy="mini-cart-checkout-button"]')))
        #print((goToCheckOut.is_displayed()))
        #goToCheckOut.click()

        # click keep shopping button and try to go to checkout page from differnt page
        #keepShopping = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'a[href="/pages/shop"]')))
        #keepShopping.click()

        

        # refreshes page
        #self.driver.refresh()

        # fafter adding item to cart i go back a page then i click go to checkout 
        # and that solves the problem of the checkout button not being visiblie on the item screen.

        self.driver.back()

        time.sleep(2)

        goToCheckOut = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-cy="mini-cart-checkout-button"]')))
        print((goToCheckOut.is_displayed()))
        goToCheckOut.click()

        # next step is filling in checkout data like name address etc.


if __name__ == "__main__":
    #set timer so that i can run program and try it manually aswell
    #time.sleep(60)
    bot = CheckOutBot()

    time.sleep(20)

    #bot.cleanup()