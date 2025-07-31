import pandas as pd

# Load the dataset
df = pd.read_csv("Concentrated_Animal_Feeding_Operations__CAFOs.csv")

# Normalize case for filtering
df["FACILITY_NAME_LOWER"] = df["FACILITY_NAME"].str.lower()

# Filter dairy farms (include 'dairy', exclude 'poultry')
dairy_farms = df[df["FACILITY_NAME_LOWER"].str.contains("dairy")]
dairy_farms_filtered = dairy_farms[~dairy_farms["FACILITY_NAME_LOWER"].str.contains("poultry")]

# Ambiguous: neither 'dairy' nor 'poultry'
ambiguous_farms = df[
    ~df["FACILITY_NAME_LOWER"].str.contains("dairy") &
    ~df["FACILITY_NAME_LOWER"].str.contains("poultry")
]

# Poultry farms: for exclusion log
poultry_farms = df[df["FACILITY_NAME_LOWER"].str.contains("poultry")]

# Print summary
print(f"Total records: {len(df)}")
print(f"Dairy farms (filtered): {len(dairy_farms_filtered)}")
print(f"Ambiguous farms: {len(ambiguous_farms)}")
print(f"Poultry farms excluded: {len(poultry_farms)}")

# Optionally save to CSV
dairy_farms_filtered.to_csv("dairy_farms_filtered.csv", index=False)
ambiguous_farms.to_csv("ambiguous_farms.csv", index=False)
poultry_farms.to_csv("excluded_poultry_farms.csv", index=False)
