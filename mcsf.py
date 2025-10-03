import geopandas as gpd

# 1. Path to shapefile
shapefile_path = "boundary_sp/neighborhood.shp"

# 2. Load shapefile
gdf = gpd.read_file(shapefile_path)

# 3. Print columns + first few rows (optional debugging)
print(gdf.columns)
print(gdf.head())

# 4. Print all neighborhood names (so you can confirm spelling)
print(gdf['NEIGHBORHD'].unique())

# 5. Reproject to WGS84 (lat/lon) so Datawrapper accepts it
gdf = gdf.to_crs(epsg=4326)

# 6. Filter just Metcalfe Park
metcalfe = gdf[gdf['NEIGHBORHD'].str.contains("METCALFE PARK", case=False, na=False)]

# 7. Save as GeoJSON (works in Datawrapper)
metcalfe.to_file("metcalfe_park.geojson", driver="GeoJSON")
