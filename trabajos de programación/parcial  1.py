print("ALMACÉN MUEBLES LA COMODIDAD")

deuda = float(input("Ingrese el valor de la deuda: "))
dia_pago = int(input("Ingrese el día del mes en que paga (1-31): "))

if dia_pago <= 10:
    descuento = deuda * 0.02
    total = deuda - descuento
    print("Pago dentro de los primeros 10 días. Descuento del 2%.")
elif dia_pago <= 20:
    total = deuda
    print("Pago entre los días 11 y 20. No hay descuento ni recargo.")
else:
    recargo = deuda * 0.02
    if recargo > 20000:
        recargo = 20000
    total = deuda + recargo
    print("Pago después del día 20. Recargo aplicado.")

print("Total a pagar: $", round(total,2 ))