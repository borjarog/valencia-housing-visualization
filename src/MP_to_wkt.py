import pandas as pd
from shapely.wkt import loads

data = pd.read_csv("./data/valencia_polygons.csv")

puntos = []

for index, row in data.iterrows():
    multipolygon = loads(row["GEO_SHAPE"])
    barrio = row["NEIGHBORHOOD"]

    for (
        polygon
    ) in multipolygon.geoms:  # Usar .geoms para obtener los polígonos individuales
        for x, y in polygon.exterior.coords:
            puntos.append({"NEIGHBORHOOD": barrio, "LONGITUDE": x, "LATITUDE": y})

puntos_df = pd.DataFrame(puntos)

puntos_df.to_csv("./data/puntos_para_tableau.csv", index=False)
