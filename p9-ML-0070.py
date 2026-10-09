
# Axel Guzman 0070
import pandas as pd

print("Version de Pandas:", pd.__version__)

# Reto ABP: deteccion de riesgo de diabetes

# 27.
datos27 = {
    'distancia_km': [4.8, 2.3, 3.2, 5.4, 1.6],
    'trafico_nivel': [2, 1, 3, 2, 1],
    'edad_repartidor': [33, 26, 40, 35, 24],
    'tiempo_entrega_min': [38, 17, 30, 44, 12]
}

# Crear el DataFrame
df = pd.DataFrame(datos27)

print("\nDatos originales:")
print(df)

# Caracteristicas para el modelo
X = df.drop(columns=["tiempo_entrega_min"])

# Variable objetivo
y = df["tiempo_entrega_min"]

print("\nCaracteristicas X:")
print(X)

print("\nVariable objetivo y:")
print(y)

print("\nColumnas utilizadas para el modelo:")
print(X.columns.tolist())

print("\nPrograma realizado por Axel Guzman 0070")
