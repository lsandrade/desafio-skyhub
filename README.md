# Integração - Skyhub
Uma solução para o desafio da Skyhub. Dada uma entrada com 3 arrays correspondentes aos valores de frete, preços de itens e o valor total, organizar os pedidos de forma que cada pedido tenha seu frete, preço de itens e valor total correspondente.
Feito com Python 3.5

## Dependências
```
unittest
```

## Testando
```
$ python test.py
```

## Rodando
Pode-se executar o programa usando qualquer um dos arquivos texto de teste. Exemplo:
```
$ python run.py test_5.txt
```

## Arquivos
```
generate_tests.py - gera os arquivos texto de testes com 10, 20, 50 e 100 requisições
integration.py - classe que trata a integração dos pedidos
run.py - programa principal
test.py - testes unitários da classe Integration
test_x.txt - arquivos com respectivamente 5,10,20,50 e 100 requisições para teste do programa
```

## Formato do arquivo de entrada
```
3 linhas com valores (inteiros ou floats) separados por vírgula.
Cada linha contém um array com os valores correspondentes a quantidade de requisições.
Exemplo:
20,25,40,45,50
25,30,40,50,60
50,60,70,100,105
```

## Considerações:
```
1 - Como o programa trata valores inteiros e floats, na hora de imprimir serão impressos valores do tipo float.
Exemplo:
{pedido1: {frete: 25.0, preco_itens: 25.0, total: 50.0}}
{pedido2: {frete: 20.0, preco_itens: 40.0, total: 60.0}}
{pedido3: {frete: 40.0, preco_itens: 30.0, total: 70.0}}
{pedido4: {frete: 50.0, preco_itens: 50.0, total: 100.0}}
{pedido5: {frete: 45.0, preco_itens: 60, total: 105.0}}

2- Foi utlizada a lingagem Python pois estou mais habituado com testes nessa linguagem

3- A solução cobre todos os tamanhos possíveis de requisição propostos (5, 10, 20, 50, 100)
```
