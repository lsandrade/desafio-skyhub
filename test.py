from integration import Integration
import unittest

class IntegrationTest(unittest.TestCase):
	input = [[20,25,40,45,50], [25,30,40,50,60], [50,60,70,100,105]]
	i = Integration()

	def test_instance_of_integration(self):
		self.assertIsInstance(self.i,Integration,"Not a Integration.")

	def test_size_input_with_error(self):
		self.assertRaises(Exception,self.i.set_input,[[12,1],[1,3]])

	def test_homogeneously_input_with_error(self):
		wrong_input = [[3,2,1],[1,2],[1]]
		self.assertRaises(Exception, self.i.set_input,wrong_input)

	def test_get_freight(self):
		self.i.set_input(self.input)
		self.assertEqual(self.input[0],self.i.get_freight(),"Not the same array of freight.")

	def test_get_itens_prices(self):
		self.i.set_input(self.input)
		self.assertEqual(self.input[1],self.i.get_itens_prices(),"Not the same array of itens.")

	def test_get_totals(self):
		self.i.set_input(self.input)
		self.assertEqual(self.input[2],self.i.get_totals(),"Not the same array of totals.")

	def test_match(self):
		self.assertTrue(self.i.match(1,1,2),"Doesn't match.")
		self.assertFalse(self.i.match(1,1,3),"Doesn't match.")


	def test_integrate(self):
		expected = [[25,25,50],[20,40,60],[40,30,70],[50,50,100],[45,60,105]]
		self.i.set_input(self.input)
		result = self.i.integrate(0,[])
		self.i.set_orders(result)
		self.assertEqual(expected,self.i.get_orders(),"Result doesn't match")		

	# testar array nulo ou vazio (exception)
	def test_null_array(self):
		self.assertRaises(Exception, self.i.set_input,None)

	def test_empty_array(self):
		self.assertRaises(Exception, self.i.set_input,[])

	def test_string_array(self):
		self.assertRaises(Exception, self.i.set_input,['a','2','c'])
		self.assertRaises(Exception, self.i.set_input,['a','b',1])
		self.assertRaises(Exception, self.i.set_input,['a',1,'c'])

	# testar array com doubles
	def test_doubles(self):
		d_input = [[20.1,25.2], [25.0,30.3], [45.1,55.5]]
		d_expected = [[20.1,25.0,45.1],[25.2,30.3,55.5]]
		d = Integration()
		d.set_input(d_input)
		d_result = d.integrate(0,[])
		d.set_orders(d_result)
		self.assertEqual(d_expected,d.get_orders(),"Result doesn't match")

	# testar para todos os tamanhos de arrays


if __name__ == '__main__':
    unittest.main()