#saving raw and filtered sensor readout into a csv file

import logging
import csv

def rolling_average(values, window):
    averaged = []
    for i in range(len(values)):
        if values[i] is None:
            averaged.append(None)
            continue
        window_values = values[max(0, i - window + 1):(i + 1)]
        window_values = [j for j in window_values if j is not None]
        avg = sum(window_values)/len(window_values) if window_values else None
        averaged.append(avg)
    return averaged

def save_results(results, config):
    raw = [i[2] for i in results] #[[x, y, value], [...]]
    window = config["rolling_average_window"]
    filtered = rolling_average(raw, window)
    
    with open(config["output_csv"], "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "raw_values", "filtered_values"])
        for i in range(len(results)):
            row = list(results[i])
            row.append(filtered[i])
            writer.writerow(row)
            
    logging.info("Saved results to {}".format(config["output_csv"]))
    return filtered
    
def detect_peak(results, filtered):
    max_val = float("-inf")
    max_coords = None
    
    for i in range(len(filtered)):
        val = filtered[i]
        if val is not None and val > max_val:
            max_val = val
            max_coords = (float(results[i][0]), float(results[i][1]))
            
    if max_coords is not None:
        logging.info("Peak detected at {} with value {}".format(max_coords, max_val))
    
    else:
        logging.warning("No valid filtered value to detect peak")