salario = float(input(' Valor do salario R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)    
print(" Quem ganhava R${} com novo Aumento passa a Ganhar R${} . ".format(salario,novo))