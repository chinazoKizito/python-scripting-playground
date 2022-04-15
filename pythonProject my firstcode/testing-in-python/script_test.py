import unittest
import script


class Testmain(unittest.TestCase):
    def setUp(self) -> None:
        print("About to run a function")

    def test_do_stuff(self):
        """Testing for 10 as a param lol"""
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'mmmmmmmjhjkh'
        result = script.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = script.do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self) -> None:
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
