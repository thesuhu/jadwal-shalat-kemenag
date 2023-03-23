import utils.helper as helper
import unittest
# import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


class TestHelper(unittest.TestCase):

    def test_getCookies(self):
        cookies = helper.getCookies()
        # print('\n')
        # print(cookies)
        # print('\n')
        self.assertTrue(len(cookies) > 0)
        self.assertIsNotNone(cookies)
        # self.assertEqual(len(cookies), 1)


if __name__ == '__main__':
    unittest.main()
