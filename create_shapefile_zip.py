import geopandas as gpd

# Load your GeoJSON
gdf = gpd.read_file("cafo_filtered.geojson")

# Export as Shapefile (writes .shp + .dbf + .shx + .prj etc.)
gdf.to_file("cafo_filtered", driver="ESRI Shapefile")



