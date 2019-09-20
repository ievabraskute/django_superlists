from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # a user has heard of a new to-do app and goes to check ut its homepage
        self.browser.get('http://localhost:8000')

        # she sees that the page header and title mention 'to-do'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #  she is invited to enter her first to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she writes 'Buy flour' into a text box.
        inputbox.send_keys('Buy flour')

        # When she hits enter, the webpage updates and now the page shows
        # '1: Buy flour' as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1. Buy flour')

        # there is still a text box to write another to-do item in. She writes
        # 'Plan vacation'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Plan vacation')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the page updates again and now both items are on the list
        self.check_for_row_in_list_table('1. Buy flour')
        self.check_for_row_in_list_table('2. Plan vacation')

        # the user can see that the site has generated a unique URL to access her list,
        # there is also some explanatory text about that
        self.fail('Finish the test!')

        # the user visits the unique URL an sees her to-do list


if __name__ == '__main__':
    unittest.main()
