def crear_contraseña (num):
    chars="abcdefghij"
    num_entero=str(num)
    num=int(num_entero[0])
    c1=num-2
    c2=num
    c3=num-5
    contraseña=f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
password=crear_contraseña(input("Dame un numero: "))
frase=f"Tu contraseña nueva es: {password}"
print(frase)