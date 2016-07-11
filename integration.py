
class Integration:
	
	def __init__(self):
		self.orders = []

	def set_input(self,input):
		if len(input) != 3:
			raise Exception("You must pass 3 arrays.")

		if len(input[0]) != len(input[1]) or len(input[1]) != len(input[2]) or len(input[0]) != len(input[2]):
			raise Exception("Your arrays must have the same size.")

		if input == None or input == [] or isinstance(input[0], str) or isinstance(input[1], str) or isinstance(input[2], str):
			raise Exception('You must pass a valid array with integers or doubles.')
		self.input = input


	def get_size_input(self):
		return len(self.input)

	def get_freight(self):
		return self.input[0]

	def get_itens_prices(self):
		return self.input[1]

	def get_totals(self):
		return self.input[2]

	def integrate(self,t_index,solutions):
		totals = sorted(self.get_totals())
		if t_index==len(totals):
			return solutions

		freights = self.get_freight()
		itens = self.get_itens_prices()

		for i_index in range(len(self.get_itens_prices())):
			for f_index in range(len(self.get_freight())):
				if ([f_index,i_index] in solutions):
					break

				if self.match(freights[f_index],itens[i_index],totals[t_index]):
					return self.integrate(t_index+1,solutions+[[f_index,i_index]])

	def match(self,f,i,t):
		if (f+i)==t:
			return True
		else:
			return False

	def set_orders(self,orders):
		totals = sorted(self.get_totals())
		freights = self.get_freight()
		itens = self.get_itens_prices()
		i = 0
		for order in orders:
			self.orders.append([freights[order[0]],itens[order[1]],totals[i]])
			i+=1
		
	def get_orders(self):
		return self.orders

		
		
