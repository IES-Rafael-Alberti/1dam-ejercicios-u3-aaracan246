"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

abecedario = list("abcdefghijklmnñopqrstuvwxyz")
        
#**********Este no lo entiendo muy bien.

def main():
    abecedarioSinMultiplos3 = []

    for i in range(len(abecedario)):
        if ((i + 1) % 3 != 0):
            abecedarioSinMultiplos3.append(abecedario[i])
    
    print(abecedarioSinMultiplos3)
            
       
            


if __name__ == "__main__":
    main()











