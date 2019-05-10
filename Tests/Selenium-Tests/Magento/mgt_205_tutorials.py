#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, os, errno, argparse, sys, random, string
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MagentoTests:
    def __init__(self):
        # UPDATE HERE (1/5)
        self.main_page = 'http://localhost:8085/magento-2.0.5/'
        self.admin_page = 'http://localhost:8085/magento-2.0.5/admin'
        print "[+] Setting up ChromeDriver"
        options = webdriver.chrome.options.Options()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.add_cookies()
        self.new_username = 'test@gmail.com'
        self.logged_in = False
    def switch_to_firefox(self):
        print "[+] Setting up GeckoDriver"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        self.add_cookies()
    def add_cookies(self):
        # Fix for https://stackoverflow.com/a/28331099/1821461
        # Must load static content not to change code coverage outcome
        self.driver.get(self.main_page + 'LICENSE.txt')
        # UPDATE HERE (2/5)
        self.driver.add_cookie({'name': 'test_group', 'value': 'mgt205_tutorials'})
        # UPDATE HERE (3/5)
        self.driver.add_cookie({'name': 'test_name', 'value': 'mgt_login_mgt205_tutorials'})
        # UPDATE HERE (4/5)
        self.driver.add_cookie({'name': 'software_id', 'value': '3'})
        # UPDATE HERE (5/5)
        self.driver.add_cookie({'name': 'software_version_id', 'value': '11'})
    def set_test_name(self, test_name):
        self.driver.delete_cookie('test_name')
        self.driver.add_cookie({'name': 'test_name', 'value': test_name})
    def click_element(self, xpath_selector, scroll=True):
        try:
            time.sleep(1)
            self.wait_for_loading_message()
            self.wait_for_element_become_visible(xpath_selector)

            element = self.driver.find_element(By.XPATH, xpath_selector)
            if scroll:
                self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-100);", element)
            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath_selector)))
            element.click()
        except Exception as e:
            print '[-] Failed to click on element'
            print e
    def hover_element(self, xpath_selector):
        try:
            self.wait_for_loading_message()
            action=ActionChains(self.driver)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-100);", element)
            action.move_to_element(element).perform()
        except Exception as e:
            print '[-] Failed to hover element'
            print e
    def fill_textbox(self, xpath_selector, text):
        try:
            self.wait_for_loading_message()
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-100);", element)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print '[-] Failed to fill textbox'
            print e
    def toggle_checkbox(self, xpath_selector, enable=True):
        try:
            self.wait_for_loading_message()
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-100);", element)
            if element.is_selected() != enable:
                element.click()
        except Exception as e:
            print '[-] Failed to enable checkbox'
            print e
    def select_dropdown(self, xpath_selector, text=None, timeout=360):
        try:
            self.wait_for_loading_message()
            self.wait_for_element_become_visible(xpath_selector, timeout=timeout)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-100);", element)
            if text != None:
                Select(element).select_by_visible_text(text)
            # Select 1st element
            else:
                Select(element).select_by_index(1)
        except Exception as e:
            print '[-] Failed to select option'
            print e
    def check_exists_and_visible_by_xpath(self, xpath_selector):
        try :
            return self.driver.find_element_by_xpath(xpath_selector).is_displayed()
        except NoSuchElementException :
            return False
        return True
    def wait_for_element_become_visible(self, xpath_selector, timeout=360) :
        item_timeout = timeout
        while not self.check_exists_and_visible_by_xpath(xpath_selector) :
            if item_timeout == timeout :
                print "[+] Waiting for %s to become visible" % xpath_selector,
            else :
                print '.',
            # Wait for login pop up to load via ajax
            time.sleep(1)
            item_timeout = item_timeout - 1
            if item_timeout == 0 :
                print "[-] Timed out %s" % xpath_selector
                return None
        if item_timeout != timeout:
            print ''
    def wait_for_text_in_page(self, text) :
        timeout = 360
        #self.wait_for_loading_message()
        try :
            if self.check_exists_and_visible_by_xpath('//*[@data-role="closeBtn"]'):
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except:
            pass
        while not text in self.driver.page_source :
            print "[+] Waiting for text: %s to load in page" % text
            time.sleep(1)
            timeout = timeout - 1
            #self.wait_for_loading_message()
            if timeout <= 0 :
                print "[-] Timed out %s" % text
                return False
        try :
            if self.check_exists_and_visible_by_xpath('//*[@data-role="closeBtn"]'):
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except:
            pass
        return True
    def wait_for_loading_message(self):
        timeout = 30
        if self.check_exists_and_visible_by_xpath('//button[@data-role="closeBtn"]'):
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
        while self.check_exists_and_visible_by_xpath('//*[contains(text(), "Please wait")]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="billing-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="payment-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="shipping-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="shipping-method-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="review-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[contains(text(), "Submitting order information")]') \
            or self.check_exists_and_visible_by_xpath('//div[@class="admin__data-grid-loading-mask"]'):
            time.sleep(1)
            timeout = timeout - 1
            if timeout <= 0:
                break
        if self.check_exists_and_visible_by_xpath('//button[@data-role="closeBtn"]'):
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

    def login(self, current_page=False, username=None, password=None):
        self.set_test_name('mgt_login')
        print "[*] Starting login process..."
        if self.logged_in:
            print '[+] Already logged in, skipping.'
            return
        if not current_page:
            self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Enter Username
            self.fill_textbox('//*[@id="username"]', 'admin' if username == None else username)
            # Enter password
            self.fill_textbox('//*[@id="login"]', 'zaq1@WSX' if password == None else password)
            # Click submit
            self.click_element('//span[text()="Sign in"]')
            time.sleep(3)
            if not self.wait_for_text_in_page('Sign Out') :
                 print '[-] Login failed'
            else :
                self.logged_in = True
                print '[+] Login successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
        self.close_popup()

    def close_popup(self):
        if self.check_exists_and_visible_by_xpath('//span[@data-dismiss="popup"]'):
            self.click_element('//span[@data-dismiss="popup"]')

    def logout(self):
        self.set_test_name('mgt_logout')
        print "[*] Starting logout process..."
        try:
            self.click_element('//span[@class="admin-user-account-text"]')
            self.click_element('//a[@class="account-signout"]')
            if not self.wait_for_text_in_page('Sign in') :
                 print '[-] Logout failed'
            else :
                self.logged_in = False
                print '[+] Logout successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def create_page(self):
        self.login()
        self.set_test_name('mgt_create_page')
        print "[*] Starting create page process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create catalog
            time.sleep(3)
            self.click_element('//*[@id="menu-magento-backend-content"]')
            self.click_element('//*[@data-ui-id="menu-magento-cms-cms-page"]')
            self.click_element('//*[@id="add"]')

            self.fill_textbox('//*[@id="page_title"]', 'page title ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="page_store_id"]', 'All Store Views')

            self.click_element('//*[@id="page_tabs_content_section"]')
            self.fill_textbox('//*[@id="page_content_heading"]', 'page heading ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//*[@id="togglepage_content"]')
            time.sleep(2)
            self.click_element('//*[@id="togglepage_content"]')
            self.fill_textbox('//*[@id="page_content"]', 'page content ' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('ou saved this page.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def quickedit_page(self):
        self.login()
        self.set_test_name('mgt_quickedit_page')
        print "[*] Starting quick edit page process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-content"]')
            self.click_element('//*[@data-ui-id="menu-magento-cms-cms-page"]')

            self.click_element('//*[@id="container"]/div/div[5]/table/tbody/tr[last()]/td[10]/div/button/span')
            self.click_element('//*[@id="container"]/div/div[5]/table/tbody/tr[last()]/td[10]/div/ul/li[1]/a')
            self.click_element('//*[@id="save"]')

            self.click_element('//*[@id="container"]/div/div[5]/table/tbody/tr[last()]/td[3]')

            self.click_element('//button[@class="action-primary"]//span[text()="Save"]')

            if self.wait_for_text_in_page('You saved this page.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_products(self):
        self.login()
        self.set_test_name('mgt_setup_products')
        print "[*] Starting setup products process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Add Product
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')
            self.click_element('//*[@id="add_new_product-button"]')
            self.fill_textbox('//*[@id="name"]', 'product name ' + ''.join(random.choice(string.digits) for _ in range(10)))
            #self.fill_textbox('//*[@id="sku"]', ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="price"]', ''.join(random.choice(string.digits) for _ in range(5)))
            #current_dir = os.path.dirname(os.path.realpath(__file__))
            #self.fill_textbox('//*[@name="image"]', current_dir + '/headphones.jpg'))

            self.click_element('//*[@id="save-split-button-button"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '[-] (1/3) Test failed'
            else :
                print '[+] (1/3) Test successful'

            # Edit and Add Video
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')
            self.click_element('//*[@id="container"]/div/div[3]/table/tbody/tr[1]/td[13]/a')
            self.click_element('//*[@id="add_video_button"]')
            self.fill_textbox('//*[@id="video_url"]', 'https://vimeo.com/152848165')
            self.fill_textbox('//*[@id="video_title"]', 'test video')

            self.click_element('//button[@class="page-actions"]//span[text()="Save"]')

            self.click_element('//*[@id="save-split-button-button"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '(2/3) [-] Test failed'
            else :
                print '(2/3) [+] Test successful'

            # Edit and Add Attributes
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-attributes-attributes"]')
            self.click_element('//*[@id="add"]')
            self.fill_textbox('//*[@id="attribute_label"]', 'attribute ' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the product attribute.') == None :
                 print '(3/3) [-] Test failed'
            else :
                print '(3/3) [+] Test successful'

        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_paymentmethods(self):
        self.login()
        self.set_test_name('mgt_manage_paymentmethods')
        print "[*] Starting manage payment methods process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            self.click_element('//strong[text()="Sales"]')
            self.click_element('//span[text()="Payment Methods"]')
            self.click_element('//*[@id="payment_us_paypal_group_all_in_one_wps_express-head"]')

            self.fill_textbox('//*[@id="payment_us_paypal_group_all_in_one_wps_express_express_checkout_required_express_checkout_required_express_checkout_business_account"]', 'test@gmail.com')

            self.click_element('//button[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def edit_store_view(self):
        self.login()
        self.set_test_name('mgt_edit_store_view')
        print "[*] Starting edit_store_view process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-backend-system-store"]')
            self.click_element('//a[@title="Edit Store View"]')
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the store view.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def enable_weight_search(self):
        self.login()
        self.set_test_name('mgt_enable_weight_search')
        print "[*] Starting enable_weight_search process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-attributes-attributes"]')
            self.click_element('//*[@id="attributeGrid_table"]/tbody/tr[1]/td[1]')
            self.click_element('//*[@id="product_attribute_tabs_front"]')

            self.select_dropdown('//*[@id="is_searchable"]', 'Yes')
            self.select_dropdown('//*[@id="search_weight"]', str(random.randint(1, 10)))

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the product attribute.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def rss_order_status_notification(self):
        self.login()
        self.set_test_name('mgt_rss_order_status_notification')
        print "[*] Starting rss_order_status_notification process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="RSS Feeds"]'):
                self.click_element('//strong[text()="Catalog"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="RSS Feeds"]')
            self.toggle_settings_tab('//*[@id="rss_order_status"]', '//*[@id="rss_order-head"]')
            self.select_dropdown('//*[@id="rss_order_status"]', 'Enable')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def change_store_scope(self):
        self.login()
        self.set_test_name('mgt_change_store_scope')
        print "[*] Starting change_store_scope process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            self.click_element('//*[@id="store-change-button"]')

            self.click_element('//li[@class="store-switcher-website  "]')
            self.click_element('//button//span[text()="OK"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def change_price_scope(self):
        self.login()
        self.set_test_name('mgt_change_price_scope')
        print "[*] Starting change_price_scope process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="Catalog"]'):
                self.click_element('//strong[text()="Catalog"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="Catalog"]')
            self.toggle_settings_tab('//*[@id="catalog_price_scope"]', '//*[@id="catalog_price-head"]')
            self.select_dropdown('//*[@id="catalog_price_scope"]', 'Website')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def toggle_settings_tab(self, element_xpath, header_xpath):
        try:
            element = self.driver.find_element(By.XPATH, element_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-100);", element)
            element.click()
        except:
            print '[+] Toggling element header'
            self.click_element(header_xpath)

    def configure_returnpathemail(self):
        self.login()
        self.set_test_name('mgt_configure_returnpathemail')
        print "[*] Starting configure_returnpathemail process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="System"]'):
                self.click_element('//strong[text()="Advanced"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="System"]')

            self.toggle_settings_tab('//*[@id="system_smtp_set_return_path"]', '//*[@id="system_smtp-head"]')
            self.select_dropdown('//*[@id="system_smtp_set_return_path"]', 'Specified')

            self.fill_textbox('//*[@id="system_smtp_return_path_email"]', 'test@gmail.com')
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def change_domain_name(self):
        self.login()
        self.set_test_name('mgt_change_domain_name')
        print "[*] Starting change_domain_name process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="Web"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="Web"]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="web_unsecure_base_url"]'):
                self.click_element('//*[@id="web_unsecure-head"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_rating(self):
        self.login()
        self.set_test_name('mgt_add_rating')
        print "[*] Starting add_rating process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-review-catalog-reviews-ratings-ratings"]')
            self.click_element('//*[@id="add"]')

            self.fill_textbox('//*[@id="rating_code"]', 'rating' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the rating.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_reviews(self):
        self.login()
        self.set_test_name('mgt_manage_reviews')
        print "[*] Starting manage_reviews process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-marketing"]')
            self.click_element('//*[@data-ui-id="menu-magento-review-catalog-reviews-ratings-reviews-all"]')
            self.click_element('//*[@id="reviwGrid_table"]/tbody/tr[1]/td[12]/a')

            self.select_dropdown('//*[@id="status_id"]', 'Approved')

            self.click_element('//*[@id="save_button"]')

            if self.wait_for_text_in_page('You saved the review.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_cache(self):
        self.login()
        self.set_test_name('mgt_manage_cache')
        print "[*] Starting manage_cache process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-system"]')
            self.click_element('//*[@data-ui-id="menu-magento-backend-system-cache"]')

            self.select_dropdown('//*[@id="cache_grid_massaction-select"]', 'Disable')
            self.click_element('//button[@title="Submit"]')
            self.click_element('//button[@class="action-primary action-accept"]//span[text()="OK"]')
            self.click_element('//button[@id="flush_magento"]')

            if self.wait_for_text_in_page('The Magento cache storage has been flushed.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_outofstocknotification(self):
        self.login()
        self.set_test_name('mgt_manage_outofstocknotification')
        print "[*] Starting manage_outofstocknotification process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="Inventory"]'):
                self.click_element('//strong[text()="Catalog"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="Inventory"]')

            self.toggle_settings_tab('//*[@id="cataloginventory_item_options_notify_stock_qty"]', '//*[@id="cataloginventory_item_options-head"]')
            self.fill_textbox('//*[@id="cataloginventory_item_options_notify_stock_qty"]', '1')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_customers(self):
        self.login()
        self.set_test_name('mgt_manage_customers')
        print "[*] Starting manage_customers process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-customer-customer"]')
            self.click_element('//*[@data-ui-id="menu-magento-customer-customer-manage"]')
            self.click_element('//*[@id="add"]')

            self.fill_textbox('//*[@name="customer[firstname]"]', 'name' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@name="customer[lastname]"]', 'lastname' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@name="customer[email]"]', 'email' + ''.join(random.choice(string.digits) for _ in range(10)) + '@gmail.com')

            self.click_element('//*[@id="tab_address"]')
            self.click_element('//*[@class="address-list-actions last"]//button//span[text()="Add New Addresses"]')

            self.fill_textbox('//*[@name="address[new_0][street][0]"]', 'street' + ''.join(random.choice(string.digits) for _ in range(10)) + '@gmail.com')
            self.fill_textbox('//*[@name="address[new_0][city]"]', 'NYC')

            self.select_dropdown('//*[@name="address[new_0][country_id]"]', 'United States')
            self.select_dropdown('//*[@name="address[new_0][region_id]"]', 'Alabama')
            self.fill_textbox('//*[@name="address[new_0][postcode]"]', '12345')
            self.fill_textbox('//*[@name="address[new_0][telephone]"]', '1234567890')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the customer.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_customer_groups(self):
        self.login()
        self.set_test_name('mgt_manage_customer_groups')
        print "[*] Starting manage_customer_groups process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-customer-customer-group"]')
            self.click_element('//*[@id="add"]')

            self.fill_textbox('//*[@id="customer_group_code"]', 'group_' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the customer group.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def configure_design(self):
        self.login()
        self.set_test_name('mgt_configure_design')
        print "[*] Starting configure_design process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-customer-customer-group"]')
            self.click_element('//*[@id="add"]')

            self.fill_textbox('//*[@id="customer_group_code"]', 'group_' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the customer group.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_widget(self):
        self.login()
        self.set_test_name('mgt_add_widget')
        print "[*] Starting add_widget process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-content"]')
            self.click_element('//*[@data-ui-id="menu-magento-widget-cms-widget-instance"]')
            time.sleep(5)
            self.click_element('//*[@id="add"]')

            self.select_dropdown('//*[@id="code"]', 'Orders and Returns')
            self.select_dropdown('//*[@id="theme_id"]', 'Magento Blank')

            self.click_element('//*[@data-ui-id="widget-button-0"]')

            self.fill_textbox('//*[@id="title"]', 'widget_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="store_ids"]', 'All Store Views')

            self.click_element('//*[@data-ui-id="widget-button-0"]')
            self.select_dropdown('//*[@id="widget_instance[0][page_group]"]', 'All Pages')
            self.select_dropdown('//*[@name="widget_instance[0][all_pages][block]"]', 'Sidebar Main')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('The widget instance has been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def customer_configuration(self):
        self.login()
        self.set_test_name('mgt_customer_configuration')
        print "[*] Starting customer_configuration process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="Customer Configuration"]'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[3]/div/strong')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="Customer Configuration"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_product_on_homepage(self):
        self.login()
        self.set_test_name('mgt_add_product_on_homepage')
        print "[*] Starting add_product_on_homepage process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-content"]')
            self.click_element('//*[@data-ui-id="menu-magento-cms-cms-page"]')
            self.click_element('//*[@id="container"]/div/div[5]/table/tbody/tr[3]/td[10]/div/button', scroll=False)
            self.click_element('//*[@id="container"]/div/div[5]/table/tbody/tr[3]/td[10]/div/ul/li[1]/a', scroll=False)
            self.click_element('//*[@id="page_tabs_content_section"]')
            time.sleep(5)
            self.toggle_settings_tab('//*[@id="page_content_magentowidget"]', '//*[@id="togglepage_content"]')
            self.select_dropdown('//*[@id="select_widget_type"]', 'Catalog Products List')
            time.sleep(5)
            self.click_element('//*[@id="insert_button"]')
            time.sleep(5)
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved this page.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def export_customers(self):
        self.login()
        self.set_test_name('mgt_export_customers')
        print "[*] Starting export_customers process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-system"]')
            self.click_element('//*[@data-ui-id="menu-magento-importexport-system-convert-export"]')

            self.select_dropdown('//*[@id="entity"]', 'Customers Main File')
            self.click_element('//button//span[text()="Continue"]')

            if self.wait_for_text_in_page('Export') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def import_customers(self):
        self.login()
        self.set_test_name('mgt_import_customers')
        print "[*] Starting import_customers process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-system"]')
            self.click_element('//*[@data-ui-id="menu-magento-importexport-system-convert-import"]')

            self.select_dropdown('//*[@id="entity"]', 'Customers Main File')
            self.select_dropdown('//*[@id="custom_behavior"]', 'Add/Update Complex Data')
            current_dir = os.path.dirname(os.path.realpath(__file__))
            self.fill_textbox('//*[@id="import_file"]', current_dir + '/customer_205.csv')

            self.click_element('//*[@id="upload_button"]')

            time.sleep(30)

            if self.wait_for_text_in_page('Export') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def view_and_export_reports(self):
        self.login()
        self.set_test_name('mgt_view_and_export_reports')
        print "[*] Starting view_and_export_reports process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-salesroot-tax"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-salesroot-invoiced"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-salesroot-shipping"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-salesroot-refunded"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-salesroot-coupons"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-paypal-report-salesroot-paypal-settlement-reports"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-customers-totals"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-customers-orders"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-customers-accounts"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-products-viewed"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-products-bestsellers"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-products-lowstock"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-products-sold"]')
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-downloadable-report-products-downloads"]')
            time.sleep(5)

            self.click_element('//*[@id="menu-magento-reports-report"]')
            self.click_element('//*[@data-ui-id="menu-magento-reports-report-salesroot-sales"]')
            self.click_element('//*[@id="messages"]/div/div[2]/div/a[2]')
            #self.click_element('//*[@id="grid_tab_new_customers"]')
            self.wait_for_text_in_page('Recent statistics have been updated.')

            self.fill_textbox('//*[@id="sales_report_from"]', '10/1/2017')
            self.fill_textbox('//*[@id="sales_report_to"]', '25/1/2018')

            self.click_element('//*[@id="filter_form_submit"]')

            if self.wait_for_text_in_page('records found') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def change_store_contact(self):
        self.login()
        self.set_test_name('mgt_change_store_contact')
        print "[*] Starting change_store_contact process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="Sales Emails"]'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/div')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="Sales Emails"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def change_welcome_message(self):
        self.login()
        self.set_test_name('mgt_change_welcome_message')
        print "[*] Starting change_welcome_message process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="Design"]'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[1]/div')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="Design"]')

            if not self.check_exists_and_visible_by_xpath('//*[@id="design_header_welcome"]'):
                self.click_element('//*[@id="design_header-head"]')
            self.fill_textbox('//*[@id="design_header_welcome"]', 'Welcome')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def enable_contact_us(self):
        self.login()
        self.set_test_name('mgt_enable_contact_us')
        print "[*] Starting enable_contact_us process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="Contacts"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="Contacts"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_locale(self):
        self.login()
        self.set_test_name('mgt_setup_locale')
        print "[*] Starting setup_locale process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="General"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="General"]')
            self.click_element('//*[@id="general_locale-head"]')
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_store_info(self):
        self.login()
        self.set_test_name('mgt_setup_store_info')
        print "[*] Starting setup_store_info process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="General"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="General"]')
            self.click_element('//*[@id="general_store_information-head"]')
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def enable_single_store_mode(self):
        self.login()
        self.set_test_name('mgt_setup_store_info')
        print "[*] Starting setup_store_info process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//a[@class="admin__page-nav-link item-nav"]//span[text()="General"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//a[@class="admin__page-nav-link item-nav"]//span[text()="General"]')

            if not self.check_exists_and_visible_by_xpath('//*[@id="general_single_store_mode_enabled"]'):
                self.click_element('//*[@id="general_single_store_mode-head"]')
            self.select_dropdown('//*[@id="general_single_store_mode_enabled"]', 'Yes')

            self.click_element('//*[@id="save"]')

            self.select_dropdown('//*[@id="general_single_store_mode_enabled"]', 'No')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def read_messages(self):
        self.login()
        self.set_test_name('mgt_read_messages')
        print "[*] Starting read_messages process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-system"]')
            self.click_element('//*[@data-ui-id="menu-magento-adminnotification-system-adminnotification"]')

            self.select_dropdown('//*[@id="notificationGrid_massaction-select"]', 'Mark as Read')
            self.click_element('//button[@title="Submit"]')

            self.click_element('//button//span[text()="OK"]')

            if self.wait_for_text_in_page('records found') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def admin_forgot_password(self):
        self.logout()
        self.set_test_name('mgt_admin_forgot_password')
        print "[*] Starting admin_forgot_password process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//a[@class="action-forgotpassword"]')
            self.fill_textbox('//*[@id="email"]', 'admin@gmail.com')

            self.click_element('//span[text()="Retrieve Password"]')

            if self.wait_for_text_in_page('processing your request') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_configurable_product(self):
        self.login()
        self.set_test_name('mgt_add_configurable_product')
        print "[*] Starting add_configurable_product process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')

            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-dropdown"]')
            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-item-configurable"]')

            self.fill_textbox('//*[@id="name"]', 'product_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="sku"]', ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="price"]', ''.join(random.choice(string.digits) for _ in range(8)))

            self.click_element('//*[@id="add_video_button"]')
            self.fill_textbox('//*[@id="video_url"]', 'https://vimeo.com/112866269')
            self.fill_textbox('//*[@id="video_title"]', 'video title')
            time.sleep(10)
            self.click_element('/html/body/div[6]/aside[5]/div[2]/header/div/div/div/button[1]')

            self.click_element('//button[@title="Create Product Configurations"]')
            self.click_element('//button[@title="Create New Attribute"]')

            time.sleep(10)
            self.driver.switch_to.frame(self.driver.find_element_by_xpath('//iframe[@id="create_new_attribute_container"]'))
            self.fill_textbox('//*[@id="attribute_label"]', 'attribute_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//button[@id="save"]')
            time.sleep(10)
            self.driver.switch_to.default_content()

            self.click_element('//button[@data-bind="click: next"]')
            self.click_element('//*[@id="variation-steps-wizard_step1"]/div[2]/div[3]/table/tbody/tr[last()]/td[1]')
            self.click_element('//button[@data-bind="click: next"]')

            self.click_element('//*[@id="variation-steps-wizard_step2"]/div/div[2]/div[1]/div/div[2]/button[1]/span')
            self.click_element('//button[@data-bind="click: next"]')

            self.click_element('//button[@data-bind="click: next"]')
            self.click_element('//button[@data-bind="click: next"]')

            self.click_element('//*[@id="save-split-button-button"]')
            if self.check_exists_and_visible_by_xpath('//button[@data-action="confirm"]'):
                self.click_element('//button[@data-action="confirm"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_downloadable_product(self):
        self.login()
        self.set_test_name('mgt_add_downloadable_product')
        print "[*] Starting add_downloadable_product process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')

            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-dropdown"]')
            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-item-downloadable"]')

            self.fill_textbox('//*[@id="name"]', 'product_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="sku"]', ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="price"]', ''.join(random.choice(string.digits) for _ in range(8)))

            self.click_element('//*[@id="add_link_item"]')
            self.fill_textbox('//*[@name="downloadable[link][0][title]"]', 'downloadable_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//label[@for="downloadable_link_0_url_type"]')
            self.fill_textbox('//*[@name="downloadable[link][0][link_url]"]', 'https://www.google.com')

            self.click_element('//*[@id="save-split-button-button"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_grouped_product(self):
        self.login()
        self.set_test_name('mgt_add_grouped_product')
        print "[*] Starting add_grouped_product process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')

            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-dropdown"]')
            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-item-grouped"]')

            self.fill_textbox('//*[@id="name"]', 'product_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="sku"]', ''.join(random.choice(string.digits) for _ in range(10)))
            #self.fill_textbox('//*[@id="price"]', ''.join(random.choice(string.digits) for _ in range(8)))

            self.click_element('//button[text()="Add Products to Group"]')
            self.click_element('//*[@id="id_1"]')
            self.click_element('//*[@id="id_2"]')
            self.click_element('//button//span[text()="Add Selected Products"]')

            self.fill_textbox('//*[@name="links[associated][1][qty]"]', '3')
            self.click_element('//*[@id="save-split-button-button"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_virtual_product(self):
        self.login()
        self.set_test_name('mgt_add_virtual_product')
        print "[*] Starting add_virtual_product process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')

            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-dropdown"]')
            self.click_element('//*[@data-ui-id="products-list-add-new-product-button-item-virtual"]')

            self.fill_textbox('//*[@id="name"]', 'product_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="sku"]', ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="price"]', ''.join(random.choice(string.digits) for _ in range(8)))

            self.click_element('//*[@id="save-split-button-button"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def configure_color_swatches(self):
        self.login()
        self.set_test_name('mgt_configure_color_swatches')
        print "[*] Starting configure_color_swatches process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-attributes-attributes"]')

            self.click_element('//td[contains(text(), "color")]')
            #self.click_element('//button[@id="add_new_swatch_visual_option_button"]')

            #self.fill_textbox('//*[@name="optionvisual[value][option_12][0]"]', 'color_' + ''.join(random.choice(string.digits) for _ in range(10)))
            # Upload swatch image
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the product attribute.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_watermark(self):
        self.login()
        self.set_test_name('mgt_add_watermark')
        print "[*] Starting add_watermark process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="Design"]'):
                self.click_element('//*[text()="General"]')
            self.click_element('//li//a//span[text()="Design"]')

            if not self.check_exists_and_visible_by_xpath('//*[@id="design_watermark_image_image"]'):
                self.click_element('//*[@id="design_watermark-head"]')
            current_dir = os.path.dirname(os.path.realpath(__file__))
            self.fill_textbox('//*[@id="design_watermark_image_image"]', current_dir + '/headphones.jpg')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_product_placeholders(self):
        self.login()
        self.set_test_name('mgt_setup_product_placeholders')
        print "[*] Starting setup_product_placeholders process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('/html/body/div[2]/main/div[2]/div[2]/div/div[2]/ul/li[1]/a/span'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[2]/div')
            self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[2]/ul/li[1]/a/span')

            if not self.check_exists_and_visible_by_xpath('//*[@id="catalog_placeholder_image_placeholder"]'):
                self.click_element('//*[@id="catalog_placeholder-head"]')
            current_dir = os.path.dirname(os.path.realpath(__file__))
            self.fill_textbox('//*[@id="catalog_placeholder_image_placeholder"]', current_dir + '/headphones.jpg')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_advanced_pricing(self):
        self.login()
        self.set_test_name('mgt_setup_advanced_pricing')
        print "[*] Starting setup_advanced_pricing process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')

            self.click_element('//*[@id="container"]/div/div[3]/table/tbody/tr[1]/td[13]/a')

            if not self.check_exists_and_visible_by_xpath('//*[@id="product_info_tabs_advanced-pricing"]'):
                self.click_element('//strong[contains(text(), "Advanced Settings")]')
            self.click_element('//*[@id="product_info_tabs_advanced-pricing"]')

            self.fill_textbox('//*[@id="special_price"]', ''.join(random.choice(string.digits) for _ in range(6)))
            self.fill_textbox('//*[@id="special_from_date"]', '1/1/2018')
            self.fill_textbox('//*[@id="special_to_date"]', '1/1/2020')

            #self.click_element('//button[@title="Add Price"]')
            self.fill_textbox('//*[@id="tier_price_row_0_qty"]', '5')
            self.fill_textbox('//*[@id="tier_price_row_0_price"]', ''.join(random.choice(string.digits) for _ in range(6)))

            self.fill_textbox('//*[@id="msrp"]', '123')

            self.click_element('//*[@id="save-split-button-button"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def warehouse_and_inventory(self):
        self.login()
        self.set_test_name('mgt_warehouse_and_inventory')
        print "[*] Starting warehouse_and_inventory process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-products"]')

            self.click_element('//*[@id="container"]/div/div[3]/table/tbody/tr[1]/td[13]/a')

            if not self.check_exists_and_visible_by_xpath('//*[@id="product_info_tabs_advanced-inventory"]'):
                self.click_element('//strong[contains(text(), "Advanced Settings")]')
            self.click_element('//*[@id="product_info_tabs_advanced-inventory"]')

            self.select_dropdown('//*[@id="inventory_enable_qty_increments"]', 'Yes')
            self.fill_textbox('//*[@id="inventory_qty_increments"]', '4')

            self.click_element('//*[@id="save-split-button-button"]')

            if self.wait_for_text_in_page('You saved the product.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def stock_options(self):
        self.login()
        self.set_test_name('mgt_stock_options')
        print "[*] Starting stock_options process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="Inventory"]'):
                self.click_element('//strong[text()="Catalog"]')
            self.click_element('//li//a//span[text()="Inventory"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def product_categories(self):
        self.login()
        self.set_test_name('mgt_product_categories')
        print "[*] Starting product_categories process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-catalog-catalog"]')
            self.click_element('//*[@data-ui-id="menu-magento-catalog-catalog-categories"]')

            self.click_element('//*[@id="extdd-8"]')
            self.select_dropdown('//*[@id="group_4is_active"]', 'No')

            time.sleep(2)
            self.click_element('//*[@id="save"]')

            time.sleep(2)
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the category.') == None :
                 print '[-] (1/3) Test failed'
            else :
                print '[+] (1/3) Test successful'

            self.click_element('//*[@id="add_root_category_button"]')
            self.fill_textbox('//*[@id="group_4name"]', 'SubCat_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="group_4is_active"]', 'Yes')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the category.') == None :
                 print '[-] (2/3) Test failed'
            else :
                print '[+] (2/3) Test successful'

            self.click_element('//*[@id="add_subcategory_button"]')
            self.fill_textbox('//*[@id="group_4name"]', 'RootCat_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="group_4is_active"]', 'Yes')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the category.') == None :
                 print '[-] (3/3) Test failed'
            else :
                print '[+] (3/3) Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def gift_message(self):
        self.login()
        self.set_test_name('mgt_gift_message')
        print "[*] Starting gift_message process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="Advanced"]'):
                self.click_element('//strong[text()="Advanced"]')
            self.click_element('//li//a//span[text()="Advanced"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def modify_invoice_fields(self):
        self.login()
        self.set_test_name('mgt_modify_invoice_fields')
        print "[*] Starting modify_invoice_fields process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="PDF Print-outs"]'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/div')
            self.click_element('//li//a//span[text()="PDF Print-outs"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def display_customer_ip(self):
        self.login()
        self.set_test_name('mgt_display_customer_ip')
        print "[*] Starting display_customer_ip process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/ul/li[1]/a'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/div/strong')
            self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/ul/li[1]/a')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def change_pdf_invoice_logo(self):
        self.login()
        self.set_test_name('mgt_change_pdf_invoice_logo')
        print "[*] Starting change_pdf_invoice_logo process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/ul/li[1]/a'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/div/strong')
            self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[4]/ul/li[1]/a')

            if not self.check_exists_and_visible_by_xpath('//*[@id="sales_identity_logo"]'):
                self.click_element('//*[@id="sales_identity-head"]')
            current_dir = os.path.dirname(os.path.realpath(__file__))
            self.fill_textbox('//*[@id="sales_identity_logo"]', current_dir + '/headphones.jpg')
            self.fill_textbox('//*[@id="sales_identity_logo_html"]', current_dir + '/headphones.jpg')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def configure_newsletters(self):
        self.login()
        self.set_test_name('mgt_configure_newsletters')
        print "[*] Starting configure_newsletters process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('/html/body/div[2]/main/div[2]/div[2]/div/div[3]/ul/li[1]/a/span'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[3]/div/strong')
            self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[3]/ul/li[1]/a/span')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_newsletter_template(self):
        self.login()
        self.set_test_name('mgt_add_newsletter_template')
        print "[*] Starting add_newsletter_template process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-marketing"]')
            self.click_element('//*[@data-ui-id="menu-magento-newsletter-newsletter-template"]')

            self.click_element('//*[@data-ui-id="page-actions-toolbar-add-button"]')

            self.fill_textbox('//*[@id="code"]', 'Template_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="subject"]', 'TSubj_' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@data-ui-id="page-actions-toolbar-preview-button"]')

            self.driver.switch_to_window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to_window(self.driver.window_handles[0])

            time.sleep(1)

            self.click_element('//*[@data-ui-id="page-actions-toolbar-save-button"]')

            if self.wait_for_text_in_page('The newsletter template has been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def configure_rss(self):
        self.login()
        self.set_test_name('mgt_configure_rss')
        print "[*] Starting configure_rss process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')


            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="RSS Feeds"]'):
                self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[2]/div')
            self.click_element('//li//a//span[text()="RSS Feeds"]')

            if not self.check_exists_and_visible_by_xpath('//*[@id="rss_config_active"]'):
                self.click_element('//*[@id="rss_config-head"]')
            self.select_dropdown('//*[@id="rss_config_active"]', 'Enable')

            if not self.check_exists_and_visible_by_xpath('//*[@id="rss_wishlist_active"]'):
                self.click_element('//*[@id="rss_wishlist-head"]')
            self.select_dropdown('//*[@id="rss_wishlist_active"]', 'Enable')

            if not self.check_exists_and_visible_by_xpath('//*[@id="rss_catalog_new"]'):
                self.click_element('//*[@id="rss_catalog-head"]')
            self.select_dropdown('//*[@id="rss_catalog_new"]', 'Enable')
            self.select_dropdown('//*[@id="rss_catalog_special"]', 'Enable')
            self.select_dropdown('//*[@id="rss_catalog_discounts"]', 'Enable')
            self.select_dropdown('//*[@id="rss_catalog_category"]', 'Enable')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def enable_breadcrumbs(self):
        self.login()
        self.set_test_name('mgt_enable_breadcrumbs')
        print "[*] Starting enable_breadcrumbs process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            time.sleep(5)
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)
            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="Web"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//li//a//span[text()="Web"]')
            time.sleep(2)
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_searchterms(self):
        self.login()
        self.set_test_name('mgt_add_searchterms')
        print "[*] Starting add_searchterms process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            time.sleep(3)
            self.click_element('//*[@id="menu-magento-backend-marketing"]')
            self.click_element('//*[@data-ui-id="menu-magento-search-search-terms"]')

            self.click_element('//*[@id="add"]')
            self.fill_textbox('//*[@id="query_text"]', 'watch' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="store_id"]', '    Default Store View')
            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the search term.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def remove_searchterms(self):
        self.login()
        self.set_test_name('mgt_remove_searchterms')
        print "[*] Starting remove_searchterms process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-marketing"]')
            self.click_element('//*[@data-ui-id="menu-magento-search-search-terms"]')
            time.sleep(5)
            self.select_dropdown('//*[@id="search_term_grid_massaction-select"]', 'Delete')
            self.click_element('/html/body/div[2]/main/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[1]//input')
            self.click_element('//*[@id="search_term_grid_table"]/tbody/tr/td[1]')
            self.click_element('//*[@data-ui-id="widget-button-2"]')

            self.click_element('//*[@id="html-body"]/div[4]/aside[2]/div[2]/footer/button[2]')

            if self.wait_for_text_in_page('record(s) were deleted.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_sitemap(self):
        self.login()
        self.set_test_name('mgt_setup_sitemap')
        print "[*] Starting setup_sitemap process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="XML Sitemap"]'):
                self.click_element('//strong[text()="Catalog"]')
            self.click_element('//li//a//span[text()="XML Sitemap"]')

            #if self.check_exists_and_visible_by_xpath('//*[@id="sitemap_generate_enabled"]'):
            self.click_element('//*[@id="sitemap_generate-head"]')
            #self.select_dropdown('//*[@id="sitemap_generate_enabled"]', 'Yes')

            #if self.check_exists_and_visible_by_xpath('//*[@id="sitemap_search_engines_submission_robots"]'):
            self.click_element('//*[@id="sitemap_search_engines-head"]')
            #self.select_dropdown('//*[@id="sitemap_search_engines_submission_robots"]', 'Yes')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_robotstxt(self):
        self.login()
        self.set_test_name('mgt_setup_robotstxt')
        print "[*] Starting setup_robotstxt process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="Design"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//li//a//span[text()="Design"]')

            #if not self.check_exists_and_visible_by_xpath('//*[@id="design_search_engine_robots_custom_instructions"]'):
            #    self.click_element('//*[@id="design_search_engine_robots-head"]')
            self.fill_textbox('//*[@id="design_search_engine_robots_custom_instructions"]', '''Disallow: /lib/
Disallow: /*.php$
Disallow: /pkginfo/
Disallow: /report/
Disallow: /var/
Disallow: /catalog/
Disallow: /customer/
Disallow: /sendfriend/
Disallow: /review/
Disallow: /*SID=''')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def create_adminuser(self):
        self.login()
        self.set_test_name('mgt_create_adminuser')
        print "[*] Starting create_adminuser process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-system"]')
            self.click_element('//*[@data-ui-id="menu-magento-user-system-acl-users"]')

            self.click_element('//*[@id="add"]')
            self.fill_textbox('//*[@id="user_username"]', 'user' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="user_firstname"]', 'name' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="user_lastname"]', 'lastname' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="user_email"]', 'email' + ''.join(random.choice(string.digits) for _ in range(10)) + '@gmail.com')
            self.fill_textbox('//*[@id="user_password"]', 'zaq1@WSX')
            self.fill_textbox('//*[@id="user_confirmation"]', 'zaq1@WSX')
            self.fill_textbox('//*[@id="user_current_password"]', 'zaq1@WSX')

            self.click_element('//*[@id="page_tabs_roles_section"]')
            self.click_element('//*[@id="permissionsUserRolesGrid_table"]/tbody/tr/td[1]/input')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the user.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def configure_cronjob(self):
        self.login()
        self.set_test_name('mgt_configure_cronjob')
        print "[*] Starting configure_cronjob process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('/html/body/div[2]/main/div[2]/div[2]/div/div[6]/ul/li[2]/a'):
                self.click_element('//strong[text()="Advanced"]')
            self.click_element('/html/body/div[2]/main/div[2]/div[2]/div/div[6]/ul/li[2]/a')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def configure_tax(self):
        self.login()
        self.set_test_name('mgt_configure_tax')
        print "[*] Starting configure_tax process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-tax-sales-tax-rates"]')

            self.click_element('//*[@id="add"]')
            self.fill_textbox('//*[@id="code"]', 'tax' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="tax_postcode"]', '1234')
            self.fill_textbox('//*[@id="rate"]', '8')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the tax rate.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def configure_taxrules(self):
        self.login()
        self.set_test_name('mgt_configure_taxrules')
        print "[*] Starting configure_taxrules process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-tax-sales-tax-rules"]')

            time.sleep(5)
            self.click_element('//*[@id="add"]')
            self.fill_textbox('//*[@id="code"]', 'taxrule' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//*[@id="base_fieldset"]/div[3]/div/section/div[1]/div/div[1]/label/span')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the tax rule.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def create_role(self):
        self.login()
        self.set_test_name('mgt_create_role')
        print "[*] Starting create_role process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-system"]')
            self.click_element('//*[@data-ui-id="menu-magento-user-system-acl-roles"]')
            time.sleep(5)
            self.click_element('//*[@id="add"]')
            self.fill_textbox('//*[@id="role_name"]', 'role' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@id="role_info_tabs_account"]')
            self.click_element('//*[@id="role_info_tabs_account_content"]/fieldset/div[2]/div/div/ul/li[1]/a')

            self.click_element('//*[@data-ui-id="page-actions-toolbar-savebutton"]')

            if self.wait_for_text_in_page('You saved the role.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def take_backup(self):
        self.login()
        self.set_test_name('mgt_take_backup')
        print "[*] Starting take_backup process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-system"]')
            self.click_element('//*[@data-ui-id="menu-magento-backup-system-tools-backup"]')

            self.click_element('//*[@data-ui-id="page-actions-toolbar-createsnapshotbutton"]')
            self.fill_textbox('//*[@id="backup_name"]', 'systembackup' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//*[@id="html-body"]/div[5]/aside[2]/div[2]/header/div/div/div/button[2]/span')

            self.click_element('//*[@data-ui-id="page-actions-toolbar-savebutton"]')

            if self.wait_for_text_in_page('You saved the role.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_currency(self):
        self.login()
        self.set_test_name('mgt_setup_currency')
        print "[*] Starting setup_currency process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-config-system-config"]')
            time.sleep(5)

            if not self.check_exists_and_visible_by_xpath('//li//a//span[text()="Currency Setup"]'):
                self.click_element('//strong[text()="General"]')
            self.click_element('//li//a//span[text()="Currency Setup"]')

            self.click_element('//*[@id="save"]')

            if self.wait_for_text_in_page('You saved the configuration.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_currency_symbols(self):
        self.login()
        self.set_test_name('mgt_setup_currency_symbols')
        print "[*] Starting setup_currency_symbols process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-currencysymbol-system-currency-symbols"]')

            self.click_element('//*[@data-ui-id="page-actions-toolbar-save-button"]')

            if self.wait_for_text_in_page('You applied the custom currency symbols.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_currency_rates(self):
        self.login()
        self.set_test_name('mgt_setup_currency_rates')
        print "[*] Starting setup_currency_rates process..."
        #self.driver.get(self.admin_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="menu-magento-backend-stores"]')
            self.click_element('//*[@data-ui-id="menu-magento-currencysymbol-system-currency-rates"]')
            self.click_element('//*[@data-ui-id="adminhtml-system-currency-0-import-button"]')

            if self.wait_for_text_in_page('Click "Save" to apply the rates we found.') == None :
                 print '[-] (1/2) Test failed'
            else :
                print '[+] (1/2) Test successful'

            self.click_element('//*[@data-ui-id="page-actions-toolbar-save-button"]')

            if self.wait_for_text_in_page('Currency Rates') == None :
                 print '[-] (2/2) Test failed'
            else :
                print '[+] (2/2) Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def customer_signup(self):
        self.set_test_name('mgt_customer_signup')
        print "[*] Starting customer_signup process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[text()="Create an Account"]')

            self.fill_textbox('//*[@id="firstname"]', 'name' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="lastname"]', 'lastname' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.new_username = 'email' + ''.join(random.choice(string.digits) for _ in range(10)) + '@gmail.com'
            self.fill_textbox('//*[@id="email_address"]', self.new_username)
            self.fill_textbox('//*[@id="password"]', 'zaq1@WSX')
            self.fill_textbox('//*[@id="password-confirmation"]', 'zaq1@WSX')

            self.click_element('//button[@title="Create an Account"]')
            time.sleep(30)
            if self.wait_for_text_in_page('Thank you for registering with Main Website Store.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def customer_login(self):
        self.set_test_name('mgt_customer_login')
        print "[*] Starting customer_login process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(text(), "Sign In")]')

            self.fill_textbox('//*[@id="email"]', 'roni_cost@example.com')
            self.fill_textbox('//*[@id="pass"]', 'roni_cost@example.com')

            self.click_element('//*[@id="send2"]')

            if self.wait_for_text_in_page('My Dashboard') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def forgot_password(self):
        self.set_test_name('mgt_forgot_password')
        print "[*] Starting forgot_password process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(text(), "Sign In")]')
            self.click_element('//a//span[text()="Forgot Your Password?"]')

            self.fill_textbox('//*[@id="email_address"]', 'test@gmail.com')
            self.click_element('//button//span[text()="Submit"]')

            if self.wait_for_text_in_page(' you will receive an email with a link to reset your password.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def customer_logout(self):
        self.set_test_name('mgt_customer_logout')
        print "[*] Starting customer_logout process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//span[@class="customer-name"]')

            self.click_element('//a[contains(text(), "Sign Out")]')

            if self.wait_for_text_in_page('You are signed out.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def customer_checkout(self):
        self.set_test_name('mgt_customer_checkout')
        print "[*] Starting customer_checkout process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('/html/body/div[1]/main/div[3]/div/div[3]/div/div/ol/li[1]/div/div/div[2]/div[1]/button')
            self.click_element('/html/body/div[1]/header/div[2]/div[1]/a')
            time.sleep(20)
            self.click_element('//*[@class="counter-number"]')
            self.click_element('//*[@id="top-cart-btn-checkout"]')
            self.click_element('//*[@id="s_method_flatrate_flatrate"]')
            self.click_element('/html/body/div[1]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button')
            self.click_element('/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div[2]/form/fieldset/div[1]/div/div[1]/div[2]/div[4]/div/button')

            self.click_element('//a[@class="order-number"]')

            if self.wait_for_text_in_page('Items Ordered') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def guest_checkout(self):
        self.set_test_name('mgt_guest_checkout')
        print "[*] Starting guest_checkout process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('/html/body/div[1]/main/div[3]/div/div[3]/div/div/ol/li[1]/div/div/div[2]/div[1]/button')
            self.click_element('/html/body/div[1]/header/div[2]/div[1]/a')
            time.sleep(10)
            self.click_element('//*[@id="top-cart-btn-checkout"]')

            self.fill_textbox('//*[@id="customer-email"]', 'customer123@gmail.com')
            self.fill_textbox('//input[@name="firstname"]', 'customer name')
            self.fill_textbox('//input[@name="lastname"]', 'customer lastname')
            self.fill_textbox('//input[@name="street[0]"]', 'street 123')
            self.fill_textbox('//input[@name="city"]', 'nyc')
            self.select_dropdown('//select[@name="region_id"]', 'Alabama')
            self.fill_textbox('//input[@name="postcode"]', '11790')
            self.fill_textbox('//input[@name="telephone"]', '1546546645')
            time.sleep(5)
            self.click_element('//input[@id="s_method_flatrate_flatrate"]')
            time.sleep(10)
            self.click_element('//button[@data-role="opc-continue"]')

            self.click_element('//button[@title="Place Order"]')

            if self.wait_for_text_in_page('Your order # is') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

if __name__ == '__main__':
    mgt = MagentoTests()
    mgt.login()
    mgt.logout()
    # Getting Started
    mgt.edit_store_view()
    mgt.enable_weight_search()
    mgt.rss_order_status_notification()
    mgt.change_store_scope()
    mgt.change_price_scope()
    mgt.configure_returnpathemail()
    mgt.change_domain_name()
    mgt.add_rating()
    mgt.manage_reviews()
    mgt.manage_cache()
    mgt.manage_outofstocknotification()
    mgt.manage_customers()
    mgt.manage_customer_groups()
    mgt.configure_design()
    mgt.add_widget()
    # Import Export Products (https://www.mageplaza.com/kb/3-steps-import-configurable-products-magento-2.html)
    mgt.customer_configuration()
    mgt.add_product_on_homepage()
    mgt.export_customers()
    mgt.view_and_export_reports()
    mgt.change_store_contact()
    mgt.change_welcome_message()
    mgt.enable_contact_us()
    mgt.setup_locale()
    mgt.setup_store_info()
    mgt.enable_single_store_mode()
    mgt.read_messages()
    mgt.admin_forgot_password()
    # Upload product images
    mgt.add_configurable_product() # Also includes tests for uploading videos
    mgt.add_downloadable_product()
    time.sleep(5)
    mgt.add_grouped_product()
    mgt.add_virtual_product()
    time.sleep(5)
    mgt.configure_color_swatches()
    mgt.add_watermark()
    mgt.setup_product_placeholders()
    mgt.setup_advanced_pricing()
    time.sleep(5)
    mgt.warehouse_and_inventory()
    time.sleep(5)
    mgt.stock_options()
    mgt.product_categories()
    mgt.gift_message()
    mgt.modify_invoice_fields()
    mgt.display_customer_ip()
    mgt.change_pdf_invoice_logo()
    mgt.configure_newsletters()
    mgt.add_newsletter_template()
    mgt.configure_rss()
    mgt.enable_breadcrumbs()
    mgt.add_searchterms()
    mgt.remove_searchterms()
    mgt.setup_sitemap()
    mgt.setup_robotstxt()
    mgt.create_adminuser()
    mgt.configure_cronjob()
    mgt.configure_tax()
    mgt.configure_taxrules()
    mgt.create_role()
    mgt.setup_currency()
    mgt.setup_currency_symbols()
    mgt.setup_currency_rates()
    # Create website
    mgt.create_page()
    mgt.quickedit_page()
    # Customer
    mgt.switch_to_firefox()
    mgt.customer_signup()
    mgt.customer_logout()
    mgt.customer_login()
    mgt.customer_checkout()
    mgt.customer_logout()
    mgt.guest_checkout()
    mgt.forgot_password()
