mis_valores = [5, 6, 10, 13, 3, 4, 7]
sumatoria = 0
promedio = 0

for mi_valor in mis_valores:
    sumatoria += mi_valor

promedio = sumatoria / len(mis_valores)

print("La sumatoria de mis valores es: ", sumatoria)
print("La cantidad de mis valores es: ", len(mis_valores))
print("El promedio de mis valores es: ", promedio)

lista = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]
maximo = max(lista)
print("El valor mas alto es: %s" % maximo)

lista4 = [201,110,187,175,156,165,156,135]
maximo1 = max(lista4)
print("La altura mas alta del grupo de estudiantes es: %s" % maximo1)
