from integration import Integration
import unittest

class IntegrationTest(unittest.TestCase):
	input = [[20,25,40,45,50], [25,30,40,50,60], [50,60,70,100,105]]
	i = Integration()

	def test_instance_of_integration(self):
		self.assertIsInstance(self.i,Integration,"Not a Integration.")

	def test_size_input(self):
		self.i.set_input(self.input)

		self.assertEqual(3,self.i.get_size_input(),"Your input must contain 3 arrays.")

	def test_homogeneously_input(self):
		self.i.set_input(self.input)

		self.assertTrue(self.i.is_input_homogeneous(),"Arrays must have the same size.")
		wrong_input = [[3,2,1],[1,2],[1]]
		self.i.set_input(wrong_input)
		self.assertFalse(self.i.is_input_homogeneous(),"Arrays must have the same size.")


if __name__ == '__main__':
    unittest.main()