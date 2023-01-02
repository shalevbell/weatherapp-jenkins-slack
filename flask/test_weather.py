from app import *
import unittest


class TestWeather(unittest.TestCase):
	def testisup(self):
        	head = requests.head("http://localhost:9090")
        	self.assertEqual(head.status_code, 200)



if __name__ == "__main__":
    unittest.main()
