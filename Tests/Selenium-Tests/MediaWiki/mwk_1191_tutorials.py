#!/usr/bin/python

import time, os, errno, argparse, sys, random, string
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from datetime import datetime
from pyvirtualdisplay import Display

class MediaWikiTests:
    def __init__(self):
        self.main_page = 'http://localhost:8085/mediawiki-1.19.1/'
        print "[+] Setting up ChromeDriver"
        options = webdriver.chrome.options.Options()
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        self.add_cookies()
        self.new_username = ''
        self.logged_in = False
    def add_cookies(self):
        self.driver.get(self.main_page + 'docs/uidesign/monospace.html')
        self.driver.add_cookie({'name': 'test_group', 'value': 'mwk1191_tutorials'})
        self.driver.add_cookie({'name': 'test_name', 'value': 'mwk_loginmwk1191_tutorials'})
        self.driver.add_cookie({'name': 'software_id', 'value': '2'})
        self.driver.add_cookie({'name': 'software_version_id', 'value': '5'})
    def set_test_name(self, test_name):
        self.driver.delete_cookie('test_name')
        self.driver.add_cookie({'name': 'test_name', 'value': test_name})
    def click_element(self, xpath_selector):
        try:
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.click()
        except Exception as e:
            print '[-] Failed to click on element'
            print e
    def fill_textbox(self, xpath_selector, text):
        try:
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print '[-] Failed to fill textbox'
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
            time.sleep(3)
            timeout = timeout - 1
            if timeout == 0 :
                print "[-] Timed out %s" % xpath_selector
                return None
    def wait_for_text_in_page(self, text) :
        timeout = 20
        while not text in self.driver.page_source :
            print "[+] Waiting for text: %s to load in page" % text
            time.sleep(3)
            timeout = timeout - 1
            if timeout == 0 :
                print "[-] Timed out %s" % text
                return None
        return True
    def login(self, username=None, password=None):
        self.set_test_name('mwk_login')
        print "[+] Starting login process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            if self.logged_in:
                print '[+] Already logged in, skipping.'
                return
            # Click Login link
            normal_login = False
            try:
                if self.driver.find_element_by_xpath('//*[@id="pt-login"]/a').is_displayed():
                    normal_login = True
            except:
                pass
            if normal_login:
                self.click_element('//*[@id="pt-login"]/a')
            else:
                self.click_element('//*[@id="pt-anonlogin"]/a')
            # Enter Username
            self.fill_textbox('//*[@id="wpName1"]', 'babak' if username == None else username)
            # Enter password
            self.fill_textbox('//*[@id="wpPassword1"]', '1234' if password == None else password)
            # Click submit
            self.click_element('//*[@id="wpLoginAttempt"]')
            time.sleep(3)
            if self.wait_for_text_in_page('Babak' if username == None else username) == None :
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
            self.click_element('//*[@id="pt-logout"]/a')
            self.logged_in = False
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def change_skin(self):
        self.login()
        self.set_test_name('mwk_changeskin')
        print "[+] Starting change skin process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Navigate to preferences, change skin page
            self.click_element('//*[@id="pt-preferences"]/a')
            self.click_element('//*[@id="preftab-rendering"]')

            # Choose skin
            self.click_element('//*[@id="mw-input-wpskin-cologneblue"]')
            self.click_element('//*[@id="prefcontrol"]')

            self.wait_for_text_in_page('Your preferences have been saved.')

            # Revert theme
            # Navigate to preferences, change skin page
            # self.click_element('//*[@id="pt-preferences"]/a')
            self.click_element('//*[@id="preftab-rendering"]')

            # Choose skin
            self.click_element('//*[@id="mw-input-wpskin-vector"]')
            self.click_element('//*[@id="prefcontrol"]')

            if self.wait_for_text_in_page('Your preferences have been saved.') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def rename_page(self):
        self.login()
        self.set_test_name('mwk_renamepage')
        print "[+] Starting rename page process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="p-cactions"]')
            self.click_element('//*[@id="ca-move"]/a')

            self.fill_textbox('//*[@id="wpNewTitleMain"]', 'Main Page_' + ''.join(random.choice(string.digits) for _ in range(5)))
            #self.click_element('//*[@id="mw-movepage-table"]/tbody/tr[5]/td[2]/input')
            self.click_element('//input[@name="wpMove"]')

            if self.wait_for_text_in_page('Move succeeded') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def create_section(self):
        self.login()
        self.set_test_name('mwk_createsection')
        print "[+] Starting create section process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            self.click_element('//*[@id="ca-edit"]/span/a')
            self.fill_textbox('//*[@id="wpTextbox1"]', '''
==section==
===subsection===
====sub-subsection===

== Getting started ==
123
[[image:/mediawiki-1.19.1/resources/assets/wiki.png]]
[[Category: category_1]]
[[Category: category_2]]
[[Category: category_3]]''')
            self.click_element('//*[@id="wpSave"]')

            if self.wait_for_text_in_page('This page was last modified') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def create_account(self):
        self.logout()
        self.add_cookies()
        self.set_test_name('mwk_createaccount')
        print "[+] Starting rename page process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            normal_login = False
            try:
                if self.driver.find_element_by_xpath('//*[@id="pt-login"]/a').is_displayed():
                    normal_login = True
            except:
                pass
            if normal_login:
                self.click_element('//*[@id="pt-login"]/a')
            else:
                self.click_element('//*[@id="pt-anonlogin"]/a')
            self.click_element('//*[@id="userloginlink"]/a')
            self.new_username = 'user' + ''.join(random.choice(string.digits) for _ in range(5))
            self.fill_textbox('//*[@id="wpName2"]', self.new_username)
            self.fill_textbox('//*[@id="wpPassword2"]', '1234567890')
            self.fill_textbox('//*[@id="wpRetype"]', '1234567890')
            self.click_element('//*[@id="wpCreateaccount"]')
            self.wait_for_text_in_page('Your account has been created')

            self.click_element('//*[@id="pt-preferences"]/a')
            self.wait_for_text_in_page('Member of groups')

            self.click_element('//*[@id="preftab-rendering"]')
            self.wait_for_text_in_page('Date format')

            self.click_element('//*[@id="preftab-editing"]')
            self.wait_for_text_in_page('Edit area font style')

            self.click_element('//*[@id="preftab-rc"]')
            self.wait_for_text_in_page('Days to show in recent changes')

            self.click_element('//*[@id="preftab-watchlist"]')
            self.wait_for_text_in_page('Days to show in watchlist')

            if self.wait_for_text_in_page('Days to show in watchlist') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
            self.logout()
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def create_page(self):
        self.login()
        self.set_test_name('mwk_createpage')
        print "[+] Starting create page process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Search for non-existing page
            self.click_element('//*[@id="searchInput"]')
            self.fill_textbox('//*[@id="searchInput"]', 'SUNDAY' + ''.join(random.choice(string.digits) for _ in range(5)))
            self.click_element('//*[@id="searchGoButton"]')

            # Create new page
            self.click_element('//*[@id="mw-content-text"]/div/p[2]/b/a')
            self.fill_textbox('//*[@id="wpTextbox1"]', '''
== Welcome to my Sunday Page ==
\'\'\'Things I like to do on Sundays.\'\'\'
<UL>
<LI>I like to sleep.</LI>
<LI>I like to go walking.</LI>
<LI>I like to go bicycling.</LI>
<LI>I like to go shopping.</LI>
</UL>
----
\'\'My Favourite Days:\'\'
I don't like [[Mondays]].
But I like [[Fridays]].
My favourite list of movies is at
[http://www.imdb.com/chart/top. IMDb Database]''')
            self.click_element('//*[@id="wpSave"]')
            self.wait_for_text_in_page('SUNDAY')

            # Check page history
            self.click_element('//*[@id="ca-history"]/span/a')
            self.wait_for_text_in_page('Created page with')

            # Discussion
            self.click_element('//*[@id="ca-talk"]/span/a')
            self.fill_textbox('//*[@id="wpTextbox1"]', 'What do you think about this page? ~~~~')
            self.click_element('//*[@id="wpSave"]')
            self.wait_for_text_in_page('Talk:SUNDAY')
            self.wait_for_text_in_page('What do you think about this page?')

            # Page permissions
            # NA
            if self.wait_for_text_in_page('What do you think about this page?') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def change_navigation_menu(self):
        self.logout()
        self.login('Pragsec', '1234567890')
        self.set_test_name('mwk_changenavigation')
        print "[+] Starting modify navigation menu process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Search for non-existing page
            self.click_element('//*[@id="searchInput"]')
            self.fill_textbox('//*[@id="searchInput"]', 'MediaWiki:Sidebar')
            self.click_element('//*[@id="searchGoButton"]')

            # Edit navigation
            self.click_element('//*[@id="ca-edit"]/span/a')
            self.fill_textbox('//*[@id="wpTextbox1"]', '''
* navigation
** mainpage|mainpage-description
** recentchanges-url|recentchanges
** randompage-url|randompage
** helppage|help
* SEARCH
* TOOLBOX
* LANGUAGES
* Nav Item
** Nav sub Item
** Saturday|Saturday''')
            self.click_element('//*[@id="wpSave"]')

            if self.wait_for_text_in_page('Nav Item') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def change_useraccount(self):
        self.login()
        self.set_test_name('mwk_changeuseraccount')
        print "[+] Starting change user account process..."
        self.driver.get(self.main_page)
        # Fill form fields
        try :
            # Change password
            self.click_element('//*[@id="pt-preferences"]/a')
            self.fill_textbox('//*[@id="mw-htmlform-info"]/tbody/tr[7]/td[2]/a')
            self.fill_textbox('//*[@id="mw-input-wpPassword"]', '1234')
            self.fill_textbox('//*[@id="mw-input-wpNewPassword"]', '12345')
            self.fill_textbox('//*[@id="mw-input-wpRetype"]', '12345')
            self.click_element('//*[@id="mw-resetpass-form"]/fieldset/span/input[1]')
            self.wait_for_text_in_page('Nav Item')

            # Log in with new password
            self.click_element('//*[@id="pt-logout"]/a')
            self.login(self.new_username, '12345')

            if self.wait_for_text_in_page('Nav Item') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'
        except (NoSuchElementException, ElementNotVisibleException) as ex :
            print "[-] Elements not found on page"
            print str(ex)
        except Exception as ex :
            print "[-] Unhandled error"
            print str(ex)
    def change_import_export(self):
        self.logout()
        self.login('Pragsec', '1234567890')
        self.set_test_name('mwk_importexport')
        print "[+] Starting import export page process..."
        self.driver.get(self.main_page + 'index.php/Special:Export')
        # Fill form fields
        try :
            self.fill_textbox('//*[@id="catname"]', 'Category_1')
            self.click_element('//*[@id="mw-content-text"]/form/input[2]')
            self.click_element('//*[@id="mw-content-text"]/form/input[6]')

            if self.wait_for_text_in_page('Export pages') == None :
                 print '[-] Test failed'
            else :
                print '[+] Test successful'

            self.driver.get(self.main_page + 'index.php/Special:Import')
            file_path = os.path.dirname(os.path.realpath(__file__)).split('/')[:-3]
            file_path = '/'.join(file_path)
            self.fill_textbox('//*[@name="xmlimport"]', file_path + '/Tests/Selenium-Tests/MediaWiki/mwk1191-20190202134027.xml')
            self.click_element('//td[@class="mw-submit"]//input')

            if self.wait_for_text_in_page('Import finished!') == None :
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
    mwt = MediaWikiTests()
    mwt.login()
    mwt.change_skin()
    mwt.rename_page()
    mwt.create_section()
    mwt.create_account()
    mwt.create_page()
    mwt.change_navigation_menu()
    mwt.change_import_export()
