import geopandas as gpd
gpd.datasets.available

data = gpd.read_file("Cantonal.geojson")

print (data.head)