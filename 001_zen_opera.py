#Primer conjunto de elementos
set_a = {'col', 'mex', 'bol', 'br'}

#Segundo conjunto de elementos
set_b = {'bol', 'pe', 'br'}

#Tercer conjunto resultante de la union de a y b
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#Tercer conjunto resultante de la interseccion de a y b
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#Tercer conjunto resultante de la diferencia de a - b
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#Tercer conjunto resultante de la deiferencia simetrica de a - b
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)

#Ejercicio de clase
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

#Union de conjuntos, eliminar duplicados
new_set = countries.union(northAm, centralAm, southAm)
print(new_set)