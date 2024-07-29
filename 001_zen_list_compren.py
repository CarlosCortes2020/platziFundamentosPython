#Llenado de lista con civlo for 
numbers = []
for element in range(1, 11):
    numbers.append(element)
print(numbers)

#Llenado de lista con conprehension
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

#Llenado de lista con ciclo for 
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)
print(numbers)

#Llenado de lista con conprehension
numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

#Calculo de numeros pares con for e if 
numbers = []
for i in range(1, 101):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)

#Calculo de numeros pares con comprehensions
numbers_v2 = [element for element in range(1, 101) if element % 2 == 0]
print(numbers_v2)

