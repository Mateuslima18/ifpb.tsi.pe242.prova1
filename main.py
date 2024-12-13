from numpy import str_


def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """
    def is_palindrome(x):  
      
     str_x = str(x)  
     
     if str_x == str_x[::-1]:  
        print(True)   
     else:  
        print(False)  

    

 

    
           


def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """
    def roma_to_int(roma):  
    
     romanos = {  
        'I': 1,  
        'V': 5,  
        'X': 10,  
        'L': 50,  
        'C': 100,  
        'D': 500,  
        'M': 1000  
    }  
    
    total = 0  
    prev_value = 0  
    
    for char in reversed(roma):
     value = romanos[char]   
        
         
     if value < prev_value:  
        total -= value  
     else:  
        total += value  
        
       
        prev_value = value  
    
    return total  

 
    numeral = "MCMXCIV"  
    resultado = roma_to_int(numeral)   
    print(f"O numeral romano {numeral} é igual a {resultado}")
    

def q3():
    """
    Quantidade de divisores de um número (incluindo 1 e o próprio número)
    """
    def contar_divisores_multiplo_3(n):
        contador = 0
    
    for i in range(1, n + 1):
        if n % i == 0 and i % 3 == 0:  
            contador += 1
     if contador > 0:
        print(f"Quantidade de divisores divisivos por 3: {contador}")
    else:
        print("O número não possui divisores múltiplos de 3")


    n = int(input())


    contar_divisores_multiplo_3(n)
   
    
   

    
    
def q4():
    """
    Soma dos números positivos no intervalo definido
    """
    def soma_positivos_no_intervalo(a, b):
    
     inicio = min(a, b)
     fim = max(a, b)
    
    soma = 0
    
   
    for i in range(inicio, fim + 1):
        if i > 0:
         soma += i
    
    return soma


    a, b = map(int, input().split())

    print(soma_positivos_no_intervalo(a, b))