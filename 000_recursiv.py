#Calculo de factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
#Calculo de fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    

factoria = factorial(5)
print(factoria)

fibonac = fibonacci(9)
print(fibonac)


    