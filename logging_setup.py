import logging

def setup_logging(config, logfile="scan.log"):
    # Remove any existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    log_level = getattr(logging, config.get("log_level", "INFO"))

    file_handler = logging.FileHandler(logfile, mode="w")
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    ))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(
        "%(message)s"
    ))

    logging.basicConfig(
        level=log_level,
        handlers=[file_handler, console_handler]
    )