import logging

def setup_logging():
    """
    Configures the logging format and level.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
