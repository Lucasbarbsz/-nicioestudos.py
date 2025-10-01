#Função Recursiva(Fatorial de um número)

def factorial(num):
    if num == 1:
        return 1
    else: # Caso recursivo
        return num * factorial(num - 1) #é a função chamando ela mesma, mas com um número menor. 
    
print('O fatorial de num é:',factorial(5))

