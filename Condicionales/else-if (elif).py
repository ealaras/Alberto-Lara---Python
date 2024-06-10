salario=80000
gasto=80000

if salario > 10000:
    if salario - gasto < 0:
        print("Estas bien en déficit")
    elif salario - gasto > 3000:
        print("Estas bien ")
    else:
        print("Estas gastanto mucho, debes revisar las cuentas")

    
elif salario > 2000:
    print("Estas bien en latinoamérica")
elif salario > 1000:
    print("Estas bien en Colombia")
elif salario > 500:
    print("Estas bien en Argentina")
else:
    print("Eres pobre")