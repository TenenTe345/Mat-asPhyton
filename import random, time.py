import random, time
# num=random.randint(1,9)

# while abs(-3)!=num:
#     print(num)
#     time.sleep(1)
#     num=random.randint(1,9)


# n1=int(input("Ingrese el valor del limite inferior: "))
# n2=int(input("Ingrese el valor del limite superior: "))
# num=random.randint(n1,n2)
# while n2>n1:
#     print("error el limite superior debe ser mayor")
#     n2=int(input("Ingrese el limite superior"))
# num=random.randint(n1,n2)
# print(num)


lata=0
plancha=0
peces=random.randint(10,20)
print("se capturaron", peces, "peces")
time.sleep
for i in range(peces):
    peso=random.randint(200,3000)
    if peso<=800:
        lata+=1
    elif peso>=801 and peso<=3000:
        plancha+=1
    else:
        print("peso invalido")
time.sleep(2)
print("El total de peces en latas son,", lata)
time.sleep(2)
print("El total de peces en plancha son", plancha)

