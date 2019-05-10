# -*- coding: utf-8 -*-

import os
import random
import string
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from wptest import WPTest

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class WPTest471(WPTest):
    def __init__(self):
        # UPDATE HERE (1/5)
        self.main_page = 'http://localhost:8085/WordPress-4.7.1/'
        #super().__init__(self.main_page)
        super(WPTest471, self).__init__(self.main_page)
        self.driver.get(self.main_page)
        self.driver.delete_all_cookies()
        self.add_cookies()

    # Override parent's method
    def add_cookies(self):
        self.driver.get(self.main_page)
        # UPDATE HERE (2/5)
        self.driver.add_cookie({'name': 'test_group', 'value': 'wp471_tutorials'})
        # UPDATE HERE (3/5)
        self.driver.add_cookie({'name': 'test_name', 'value': 'wp_login_wp471_tutorials'})
        # UPDATE HERE (4/5)
        self.driver.add_cookie({'name': 'software_id', 'value': '4'})
        # UPDATE HERE (5/5)
        self.driver.add_cookie({'name': 'software_version_id', 'value': '20'})

    def init_new_post(self):
        print('[*] Starting new post test...')
        self.get_by_relative_url('wp-admin/post-new.php')
        # Must logged in to post new article
        assert self.driver.get_cookie('wp_login') != 'success', '[-] Cannot initialize new post page: login failed'
        self.click_element('//*[@id="show-settings-link"]')
        time.sleep(2)

        if not self.checkbox_is_checked('//*[@id="postexcerpt-hide"]'):
            self.click_element('//*[@id="postexcerpt-hide"]')
        if not self.checkbox_is_checked('//*[@id="trackbacksdiv-hide"]'):
            self.click_element('//*[@id="trackbacksdiv-hide"]')
        if not self.checkbox_is_checked('//*[@id="postcustom-hide"]'):
            self.click_element('//*[@id="postcustom-hide"]')
        if not self.checkbox_is_checked('//*[@id="commentstatusdiv-hide"]'):
            self.click_element('//*[@id="commentstatusdiv-hide"]')
        if not self.checkbox_is_checked('//*[@id="slugdiv-hide"]'):
            self.click_element('//*[@id="slugdiv-hide"]')
        if not self.checkbox_is_checked('//*[@id="authordiv-hide"]'):
            self.click_element('//*[@id="authordiv-hide"]')

        self.click_element('//*[@id="show-settings-link"]')
        time.sleep(2)
        if self.success:
            self.driver.add_cookie({'name': 'wp_new_post_init', 'value': 'success'})
            print('[+] Test initialization finished')

    def add_title_text(self, text):
        print('[+] Adding title...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.fill_textbox('//*[@id="title"]', text)

    def add_body_text(self, text):
        print('[+] Adding body...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.click_element('//*[@id="content-html"]')
        self.fill_textbox('//*[@id="content"]', text)

    def preview_post(self):
        print('[+] Preview post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.click_element('//*[@id="post-preview"]')

    def save_post(self):
        print('[+] Saving post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        if self.driver.find_element_by_xpath('//*[@id="save-post"]').is_displayed():
            self.click_element('//*[@id="save-post"]')
            print('[+] Saving post finished')
        else:
            print('[!] No need to save post')

    def publish_post(self):
        print('[+] Publishing post...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        self.click_element('//*[@id="publish"]')
        if self.wait_for_text_in_page('Post published.') is None:
            print('[-] Publishing failed')

    def select_category(self, idx):
        print('[+] Select category...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        categories = self.driver.find_elements_by_xpath('//*[@id="categorychecklist"]/li')
        if 1 <= idx <= len(categories):
            self.click_element('//*[@id="in-category-' + str(idx) + '"]')
        else:
            print('[!] Invalid category index, using 1 instead')
            self.click_element('//*[@id="in-category-1"]')

    def add_excerpt(self, text):
        print('[+] Adding excerpt...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        # styles = StyleParser(self.driver.find_element_by_xpath('//*[@id="postexcerpt"]').get_attribute('style'))
        # # print(styles)
        # if styles.get_style_value('display') != 'none' or styles.get_style_value('display') is None:
        if self.driver.find_element_by_xpath('//*[@id="postexcerpt"]').is_displayed():
            self.fill_textbox('//*[@id="excerpt"]', text)
        else:
            print('[-] Cannot find excerpt textarea')

    # status_text should be one of Published, Draft(default) or Pending Review
    def change_status(self, status_text='Published'):
        print('[+] Changing status')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        # If article is private, we cannot change its status
        if self.driver.find_element_by_xpath('//*[@id="post-status-display"]').text == 'Privately Published':
            print('[!] Cannot set status since this article is private')
            return
        self.click_element('//*[@id="misc-publishing-actions"]/div[1]/a')
        # styles = StyleParser(self.driver.find_element_by_xpath('//*[@id="post-status-select"]')
        #                     .get_attribute('style'))
        # if styles.get_style_value('display') == 'none':
        time.sleep(1)
        self.select_dropdown('//*[@id="post_status"]', status_text)
        self.click_element('//*[@id="post-status-select"]/a[1]')
        if self.wait_for_text_in_page(status_text) is None:
            self.success = False
            print('[-] Changing status failed')

    # Change visibility of article
    def change_visibility(self, visibility="public", password=None):
        print('[+] Changing visibility')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()
        time.sleep(1)
        self.click_element('//*[@id="visibility"]/a')
        if visibility == 'public':
            self.click_element('//*[@id="visibility-radio-public"]')
        elif visibility == 'public_sticky':
            self.click_element('//*[@id="visibility-radio-public"]')
            if not self.checkbox_is_checked('//*[@id="sticky"]'):
                self.click_element('//*[@id="sticky"]')
        elif visibility == 'protected':
            self.click_element('//*[@id="visibility-radio-password"]')
            if password is None:
                self.success = False
                print('[-] Password needed')
            elif len(password) > 20:
                print('[-] Password too long')
            else:
                self.fill_textbox('//*[@id="post_password"]', password)
        elif visibility == 'private':
            self.click_element('//*[@id="visibility-radio-private"]')
        else:
            self.success = False
            print('[-] Invalid visibility level. It should be one of public, public_sticky, protected and private.')
            return

        self.click_element('//*[@id="post-visibility-select"]/p/a[1]')

        updated_state = self.driver.find_element_by_xpath('//*[@id="post-visibility-display"]').text

        if (visibility == 'public' and updated_state == 'Public') or \
                (visibility == 'public_sticky' and updated_state == 'Public, Sticky') or \
                (visibility == 'protected' and updated_state == 'Password Protected') or \
                (visibility == 'private' and updated_state == 'Private'):
            print('[+] Changing visibility successfully')
        else:
            self.success = False
            print('[-] Failed to change visibility, current visibility does not match')

        time.sleep(1)

    def change_publish_datetime(self, year=None, month=None, day=None, hour=None, minute=None):
        print('[+] Changing publishing datetime')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        trans_mon_str = ['', '01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-May', '06-Jun', '07-Jul', '08-Aug', '09-Sep',
                         '10-Oct', '11-Nov', '12-Dec']
        self.click_element('//*[@id="misc-publishing-actions"]/div[3]/a')

        if year is not None:
            self.fill_textbox('//*[@id="aa"]', str(year))
        if month is not None:
            self.select_dropdown('//*[@id="mm"]', trans_mon_str[month])
        if day is not None:
            self.fill_textbox('//*[@id="jj"]', str(day))
        if hour is not None:
            self.fill_textbox('//*[@id="hh"]', str(hour))
        if minute is not None:
            self.fill_textbox('//*[@id="mn"]', str(minute))

        self.click_element('//*[@id="timestampdiv"]/p/a[1]')

        # Check datetime in format like Nov 15, 2018 @ 20:19
        publishing_datetime = '%s %d, %d @ %02d:%02d' % (trans_mon_str[month][3:], day, year, hour, minute)
        if publishing_datetime == self.driver.find_element_by_xpath('//*[@id="timestamp"]/b').text:
            print('[+] Changing publishing datetime successfully')
        else:
            self.success = False
            print('[-] Current publishing datetime does not match')

    def add_tags(self, tag_list):
        print('[+] Adding tags')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        if len(tag_list) == 0:
            print('[!] No tag provided')
            return
        tag_str = ''
        for tag in tag_list:
            tag_str += tag + ','
        tag_str = tag_str[:-1]

        self.fill_textbox('//*[@id="new-tag-post_tag"]', tag_str)
        self.click_element('//*[@id="new-tag-post_tag"]/../input[2]')

        ele = self.driver.find_elements_by_xpath('//*[@id="post_tag"]/div[2]/span')
        updated_tag_list = []
        for e in ele:
            updated_tag_list.append(e.text[e.text.rfind(' ') + 1:])
        for tag in tag_list:
            if tag not in updated_tag_list:
                self.success = False
                print('[-] Adding tag %s failed' % tag)
                return
        print('[+] Adding tag finished')

    def set_feature_image_by_uploading(self, image_path):
        print('[+] Selecting feature image...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        self.click_element('//*[@id="set-post-thumbnail"]')

        self.click_element('//*[@id="__wp-uploader-id-0"]/div[3]/div/a[1]')

        self.upload_file_input('//*[@id="__wp-uploader-id-0"]/div[@class="moxie-shim moxie-shim-html5"]/input',
                               image_path)

        if self.wait_for_text_in_page("Edit Image"):
            time.sleep(3)
            self.click_element(
                '//*[@id="__wp-uploader-id-0"]/div[5]/div/div[2]/button')  # Can be improved by class name
            if self.wait_for_text_in_page('Remove featured image'):
                print('[+] Setting feature image finished')
            else:
                self.success = False
                print('[-] Failed to set uploaded image')
        else:
            self.success = False
            print('[-] Failed to set uploaded image')

    def set_traceback(self, link):
        print('[+] Setting traceback link')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        if self.driver.find_element_by_xpath('//*[@id="trackback_url"]').is_displayed():
            self.fill_textbox('//*[@id="trackback_url"]', link)
            print('[+] Setting traceback link finished')
        else:
            self.success = False
            print('[-] Traceback textbox not found')

    def add_custom_fields(self, fields):
        print('[*] Adding custom fields...')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        for name in fields.key():
            value = fields[name]
            if self.driver.find_element_by_xpath('//*[@id="newmetaleft"]/a').is_displayed():
                # There exists a field, click "Enter new" first
                self.click_element('//*[@id="newmetaleft"]/a')

            # Fill in field
            self.fill_textbox('//*[@id="metakeyinput"]', name)
            self.fill_textbox('//*[@id="metavalue"]', value)
            self.click_element('//*[@id="newmeta-submit"]')

        if self.success:
            print('[+] Adding custom fields finished')
        else:
            print('[+] Failed to addi custom fields')

    def change_slug(self, name):
        print('[+] Changing slug')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        self.fill_textbox('//*[@id="post_name"]', name)
        print('[+] Changing slug finished')

    def change_discussion_state(self, comments=False, ping_status=False):
        print('[+] Changing discussion state')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        current_comment_state = self.checkbox_is_checked('//*[@id="comment_status"]')
        if current_comment_state != comments:
            self.click_element('//*[@id="comment_status"]')
        current_ping_status = self.checkbox_is_checked('//*[@id="ping_status"]')
        if current_ping_status != ping_status:
            self.click_element('//*[@id="ping_status"]')
        if self.success:
            print('[+] Changing discussion state finished')
        else:
            print('[-] Failed to change discussion state')

    # format_name should be one of the standard, aside, image, video, audio, quote, link, gallery
    def change_format(self, format_name='standard'):
        print('[+] Changing format')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        format_name = format_name.lower()
        if format_name not in ['standard', 'aside', 'image', 'video', 'audio', 'quote', 'link', 'gallery']:
            print('[!] Invalid format name %s, using standard instead' % format_name)
        self.click_element('//*[@id="post-format-' + format_name + '"]')
        if self.success:
            print('[+] Changing format finished')
        else:
            print('[-] Failed to change format')

    def move_to_trash_post_page(self):
        print('[+] Moving post to trash')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        self.click_element('//*[@id="delete-action"]/a')
        if self.wait_for_text_in_page('1 post moved to the Trash.'):
            print('[+] Moving post to trash finished')
        else:
            self.success = False
            print('[-] Failed to move post to trash')

    def change_permalink(self, new_name):
        print('[+] Moving post to trash')
        assert self.driver.current_url.rfind('post-new.php'), '[-] Not in /admin/post-new.php page'
        assert self.driver.get_cookie('wp_new_post_init') != 'success', '[-] init_new_post() not finished yet'
        self.to_page_top()

        if not self.driver.find_element_by_xpath('//*[@id="edit-slug-buttons"]/button').is_displayed():
            self.success = False
            print('[-] Failed to change permalink, please set title first')
            return

        self.click_element('//*[@id="edit-slug-buttons"]/button')

        self.fill_textbox('//*[@id="new-post-slug"]', new_name)

        self.click_element('//*[@id="edit-slug-buttons"]/button[1]')

        if self.success:
            print('[+] Changing permalink finished')
        else:
            print('[-] Failed to change permalink')

    def new_post_tests(self):
        self.init_new_post() if self.success else None
        # self.select_category(1) if self.success else None
        self.add_title_text('Test title') if self.success else None
        self.add_body_text(
            '<h2>This is a test article.</h2>\n<p>This is a paragraph. 12345\n%s</p>' % self.get_random_text(3, 10)) \
            if self.success else None
        self.save_post() if self.success else None if self.success else None
        self.add_excerpt('This is a test') if self.success else None
        self.change_status('Pending Review') if self.success else None
        self.change_visibility('private') if self.success else None
        self.change_publish_datetime(2017, 8, 9, 1, 2) if self.success else None
        self.add_tags(['test', 'example']) if self.success else None
        self.set_feature_image_by_uploading(os.path.abspath('./leaf.png')) if self.success else None
        self.set_traceback('http://localhost/wordpress3_9/?p=1') if self.success else None
        self.change_format('image') if self.success else None
        self.change_slug('another-title') if self.success else None
        self.change_discussion_state(comments=True, ping_status=False) if self.success else None
        #self.change_permalink('permalink-'+self.get_random_text(2, 2)) if self.success else None
        self.preview_post() if self.success else None
        self.publish_post() if self.success else None
        self.move_to_trash_post_page() if self.success else None
        if self.success:
            print('[+] New post tests finished\n----------\n')

    def init_theme_tests(self):
        print('[*] Starting theme tests...')
        self.get_by_relative_url('wp-admin/themes.php')
        # Must logged in to post new article
        assert self.driver.get_cookie('wp_login') != 'success', \
            '[-] Cannot initialize theme page: login failed'
        if self.success:
            self.driver.add_cookie({'name': 'wp_theme_init', 'value': 'success'})
            print('[+] Test initialization finished')

    def upload_theme(self, theme_path):
        print('[+] Uploading theme')
        self.get_by_relative_url('wp-admin/theme-install.php')
        if not self.wait_for_text_in_page('Upload Theme'):
            self.success = False
            print('[-] Cannot open theme installation page')
            return

        self.click_element('//*[@id="wpbody-content"]/div[@class="wrap"]/h1/button')

        self.upload_file_input('//*[@name="themezip"]', theme_path)

        timeout = 10
        while self.driver.find_element_by_xpath('//*[@id="install-theme-submit"]').get_attribute('disabled'):
            if timeout <= 0:
                self.success = False
                print('[-] Failed to specify file to be upload')
                return
            timeout -= 1
            time.sleep(1)

        self.click_element('//*[@id="install-theme-submit"]')

        if self.wait_for_text_in_page('Theme installed successfully.'):
            print('[+] Uploading theme finished')
        else:
            self.success = False
            print('[-] Failed to upload theme, provided information:\n %s'
                  % self.driver.find_element_by_xpath('//*[@id="wpbody-content"]/div[3]'))

    def activate_theme(self, theme_name):
        print('[+] Activating theme %s' % theme_name)
        self.get_by_relative_url('wp-admin/themes.php')
        ele = self.driver.find_element_by_xpath('//*[@aria-describedby="%s-action %s-name"]' % (theme_name, theme_name))
        if ele is None:
            self.success = False
            print('[-] Theme with name %s not found' % theme_name)
            return

        try:
            ele.find_element_by_xpath('//*[@aria-describedby="%s-action %s-name"]//a[@class="button activate"]'
                                      % (theme_name, theme_name))
        except Exception as e:
            print('[!] It seems the theme has been activated')
            return

        ele.find_element_by_xpath('//*[@aria-describedby="%s-action %s-name"]//a[@class="button activate"]'
                                      % (theme_name, theme_name)).click()

        if self.wait_for_text_in_page('New theme activated'):
            print('[+] Activating theme finished')
        else:
            self.success = False
            print('[-] Failed to activate theme')

    def change_background_color_theme_twentyten(self, color_code):
        print('[+] Changing background color')
        self.get_by_relative_url('wp-admin/customize.php')

        if not self.wait_for_text_in_page('You are customizing'):
            self.success = False
            print('[-] Failed to load customization page')
            return

        self.click_element('//*[@id="accordion-section-colors"]')

        if not self.wait_for_text_in_page('Background Color'):
            self.success = False
            print('[-] Failed to show control panel of color')
            return

        # self.driver.save_screenshot('1.png')
        time.sleep(2)

        ele = self.driver.find_element_by_xpath(
            '//*[@id="customize-control-background_color"]/label/div/div/a')
        # //*[@id="customize-control-background_color"]/label/div/div/span/input[1]
        # //*[@id="customize-control-background_color"]/label/div/div/a
        # //*[@id="customize-control-background_color"]/*/[@title="Select Color"]

        if ele is None:
            self.success = False
            print('[-] Failed to find color picker')
            return

        ele.click()

        timeout = 10
        while 'wp-picker-open' not in ele.get_attribute('class'):
            if timeout <= 0:
                self.success = False
                print('[-] Failed to load color picker')
                return
            timeout -= 1

        self.fill_textbox('//*[@id="customize-control-background_color"]/label/div/div/span/input[1]',
                          color_code)

        time.sleep(1)

        if 'iris-error' in self.driver.find_element_by_xpath(
                '//*[@id="customize-control-background_color"]/label/div/div/span/input[1]').get_attribute('class'):
            self.success = False
            print('[-] Invalid color code format')
            return

        self.click_element('//*[@id="save"]')

        timeout = 10
        while self.driver.find_element_by_xpath('//*[@id="save"]').get_attribute('value') != 'Saved':
            if timeout < 0:
                self.success = False
                print('[-] Failed to save changes')
                return
            time.sleep(1)
            timeout -= 1

        print('[+] Changing background color finished')

    def delete_theme(self, theme_name):
        print('[+] Deleting theme')
        self.get_by_relative_url('wp-admin/themes.php')

        try:
            self.driver.find_element_by_xpath('//*[@aria-describedby="%s-action %s-name"]' % (theme_name, theme_name))
        except Exception as e:
            print('[!] Theme of %s not found' % theme_name)
            return
        else:
            self.click_element(
                '//*[@aria-describedby="%s-action %s-name"]' % (theme_name, theme_name))

        # self.driver.save_screenshot('1.png')

        try:
            self.wait_for_element_become_visible('//div[@class="theme-backdrop"]')
        except NoSuchElementException:
            self.success = False
            print('[-] Failed to open theme popup')
            return
        else:
            self.driver.execute_script("window.onbeforeunload = function() {};")
            self.click_element('//div[@class="theme-overlay"]//div[@class="theme-actions"]/a')
            time.sleep(1)

            # Handle confirmation popup
            alert_popup = self.driver.switch_to.alert
            alert_popup.accept()
            time.sleep(1)

        if self.success:
            print('[+] Theme deleted')
        else:
            print('[-] Failed to delete theme')

    def theme_tests(self):
        print('[*] Starting theme tests...')
        self.init_theme_tests() if self.success else None
        self.activate_theme('twentyseventeen') if self.success else None
        self.delete_theme('twentyten') if self.success else None
        self.upload_theme(os.path.abspath('./twentyten.2.5.zip')) if self.success else None
        self.activate_theme('twentyten') if self.success else None

        def get_random_color(r, g, b):
            return "#%02x%02x%02x" % (r, g, b)

        self.change_background_color_theme_twentyten(
            get_random_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) \
            if self.success else None

        if self.success:
            print('[+] Theme tests finished\n----------\n')

    def change_site_title(self, title):
        print('[+} Changing site title')
        self.get_by_relative_url('wp-admin/options-general.php')
        self.fill_textbox('//*[@id="blogname"]', title)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Site title changed')
        else:
            self.success = False
            print('[-] Failed to change site title')

    def change_default_post_format(self, new_format='Standard'):
        print('[+] Changing default post format')
        self.get_by_relative_url('wp-admin/options-writing.php')
        self.select_dropdown('//*[@id="default_post_format"]', new_format)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Default post format changed')
        else:
            self.success = False
            print('[-] Failed to change default post format')

    def change_posts_per_page(self, count):
        print('[+] Changing posts per page')
        self.get_by_relative_url('wp-admin/options-reading.php')
        self.fill_textbox('//*[@id="posts_per_page"]', count)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Posts per page changed')
        else:
            self.success = False
            print('[-] Failed to change posts per page')

    # Level is an integer from 2 to 10
    def change_nested_comment_level(self, level):
        print('[+] Changing nested comment level')
        self.get_by_relative_url('wp-admin/options-discussion.php')
        if not self.checkbox_is_checked('//*[@id="thread_comments"]'):
            self.click_element('//*[@id="thread_comments"]')
        if not 2 <= level <= 10 or type(level) != int:
            self.success = False
            print('[-] Level should be an integer from 2 to 10')
            return

        self.select_dropdown('//*[@id="thread_comments_depth"]', str(level))
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Nested comment level changed')
        else:
            self.success = False
            print('[-] Failed to change nested comment level')

    def change_media_medium_size(self, max_width, max_height):
        print('[+] Changing media medium size')
        self.get_by_relative_url('wp-admin/options-media.php')
        self.fill_textbox('//*[@id="medium_size_w"]', max_width)
        self.fill_textbox('//*[@id="medium_size_h"]', max_height)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Settings saved.'):
            print('[+] Nested comment level changed')
        else:
            self.success = False
            print('[-] Failed to change nested comment level')

    def change_permalink_category_base(self, base):
        print('[+] Changing permalink category base')
        self.get_by_relative_url('wp-admin/options-permalink.php')
        self.fill_textbox('//*[@id="category_base"]', base)
        self.click_element('//*[@id="submit"]')
        if self.wait_for_text_in_page('Permalink structure updated.'):
            print('[+] Category base of permalink changed')
        else:
            self.success = False
            print('[-] Failed to change category base of permalink')

    def setting_tests(self):
        print('[*] Starting setting tests...')
        assert self.driver.get_cookie('wp_login') != 'success', '[-] Cannot initialize setting page: login failed'

        self.change_site_title('wp3_9_test') if self.success else None
        self.change_default_post_format('Image') if self.success else None
        self.change_posts_per_page(random.randint(10, 15)) if self.success else None
        self.change_nested_comment_level(random.randint(4, 8)) if self.success else None
        self.change_media_medium_size(random.randint(300, 500), random.randint(300, 500)) if self.success else None
        self.change_permalink_category_base('category') if self.success else None
        if self.success:
            print('[+] Setting tests finished\n----------\n')

    # Category & Tag tests

    def add_category(self, name, slug, description, parent="None", is_tag=False):
        print('[+] Adding category/tag')
        if not is_tag:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=category')
        else:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=post_tag')

        self.fill_textbox('//*[@id="tag-name"]', name)
        self.fill_textbox('//*[@id="tag-slug"]', slug)
        parent_id = (self.select_dropdown('//*[@id="parent"]', str(parent)) if not is_tag else None)
        self.fill_textbox('//*[@id="tag-description"]', description)
        self.click_element('//*[@id="submit"]')

        time.sleep(2)
        if 'A term with the name and slug provided already exists.' in self.driver.page_source:
            self.success = False
            print('[-] Cannot create category/tag since a term with the name and slug provided already exists')
            return None
        else:
            print('[+] Category/Tag added')
            category_list = self.driver.find_elements_by_xpath('//*[@id="the-list"]//div[@class="hidden"]')
            # print(name, slug, parent_id, is_tag)
            for c in category_list:
                self.driver.execute_script(
                    'document.getElementById("%s").style.display = "block";' % c.get_attribute("id"))

                cname = c.find_element_by_css_selector('.name').text
                cslug = c.find_element_by_css_selector('.slug').text
                cparent = c.find_element_by_css_selector('.parent').text
                # print(cname, cslug, cparent, cname.lower() == name.lower(), cslug.lower() == slug.lower(),
                #       (is_tag or (not is_tag and parent_id == cparent)))
                if cname.lower() == name.lower() and \
                        cslug.lower() == slug.lower() and \
                        (is_tag or (not is_tag and parent_id == cparent)):
                    cid = c.get_attribute('id')
                    return int(cid[7:])
            return None

    def quick_edit_category(self, id, new_name, new_slug, is_tag=False):
        print('[+] Quick Editing category/tag')
        if not is_tag:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=category')
        else:
            self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=post_tag')

        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="tag-%d"]/td[1]' % id))
        hover.perform()

        self.click_element('//*[@id="tag-%d"]/td[1]/div[@class="row-actions"]/span[2]/a' % id)
        self.fill_textbox('//*[@class="input-text-wrap"]/input[@name="name"]', new_name)
        self.fill_textbox('//*[@class="input-text-wrap"]/input[@name="slug"]', new_slug)
        self.click_element('//*[@class="inline-edit-save submit"]/button[2]')
        error = self.driver.find_element_by_xpath('//*[@class="inline-edit-save submit"]/span[@class="error"]')
        if error.is_displayed():
            self.success = False
            print('[-] Failed to update category/tag: %s' % error.text)
        else:
            print('[+] Category/Tag updated')

    def get_category_name(self, id=None, isRandom=True):
        print('[+] Getting category name')
        self.get_by_relative_url('wp-admin/edit-tags.php?taxonomy=category')
        if id is None:
            isRandom = True
        if id is not None and type(id) == int:
            cid = self.driver.find_element_by_xpath('//*[@id="tag-%d"]/td[1]/strong/a' % id).text
            return cid.replace('— ', u'\u00a0\u00a0\u00a0')
        elif id is None and isRandom:
            cid_list = self.driver.find_elements_by_xpath('//*[@id="the-list"]/tr')
            idx = random.randint(0, len(cid_list))
            if idx == len(cid_list):
                return None
            else:
                cid = cid_list[idx].find_element_by_xpath('//td[1]/strong/a').text
                return cid.replace('— ', u'\u00a0\u00a0\u00a0')
        else:
            self.success = False
            print('[-] Failed to get category name')
            return None

    def category_tag_tests(self):
        print('[*] Starting category/tag tests')
        parent_name = self.get_category_name(isRandom=True)

        category_id = self.add_category('test_name' + self.get_random_text(2, 2),
                                        'test-slug' + self.get_random_text(2, 2),
                                        'This is a test category', parent=parent_name, is_tag=False)
        tag_id = self.add_category('test_tag' + self.get_random_text(2, 2),
                                   'test-tag-slug' + self.get_random_text(2, 2),
                                   'This is a test tag', is_tag=True)

        self.quick_edit_category(id=category_id, new_name='new_name' + self.get_random_text(2, 2),
                                 new_slug='new-slug' + self.get_random_text(2, 2), is_tag=False) \
            if category_id is not None else None

        self.quick_edit_category(id=tag_id, new_name='new_name' + self.get_random_text(2, 2),
                                 new_slug='new-slug' + self.get_random_text(2, 2), is_tag=True) \
            if tag_id is not None else None

        if self.success:
            print('[+] Category/Tag tests finished\n----------\n')

    def post_new_comment(self, relative_article_url, author, email, website, comment_text):
        print('[+] Posting new comment to article')
        self.get_by_relative_url(relative_article_url)
        comment_id = None
        if self.wait_for_text_in_page('Leave a Reply'):
            if self.wait_for_text_in_page('Logged in as'):
                # Have already logged in as one user
                self.fill_textbox('//*[@id="comment"]', comment_text)
                self.click_element('//*[@id="submit"]')
            else:
                self.fill_textbox('//*[@id="author"]', author)
                self.fill_textbox('//*[@id="email"]', email)
                self.fill_textbox('//*[@id="url"]', website) if website is not None and len(website) > 0 else None
                self.fill_textbox('//*[@id="comment"]', comment_text)
                self.click_element('//*[@id="submit"]')

            previous_success = self.success
            if self.wait_for_text_in_page('Duplicate', timeout=5):
                self.success = False
                print('[-] Duplicated comment detected.')
            else:
                self.success = previous_success

            if self.success:
                print('[+] New comment posted')
                comment_link = self.driver.current_url
                comment_id = int(comment_link[comment_link.find('comment-') + 8:])
            else:
                self.success = False
                print('[-] Failed to post new comment')
        else:
            self.success = False
            print('[-] Reply panel not found')

        return comment_id

    def approve_comment(self, comment_id):
        print('[+] Approve comment')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=all')

        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        ele_xpath = '//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/div[@class="row-actions"]/span[@class="approve"]' % comment_id
        if self.driver.find_element_by_xpath(ele_xpath).is_displayed():
            self.click_element(ele_xpath + '/a')
        else:
            print('[!] This comment has been approved')

        if self.success:
            print('[+] Approving comment finished')
        else:
            print('[-] Failed to approve this comment')

    def unapprove_comment(self, comment_id):
        print('[+] Unapprove comment')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=all')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        ele_xpath = '//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/div[@class="row-actions"]/span[@class="unapprove"]' % comment_id
        if self.driver.find_element_by_xpath(ele_xpath).is_displayed():
            self.click_element(ele_xpath + '/a')
        else:
            print('[!] This comment has been approved')

        if self.success:
            print('[+] Unapproving comment finished')
        else:
            print('[-] Failed to unapprove this comment')

    def reply_comment(self, comment_id, reply_content):
        print('[+] Replying comment')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=all')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        ele_xpath = '//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/div[@class="row-actions"]/span[@class="reply hide-if-no-js"]' % comment_id
        if self.driver.find_element_by_xpath(ele_xpath).is_displayed():
            self.click_element(ele_xpath + '/a')
        else:
            self.success = False
            print('[-] Cannot find reply link')
            return

        self.fill_textbox('//*[@id="replycontent"]', reply_content)

        self.click_element('//*[@id="replybtn"]')

        if self.success:
            print('[+] Replying comment finished')
        else:
            print('[-] Failed to replying comment')

    def quick_edit_comment(self, comment_id, new_author=None, new_email=None, new_website=None, new_content=None):
        print('[+] Quick Editing comment')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=all')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        ele_xpath = '//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/div[@class="row-actions"]/span[@class="quickedit hide-if-no-js"]' % comment_id
        if self.driver.find_element_by_xpath(ele_xpath).is_displayed():
            self.click_element(ele_xpath + '/a')
        else:
            self.success = False
            print('[-] Cannot find quick edit link')
            return

        self.fill_textbox('//*[@id="author"]', new_author) if new_author is not None and len(new_author) > 0 else None
        self.fill_textbox('//*[@id="author-email"]', new_email) if new_email is not None and len(
            new_email) > 0 else None
        self.fill_textbox('//*[@id="author-url"]', new_website) if new_website is not None and len(
            new_website) > 0 else None
        self.fill_textbox('//*[@id="replycontent"]', new_content) if new_content is not None and len(
            new_content) > 0 else None

        self.click_element('//*[@id="replysubmit"]/a[1]')

        if self.success:
            print('[+] Quick editing comment finished')
        else:
            print('[-] Failed to quick edit comment')

    def spam_comment(self, comment_id):
        print('[+] Marking comment as spam')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=all')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        ele_xpath = '//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/div[@class="row-actions"]/span[@class="spam"]' % comment_id
        if self.driver.find_element_by_xpath(ele_xpath).is_displayed():
            self.click_element(ele_xpath + '/a')
        else:
            self.success = False
            print('[-] Cannot find spam link')
            return

        if self.driver.find_element_by_xpath('//*[@id="undo-%d"]' % comment_id):
            print('[+] Marking comment as spam finished')
        else:
            print('[-] Failed to mark comment as spam')

    def move_comment_to_trash(self, comment_id):
        print('[+] Moving comment to trash')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=all')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        ele_xpath = '//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/div[@class="row-actions"]/span[@class="trash"]' % comment_id
        if self.driver.find_element_by_xpath(ele_xpath).is_displayed():
            self.click_element(ele_xpath + '/a')
        else:
            self.success = False
            print('[-] Cannot find trash link')
            return

        if self.driver.find_element_by_xpath('//*[@id="undo-%d"]' % comment_id):
            print('[+] Moving comment to trash finished')
        else:
            print('[-] Failed to move comment to trash')

    # new_status should be one of the following: None(Not change), 'approved', 'pending', 'spam'.
    def edit_comment(self, comment_id, new_author=None, new_email=None, new_url=None, new_content=None, new_status=None,
                     year=None, month=None, day=None, hour=None, minute=None):
        print('[+] Editing comment')

        self.get_by_relative_url('wp-admin/comment.php?action=editcomment&c=%d' % comment_id)

        self.fill_textbox('//*[@id="name"]', new_author) if new_author is not None and len(new_author) > 0 else None
        self.fill_textbox('//*[@id="email"]', new_email) if new_email is not None and len(new_email) > 0 else None
        self.fill_textbox('//*[@id="newcomment_author_url"]', new_url) if new_url is not None and len(
            new_url) > 0 else None
        self.fill_textbox('//*[@id="content"]', new_content) if new_content is not None and len(
            new_content) > 0 else None

        self.to_page_top()

        status2value = {'approved': '1', 'pending': '0', 'spam': 'spam'}

        if new_status in ['approved', 'spam', 'pending']:
            self.click_element('//*[@id="comment-status-radio"]/label/input[@value="%s"]' % status2value[new_status])
        else:
            print("[!] new_status should be one of the following: None(Not change), 'approved', 'pending', 'spam'.")

        trans_mon_str = ['', '01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-May', '06-Jun', '07-Jul', '08-Aug', '09-Sep',
                         '10-Oct', '11-Nov', '12-Dec']
        self.click_element('//*[@id="misc-publishing-actions"]/div[@class="misc-pub-section curtime misc-pub-curtime"]/a')

        if year is not None:
            self.fill_textbox('//*[@id="aa"]', str(year))
        else:
            year = self.driver.find_element_by_xpath('//*[@id="aa"]').get_attribute('value')
        if month is not None:
            self.select_dropdown('//*[@id="mm"]', trans_mon_str[month])
        else:
            month = self.driver.find_element_by_xpath('//*[@id="mm"]').get_attribute('value')
        if day is not None:
            self.fill_textbox('//*[@id="jj"]', str(day))
        else:
            day = self.driver.find_element_by_xpath('//*[@id="jj"]').get_attribute('value')
        if hour is not None:
            self.fill_textbox('//*[@id="hh"]', str(hour))
        else:
            hour = self.driver.find_element_by_xpath('//*[@id="hh"]').get_attribute('value')
        if minute is not None:
            self.fill_textbox('//*[@id="mn"]', str(minute))
        else:
            minute = self.driver.find_element_by_xpath('//*[@id="mn"]').get_attribute('value')

        self.click_element('//*[@id="timestampdiv"]/p/a[1]')

        # Check datetime in format like Nov 15, 2018 @ 20:19
        '''publishing_datetime = '%s %s, %s @ %s:%s' % (trans_mon_str[int(month)][3:], day, year, hour, minute)
        if publishing_datetime == self.driver.find_element_by_xpath('//*[@id="timestamp"]/b').text:
            print('[+] Changing publishing datetime successfully')
        else:
            self.success = False
            print('[-] Current publishing datetime does not match')'''

        self.click_element('//*[@id="save"]')

        if self.success:
            print('[+] Editing comment finished')
        else:
            print('[-] Failed to edit comment')

    def delete_comment(self, comment_id):
        print('[+] Deleting comment permanently')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=trash')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        self.click_element(
            '//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/div[@class="row-actions"]/span[2]/a' % comment_id)

        if self.success:
            print('[+] Deleting comment finished')
        else:
            self.success = False
            print('[-] Failed to delete comment')

    def unspam_comment(self, comment_id):
        print('[+] Marking comment as unspam')
        self.get_by_relative_url('wp-admin/edit-comments.php?comment_status=spam')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="comment-%d"]' % comment_id))
        hover.perform()

        self.click_element('//*[@id="comment-%d"]/td[@class="comment column-comment has-row-actions column-primary"]/'
                           'div[@class="row-actions"]/span[1]' % comment_id)

        if self.success:
            print('[+] Marking comment as unspam finished')
        else:
            print('[-] Failed to mark comment as unspam')

    def comment_tests(self):
        print('[*] Starting comment tests...')
        comment_id = self.post_new_comment('?p=1', 'comment_user', 'comment_user@a.com', '',
                                           'A test comment_' + self.get_random_text())
        self.approve_comment(comment_id) if comment_id is not None and self.success else None
        self.unapprove_comment(comment_id) if comment_id is not None and self.success else None
        self.reply_comment(comment_id, 'Test comment reply') if comment_id is not None and self.success else None
        self.quick_edit_comment(comment_id,
                                new_content='New test comment_' + self.get_random_text()) if comment_id is not None and self.success else None
        self.edit_comment(comment_id, new_author='New User',
                          new_status='spam') if comment_id is not None and self.success else None
        self.unspam_comment(comment_id) if comment_id is not None and self.success else None
        time.sleep(2)
        self.spam_comment(comment_id) if comment_id is not None and self.success else None
        time.sleep(2)
        self.unspam_comment(comment_id) if comment_id is not None and self.success else None
        time.sleep(2)
        self.move_comment_to_trash(comment_id) if comment_id is not None and self.success else None
        time.sleep(1)
        self.delete_comment(comment_id) if comment_id is not None and self.success else None
        if self.success:
            print('[+] Comment tests finished\n----------\n')

    # By default, export_content should be one of the following: 'all', 'posts', 'pages'.
    def export(self, export_content=None):
        print('[+] Exporting contents...')
        self.get_by_relative_url('wp-admin/export.php')
        export_content = 'all' if export_content is None else export_content
        self.click_element('//*[@id="export-filters"]//input[@value="%s"]' % export_content)
        self.click_element('//*[@id="submit"]')
        if self.success:
            print('[+] Exporting finished')
        else:
            print('[-] Failed to export')

    def add_user(self, username, email, password, first_name=None, last_name=None, website=None, send_password=False,
                 role=None):
        print('[+] Adding user')
        self.get_by_relative_url('wp-admin/user-new.php')

        if username is None or len(username) == 0 or \
                email is None or len(email) == 0 or \
                password is None or len(password) == 0:
            self.success = False
            print('[-] Invalid parameter(s)')
            return None

        self.fill_textbox('//*[@id="user_login"]', username)
        self.fill_textbox('//*[@id="email"]', email)
        self.fill_textbox('//*[@id="first_name"]', first_name) if first_name is not None and len(
            first_name) > 0 else None
        self.fill_textbox('//*[@id="last_name"]', last_name) if last_name is not None and len(last_name) > 0 else None
        self.fill_textbox('//*[@id="url"]', website) if website is not None and len(website) > 0 else None
        self.click_element('//*[@id="createuser"]/table/tbody/tr[6]/td/button')
        self.fill_textbox('//*[@id="pass1-text"]', password)
        if self.driver.find_element_by_xpath('//*[@name="pw_weak"]').is_displayed():
            self.click_element('//*[@name="pw_weak"]')
        self.click_element('//*[@id="send_user_notification"]') if send_password else None
        self.select_dropdown('//*[@id="role"]', 'Subscriber' if role is None else role)

        self.click_element('//*[@id="createusersub"]')

        user_id = None

        if self.wait_for_text_in_page('New user created.', timeout=5):
            print('[+] Adding user finished')
            user_link = self.driver.find_element_by_xpath('//*[@id="message"]/p/a').get_attribute('href')
            user_id = int(user_link[user_link.find('user_id=') + 8:user_link.find('&', user_link.find('user_id='))])
        elif 'ERROR' in self.driver.page_source:
            self.success = False
            print('[-] Failed to add user: %s' % self.driver.find_element_by_xpath(
                '//*[@id="wpbody-content"]/div[4]/div[1]').text)
        else:
            self.success = False
            print('[-] Failed to add user')

        return user_id

    def delete_user(self, user_id, reassign_user=None):
        print('[+] Deleting user')
        self.get_by_relative_url('wp-admin/users.php')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="user-%d"]' % user_id))
        hover.perform()

        self.click_element('//*[@id="user-%d"]//span[@class="delete"]/a' % user_id)

        if self.wait_for_text_in_page('Delete Users'):
            self.click_element('//*[@id="submit"]')

            if self.wait_for_text_in_page('User deleted.'):
                print('[+] Deletion finished')
            else:
                self.success = False
                print('[-] Failed to delete user')
        else:
            self.success = False
            print('[-] Failed to open deletion page')

    # user_id is None -> change profile of current user; else change profile of specific user
    def edit_user_color_scheme(self, scheme_idx=0, user_id=None):
        print('[+] Editing user color scheme')
        if user_id is None:
            self.get_by_relative_url('wp-admin/profile.php')
        else:
            # Move cursor to the comment block given its id to display operations texts
            hover = ActionChains(self.driver).move_to_element(
                self.driver.find_element_by_xpath('//*[@id="user-%d"]' % user_id))
            hover.perform()

            self.click_element('//*[@id="user-%d"]/td[@class="username column-username has-row-actions column-primary"]/div/span[@class="edit"]'
                               % user_id)

        scheme_idx2id = ['admin_color_fresh', 'admin_color_light', 'admin_color_blue', 'admin_color_coffee',
                         'admin_color_ectoplasm', 'admin_color_midnight', 'admin_color_ocean', 'admin_color_sunrise']
        if scheme_idx < 0 or scheme_idx >= len(scheme_idx2id):
            self.success = False
            print('[-] Invalid scheme index')
            return
        self.click_element('//*[@id="%s"]' % scheme_idx2id[scheme_idx])

        self.click_element('//*[@id="submit"]')

        if self.wait_for_text_in_page('updated'):
            print('[+] Editing user color scheme finished')
        else:
            self.success = False
            print('[-] Failed to edit user color scheme')

    def user_test(self):
        print('[*] Starting user tests...')
        user_id = self.add_user(username='new_user1', email='new_user1@example.com', password='123456')
        self.edit_user_color_scheme(1, user_id) if self.success else None
        self.delete_user(user_id) if user_id is not None and self.success else None
        if self.success:
            print('[+] User tests finished\n----------\n')

    def upload_media(self, media_path):
        print('[+] Uploading media')
        self.get_by_relative_url('wp-admin/media-new.php')
        self.upload_file_input('//*[@id="file-form"]//div[@class="moxie-shim moxie-shim-html5"]/input', media_path)

        uploaded_media_list = self.driver.find_elements_by_xpath('//*[@id="media-items"]/div')
        uploaded_media_list.reverse()

        media_id = None

        # self.driver.save_screenshot('1.png')
        if self.wait_for_element_become_visible('//*[@id="media-items"]/div[last()]/a'):
            is_uploaded = False

            for media_item in uploaded_media_list:
                if media_item.find_element_by_css_selector('.title').text in media_path:
                    media_link = media_item.find_element_by_css_selector('.edit-attachment').get_attribute('href')
                    media_id = int(media_link[media_link.find('post=') + 5:media_link.rfind('&action')])
                    is_uploaded = True
                    break

            if self.success and is_uploaded:
                print('[+] Uploading media finished')

            else:
                self.success = False
                print('[-] Failed to upload media')
        else:
            self.success = False
            print('[-] Failed to upload media')

        return media_id

    def edit_media_prop(self, media_id, new_title=None, new_caption=None, new_alt_text=None, new_desc=None):
        print('[+] Editing media properties')
        self.get_by_relative_url('wp-admin/post.php?post=%d&action=edit' % media_id)

        if self.wait_for_text_in_page('Edit Media'):
            self.fill_textbox('//*[@id="title"]', new_title) if new_title is not None and len(new_title) > 0 else None
            self.fill_textbox('//*[@id="attachment_caption"]', new_caption) if new_caption is not None else None
            self.fill_textbox('//*[@id="attachment_alt"]', new_alt_text) if new_alt_text is not None else None
            self.fill_textbox('//*[@id="attachment_content"]', new_desc) if new_desc is not None else None
            self.click_element('//*[@id="publish"]')
            if self.wait_for_text_in_page('Media file updated.'):
                print('[+] Editing media properties finished')
            else:
                self.success = False
                print('[-] Failed to edit media properties')
        else:
            self.success = False
            print('[-] Failed to open editing media page')

    def delete_media(self, media_id):
        print('[+] Deleting media')
        self.get_by_relative_url('wp-admin/upload.php?mode=list')

        # Move cursor to the comment block given its id to display operations texts
        hover = ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath('//*[@id="post-%d"]' % media_id))
        hover.perform()

        self.click_element('//*[@id="post-%d"]/td[1]/div/span[@class="delete"]/a' % media_id)
        # '//*[@id="post-45"]/td[1]/div/span[2]'
        # Handle confirmation popup
        alert_popup = self.driver.switch_to.alert
        alert_popup.accept()

        if self.wait_for_text_in_page('Media file permanently deleted.'):
            print('[+] Media deletion finished')
        else:
            self.success = False
            print('[-] Failed to delete media')

    def media_test(self):
        print('[*] Starting media tests')
        media_id = self.upload_media(os.path.abspath('./apple.jpg'))
        self.edit_media_prop(media_id, new_caption='New Apple') if media_id is not None and self.success else None
        self.delete_media(media_id) if media_id is not None and self.success else None
        if self.success:
            print('[+] Media tests finished\n----------\n')


if __name__ == '__main__':
    # Test chrome driver
    test = WPTest471()
    test.login('admin', 'zaq1@WSX')

    test.new_post_tests() if test.success else None

    test.theme_tests() if test.success else None

    test.setting_tests() if test.success else None

    test.category_tag_tests() if test.success else None

    test.comment_tests() if test.success else None

    test.export('all') if test.success else None

    test.user_test() if test.success else None

    test.media_test() if test.success else None

    print('[+] Finished.')

    test.close_all(delay=3)
