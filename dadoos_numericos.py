num1 = 5 
num2 = 3.6
num_string = '5'

print(type(num_string))

a = float(5)
b = float(a)
print(b)
print(a)
print(type(b))

b = int(num2)
print(b)
print(type(b))

c = int(num_string)
print(c)
print(type(c))

altura = 1.70
peso = 70
print(f'seu imc é {int(peso / (altura * altura))}')