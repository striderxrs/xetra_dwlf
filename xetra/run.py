"""Running the XETRA ETL application"""

import logging
import logging.config
import yaml

def main():
    """ XETRA ETL entry point """
    # Parsing YAML file
    config_path = 'F:/xetra_project/xetra_dwlf/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))

    # Configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("Test")

if __name__ == '__main__':
    main()