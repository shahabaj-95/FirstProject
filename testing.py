from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
#from selenium.webdriver.support.select import Select
class AmazonTest:
    def __init__(self, username, password):
        self.driver=webdriver.Chrome("C:\Users\shaik.shahabaj\Documents\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://www.amazon.com")
        self.driver.maximize_window()
        self.username=username
        self.password=password
        self.actions = ActionChains(self.driver)

    def login(self):
        self.actions.move_to_element('#nav-tools>a[id="nav-link-accountList"]')
        self.driver.find_element_by_css_selector('#nav-signin-tooltip>a').click()
        if self.driver.find_element_by_css_selector('#a-page').is_displayed():
            email_id=self.driver.find_element_by_css_selector('[type="email"]')
            email_id.send_keys(self.username)
            self.driver.find_element_by_css_selector('div>#continue').click()
            password=self.driver.find_element_by_css_selector('[type="password"]')
            password.send_keys(self.password)
            self.driver.find_element_by_css_selector('div>#auth-signin-button').click()
            try:
                if self.driver.find_element_by_css_selector('#continue').is_displayed():
                    self.driver.find_element_by_css_selector('#continue').click()
                    self.driver.find_element_by_css_selector('[type="text"]').send_keys("900019")
            except NoSuchElementException:
                pass

    def click_hamburger_menu(self):
        #WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, "#nav-belt>div>a>i")))
        #yes
        try:
            self.driver.find_element_by_css_selector('#nav-belt>div>a>i').click()
        except TimeoutException:
            self.driver.find_element_by_css_selector('#nav-belt>div>a>i').click()


    def menu_items(self, menu_item, sub_menu_items):
        #self.driver.implicitly_wait(10)
        try:
            WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.ID, "#hmenu-content")))
        except TimeoutException:
            if self.driver.find_element_by_css_selector("#hmenu-canvas").is_displayed():
                drop_down_menu_item=self.driver.find_element_by_xpath('//div[contains(text(),"%s")]' %menu_item)
                drop_down_menu_item.click()
        self.click_submenu_items(sub_menu_items)

    def click_submenu_items(self,sub_menu_items_list):
        if self.driver.find_element_by_css_selector(".hmenu-visible.hmenu-translateX").is_displayed():
            actual_sub_menu_items=self.driver.find_elements_by_css_selector('.hmenu-visible.hmenu-translateX li a')
            for sub_menu_item in sub_menu_items_list:
                print "{0}".format(sub_menu_item)
                self.driver.find_element_by_xpath('//li/a[contains(text(),"%s")]'%sub_menu_item).click()
                self.driver.find_element_by_xpath('//a[contains(text(),"%s")]'%sub_menu_item).is_displayed()


    def teardown(self):
        amazon_obj.driver.quit()

amazon_obj=AmazonTest("shahabaj.95@gmail.com","SHAHABAJ@1995")
amazon_obj.login()
amazon_obj.click_hamburger_menu()
menu_items=["Amazon Music", "Fire TV"]
sub_menu_items=["Amazon Music Unlimited", "Prime Music", "Fire TV Stick", "Fire TV Recast"]
for menu_item in menu_items:
    amazon_obj.menu_items(menu_item, sub_menu_items)
amazon_obj.teardown()

# if __name__=="__main__":
#   login()
#  click_hamburger_menu()


