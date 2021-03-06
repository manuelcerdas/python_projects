import json
import pandas as pd
import plotly.express as px


#load geographic data
with open ("Cantonal.geojson") as f:
    mapa = json.load (f)

#load the birth data
datos = pd.read_csv("nacimientos.csv")    

fig = px.choropleth(
    datos, 
    geojson=mapa, 
    locations='cod_canton',
    featureidkey="properties.cod_canton",
    color='nacimientos',
    color_continuous_scale="Hot",
    range_color=(datos["nacimientos"].min(), datos["nacimientos"].max()),
    scope="north america",
    labels={'nacimientos':'Cantidad de nacimientos'},
    hover_name="canton",
    hover_data=["hombres","mujeres"],         
)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    #margin={"r":0,"t":0,"l":0,"b":0}
    title_text="Nacimientos por cantón, Primer semestre 2021"
)
fig.show()