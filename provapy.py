
i = 5
o = 0
while i == 5:
    import random
    numero1 = random.randint(0, 10000000)   
    numero2 = random.randint(0, 10000000)
    o += 1
    if numero1 != numero2:
        print(numero1, numero2)
       
    else:        
        print(numero1, "=", numero2)
        i = 4

print("fine")
print(o, "tentativi")

# commento