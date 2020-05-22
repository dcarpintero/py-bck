import yaml
import logging
import logging.config

def init(name):
    with open('./conf/logging.yaml', 'r') as f:
        logging_config = yaml.safe_load(f.read())

    logging.config.dictConfig(logging_config)
    return logging.getLogger(name)