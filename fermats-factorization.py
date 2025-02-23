# primtalsfaktorisera
import math
import sys

while True:
    try:
        user_input=input("Odd number (or 'exit'): ")
        if user_input.lower() == "exit":
            sys.exit("Exiting")
        
        n = int(user_input)
        
        if n % 2 == 0:
            print("Only odd numbers.")
        else:
            x=int(math.sqrt(n))+1
            kvadrat= None

            while kvadrat == None:
                x+=1
                kvadrat = math.sqrt(x**2-n)
                
                if kvadrat.is_integer():
                    faktor1=int(x+kvadrat)
                    faktor2=int(x-kvadrat)
                    if faktor1*faktor2 == n:
                        print(f"{faktor1} * {faktor2} = {n}")
                        break
                else:
                    kvadrat = None

    except ValueError:
        print("Must be integer.")
    except Exception as e:
        print(f"Error {e}")


