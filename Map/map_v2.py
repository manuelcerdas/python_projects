#References
#https://plotly.com/python/choropleth-maps/#customize-choropleth-chart

import json
import pandas as pd
import plotly.graph_objects as go

#load geographic data
with open ("Cantonal.geojson") as f:
    mapa = json.load (f)

#load the birth data
datos = pd.read_csv("nacimientos.csv")    

#change all cells to string
for col in datos.columns:
    datos[col] = datos[col].astype(str)

#add a new cell with the text for the hover
datos["caption"] = "Cantón: " + datos['canton'] + "<br />Total de nacimientos: " + datos['nacimientos'] + "<br />Hombres: " + datos['hombres'] + "<br />Mujeres: " + datos['mujeres'] 

fig = go.Figure(
    data = go.Choropleth(
        geojson=mapa, #gejson map 
        locations=datos["cod_canton"], #the column in the dataframe we use as key
        featureidkey="properties.cod_canton", #the column in the 
        z=datos["nacimientos"], #the value in the dataframe used to generate the colors
        colorscale="aggrnyl", #A predefined color scale, see reference for posible values
        text=datos["caption"], #the text in the hover
        marker_line_color='white', # line markers between cantons
    )
)            

#this line makes the map show only the geojson
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    #margin={"r":0,"t":0,"l":0,"b":0}
    title_text="Nacimientos por cantón, Primer semestre 2021"
)
fig.show()