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

def save_results(measurement, config):
    raw = [i[2] for i in measurement] #[[x, y, value], [...]]
    window = config["rolling_average_window"]
    filtered = rolling_average(raw, window)
    
    with open(config["output_csv"], "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "raw_values", "filtered_values"])
        for i in range(len(measurement)):
            row = list(measurement[i])
            row.append(filtered[i])
            writer.writerow(row)
            
    logging.info("Saved results to {}".format(config["output_csv"]))