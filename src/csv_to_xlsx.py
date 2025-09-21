import pandas as pd

ruta_csv = r"C:\Users\borog\OneDrive - UPV\3º Curso\VIS (Visualización)\Proyecto Académico\data\puntos_para_tableau.csv"
df = pd.read_csv(ruta_csv)

print("Datos cargados:")
print(df.head())

if 'Latitude' in df.columns and 'Longitude' in df.columns:
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')

print("\nResumen de los datos:")
print(df.info())

ruta_salida = r'C:\Users\borog\OneDrive - UPV\3º Curso\VIS (Visualización)\Proyecto Académico\data\puntos_para_tableau.xlsx'
df.to_excel(ruta_salida, index=False)
print(f"\nArchivo procesado guardado como: {ruta_salida}")
