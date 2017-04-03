x = int(input("digite um valor "))


def falar(palavra):
    print(palavra + "!!")


def tossir():
    falar("cough")


def espirrar():
    falar("atchoo")


for i in range(x):
    tossir()
    espirrar()
