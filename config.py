import yaml
import logging

def load_config(path: str = "config.yaml") -> dict:
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
            logging.info("Loaded config from {}".format(path))
            if config is None:
                raise ValueError("Config file is empty.")
            return config
        
    except FileNotFoundError:
        logging.error("Configuration file not found.")
        raise
    
    except yaml.YAMLError as yamlError:
        logging.error("Error parsing YAML config: {}.".format(yamlError))
        raise
    