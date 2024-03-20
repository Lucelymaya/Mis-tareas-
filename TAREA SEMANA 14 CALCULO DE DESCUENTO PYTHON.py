def calcular_descuento(monto_total, porcentaje_descuento = 10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función proporcionando solo el monto total de la compra
monto_compra_1 = 200
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

print("Para una compra de $", monto_compra_1, "el descuento es de $", descuento_1, "(", 'porcentaje_descuento_1', "%) y el monto final a pagar es de $", monto_final_1)

# Llamada a la función proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_compra_2 = 300
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

print("Para una compra de $", monto_compra_2, "con un descuento del", porcentaje_descuento_2, "%, el descuento es de $", descuento_2, "(", porcentaje_descuento_2, "%) y el monto final a pagar es de $", monto_final_2)

