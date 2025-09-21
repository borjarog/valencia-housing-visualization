import pandas as pd
import plotly.graph_objects as go
import numpy as np
import geopandas as gpd

valencia_sale = pd.read_csv("./data/valencia_sale.csv")
valencia_sale = gpd.GeoDataFrame(
    valencia_sale,
    geometry=gpd.points_from_xy(valencia_sale.LONGITUDE, valencia_sale.LATITUDE),
    crs="EPSG:4326",
)

corr = valencia_sale.select_dtypes(np.number).corr()

text_values = [
    [f"{value:.2f}" if abs(value) > 0.2 else "" for value in row] for row in corr.values
]

threshold = 0.2
filtered_corr_price = corr.loc["PRICE", (corr.loc["PRICE"].abs() > threshold)]
filtered_corr_unitprice = corr.loc[
    "UNITPRICE", (corr.loc["UNITPRICE"].abs() > threshold)
]

# Crear un DataFrame largo
data_price = pd.DataFrame(
    {"Variable": filtered_corr_price.index, "Correlation": filtered_corr_price.values}
)
data_price["Type"] = "PRICE"

data_unitprice = pd.DataFrame(
    {
        "Variable": filtered_corr_unitprice.index,
        "Correlation": filtered_corr_unitprice.values,
    }
)
data_unitprice["Type"] = "UNITPRICE"

# Concatenar ambas tablas
data_combined = pd.concat([data_price, data_unitprice])

# Exportar a CSV
data_combined.to_excel("correlations_for_tableau.xlsx", index=False)
