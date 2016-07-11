from integration import Integration
import unittest

class IntegrationTest(unittest.TestCase):
	input = [[20,25,40,45,50], [25,30,40,50,60], [50,60,70,100,105]]
	i = Integration()

	def test_instance_of_integration(self):
		self.assertIsInstance(self.i,Integration,"Not a Integration.")

	


if __name__ == '__main__':
    unittest.main()