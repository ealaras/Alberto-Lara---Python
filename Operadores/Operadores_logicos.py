edad = int(input("Por favor, ingresa tu edad: "))

if 18 <= edad < 30:
    print("Eres joven")
elif 0 <= edad < 10:
    print("Eres un niño")
elif 11 <= edad < 18:
    print("Eres un adolescente")
elif 31 <= edad < 50:
    print("Eres un adulto")
else:
    print("Eres viejo")
Mensaje=f"Tienes {edad} años"
print(Mensaje)