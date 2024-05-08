import random
continuar  = "S"

while continuar.upper() == "S" :
    ns = random.randint(1,10)

    T = 3

    while( t > 0):
        print(" voce tem" , t, "tentativa")
        T = T -1

        nc = int(input ("Digite um Número de 1 a 10: "))
        if (ns == nc):
            print("você acertou.")
        else:
            print("você errou.")

continuar = input("deseja continuar (S)im")
