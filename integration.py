
class Integration:

	def integrate(self):
		return 1


	def set_input(self,input):
		self.input = input

	def get_size_input(self):
		return len(self.input)

	def is_input_homogeneous(self):
		if len(self.input[0]) == len(self.input[1]) and len(self.input[1])==len(self.input[2]):
			return True
		else:
			return False