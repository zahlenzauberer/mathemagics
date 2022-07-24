lista = []
def collatz(x):
    while x > 1:
        if x % 2 == 0:
            x = int(x/2)
            lista.append(x)
        else:
            x  = int((3*x)+1)
            lista.append(x)
num = int(input("Digite um número natural: "))
print("A sequência de Collatz para o número %d é: " %num)
collatz(num)
print(*lista, sep=", ")
