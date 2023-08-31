año = int(input("Ingrese un año "))
bis = False
if año % 4 == 0:
    if año % 100 ==0:
        if año % 400 == 0:
            bis = True

    else:
        bis = True


if bis:
    print("el "+ str(año) + " es bisiesto ")
else:
    print("el "+str(año)+ " no es bisiesto")

