from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

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

        # she writes 'buy flour' into a text box.
        inputbox.send_keys('buy flour')

        # When she hits enter, the webpage updates and now the page shows
        # '1: buy flour' as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: buy four' for row in rows),
            "New to-do item did not appear in table"
        )

        # there is still a text box to write another to-do item in. She writes
        # 'plan vacation'
        self.fail('finish the test!')

        # the page updates again and now both items are on the list

        # the user can see that the site has generated a unique URL to access her list,
        # there is also some explanatory text about that

        # the user visits the unique URL an sees her to-do list


if __name__ == '__main__':
    unittest.main(warnings='ignore')
