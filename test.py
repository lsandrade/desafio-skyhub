from integration import Integration
import unittest

class IntegrationTest(unittest.TestCase):
	input = [[20,25,40,45,50], [25,30,40,50,60], [50,60,70,100,105]]
	i = Integration()

	# teste de criação da classe
	def test_instance_of_integration(self):
		self.assertIsInstance(self.i,Integration,"Not a Integration.")

	def test_correct_input(self):
		self.i.set_input(self.input)
		self.assertEqual(self.input,self.i.get_input(),"Not the same input.")

	# teste faltando 1 array de valores
	def test_size_input_with_error(self):
		self.assertRaises(Exception,self.i.set_input,[[12,1],[1,3]])

	# teste array heterogeneo
	def test_homogeneously_input_with_error(self):
		wrong_input = [[3,2,1],[1,2],[1]]
		self.assertRaises(Exception, self.i.set_input,wrong_input)

	# teste valores de frete
	def test_get_freight(self):
		self.i.set_input(self.input)
		self.assertEqual(self.input[0],self.i.get_freight(),"Not the same array of freight.")

	# teste valores de preços dos itens
	def test_get_itens_prices(self):
		self.i.set_input(self.input)
		self.assertEqual(self.input[1],self.i.get_itens_prices(),"Not the same array of itens.")

	# teste valores de totais
	def test_get_totals(self):
		self.i.set_input(self.input)
		self.assertEqual(self.input[2],self.i.get_totals(),"Not the same array of totals.")

	# teste se 3 valores 'combinam' (se a soma dos 2 primeiros da o terceiro)
	def test_match(self):
		self.assertEqual(0,self.i.match(1,1,2),"Doesn't match.")
		self.assertEqual(-1,self.i.match(1,1,3),"Doesn't match.")
		self.assertEqual(1,self.i.match(1,4,3),"Doesn't match.")


	# teste médodo de integração
	def test_integrate(self):
		expected = [[25,25,50],[20,40,60],[40,30,70],[50,50,100],[45,60,105]]
		self.i.set_input(self.input)
		self.i.integrate(0,[])
		result = self.i.get_solutions()
		self.i.set_orders(result)
		self.assertEqual(expected,self.i.get_orders(),"Result doesn't match")		

	# testar array nulo ou vazio (exception)
	def test_null_array(self):
		self.assertRaises(Exception, self.i.set_input,None)

	def test_empty_array(self):
		self.assertRaises(Exception, self.i.set_input,[])

	# teste array de strings
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
		d.integrate(0,[])
		d_result = d.get_solutions()
		d.set_orders(d_result)
		self.assertEqual(d_expected,d.get_orders(),"Result doesn't match")

	# testar valores de indices que podem estar no array de solutions
	def test_verify_in_solutions(self):
		solutions = [[0,1],[1,2]]
		self.assertTrue(self.i.verify_in_solutions(1,1,solutions),"This number sould be in solutions.")
		self.assertTrue(self.i.verify_in_solutions(1,0,solutions),"This number sould be in solutions.")
		self.assertTrue(self.i.verify_in_solutions(0,1,solutions),"This number sould be in solutions.")
		self.assertTrue(self.i.verify_in_solutions(2,0,solutions),"This number sould be in solutions.")
		self.assertFalse(self.i.verify_in_solutions(0,2,solutions),"This number souldn't be in solutions.")

	
if __name__ == '__main__':
    unittest.main()