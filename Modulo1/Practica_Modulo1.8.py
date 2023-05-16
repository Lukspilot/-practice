from binascii import b2a_hex


a = 300
b = 500
                                                c = 700

promedio = (a + b + c)/3

print("El sueldo promedio de este empleado es: ")
print(promedio)

if promedio<300:
    print("Sueldo bajo")
if promedio<900:
    print("Sueldo normal")
if promedio>900:
    print("Sueldo mejor de lo normal")

print("Fin del programa")