from integration import Integration
import sys

inFile = sys.argv[1]
f = open(inFile,'r')
input = f.read().splitlines()

f.close()

fretes = [float(x) for x in input[0].split(',')]
itens = [float(x) for x in input[1].split(',')]
totais = [float(x) for x in input[2].split(',')]

input = [fretes,itens,totais]

i = Integration()
i.set_input(input)
result = i.integrate(0,[])
i.set_orders(result)
i.pretty_print()
