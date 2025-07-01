#Generating the heatmap based on filtered sensor value and scan coordinates

import matplotlib.pyplot as plt
import numpy as np
import logging
from save_file import get_measurement_paths

def plot_heatmap(results, filtered, config):
    x_coords = [i[0] for i in results]
    y_coords = [i[1] for i in results]
    
    x_vals = sorted(set(x_coords))
    x_index_map = {}
    for i in range(len(x_vals)):
        x_index_map[x_vals[i]] = i
        
    y_vals = sorted(set(y_coords))
    y_index_map = {}
    for i in range(len(y_vals)):
        y_index_map[y_vals[i]] = i

    heatmap = np.full((len(y_vals), len(x_vals)), np.nan)
    
    for i in range(len(results)):
        zValue = filtered[i]
        
        if zValue is not None:
            xi = x_index_map[x_coords[i]]
            yi = y_index_map[y_coords[i]]
            heatmap[yi][xi] = zValue
            
    plt.figure()
    plt.imshow(
        heatmap,
        origin="lower",
        cmap="viridis",
        extent=[min(x_coords), max(x_coords), min(y_coords), max(y_coords)],
        aspect="auto",
        interpolation="none"
    )
    plt.colorbar(label="Filtered Signal")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("2D Heatmap (Filtered)")
    
    _ , plot_path = get_measurement_paths(config)
     
    plt.savefig(plot_path, dpi = 300)
    
    logging.info("Saved heatmap as {}".format(plot_path))
    

