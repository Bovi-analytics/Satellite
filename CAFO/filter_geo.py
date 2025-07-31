import geopandas as gpd

# Step 1: Load the GeoJSON file
gdf = gpd.read_file("Concentrated_Animal_Feeding_Operations_CAFOs.geojson")

# Step 2: Normalize names for case-insensitive filtering
gdf["FACILITY_NAME_LOWER"] = gdf["FACILITY_NAME"].str.lower()

# Step 3: Remove farms with OBJECTID in the exclusion list
objectids_to_delete = [612, 606, 913, 526, 609, 613, 611, 608, 610, 621]
gdf = gdf[~gdf["OBJECTID"].isin(objectids_to_delete)]

# Step 4: Remove facilities related to poultry/avian
keywords = ["poultry", "chicken", "turkey", "avian", "broiler", "egg"]
gdf = gdf[~gdf["FACILITY_NAME_LOWER"].str.contains('|'.join(keywords), na=False)]

# Step 5: Export the filtered GeoDataFrame to a new GeoJSON file
gdf.drop(columns=["FACILITY_NAME_LOWER"], inplace=True)  # Optional: clean up temp column
gdf.to_file("cafo_filtered.geojson", driver="GeoJSON")
