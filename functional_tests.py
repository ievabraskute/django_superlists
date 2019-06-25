from selenium import webdriver
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
        self.fail('Finish the test!')

        #  she is invited to enter her first to-do item straight away

        # she writes 'buy flour' into a text box.

        # When she hits enter, the webpage updates and now the page shows
        # '1: buy flour' as an item in the to-do list

        # there is still a text box to write another to-do item in. She writes
        # 'plan vacation'

        # the page updates again and now both items are on the list

        # the user can see that the site has generated a unique URL to access her list,
        # there is also some explanatory text about that

        # the user visits the unique URL an sees her to-do list


if __name__ == '__main__':
    unittest.main(warnings='ignore')
