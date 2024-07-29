#Llenado de diccioanrio con ciclo for 
dictio = {}
for i in range(1, 11):
    dictio[i] = i * 2 
print(dictio)

#Llenado de diccionario con conprehension
dictio_v2 = {i: i * 2 for i in range(1, 11)}
print(dictio_v2)


#===================================================================================
import random

#Llenado de diccionario con ciclo for
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 1000)
print(population)

#Llenado de diccionario con comprehension
population_v2 = {country: random.randint(1, 1000) for country in countries}
print(population_v2)


#======================================================================================
names = ['Nico', 'Santi', 'Thiago']
ages = [23, 68, 45]

names_ages = list(zip(names, ages))
print(names_ages)

new_dicti = {name: age for (name, age) in names_ages}
print(new_dicti)

#===================================================================================
countries = ['col', 'mex', 'bol', 'pe', 'br', 'usa']

#Llenado de diccionario con comprehension
population_v2 = {country: random.randint(1, 1000) for country in countries}
print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population >= 300}
print(result)

#=======================================================================================================
text = 'Con cada dia que pasa, siento que aprendo algo nuevo, sin embargo, he de ser disciplinado para no caer en la procrastinacion'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print(unique)