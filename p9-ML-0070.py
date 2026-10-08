# Axel Guzman 0070
import pandas as pd

print(pd.__version__)

# Reto ABP: deteccion de riesgo de diabetes

datos = {
    "id_paciente": [1, 2, 3, 4],
    "edad": [25, 45, 60, 35],
    "nivel_glucosa": [90, 160, 180, 110],
    "presion_arterial": [120, 140, 150, 125],
    "indice_masa_corporal": [22.5, 30.2, 32.8, 25.4],
    "diagnostico_diabetes": [0, 1, 1, 0]
}

df = pd.DataFrame(datos)

print("\nDatos originales:")
print(df)

# Eliminar identificador
X = df.drop(columns=["id_paciente", "diagnostico_diabetes"])

# Variable objetivo
y = df["diagnostico_diabetes"]

print("\nCaracteristicas X:")
print(X)

print("\nVariable objetivo y:")
print(y)

print("\nColumnas utilizadas para el modelo:")
print(X.columns.tolist())
print("programa realizado por Axel Guzman 0070")