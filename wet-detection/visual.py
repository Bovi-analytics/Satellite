import geopandas as gpd
import folium
from folium import Map, Marker, Icon, TileLayer, LayerControl
from branca.element import Template, MacroElement

# === Load labeled GeoJSON ===
gdf = gpd.read_file("/Users/a11/Desktop/Postdoc/NGO joint project/Satellite/cafo_filtered_labeled.geojson")

# === Count label types ===
label_counts = gdf["label"].value_counts().to_dict()
wet_count = label_counts.get("Wet", 0)
dry_count = label_counts.get("Dry", 0)
unknown_count = label_counts.get("Unknown", 0)

# === Calculate map center ===
center = [gdf.geometry.y.mean(), gdf.geometry.x.mean()]
m = Map(location=center, zoom_start=7)

# === Add Google Satellite tile layer ===
TileLayer(
    tiles='http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google Satellite',
    name='Google Satellite',
    subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
    overlay=False,
    control=True
).add_to(m)

# === Add farm markers with color based on label ===
for _, row in gdf.iterrows():
    label = row.get("label", "Unknown")
    color = "blue" if label == "Wet" else "red"
    Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=f"{row.get('FACILITY_NAME', 'Unnamed')} ({label})",
        icon=Icon(color=color, icon="info-sign")
    ).add_to(m)

# === Add layer controls ===
LayerControl().add_to(m)

# === Add summary box with label counts ===
template = """
{{% macro html(this, kwargs) %}}
<div style="
    position: fixed;
    bottom: 50px;
    left: 50px;
    width: 200px;
    height: 100px;
    z-index:9999;
    background-color: white;
    border:2px solid grey;
    padding:10px;
    font-size:14px;
">
<b>Farm Label Summary</b><br>
Wet: {wet}<br>
Dry: {dry}<br>
Unknown: {unknown}
</div>
{{% endmacro %}}
""".format(wet=wet_count, dry=dry_count, unknown=unknown_count)

legend = MacroElement()
legend._template = Template(template)
m.get_root().add_child(legend)

# === Save the map ===
output_path = "/Users/a11/Desktop/Postdoc/NGO joint project/Satellite/labeled_farms_map.html"
m.save(output_path)
print(f"✅ Map saved to: {output_path}")
