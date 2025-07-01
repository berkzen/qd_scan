#Script for interfacing to (sim)Stage and (sim)Sensor w/ retry after delay, error handling & logging

import time
import logging

class stageController:
    def __init__(self, stage, max_retries: int = 3, retry_delay: float = 0.5):
        self.stage = stage
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        
    def move_to(self, x, y) -> bool:
        for attempt in range(1, self.max_retries + 1):
            try:
                self.stage.move_to(x,y)
                logging.info("Moved to ({}, {}) at attempt: {}".format(x, y, attempt))
                return True
            except TimeoutError as e:
                logging.warning("Stage failed to move: {}".format(e))
                time.sleep(self.retry_delay)
        logging.error("Failed to move to ({}, {}) after {} attempts".format(x, y, attempt))
        return False
        
        
class sensorController:
    def __init__(self, sensor, max_retries: int = 3, retry_delay: float = 0.5):
        self.sensor = sensor
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        
    def measure(self):
        for attempt in range(1, self.max_retries + 1):
            try:
                value = self.sensor.measure()
                if value is not None:
                    logging.debug("Sensor read successful in attempt: {} value: {}".format(attempt, value))
                    return value
                else:
                    logging.warning("Sensor returned None on attempt: {}".format(attempt))
            except ValueError:
                logging.warning("Sensor raised ValueError on attempt: {}".format(attempt))
                time.sleep(self.retry_delay)
        #After failure to retain value for max_retries        
        logging.error("Sensor failed to produce valid reading after {} attempts".format(self.max_retries))
        return None


        
 