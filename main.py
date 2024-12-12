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
print(f"O numeral romano {numeral} é igual a {resultado}.
    

