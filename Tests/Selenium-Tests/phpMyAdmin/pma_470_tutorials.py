#!/usr/bin/python

import time, os, errno, argparse, sys, random, string
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from datetime import datetime
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import Select

class PhpMyAdminTests:
    def __init__(self):
        # UPDATE HERE (1/5)
        self.main_page = 'http://localhost:8085/phpMyAdmin-4.7.0-all-languages/'
        print "[+] Setting up ChromeDriver"
        options = webdriver.chrome.options.Options()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        self.add_cookies()
        self.new_username = ''
        self.logged_in = False
    def add_cookies(self):
        self.driver.get(self.main_page + 'doc/html/intro.html')
        # UPDATE HERE (2/5)
        self.driver.add_cookie({'name': 'test_group', 'value': 'pma470_tutorials'})
        # UPDATE HERE (3/5)
        self.driver.add_cookie({'name': 'test_name', 'value': 'pma_login_pma470_tutorials'})
        # UPDATE HERE (4/5)
        self.driver.add_cookie({'name': 'software_id', 'value': '1'})
        # UPDATE HERE (5/5)
        self.driver.add_cookie({'name': 'software_version_id', 'value': '4'})
    def set_test_name(self, test_name):
        self.driver.delete_cookie('test_name')
        self.driver.add_cookie({'name': 'test_name', 'value': test_name})
    def click_element(self, xpath_selector):
        try:
            time.sleep(1)
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.click()
        except Exception as e:
            print '[-] Failed to click on element'
            print e
    def fill_textbox(self, xpath_selector, text):
        try:
            time.sleep(1)
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print '[-] Failed to fill textbox'
            print e
    def select_dropdown(self, xpath_selector, text):
        try:
            time.sleep(1)
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            Select(element).select_by_visible_text(text)
        except Exception as e:
            print '[-] Failed to select optin'
            print e
    def check_exists_and_visible_by_xpath(self, xpath_selector):
        try :
            return self.driver.find_element_by_xpath(xpath_selector).is_displayed()
        except NoSuchElementException :
            return False
        return True
    def wait_for_element_become_visible(self, xpath_selector) :
        timeout = 20
        while not self.check_exists_and_visible_by_xpath(xpath_selector) :
            print "[+] Waiting for %s to become visible" % xpath_selector
            # Wait for login pop up to load via ajax
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0 :
                print "[-] Timed out %s" % xpath_selector
                return None
    def wait_for_text_in_page(self, text) :
        timeout = 20
        while not text in self.driver.page_source :
            print "[+] Waiting for text: %s to load in page" % text
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0 :
                print "[-] Timed out %s" % text
                return None
        return True
    def login(self, username=None, password=None):
        self.set_test_name('pma_login')
        print "[*] Starting login process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            if self.logged_in:
                print '[+] Already logged in, skipping.'
                return
            # Enter Username
            self.fill_textbox('//*[@id="input_username"]', 'root' if username == None else username)
            # Enter password
            self.fill_textbox('//*[@id="input_password"]', 'root' if password == None else password)
            # Click submit
            self.click_element('//*[@id="input_go"]')
            time.sleep(3)
            if self.wait_for_text_in_page('Log out' if username == None else username) == None :
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
            self.click_element('//*[@id="leftframelinks"]/a[2]')
            self.logged_in = False
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)

    def create_database(self):
        self.login()
        self.set_test_name('pma_create_database')
        print "[*] Starting create database process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Create database
            self.click_element('//*[@id="topmenu"]/li[1]/a')
            self.fill_textbox('//*[@id="text_create_db"]', 'test_db')
            self.click_element('//*[@id="buttonGo"]')

            # Select database
            self.click_element('//a[contains(@href, "test_db") and contains(@href, "db_structure.php")]')
            self.fill_textbox('//*[@id="create_table_form_minimal"]/fieldset[1]/div[2]/input', '5')
            self.fill_textbox('//*[@id="create_table_form_minimal"]/fieldset[1]/div[1]/input', 'tbl1')
            self.click_element('//*[@id="create_table_form_minimal"]/fieldset[2]/input')

            # Create columns
            self.fill_textbox('//*[@id="field_0_1"]', 'col1')
            self.select_dropdown('//*[@id="field_0_7"]', 'PRIMARY')
            self.click_element('//button[contains(text(), "Go")]')
            self.click_element('//*[@id="field_0_8"]')

            self.fill_textbox('//*[@id="field_1_1"]', 'col2')
            self.select_dropdown('//*[@id="field_1_2"]', 'VARCHAR')
            self.fill_textbox('//*[@id="field_1_3"]', '50')
            self.select_dropdown('//*[@id="field_1_4"]', 'As defined:')
            self.fill_textbox('//*[@id="table_columns"]/tbody/tr[3]/td[4]/input', 'a')

            self.fill_textbox('//*[@id="field_2_1"]', 'col3')
            self.select_dropdown('//*[@id="field_2_2"]', 'DATE')

            self.fill_textbox('//*[@id="field_3_1"]', 'col4')
            self.select_dropdown('//*[@id="field_2_2"]', 'DATE')

            self.fill_textbox('//*[@id="field_4_1"]', 'col5')

            self.click_element('//input[@value="Save"]')

            if (self.wait_for_text_in_page('tbl1') == None) and (self.wait_for_text_in_page('Browse') == None) :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def input_data_to_table(self):
        self.login()
        self.set_test_name('pma_input_data_to_table')
        print "[*] Starting input data to table process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "test_db") and contains(@href, "db_structure.php")]')
            self.click_element('//span[contains(text(), "Insert")]')

            self.fill_textbox('//*[@id="field_2_3"]', 'b')
            self.fill_textbox('//*[@id="field_3_3"]', '2018-07-01')
            self.fill_textbox('//*[@id="field_4_3"]', '4')
            self.fill_textbox('//*[@id="field_5_3"]', '6')
            self.click_element('//*[@id="insertForm"]/table[1]/tfoot/tr/th/input')

            if self.wait_for_text_in_page('1 row inserted.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def run_query(self):
        self.login()
        self.set_test_name('pma_run_query')
        print "[*] Starting run query process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "server_sql")]')
            self.fill_textbox('//*[@id="sqlquery"]', 'USE test_db;\nINSERT INTO tbl1(col2,col3,col4,col5) VALUES(2,NOW(),4,5);\nSELECT * FROM tbl1;')
            self.click_element('//*[@id="button_submit_query"]')

            if self.wait_for_text_in_page('Your SQL query has been executed successfully') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def create_index(self):
        self.login()
        self.set_test_name('pma_create_index')
        print "[*] Starting create index process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "test_db") and contains(@href, "db_structure.php")]')
            self.click_element('//*[@id="tablesForm_checkall"]')
            self.click_element('//span[contains(text(), "Structure")]')
            self.click_element('//span[contains(text(), "Index")]')
            self.click_element('//div[@role="dialog"]//button[contains(text(), "OK")]')

            if self.wait_for_text_in_page('MySQL returned an empty result set (i.e. zero rows)') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def browse_table(self):
        self.login()
        self.set_test_name('pma_browse_table_data')
        print "[*] Starting browse table process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "test_db") and contains(@href, "db_structure.php")]')
            self.click_element('//span[contains(text(),"Browse")]')

            if self.wait_for_text_in_page('Showing rows') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def backup_export(self):
        self.login()
        self.set_test_name('pma_backup_export')
        print "[*] Starting backup export process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "test_db") and contains(@href, "db_structure.php")]')
            time.sleep(5)
            self.click_element('//a[contains(@href,"db_export")]')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click_element('//*[@id="buttonGo"]')

            if self.wait_for_text_in_page('Exporting tables from "test_db" database') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def adduser(self):
        self.login()
        self.set_test_name('pma_adduser')
        print "[*] Starting add user process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "test_db") and contains(@href, "db_structure.php")]')
            self.click_element('//a[contains(@href,"server_privi")]')
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click_element('//*[@id="fieldset_add_user"]/a')
            self.fill_textbox('//*[@id="fieldset_add_user_login"]/div[1]/input', 'testuser' + ''.join(random.choice(string.digits) for _ in range(5)))
            self.fill_textbox('//*[@id="text_pma_pw"]', '1234567890')
            self.fill_textbox('//*[@id="text_pma_pw2"]', '1234567890')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click_element('//input[@value="Go"]')

            if self.wait_for_text_in_page('CREATE USER \'testuser') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def optimize_database(self):
        self.login()
        self.set_test_name('pma_optimize_database')
        print "[*] Starting optimize database process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "test_db") and contains(@href, "db_structure.php")]')
            self.click_element('//input[contains(@title, "Check")]')
            self.select_dropdown('//*[@id="tablesForm"]/div/select', 'Optimize table')

            if self.wait_for_text_in_page('Your SQL query has been executed successfully') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def check_status(self):
        self.login()
        self.set_test_name('pma_check_status')
        print "[*] Starting check status process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href,"server_status")]')

            if self.wait_for_text_in_page('This MySQL server has been running for') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def check_variables(self):
        self.login()
        self.set_test_name('pma_check_variables')
        print "[*] Starting check variables process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href,"server_variables")]')

            if self.wait_for_text_in_page('Server variables and settings') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def check_charsets(self):
        self.login()
        self.set_test_name('pma_check_charsets')
        print "[*] Starting check charsets process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href,"server_collations")]')
            if self.wait_for_text_in_page('Character Sets and Collations') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def check_engines(self):
        self.login()
        self.set_test_name('pma_check_engines')
        print "[*] Starting check charsets process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href, "server_engines")]')

            if self.wait_for_text_in_page('Storage Engines') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def import_sql(self):
        self.login()
        self.set_test_name('pma_import')
        print "[*] Starting import process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href,"server_import")]')
            script_dir = os.path.dirname(os.path.realpath(__file__))
            self.fill_textbox('//*[@id="input_import_file"]', script_dir + '/test_db.sql')
            self.click_element('//*[@id="buttonGo"]')

            if self.wait_for_text_in_page('Import has been successfully finished') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def drop_database(self):
        self.login()
        self.set_test_name('pma_drop_database')
        print "[*] Starting drop database process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//a[contains(@href,"server_databases")]')
            self.click_element('//a[@title="Jump to database" and contains(text(), "test_db")]/preceding::input[1]')
            self.click_element('//*[@id="dbStatsForm"]/button/span')
            self.click_element('//div[@role="dialog"]//button[contains(text(), "OK")]')

            if self.wait_for_text_in_page('test_db') == None :
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
    pma = PhpMyAdminTests()
    pma.login()
    pma.create_database()
    pma.input_data_to_table()
    pma.run_query()
    pma.create_index()
    pma.browse_table()
    pma.backup_export()
    pma.adduser()
    pma.optimize_database()
    pma.check_status()
    pma.check_variables()
    pma.check_charsets()
    pma.check_engines()
    pma.import_sql()
    pma.drop_database()
