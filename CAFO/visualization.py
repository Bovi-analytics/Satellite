import folium
import geopandas as gpd

# Load your filtered dairy GeoJSON
gdf = gpd.read_file("cafo_filtered.geojson")

# Calculate map center by averaging coordinates
center = [gdf.geometry.y.mean(), gdf.geometry.x.mean()]

# Create a Folium Map using a default base map (optional)
m = folium.Map(location=center, zoom_start=7)

# Add a Google Satellite tile layer
folium.TileLayer(
    tiles='http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google Satellite',
    name='Google Satellite',
    subdomains=['mt0','mt1','mt2','mt3'],
    overlay=False,
    control=True
).add_to(m)

# Add a layer control panel so you can switch between base maps
folium.LayerControl().add_to(m)

# Plot each dairy CAFO location as a marker with its name
for _, row in gdf.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=row["FACILITY_NAME"],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save the map to an HTML file
m.save("cafo_filtered.html")
print("Map saved as cafo_filtered.html")