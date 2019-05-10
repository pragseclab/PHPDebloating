import time, os, errno, argparse, sys, random, string
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class WPTest(object):
    def __init__(self, main_page):
        self.main_page = main_page
        print("[+] Setting up ChromeDriver")
        options = webdriver.chrome.options.Options()
        options.add_argument("--start-maximized");
        self.driver = webdriver.Chrome(chrome_options=options)
        # try:
        #     self.driver.maximize_window()
        # except WebDriverException as e:
        #     # Change dimension of screen to actual resolution
        #     pass
        self.driver.set_page_load_timeout(60)
        self.success = True

    # A virtual method provided by parent, children should override it
    def add_cookies(self):
        pass

    def set_test_name(self, test_name):
        self.driver.delete_cookie('test_name')
        self.driver.add_cookie({'name': 'test_name', 'value': test_name})

    def get_by_relative_url(self, url):
        self.driver.get(self.url_with_base(url))

    def click_element(self, xpath_selector):
        if not self.success:
            return
        try:
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.click()
        except Exception as e:
            self.success = False
            print('[-] Failed to click on element')
            print(e)

    def fill_textbox(self, xpath_selector, text):
        if not self.success:
            return
        try:
            self.wait_for_element_become_visible(xpath_selector)
            time.sleep(1)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.success = False
            print('[-] Failed to fill textbox')
            print(e)

    def select_dropdown(self, xpath_selector, text):
        if not self.success:
            return None
        try:
            self.wait_for_element_become_visible(xpath_selector)
            element = self.driver.find_element(By.XPATH, xpath_selector)
            Select(element).select_by_visible_text(text)
            return Select(element).all_selected_options[0].get_attribute('value')
        except Exception as e:
            self.success = False
            print('[-] Failed to select option')
            print(e)
            return None

    def checkbox_is_checked(self, xpath_selector):
        if not self.success:
            return
        ele = None
        try:
            self.wait_for_element_become_visible(xpath_selector)
            ele = self.driver.find_element_by_xpath(xpath_selector)
        except NoSuchElementException:
            print('[-] Element of %s is not found' % xpath_selector)
            self.success = False
            return None
        except Exception as e:
            self.success = False
            print('[-] Failed to check the state of checkbox')
            print(e)

        state = ele.get_attribute('checked')
        return False if state is None or state.lower() == 'false' else True

    def upload_file_input(self, xpath_selector, file_path):
        try:
            ele = self.driver.find_element_by_xpath(xpath_selector)
            if ele.tag_name != "input" or ele.get_attribute("type") != "file":
                self.success = False
                print('[-] Must use <input type="file"> for uploading')
                return
            self.driver.find_element_by_xpath(xpath_selector).send_keys(file_path)
        except Exception as e:
            self.success = False
            print('[-] Failed to Upload file')
            print(e)

    def check_exists_and_visible_by_xpath(self, xpath_selector):
        if not self.success:
            return False
        try:
            return self.driver.find_element_by_xpath(xpath_selector).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def to_page_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def wait_for_element_become_visible(self, xpath_selector, timeout=20):
        if not self.success:
            return None
        # timeout = 20
        while not self.check_exists_and_visible_by_xpath(xpath_selector):
            print("[+] Waiting for %s to become visible" % xpath_selector)
            # Wait for login pop up to load via ajax
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0:
                self.success = False
                print("[-] Timed out %s" % xpath_selector)
                return False
        return True

    def wait_for_text_in_page(self, text, timeout=20):
        if not self.success:
            return None
        # timeout = 20
        while not text in self.driver.page_source:
            print("[+] Waiting for text: %s to load in page" % text)
            time.sleep(1)
            timeout = timeout - 1
            if timeout == 0:
                self.success = False
                print("[-] Timed out %s" % text)
                return False
        return True

    # This method would provide common login method and write related cookies
    # If detailed login test needed, override it in subclass
    def login(self, username=None, password=None, is_remember=False, success_login_text='Log Out'):
        self.set_test_name('wp_login')
        print("[*] Starting login process...")
        self.driver.get(self.url_with_base('wp-login.php'))
        # Fill form fields
        try:
            if self.driver.get_cookie('wp_login') == 'success':
                print('[+] Already logged_in, skipped')
                return

            self.fill_textbox('//*[@id="user_login"]', 'wpuser' if username is None else username)
            # Enter password
            self.fill_textbox('//*[@id="user_pass"]', 'password' if password is None else password)
            # Click remember me
            if is_remember:
                self.click_element('//*[@id="rememberme"]')
            # Click submit
            self.click_element('//*[@id="wp-submit"]')
            time.sleep(3)
            if "login_error" in self.driver.page_source:
                self.success = False
                print('[-] Login failed')
            elif self.wait_for_text_in_page(success_login_text) is None:
                self.success = False
                print('[-] Login failed')
            else:
                # self.logged_in = True
                self.driver.add_cookie({'name': 'wp_login', 'value': 'success'})
                print('[+] Login successful')
        except (NoSuchElementException, ElementNotVisibleException) as ex:
            self.success = False
            print("[-] Elements not found on page")
            print(str(ex))
        except Exception as ex:
            self.success = False
            print("[-] Unhandled error")
            print(str(ex))

    # Concat URL main_page and additional path with '/'
    def url_with_base(self, path):
        if self.main_page.endswith('/'):
            self.main_page = self.main_page[:-1]
        if path.startswith('/'):
            path = path[1:]
        return self.main_page + '/' + path

    def close(self, close_on_suc=False, delay=0):
        if close_on_suc and not self.success:
            pass
        else:
            print('[+] Window will be closed after', delay, 'seconds')
            time.sleep(delay)
            print('[+] Window closed')
            self.driver.close()

    def close_all(self, delay=0):
        handles = self.driver.window_handles
        print('[*] Find %d window(s), these will be closed after %d seconds...'
              % (len(handles), delay))
        time.sleep(delay)
        for window in handles:
            self.driver.switch_to_window(window)
            print('[+] Find window with title:', self.driver.title)
            print('[+] Window closed')
            self.driver.close()

    def get_random_text(self, char_type=3, length=6):
        char_list = ''
        if char_type & 0x111 == 0:
            char_type = 3
        char_list += string.ascii_uppercase if char_type & 0x1 == 1 else ''
        char_list += string.digits if char_type & 0x2 == 1 else ''
        char_list += string.ascii_lowercase if char_type & 0x4 == 1 else ''
        return ''.join(random.choice(char_list) for _ in range(length))
