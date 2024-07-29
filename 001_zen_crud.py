set_countries = {'col', 'mex', 'bol'} #Esto es un conjunto de datos
print(set_countries)
print(len(set_countries))       #Tamaño del conjunto

print('col' in set_countries)   #Existe en conjunto?
print('pe' in set_countries)   #Existe en conjunto?

set_countries.add('pe')        #Agregamos Peru al conjunto
print(set_countries)  

set_countries.update({'mx', 'ar', 'br'}) #Actualizar con nuevos elementos al conjunto
print(set_countries)  

set_countries.remove('br') #Remover algun elemento del conjunto
print(set_countries)  

set_countries.clear() #Elimina todos los elementos del conjunto
print(set_countries)  