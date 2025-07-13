import geopandas as gpd
import os

def load_and_clip_roads(country: str, boundary_path: str):
    roads_path = f"data/{country}/roads.shp"
    roads = gpd.read_file(roads_path)
    boundary = gpd.read_file(boundary_path)
    clipped = gpd.overlay(roads, boundary, how='intersection')
    return clipped

def save_gpkg(gdf, out_path):
    gdf.to_file(out_path, driver='GPKG')

if __name__ == "__main__":
    morocco_roads = load_and_clip_roads('morocco', 'data/morocco/boundary.shp')
    save_gpkg(morocco_roads, 'data/morocco/roads_clipped.gpkg')

    tunisia_roads = load_and_clip_roads('tunisia', 'data/tunisia/boundary.shp')
    save_gpkg(tunisia_roads, 'data/tunisia/roads_clipped.gpkg')
