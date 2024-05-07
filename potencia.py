b = int(input("Digite o valor da Base:"))
e = int(input("Diite o valor do Expoente:"))
r = b
for g in range (1,e):
    r = r * b
print(" resultado: ", "{:.2f}".format(r))
