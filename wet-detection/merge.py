import pandas as pd
import geopandas as gpd

# Paths to your files
geojson_path = "/Users/a11/Desktop/Postdoc/NGO joint project/Satellite/cafo_filtered.geojson"
labels_path = "/Users/a11/Desktop/Postdoc/NGO joint project/Satellite/wet-detection/cafo_labels.csv"
output_path = "/Users/a11/Desktop/Postdoc/NGO joint project/Satellite/cafo_filtered_labeled.geojson"

# Load label CSV
labels_df = pd.read_csv(labels_path)

# Extract numeric ID from filename like "chip_463.tif" → 463
labels_df["OBJECTID"] = labels_df["filename"].str.extract(r"chip_(\d+)\.tif").astype(int)

# Load GeoJSON
gdf = gpd.read_file(geojson_path)

# Merge on OBJECTID
merged_gdf = gdf.merge(labels_df[["OBJECTID", "label"]], on="OBJECTID", how="left")

# Save result
merged_gdf.to_file(output_path, driver="GeoJSON")

print("✅ Merged GeoJSON saved to:", output_path)
