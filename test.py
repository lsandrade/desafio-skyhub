from integration import integration
import unittest

class IntegrationTest(unittest.TestCase):
	input = [[20,25,40,45,50], [25,30,40,50,60], [50,60,70,100,105]]

	def testOne(self):
		self.assertEqual(integration(),1)


if __name__ == '__main__':
    unittest.main()