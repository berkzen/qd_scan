import logging

def setup_logging(config, logfile="scan.log"):
    # Remove any existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # Get the default log level from the config file
    log_level = getattr(logging, config["log_level"])
    # Establish the file handler for recording the log to file
    file_handler = logging.FileHandler(logfile, mode="w")
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    ))
    # Establish the logging into the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(
        "%(message)s"
    ))
    # Setting logging with basic config with log level and multiple handlers
    logging.basicConfig(
        level=log_level,
        handlers=[file_handler, console_handler]
    )