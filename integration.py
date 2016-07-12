
class Integration:

	# construtor
	def __init__(self):
		self.orders = [] # valores de fretes, itens e totais dos pedidos ordenados pelo valor total crescente
		self.solutions = [] # soluções com combinações de índices de fretes e itens ordenados pelo valor total crescente 

	# set variável input e verifica se é válida.
	def set_input(self,input):
		if len(input) != 3:
			raise Exception("You must pass 3 arrays.")

		if len(input[0]) != len(input[1]) or len(input[1]) != len(input[2]) or len(input[0]) != len(input[2]):
			raise Exception("Your arrays must have the same size.")

		if input == None or input == [] or isinstance(input[0], str) or isinstance(input[1], str) or isinstance(input[2], str):
			raise Exception('You must pass a valid array with integers or doubles.')
		
		input[0] = sorted(input[0])
		input[1] = sorted(input[1])
		input[2] = sorted(input[2])
		
		self.input = input

	# retorna array de inputs
	def get_input(self):
		return self.input

	# retorna tamanho do array de inputs
	def get_size_input(self):
		return len(self.input)

	# array de fretes
	def get_freight(self):
		return self.input[0]

	# array de preços de itens
	def get_itens_prices(self):
		return self.input[1]

	# array de totais
	def get_totals(self):
		return self.input[2]

	# retorna array de solutions calculadas no método integrate
	def get_solutions(self):
		return self.solutions


	"""
	Método que realiza a integração.
	Parametros: indice total e soluções. 
	Retorna: array com soluções ordenados pelo total de maneira crescente.
		Os valores são: [indice_frete,indice_itens]
		Ex: [[1,2],[1,3],[3,4]]. Deve retornar: [[1,0],[0,1]]
	Funcionamento: Percorre os arrays de fretes e itens procurando combinações com valor total,
	eliminando soluções já encontradas anteriormente. Uma vez encontrado um match, tenta o próximo total.
	Caso não haja match, volta e tenta a próxima combinação para o total anterior.
	Ideia: Algoritmo de Backtracking
	"""
	def integrate(self,t_index,solutions):
		totals = self.get_totals()
		
		if t_index==len(totals):
			self.solutions = solutions
			return

		freights = self.get_freight()
		itens = self.get_itens_prices()

		for i_index in range(len(self.get_itens_prices())):
			for f_index in range(len(self.get_freight())):
				match = self.match(freights[f_index],itens[i_index],totals[t_index])
				if match > 0:
					break
				elif match == 0:
					if not (self.verify_in_solutions(i_index,f_index,solutions)):
						self.integrate(t_index+1,solutions+[[f_index,i_index]])
			

	"""
	Método que testa se há um match. Se uma combnação de frete + item = total
	Parametros: f = frete, i = item, t = total
	Retorna: 0 se for igual, 1 se o valor for maior, -1 se for menor
	"""
	def match(self,f,i,t):
		r = f+i 
		if r==t:
			return 0
		elif r > t:
			return 1
		else:
			return -1

	"""
	Método que organiza uma lista de pedidos índices já integrada com seus respectivos valores e armazena no atributo orders
	Parametros: array com listas de índices retornados pelo metodo integrate()
	Retorna: void
	"""
	def set_orders(self,orders):
		totals = self.get_totals()
		freights = self.get_freight()
		itens = self.get_itens_prices()
		i = 0
		for order in orders:
			self.orders.append([freights[order[0]],itens[order[1]],totals[i]])
			i+=1
			
	def get_orders(self):
		return self.orders

	"""
	Imprime os pedidos como mencionado no desafio.
	"""
	def pretty_print(self):
		i = 1
		for order in self.orders:
			print("{pedido"+str(i)+": {frete:"+str(order[0])+", preco_itens:"+str(order[1])+",total:"+str(order[2])+"}}")
			i+=1

	"""
	Dados valores do índice de itens e índice de fretes, verificar se já estão no array de soluções
	"""
	def verify_in_solutions(self,i,f,s):
		for solution in s:
			if solution[0]==f or solution[1]==i:
				return True

		return False
		
