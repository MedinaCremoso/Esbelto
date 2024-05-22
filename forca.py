def continua():
    while True:
        print("-" * 20)
        novamente = input("Quer jogar de novo S/N? ").upper()
        if novamente == "S":
            acabou = True
            break
        elif novamente == "N":
            acabou = False
            break
        else:
            print("Digite S ou N")
    return acabou

jogar = True
while jogar :
    jogar = continua()


(2° trimestre)
