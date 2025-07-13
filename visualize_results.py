import geopandas as gpd
import matplotlib.pyplot as plt

def plot_exposure(ma_path, tn_path):
    morocco = gpd.read_file(ma_path)
    tunisia = gpd.read_file(tn_path)

    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    morocco.plot(ax=axes[0], color='red')
    axes[0].set_title("Morocco: Exposed Roads")

    tunisia.plot(ax=axes[1], color='orange')
    axes[1].set_title("Tunisia: Exposed Roads")

    plt.tight_layout()
    plt.savefig("results/maps/exposure_comparison.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_exposure("results/morocco_exposed.gpkg", "results/tunisia_exposed.gpkg")
