import geopandas as gpd

# Path to your shapefile (without extension, geopandas reads all parts)
shapefile_path = "boundary_sp/neighborhood.shp"

# Load shapefile
gdf = gpd.read_file(shapefile_path)

# Inspect attribute columns to confirm which contains neighborhood names
print(gdf.columns)
print(gdf.head())

# Filter for Metcalfe Park (replace 'NEIGHBORHOOD' with actual column name)
metcalfe = gdf[gdf['NEIGHBORHD'].str.contains("Metcalfe Park", case=False, na=False)]

# Or save as GeoJSON
metcalfe.to_file("boundary_sp/metcalfe_park.geojson", driver="GeoJSON")