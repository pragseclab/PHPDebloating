#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, os, errno, argparse, sys, random, string
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import Select

class MagentoTests:
    def __init__(self):
        # UPDATE HERE (1/5)
        self.main_page = 'http://localhost:8085/magento-1.9.0/'
        self.admin_page = 'http://localhost:8085/magento-1.9.0/admin'
        print "[+] Setting up ChromeDriver"
        options = webdriver.chrome.options.Options()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        self.add_cookies()
        self.new_username = 'test@gmail.com'
        self.logged_in = False
    def add_cookies(self):
        # Fix for https://stackoverflow.com/a/28331099/1821461
        # Must load static content not to change code coverage outcome
        self.driver.get(self.main_page + 'LICENSE.txt')
        # UPDATE HERE (2/5)
        self.driver.add_cookie({'name': 'test_group', 'value': 'mgt190_tutorials'})
        # UPDATE HERE (3/5)
        self.driver.add_cookie({'name': 'test_name', 'value': 'mgt_login_mgt190_tutorials'})
        # UPDATE HERE (4/5)
        self.driver.add_cookie({'name': 'software_id', 'value': '3'})
        # UPDATE HERE (5/5)
        self.driver.add_cookie({'name': 'software_version_id', 'value': '10'})
    def set_test_name(self, test_name):
        self.driver.delete_cookie('test_name')
        self.driver.add_cookie({'name': 'test_name', 'value': test_name})
    def click_element(self, xpath_selector):
        try:
            self.wait_for_loading_message()
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-50);", element)
            element.click()
        except Exception as e:
            print '[-] Failed to click on element'
            print e
    def hover_element(self, xpath_selector):
        try:
            self.wait_for_loading_message()
            action=ActionChains(self.driver)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-50);", element)
            action.move_to_element(element).perform()
        except Exception as e:
            print '[-] Failed to hover element'
            print e
    def fill_textbox(self, xpath_selector, text):
        try:
            self.wait_for_loading_message()
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-50);", element)
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
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-50);", element)
            if element.is_selected() != enable:
                element.click()
        except Exception as e:
            print '[-] Failed to enable checkbox'
            print e
    def select_dropdown(self, xpath_selector, text=None):
        try:
            self.wait_for_loading_message()
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0,-50);", element)
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
    def wait_for_element_become_visible(self, xpath_selector) :
        timeout = 30
        while not self.check_exists_and_visible_by_xpath(xpath_selector) :
            if timeout == 30 :
                print "[+] Waiting for %s to become visible" % xpath_selector,
            else :
                print '.',
            # Wait for login pop up to load via ajax
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0 :
                print "[-] Timed out %s" % xpath_selector
                return None
        if timeout != 30:
            print ''
    def wait_for_text_in_page(self, text) :
        timeout = 60
        while not text in self.driver.page_source :
            print "[+] Waiting for text: %s to load in page" % text
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0 :
                print "[-] Timed out %s" % text
                return False
        return True
    def wait_for_loading_message(self):
        while self.check_exists_and_visible_by_xpath('//*[contains(text(), "Please wait")]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="billing-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="payment-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="shipping-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="shipping-method-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[@id="review-please-wait"]') \
            or self.check_exists_and_visible_by_xpath('//*[contains(text(), "Submitting order information")]'):
            time.sleep(1)

    def login(self, current_page=False, username=None, password=None):
        self.set_test_name('mgt_login')
        print "[*] Starting login process..."
        if not current_page:
            self.driver.get(self.admin_page)
        # Fill form fields
        try :
            if self.logged_in:
                print '[+] Already logged in, skipping.'
                return
            # Enter Username
            self.fill_textbox('//*[@id="username"]', 'admin' if username == None else username)
            # Enter password
            self.fill_textbox('//*[@id="login"]', 'zaq1@WSX' if password == None else password)
            # Click submit
            self.click_element('//*[@title="Login"]')
            time.sleep(3)
            if not self.wait_for_text_in_page('Log Out') :
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
    def logout(self):
        try:
            self.click_element('//*[@id="html-body"]/div[1]/div[1]/div[1]/div/p/a[2]')
            self.logged_in = False
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def add_product_attribute(self):
        self.login()
        self.set_test_name('mgt_add_product_attribute')
        print "[*] Starting add product attribute process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create catalog
            self.hover_element('//span[text()="Catalog"]')
            self.hover_element('//span[text()="Attributes"]')
            self.click_element('//span[text()="Manage Attributes"]')
            self.click_element('//span[contains(text(), "Add New Attribute")]')
            attribute_name = 'product' + ''.join(random.choice(string.digits) for _ in range(10))
            self.fill_textbox('//*[@id="attribute_code"]', attribute_name)
            self.click_element('//span[contains(text(), "Save Attribute")]')
            self.fill_textbox('//input[@name="frontend_label[0]"]', attribute_name)
            self.click_element('//span[contains(text(), "Save Attribute")]')

            if self.wait_for_text_in_page('The product attribute has been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_contact(self):
        self.login()
        self.set_test_name('mgt_setup_contact')
        print "[*] Starting setup contact process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create catalog
            self.hover_element('//span[text()="CMS"]')
            self.click_element('//span[text()="Pages"]')
            self.click_element('//span[contains(text(), "Add New Page")]')

            page_title = 'contact_page' + ''.join(random.choice(string.digits) for _ in range(10))
            self.fill_textbox('//input[@id="page_title"]', page_title)
            self.fill_textbox('//input[@id="page_identifier"]', page_title)
            self.select_dropdown('//*[@id="page_store_id"]', 'All Store Views')

            self.click_element('//span[contains(text(), "Content")]')
            self.fill_textbox('//input[@id="page_content_heading"]', 'Contact')
            self.fill_textbox('//*[@id="page_content"]', '<!- CONTACT FORM- >{{block type = "core/template" name = "contactForm" form_action = "/contacts/index/post" template = "contacts/form.phtml"}}<!- END OF CONTACT FORM- >')

            self.click_element('//span[contains(text(), "Save Page")]')

            if self.wait_for_text_in_page('The page has been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_categories(self):
        self.login()
        self.set_test_name('mgt_setup_categories')
        print "[*] Starting setup categories process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create catalog
            self.hover_element('//span[text()="Catalog"]')
            self.click_element('//span[text()="Manage Categories"]')
            time.sleep(5)
            group_name = 'group' + ''.join(random.choice(string.digits) for _ in range(10))
            self.fill_textbox('//input[@id="group_4name"]', group_name)
            self.select_dropdown('//*[@id="group_4is_active"]', 'Yes')

            self.click_element('//span[contains(text(), "Save Category")]')

            if self.wait_for_text_in_page('The category has been saved.') == None :
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
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create catalog
            self.hover_element('//span[text()="Catalog"]')
            self.click_element('//span[text()="Manage Products"]')
            self.click_element('//span[text()="Add Product"]')
            self.click_element('//span[text()="Continue"]')
            product_name = 'product' + ''.join(random.choice(string.digits) for _ in range(10))
            self.fill_textbox('//input[@id="name"]', product_name)
            self.fill_textbox('//*[@id="description"]', 'Description of ' + product_name)
            self.fill_textbox('//*[@id="short_description"]', 'Short description of ' + product_name)
            self.fill_textbox('//*[@id="sku"]', ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="weight"]', ''.join(random.choice(string.digits) for _ in range(2)))
            self.select_dropdown('//*[@id="status"]', 'Enabled')
            self.click_element('//span[contains(text(), "Save and Continue Edit")]')

            self.fill_textbox('//input[@id="price"]', '1100')
            self.select_dropdown('//*[@id="tax_class_id"]', 'Taxable Goods')

            self.click_element('//span[contains(text(), "Save")]')

            if self.wait_for_text_in_page('The product has been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_products(self):
        self.login()
        self.set_test_name('mgt_manage_products')
        print "[*] Starting manage products process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create catalog
            self.hover_element('//span[text()="Catalog"]')
            self.click_element('//span[text()="Manage Products"]')
            self.click_element('//*[@id="productGrid_table"]/tbody/tr[1]/td[12]/a')
            self.click_element('//span[contains(text(), "Inventory")]')
            self.fill_textbox('//input[@id="inventory_qty"]', '15')
            self.select_dropdown('//*[@id="inventory_stock_availability"]', 'In Stock')
            self.click_element('//span[contains(text(), "Save")]')

            if self.wait_for_text_in_page('The product has been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_inventory(self):
        self.login()
        self.set_test_name('mgt_setup_inventory')
        print "[*] Starting setup inventory process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create catalog
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//span[contains(text(), "Inventory")]')
            self.click_element('//a[@id="cataloginventory_options-head"]')
            self.click_element('//a[@id="cataloginventory_item_options-head"]')
            self.click_element('//a[@id="cataloginventory_options-head"]')
            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def notify_lowinventory(self):
        self.set_test_name('mgt_notify_lowinventory')
        print "[*] Starting notify low inventory process..."
        self.driver.get('http://admin:zaq1@WSX@' + self.main_page.replace('http://', '') + 'default/rss/catalog/notifystock/')
        try :
            if self.wait_for_text_in_page('Low Stock Products') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_tax(self):
        self.login()
        self.set_test_name('mgt_setup_tax')
        print "[*] Starting setup tax process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Tax Class 1/5
            self.hover_element('//span[text()="Sales"]')
            self.hover_element('//span[text()="Tax"]')
            self.click_element('//span[text()="Product Tax Classes"]')
            self.click_element('//span[contains(text(), "Add New")]')
            self.fill_textbox('//input[@id="class_name"]', 'tax_class' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//span[contains(text(), "Save Class")]')

            if self.wait_for_text_in_page('The tax class has been saved.') == None :
                 print '[-] (1/5) Test failed'
            else :
                print '[+] (1/5) Test successful'

            # Tax zone 2/5
            self.hover_element('//span[text()="Sales"]')
            self.hover_element('//span[text()="Tax"]')
            self.click_element('//span[text()="Manage Tax Zones & Rates"]')
            self.click_element('//span[contains(text(), "Add New Tax Rate")]')
            new_tax_code = 'tax_code' + ''.join(random.choice(string.digits) for _ in range(10))
            self.fill_textbox('//input[@id="code"]', new_tax_code)
            self.fill_textbox('//input[@id="rate"]', '8')
            self.click_element('//span[text()="Save Rate"]')

            if self.wait_for_text_in_page('The tax rate has been saved.') == None :
                 print '[-] (2/5) Test failed'
            else :
                print '[+] (2/5) Test successful'

            # Tax rule 3/5
            self.hover_element('//span[text()="Sales"]')
            self.hover_element('//span[text()="Tax"]')
            self.click_element('//span[text()="Manage Tax Rules"]')
            self.click_element('//span[contains(text(), "Add New Tax Rule")]')

            self.fill_textbox('//input[@id="code"]', 'tax_code' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="tax_customer_class"]', 'General')
            self.select_dropdown('//*[@id="tax_product_class"]', 'Shipping')
            self.select_dropdown('//*[@id="tax_rate"]', new_tax_code)
            self.click_element('//span[text()="Save Rule"]')

            if self.wait_for_text_in_page('The tax rule has been saved.') == None :
                 print '[-] (3/5) Test failed'
            else :
                print '[+] (3/5) Test successful'

            # Tax export 4/5
            self.hover_element('//span[text()="Sales"]')
            self.hover_element('//span[text()="Tax"]')
            self.click_element('//span[text()="Import / Export Tax Rates"]')
            time.sleep(3)
            self.click_element('//button[contains(@title, "Export Tax Rates")]')

            if self.wait_for_text_in_page('Export Tax Rates') == None :
                 print '[-] (4/5) Test failed'
            else :
                print '[+] (4/5) Test successful'

            # Tax import 5/5
            self.hover_element('//span[text()="Sales"]')
            self.hover_element('//span[text()="Tax"]')
            self.click_element('//span[text()="Import / Export Tax Rates"]')
            current_dir = os.path.dirname(os.path.realpath(__file__))
            self.fill_textbox('//*[@name="import_rates_file"]', current_dir + '/tax_rates.csv')
            self.click_element('//span[contains(text(), "Import Tax Rates")]')

            if self.wait_for_text_in_page('The tax rate has been imported.') == None :
                 print '[-] (5/5) Test failed'
            else :
                print '[+] (5/5) Test successful'

        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_shipping(self):
        self.login()
        self.set_test_name('mgt_setup_shipping')
        print "[*] Starting setup shipping process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup shipping
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//span[contains(text(), "Shipping Methods")]')
            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                 print '[-] (1/2) Test failed'
            else :
                print '[+] (1/2) Test successful'

            # export shipping
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.select_dropdown('//*[@id="store_switcher"]', 'Main Website')
            self.click_element('//span[contains(text(), "Shipping Methods")]')
            if not self.check_exists_and_visible_by_xpath('//span[text()="Export CSV"]'):
                self.click_element('//a[@id="carriers_tablerate-head"]')
            self.click_element('//span[text()="Export CSV"]')
            time.sleep(5)

            # import shipping
            current_dir = os.path.dirname(os.path.realpath(__file__))
            self.fill_textbox('//*[@id="carriers_tablerate_import"]', current_dir + '/tablerates.csv')
            self.click_element('//span[text()="Save Config"]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                 print '[-] (2/2) Test failed'
            else :
                print '[+] (2/2) Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_paymentmethods(self):
        self.login()
        self.set_test_name('mgt_setup_paymentmethods')
        print "[*] Starting setup payment methods process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup payment methods
            self.hover_element('//span[text()="System"]')
            self.click_element('//ul[@id="nav"]//span[text()="Configuration"]')
            self.click_element('//span[contains(text(), "Payment Methods")]')
            self.click_element('//*[@id="payment_payflow_advanced-head"]/span[1]')
            self.fill_textbox('//*[@id="payment_payments_advanced_partner"]', 'www.magento.com')
            self.fill_textbox('//*[@id="payment_payments_advanced_vendor"]', 'www.magento.com')
            self.fill_textbox('//*[@id="payment_payments_advanced_user"]', 'magento')
            self.fill_textbox('//*[@id="payment_payments_advanced_pwd"]', 'magento')
            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] (1/2) Test failed'
            else :
                print '[+] (1/2) Test successful'

            # Setup payment gateways
            self.hover_element('//span[text()="System"]')
            self.click_element('//ul[@id="nav"]//span[text()="Configuration"]')
            self.select_dropdown('//*[@id="store_switcher"]', 'Main Website')
            self.click_element('//span[contains(text(), "Payment Methods")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="payment_paypal_verisign_with_express_checkout-head"]/span[1]'):
                self.click_element('//*[@id="payment_account-head"]')
                self.click_element('//*[@id="payment_paypal_group_all_in_one-head"]')
                self.click_element('//*[@id="payment_paypal_payment_gateways-head"]')
            self.click_element('//*[@id="payment_paypal_verisign_with_express_checkout-head"]')

            self.toggle_checkbox('//*[@id="payment_paypal_payflow_api_settings_business_account_inherit"]', enable=False)
            self.fill_textbox('//*[@id="payment_paypal_payflow_api_settings_business_account"]', 'email' + ''.join(random.choice(string.digits) for _ in range(10)) + '@gmail.com')
            self.toggle_checkbox('//*[@id="payment_paypal_payflow_api_settings_partner_inherit"]', enable=False)
            self.fill_textbox('//*[@id="payment_paypal_payflow_api_settings_partner"]', 'www.magento.com')
            self.toggle_checkbox('//*[@id="payment_paypal_payflow_api_settings_user_inherit"]', enable=False)
            self.fill_textbox('//*[@id="payment_paypal_payflow_api_settings_user"]', 'magento')
            self.toggle_checkbox('//*[@id="payment_paypal_payflow_api_settings_vendor_inherit"]', enable=False)
            self.fill_textbox('//*[@id="payment_paypal_payflow_api_settings_vendor"]', 'magento')
            self.toggle_checkbox('//*[@id="payment_paypal_payflow_api_settings_pwd_inherit"]', enable=False)
            self.fill_textbox('//*[@id="payment_paypal_payflow_api_settings_pwd"]', 'magento')
            self.click_element('//span[text()="Save Config"]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                 print '[-] (2/2) Test failed'
            else :
                print '[+] (2/2) Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_currencies(self):
        self.login()
        self.set_test_name('mgt_setup_currencies')
        print "[*] Starting setup currencies process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup currencies
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//span[contains(text(), "Currency Setup")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="currency_options_base"]'):
                self.click_element('//*[@id="currency_options-head"]')
            self.select_dropdown('//*[@id="currency_options_base"]', 'Afghan Afghani')
            self.select_dropdown('//*[@id="currency_options_allow"]', 'Afghan Afghani')
            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_checkoutoptions(self):
        self.login()
        self.set_test_name('mgt_setup_checkoutoptions')
        print "[*] Starting setup checkout options process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup currencies
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//*[@id="system_config_tabs"]//span[contains(text(), "Checkout")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="checkout_options_enable_agreements"]'):
                self.click_element('//*[@id="checkout_options-head"]')
            self.select_dropdown('//*[@id="checkout_options_enable_agreements"]', 'Yes')
            if not self.check_exists_and_visible_by_xpath('//*[@id="checkout_sidebar_display"]'):
                self.click_element('//*[@id="checkout_sidebar-head"]')
            self.select_dropdown('//*[@id="checkout_sidebar_display"]', 'Yes')

            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_googlecheckout(self):
        self.login()
        self.set_test_name('mgt_setup_googlecheckout')
        print "[*] Starting setup google checkout options process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup currencies
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//span[contains(text(), "Google API")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="google_analytics_active"]'):
                self.click_element('//*[@id="google_analytics-head"]')
            self.select_dropdown('//*[@id="google_analytics_active"]', 'Yes')
            self.fill_textbox('//*[@id="google_analytics_account"]', '123456')
            self.click_element('//*[@id="google_analytics_anonymization"]')
            # Missing option in 1.9.0

            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_store(self):
        self.login()
        self.set_test_name('mgt_setup_store')
        print "[*] Starting setup store process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup currencies
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Manage Stores"]')
            self.click_element('//span[contains(text(), "Create Store")]')
            self.fill_textbox('//*[@id="group_name"]', 'store' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="group_root_category_id"]', 'Default Category')

            self.click_element('//span[contains(text(), "Save Store")]')

            if self.wait_for_text_in_page('The store has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def process_order(self):
        self.login()
        self.set_test_name('mgt_process_order')
        print "[*] Starting process order process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup currencies
            self.hover_element('//span[text()="Sales"]')
            self.click_element('//span[text()="Orders"]')
            self.click_element('//*[@id="sales_order_grid_table"]/tbody/tr[1]/td[10]/a')
            # Tracking is not enabled!
            self.fill_textbox('//*[@name="history[comment]"]', 'comment' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//*[@name="history[is_customer_notified]"]')
            self.click_element('//span[contains(text(), "Submit Comment")]')

            if self.wait_for_text_in_page('Notified') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def export_sales_report(self):
        self.login()
        self.set_test_name('mgt_export_sales_order')
        print "[*] Starting export sales order process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup currencies
            self.hover_element('//span[text()="Reports"]')
            self.hover_element('//span[text()="Reports"]/ancestor::li//span[text()="Sales"]')
            self.click_element('//span[text()="Reports"]/ancestor::li//span[text()="Orders"]')
            self.fill_textbox('//*[@id="sales_report_from"]', '1/1/2015')
            self.fill_textbox('//*[@id="sales_report_to"]', '1/1/2017')
            self.click_element('//button[@title="Export"]//span[contains(text(), "Export")]')

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

    def setup_order_emails(self):
        self.login()
        self.set_test_name('mgt_setup_order_emails')
        print "[*] Starting setup order emails process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Setup currencies
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//span[contains(text(), "Sales Emails")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="sales_email_order_enabled"]'):
                self.click_element('//*[@id="sales_email_order-head"]')
            self.select_dropdown('//*[@id="sales_email_order_enabled"]', 'Yes')
            self.select_dropdown('//*[@id="sales_email_order_identity"]', 'Sales Representative')
            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def create_order(self):
        self.login()
        self.set_test_name('mgt_create_order')
        print "[*] Starting create order process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create order
            self.hover_element('//span[text()="Sales"]')
            self.click_element('//span[text()="Orders"]')
            self.click_element('//span[contains(text(), "Create New Order")]')
            self.click_element('//span[contains(text(), "Create New Customer")]')
            self.click_element('//*[@id="store_1"]')

            # Add product
            self.click_element('//span[contains(text(), "Add Products")]')
            self.click_element('//*[@value="905"]')
            self.click_element('//*[@value="904"]')
            self.click_element('//*[@value="903"]')
            self.click_element('//span[contains(text(), "Add Selected Product(s) to Order")]')

            # Create customer
            self.fill_textbox('//*[@id="email"]', 'email' + ''.join(random.choice(string.digits) for _ in range(10)) + '@gmail.com')
            self.fill_textbox('//*[@id="order-billing_address_firstname"]', 'name' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="order-billing_address_lastname"]', 'lastname' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="order-billing_address_street0"]', 'street' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="order-billing_address_city"]', 'San Jose')
            self.select_dropdown('//*[@id="order-billing_address_country_id"]', 'United States')
            self.select_dropdown('//*[@id="order-billing_address_region_id"]', 'California')
            self.fill_textbox('//*[@id="order-billing_address_postcode"]', '94088')
            self.fill_textbox('//*[@id="order-billing_address_telephone"]', '1234567890')
            self.click_element('//*[@id="order-billing_address_fax"]')
            self.click_element('//*[@id="order-shipping-method-summary"]/a')
            self.click_element('//*[@id="s_method_freeshipping_freeshipping"]')
            #if self.driver.find_element_by_xpath('//*[@id="order-shipping_address_prefix"]').is_enabled():
            #    self.toggle_checkbox('//*[@id="order-shipping_same_as_billing"]')
            self.click_element('//*[@id="submit_order_top_button"]')
            time.sleep(5)

            if self.wait_for_text_in_page('The order has been created.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def manage_order(self):
        self.login()
        self.set_test_name('mgt_manage_order')
        print "[*] Starting manage order process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="Sales"]')
            self.click_element('//span[text()="Orders"]')
            self.click_element('//*[@id="sales_order_grid_table"]/tbody/tr[1]/td[10]/a')

            self.click_element('//button[@title="Invoice"]')
            self.click_element('//span[contains(text(), "Submit Invoice")]')

            if self.wait_for_text_in_page('The invoice has been created.') == None :
                print '[-] (1/3) Test failed'
            else :
                print '[+] (1/3) Test successful'

            # Add comment
            self.fill_textbox('//*[@id="history_comment"]', 'comment' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//*[@id="history_notify"]')
            self.click_element('//span[contains(text(), "Submit Comment")]')
            if self.wait_for_text_in_page('Notified') == None :
                print '[-] (2/3) Test failed'
            else :
                print '[+] (2/3) Test successful'

            # Ship
            self.click_element('//button[@title="Ship"]')
            self.click_element('//span[contains(text(), "Add Tracking Number")]')
            self.select_dropdown('//*[@id="trackingC1"]', 'United States Postal Service')
            self.fill_textbox('//*[@id="trackingN1"]', ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//span[contains(text(), "Submit Shipment")]')
            if self.wait_for_text_in_page('The shipment has been created.') == None :
                print '[-] (3/3) Test failed'
            else :
                print '[+] (3/3) Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_customers(self):
        self.login()
        self.set_test_name('mgt_setup_customers')
        print "[*] Starting setup customers process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//span[contains(text(), "Customer Configuration")]')

            self.click_element('//button[@title="Save Config"]')


            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_prettyurls(self):
        self.login()
        self.set_test_name('mgt_setup_prettyurls')
        print "[*] Starting setup pretty urls process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//*[@id="system_config_tabs"]//span[contains(text(), "Web")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="web_seo_use_rewrites"]'):
                self.click_element('//*[@id="web_seo-head"]')
            self.select_dropdown('//*[@id="web_seo_use_rewrites"]', 'Yes')
            self.click_element('//button[@title="Save Config"]')


            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_youtubevideo(self):
        self.login()
        self.set_test_name('mgt_setup_youtubevideo')
        print "[*] Starting setup youtube video process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="CMS"]')
            self.click_element('//span[text()="Pages"]')
            self.click_element('//*[@id="cmsPageGrid_table"]/tbody/tr[1]/td[1]')
            self.click_element('//*[@id="page_tabs_content_section"]')
            self.fill_textbox('//*[@id="page_content"]', '''<div class="page-head">
                <h3>OUR STORY</h3>
                </div>
                <div class="col2-set content-seperator">
                <div class="col-1">
                <p>Madison Island is...</p>
                <p style="padding-left: 30px;">...a breath of fresh air.<br />&hellip;a mecca for style savvy travellers. <br />&hellip;a curator of gorgeous sartorial design. <br />&hellip;a world class concept store.</p></div>
                <div class="col-2">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/TCVTOa01uN8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                <p><img src="{{media url="wysiwyg/about_us.jpg"}}" alt="about-usimage" /></p>
                <h2 style="text-align: center;padding-left:30px">Madison Island Boutique in NYC</h2></div><div class="std">
                <p>Uniquely designed with cosmopolitan appeal, Madison Island gives couture-conscious frequent flyers exactly what they want&mdash;unprecedented access to the latest looks of the season, style solutions for easy international jet setting, and convenient worldwide delivery.</p>
                <p style="margin-top: 13px;">With its website relaunch in 2013, Madison Island has solidified its standing as the new essential luxury. Its pages are filled with exquisite finds for fashion and home.</p>
                </div>
                </div>
                ''')
            self.click_element('//button[@title="Save Page"]')

            if self.wait_for_text_in_page('The page has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def refresh_cache(self):
        self.login()
        self.set_test_name('mgt_refresh_cache')
        print "[*] Starting refresh cache process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Cache Management"]')
            self.select_dropdown('//*[@id="cache_grid_massaction-select"]', 'Refresh')
            self.click_element('//a[text()="Select All"]')
            self.click_element('//button[@title="Submit"]')


            if self.wait_for_text_in_page('cache type(s) refreshed.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_translation(self):
        self.login()
        self.set_test_name('mgt_setup_translation')
        print "[*] Starting setup translation process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="general_locale_code"]'):
                self.click_element('//*[@id="general_locale-head"]')
            self.select_dropdown('//*[@id="general_locale_code"]', 'Persian (Iran)')
            self.click_element('//button[@title="Save Config"]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
                self.logout()
                self.login()
                self.driver.get(self.admin_page)
                print '[*] Reverting language to english'
                self.hover_element('//span[text()="System"]')
                self.click_element('//span[text()="Configuration"]')
                if not self.check_exists_and_visible_by_xpath('//*[@id="general_locale_code"]'):
                    self.click_element('//*[@id="general_locale-head"]')
                self.select_dropdown('//*[@id="general_locale_code"]', 'انگلیسی (ایالات متحدهٔ امریکا)')
                self.click_element('//button[@title="Save Config"]')
                self.logout()
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_theme(self): #NOT WORKING
        self.login()
        self.set_test_name('mgt_setup_theme')
        print "[*] Starting setup theme process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="System"]')
            self.hover_element('//span[text()="Magento Connect"]')
            self.click_element('//span[text()="Magento Connect Manager"]')
            self.login(current_page=True)
            self.fill_textbox('//*[@id="install_package_id"]', 'https://connect20.magentocommerce.com/e8dd713766cdf2894825dfb758c5d350/swissup+TM_Templatef001-2.0.1')
            self.click_element('//button[text()="Install"]')
            self.click_element('//button[text()="Proceed"]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_pagetitle(self):
        self.login()
        self.set_test_name('mgt_setup_pagetitle')
        print "[*] Starting setup page title process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//*[@id="system_config_tabs"]//span[contains(text(), "Design")]')
            self.fill_textbox('//*[@id="design_head_default_title"]', 'title ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//span[contains(text(), "Save Config")]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_pagelayout(self):
        self.login()
        self.set_test_name('mgt_setup_pagelayout')
        print "[*] Starting setup page layout process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="CMS"]')
            self.click_element('//span[text()="Pages"]')
            self.click_element('//*[@id="cmsPageGrid_table"]/tbody/tr[1]/td[1]')
            self.click_element('//*[@id="page_tabs"]//span[contains(text(), "Design")]')
            self.select_dropdown('//*[@id="page_root_template"]', '3 columns')

            self.click_element('//span[contains(text(), "Save Page")]')

            if self.wait_for_text_in_page('The page has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_newpage(self):
        self.login()
        self.set_test_name('mgt_setup_newpage')
        print "[*] Starting setup new page process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="CMS"]')
            self.click_element('//span[text()="Pages"]')
            self.click_element('//button[@title="Add New Page"]')
            self.fill_textbox('//*[@id="page_title"]', 'title ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="page_identifier"]', 'page_id_' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="page_store_id"]', 'All Store Views')
            self.click_element('//span[contains(text(), "Save and Continue Edit")]')

            self.fill_textbox('//*[@id="page_content_heading"]', 'heading ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="page_content"]', 'page content ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//*[@id="page_content"]')

            self.click_element('//*[@id="page_tabs"]//span[contains(text(), "Design")]')

            self.click_element('//button[@title="Save Page"]')

            if self.wait_for_text_in_page('The page has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_cms(self):
        self.login()
        self.set_test_name('mgt_setup_cms')
        print "[*] Starting setup cms process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # 1/3 Create static block
            self.hover_element('//span[text()="CMS"]')
            self.click_element('//span[text()="Static Blocks"]')
            self.click_element('//button[@title="Add New Block"]')
            self.fill_textbox('//*[@id="block_title"]', 'block' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="block_identifier"]', 'blockid' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="block_store_id"]', 'All Store Views')
            self.fill_textbox('//*[@id="block_content"]', 'block content ' + ''.join(random.choice(string.digits) for _ in range(10)))

            self.click_element('//button[@title="Save Block"]')

            if self.wait_for_text_in_page('The block has been saved.') == None :
                print '[-] (1/2) Test failed'
            else :
                print '[+] (1/2) Test successful'

            # 2/3 Create widgets
            self.hover_element('//span[text()="CMS"]')
            self.click_element('//span[text()="Widgets"]')
            self.click_element('//button[@title="Add New Widget Instance"]')
            self.select_dropdown('//*[@title="Type"]', 'CMS Static Block')
            self.select_dropdown('//*[@id="package_theme"]', 'base / default')
            self.click_element('//button[@title="Continue"]')
            self.fill_textbox('//*[@id="title"]', 'widget title ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="store_ids"]', 'All Store Views')

            self.click_element('//button[@title="Add Layout Update"]')
            self.select_dropdown('//*[@id="widget_instance[0][page_group]"]', 'All Pages')
            self.select_dropdown('//*[@name="widget_instance[0][all_pages][block]"]', 'Left Column')

            self.click_element('//span[contains(text(), "Widget Options")]')
            self.click_element('//button[@title="Select Block..."]')
            self.click_element('//td[contains(text(), "Footer Links SM")]')
            self.click_element('//button[@title="Save"]')

            if self.wait_for_text_in_page('The widget instance has been saved.') == None :
                print '[-] (2/2) Test failed'
            else :
                print '[+] (2/2) Test successful'

            # Not available in 1.9.0
            # 3/3 Create polls
            '''self.hover_element('//span[text()="CMS"]')
            self.click_element('//span[text()="Polls"]')
            self.click_element('//button[@title="Add New Widget Instance"]')
            self.select_dropdown('//*[@id="type"]', 'CMS Static Block')
            self.select_dropdown('//*[@id="package_theme"]', 'base / default')
            self.hover_element('//span[text()="Continue"]')
            self.fill_textbox('//*[@id="title"]', 'widget title ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.select_dropdown('//*[@id="store_ids"]', 'All Store Views')

            self.click_element('//button[@title="Add Layout Update"]')
            self.select_dropdown('//*[@id="widget_instance[0][page_group]"]', 'All Pages')
            self.select_dropdown('//*[@name="widget_instance[0][all_pages][block]"]', 'Left Column')

            self.click_element('//span[contains(text(), "Widget Options")]')
            self.click_element('//button[@title="Select Block..."]')
            self.click_element('//td[contains(text(), "Footer Links SM")]')
            self.click_element('//button[@title="Save"]')'''

            if self.wait_for_text_in_page('The widget instance has been saved.') == None :
                print '[-] (2/3) Test failed'
            else :
                print '[+] (2/3) Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_newsletter(self):
        self.login()
        self.set_test_name('mgt_setup_newsletter')
        print "[*] Starting setup newsletter process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # 1/4 enable newsletter
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//*[@id="system_config_tabs"]/li[6]/dl/dd[3]/a')
            if not self.check_exists_and_visible_by_xpath('//*[@id="Cm_RedisSession"]'):
                self.click_element('//a[@id="advanced_modules_disable_output-head"]')
            self.select_dropdown('//*[@id="Mage_Newsletter"]', 'Enable')
            self.click_element('//button[@title="Save Config"]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] (1/4) Test failed'
            else :
                print '[+] (1/4) Test successful'
            # 2/4 config newsletter
            self.click_element('//*[@id="system_config_tabs"]//span[contains(text(), "Newsletter")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="newsletter_subscription_confirm"]'):
                self.click_element('//a[@id="newsletter_subscription-head"]')
            self.select_dropdown('//*[@id="newsletter_subscription_confirm"]', 'Yes')
            self.click_element('//button[@title="Save Config"]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] (2/4) Test failed'
            else :
                print '[+] (2/4) Test successful'
            # 3/4 create newsletter template
            self.hover_element('//span[text()="Newsletter"]')
            self.click_element('//span[text()="Newsletter Templates"]')
            self.click_element('//span[text()="Add New Template"]')
            template_name = 'newsletter template ' + ''.join(random.choice(string.digits) for _ in range(10))
            self.fill_textbox('//*[@id="code"]', template_name)
            self.fill_textbox('//*[@id="subject"]', 'newsletter template ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.click_element('//button[@title="Save Template"]')

            if self.wait_for_text_in_page(template_name) == None :
                print '[-] (3/4) Test failed'
            else :
                print '[+] (3/4) Test successful'
            # 4/4 send newsletter
            # 3/4 create newsletter template
            self.hover_element('//span[text()="Newsletter"]')
            self.click_element('//span[text()="Newsletter Queue"]')
            self.hover_element('//span[text()="Newsletter"]')
            self.click_element('//span[text()="Newsletter Templates"]')
            self.select_dropdown('//table[@class="data"]/tbody/tr[1]/td[8]/select', 'Queue Newsletter...')
            self.click_element('//button[@title="Save Newsletter"]')

            if self.wait_for_text_in_page('Newsletter Queue') == None :
                print '[-] (4/4) Test failed'
            else :
                print '[+] (4/4) Test successful'

        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def setup_seo(self):
        self.login()
        self.set_test_name('mgt_setup_seo')
        print "[*] Starting setup seo process..."
        self.driver.get(self.admin_page)
        # Fill form fields
        try :
            # Create invoice
            self.hover_element('//span[text()="System"]')
            self.click_element('//span[text()="Configuration"]')
            self.click_element('//*[@id="system_config_tabs"]//span[contains(text(), "Web")]')
            if not self.check_exists_and_visible_by_xpath('//*[@id="web_url_use_store"]'):
                self.click_element('//*[@id="web_url-head"]')
            self.select_dropdown('//*[@id="web_url_use_store"]', 'Yes')


            self.click_element('//button[@title="Save Config"]')

            if self.wait_for_text_in_page('The configuration has been saved.') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def customer_signup(self):
        self.set_test_name('mgt_customer_signup')
        print "[*] Starting customer signup process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Create invoice
            self.click_element('//span[text()="Account"]')
            self.click_element('//a[text()="Register"]')
            self.fill_textbox('//*[@id="firstname"]', 'name ' + ''.join(random.choice(string.digits) for _ in range(10)))
            self.fill_textbox('//*[@id="lastname"]', 'lastname ' + ''.join(random.choice(string.digits) for _ in range(10)))
            new_user = 'email' + ''.join(random.choice(string.digits) for _ in range(10)) + '@gmail.com'
            self.fill_textbox('//*[@id="email_address"]', new_user)
            self.fill_textbox('//*[@id="password"]', 'zaq1@WSX')
            self.fill_textbox('//*[@id="confirmation"]', 'zaq1@WSX')
            self.click_element('//*[@id="is_subscribed"]')
            self.click_element('//button[@title="Register"]')

            if self.wait_for_text_in_page('Thank you for registering with') == None :
                print '[-] Test failed'
            else :
                print '[+] Test successful'
                self.new_username = new_user
            mgt.customer_logout()
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def customer_login(self):
        self.set_test_name('mgt_customer_login')
        print "[*] Starting customer login process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Create invoice
            self.click_element('//span[text()="Account"]')
            self.click_element('//a[text()="Log In"]')
            self.fill_textbox('//*[@id="email"]', self.new_username)
            self.fill_textbox('//*[@id="pass"]', 'zaq1@WSX')
            self.click_element('//button[@title="Login"]')

            if self.wait_for_text_in_page('Log Out') == None :
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
        print "[*] Starting customer logout process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Create invoice
            self.click_element('//span[text()="Account"]')
            self.click_element('//a[text()="Log Out"]')

            if self.wait_for_text_in_page('You are now logged out') == None :
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
        print "[*] Starting customer checkout process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Add to cart
            self.click_element('//*[@id="top"]/body/div/div/div[2]/div/div/div/div[2]/div[2]/ul/li[1]')
            self.select_dropdown('//*[@id="attribute92"]')
            self.select_dropdown('//*[@id="attribute180"]')
            self.click_element('//button[@title="Add to Cart"]')

            if self.wait_for_text_in_page('was added to your shopping cart.') == None :
                print '[-] (1/3) Test failed'
            else :
                print '[+] (1/3) Test successful'

            self.select_dropdown('//*[@id="region_id"]', 'Alabama')
            self.fill_textbox('//*[@id="postcode"]', '12345')
            self.click_element('//button[@title="Estimate"]')
            self.click_element('(//*[@name="estimate_method"])[1]')
            self.click_element('//button[@title="Update Total"]')
            self.click_element('//button[@title="Proceed to Checkout"]')

            self.fill_textbox('//*[@id="login-email"]', 'test@gmail.com')
            self.fill_textbox('//*[@id="login-password"]', 'zaq1@WSX')
            self.click_element('//span[text()="Login"]')

            # Confirm Address
            self.click_element('//button[@title="Continue"]')
            self.click_element('(//*[@name="shipping_method"])[1]')
            # Confirm Shipping
            self.click_element('//*[@id="shipping-method-buttons-container"]//button')
            # Confirm Cash on Delivery
            self.click_element('//*[@id="payment-buttons-container"]//span[text()="Continue"]')
            # Place Order
            self.click_element('//button[@title="Place Order"]')

            if self.wait_for_text_in_page('Your order has been received.') == None :
                print '[-] (2/3) Test failed'
            else :
                print '[+] (2/3) Test successful'

            # View order
            self.click_element('//a[contains(@href, "sales/order/view")]')
            if self.wait_for_text_in_page('About This Order:') == None :
                print '[-] (3/3) Test failed'
            else :
                print '[+] (3/3) Test successful'

        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def guest_checkout(self):
        self.set_test_name('mgt_guest_checkout')
        print "[*] Starting guest checkout process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Add to cart
            self.click_element('//*[@id="top"]/body/div/div/div[2]/div/div/div/div[2]/div[2]/ul/li[1]')
            self.select_dropdown('//*[@id="attribute92"]')
            self.select_dropdown('//*[@id="attribute180"]')
            self.click_element('//button[@title="Add to Cart"]')

            if self.wait_for_text_in_page('was added to your shopping cart.') == None :
                print '[-] (1/2) Test failed'
            else :
                print '[+] (1/2) Test successful'

            self.select_dropdown('//*[@id="region_id"]', 'Alabama')
            self.fill_textbox('//*[@id="postcode"]', '12345')
            #self.click_element('//button[@title="Estimate"]')
            if self.check_exists_and_visible_by_xpath('//*[@id="s_method_flatrate_flatrate"]'):
                self.click_element('//*[@id="s_method_flatrate_flatrate"]')
            #self.click_element('//button[@title="Update Total"]')
            self.click_element('//button[@title="Proceed to Checkout"]')

            self.click_element('//*[@id="onepage-guest-register-button"]')

            self.fill_textbox('//*[@id="billing:firstname"]', 'customer name')
            self.fill_textbox('//*[@id="billing:lastname"]', 'customer lastname')
            self.fill_textbox('//*[@id="billing:email"]', 'customer123@gmail.com')
            self.fill_textbox('//*[@id="billing:street1"]', 'street 123')
            self.fill_textbox('//*[@id="billing:city"]', 'nyc')
            self.select_dropdown('//*[@id="billing:region_id"]', 'Alabama')
            self.fill_textbox('//*[@id="billing:postcode"]', '12345')
            self.fill_textbox('//*[@id="billing:telephone"]', '1234564494')
            self.click_element('//*[@id="billing-buttons-container"]//button')

            time.sleep(10)
            if self.check_exists_and_visible_by_xpath('//*[@id="s_method_flatrate_flatrate"]'):
                self.click_element('//*[@id="s_method_flatrate_flatrate"]')

            self.click_element('//*[@id="shipping-method-buttons-container"]//button')
            self.click_element('//*[@id="payment-buttons-container"]//button')
            self.click_element('//*[@id="review-buttons-container"]//button')

            if self.wait_for_text_in_page('Your order has been received.') == None :
                print '[-] (2/2) Test failed'
            else :
                print '[+] (2/2) Test successful'

        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def forgot_password(self):
        self.set_test_name('mgt_forgot_password')
        print "[*] Starting forgot password process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Create invoice
            self.click_element('//span[text()="Account"]')
            self.click_element('//a[text()="Log In"]')
            self.click_element('//a[text()="Forgot Your Password?"]')
            self.fill_textbox('//*[@id="email_address"]', self.new_username)
            self.click_element('//button[@title="Submit"]')

            if self.wait_for_text_in_page('you will receive an email with a link to reset your password.') == None :
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
    # Store Setup
    mgt.add_product_attribute()
    mgt.setup_contact()
    mgt.setup_categories()
    mgt.setup_products()
    mgt.manage_products()
    mgt.setup_inventory()
    mgt.notify_lowinventory()
    mgt.setup_tax()
    mgt.setup_shipping()
    mgt.setup_paymentmethods()
    mgt.setup_currencies()
    mgt.setup_checkoutoptions()
    mgt.setup_googlecheckout()
    mgt.setup_store()
    # Order
    mgt.process_order()
    mgt.export_sales_report()
    mgt.setup_order_emails()
    mgt.create_order()
    mgt.manage_order()
    # System Setup
    mgt.setup_customers()
    mgt.setup_prettyurls()
    mgt.setup_youtubevideo()
    mgt.refresh_cache()
    mgt.setup_translation()
    # Install module
    mgt.setup_pagetitle()
    mgt.setup_pagelayout()
    mgt.setup_newpage()
    mgt.setup_cms()
    mgt.setup_newsletter()
    mgt.setup_seo()
    # Customer
    mgt.customer_signup()
    mgt.customer_login()
    mgt.customer_logout()
    mgt.customer_checkout()
    mgt.customer_logout()
    mgt.guest_checkout()
    mgt.forgot_password()
