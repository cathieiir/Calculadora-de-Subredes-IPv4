# ==============================================================================
# Proyecto: Calculadora de Subredes IPv4
# Autora: Catherine Lisbeth Rodríguez de la Cruz
# Área: Telemática
# ==============================================================================

# Creé una variable para guardar el nombre del proyecto
nombre_proyecto = "Calculadora de Subredes IPv4"

# Mostré el título del programa
print("========================================")
print(nombre_proyecto)
print("Autora: Catherine Rodríguez")
print("========================================")

# Pedí la IP al usuario y la guardé en una variable
ip = input("\nIngresa una dirección IP: ")

# Pedí el prefijo CIDR al usuario
prefijo = input("Ingresa el prefijo (ej. 24): ")

# Creé una variable para la máscara según el prefijo
if prefijo == "8":
    mascara = "255.0.0.0"
elif prefijo == "16":
    mascara = "255.255.0.0"
elif prefijo == "24":
    mascara = "255.255.255.0"
else:
    mascara = "No definida"

# Mostré los resultados
print("\n--- RESULTADOS ---")
print(f"IP: {ip}")
print(f"Prefijo: /{prefijo}")
print(f"Máscara: {mascara}")
print("------------------")

# Hice una comparación simple para dar un mensaje
if prefijo == "24":
    print("Esta es una red común en hogares.")
elif prefijo == "16":
    print("Esta es una red mediana.")
else:
    print("Prefijo personalizado.")

print("\n¡Gracias por usar la calculadora!")