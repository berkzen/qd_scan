#main logic file for executing scan and collecting data

from sim_devices import SimStage, SimSensor
from devices import stageController, sensorController
from config import load_config
from logging_setup import setup_logging
from save_file import save_results, detect_peak
from plotting import plot_heatmap
import logging
import numpy as np
import sys

def run_scan(config_path: str = "config.yaml"):
    #load config file and set up logging
    config = load_config(config_path)
    setup_logging(config)
    
    #initialize devices
    stage_init = SimStage()
    sensor_init = SimSensor()
    
    #wrap with controller to retry upon failure/None return
    stage = stageController(stage_init, 
                            max_retries=config["max_retries"], 
                            retry_delay=config["retry_delay"])
    sensor = sensorController(sensor_init, 
                              max_retries=config["max_retries"], 
                              retry_delay=config["retry_delay"])
    
    #scan grid
    x_axis = np.linspace(*config["x_range"])
    y_axis = np.linspace(*config["y_range"])
    
    results = []
    
    for y in y_axis:
        for x in x_axis:
            logging.info("Scanning point {}, {}".format(x, y))
            if stage.move_to(x, y):
                measurement = sensor.measure()
            else:
                measurement = None
                logging.error("The stage has failed to move, aborting the scan")
                results.append((x, y, measurement))
                
                #save before quitting the measurement
                filtered = save_results(results, config)
                detect_peak(results, filtered)
                plot_heatmap(results, filtered, config)
                sys.exit("Scan aborted due to stage failure")
                
            results.append((x, y, measurement))
    
    logging.info("Scan complete.")
    
    filtered = save_results(results, config)
    detect_peak(results, filtered)
    plot_heatmap(results, filtered, config)
    return config, results
           
if __name__ == "__main__":
    run_scan()   