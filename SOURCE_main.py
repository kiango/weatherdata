import os
import logging.config
import yaml
import sys

from process import *


def setup_logging(default_path='configurations/logging.yaml', default_level=logging.DEBUG, env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    logging.getLogger('suds.transport').setLevel(logging.DEBUG)


def main():
    # Setup logger
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    project_yaml = 'configurations/project.yaml'
    log_path = 'configurations/logging.yaml'

    try:
        # Setup logger
        setup_logging(default_path=log_path)

        logger = logging.getLogger(__name__)

        # Read configurations
        logger.debug("Reading configurations...")
        project_config = '' #TODO

        total = len(sys.argv)
        if total == 2:
            project_yaml = sys.argv[1] 
            project_config =  '' #TODO

        # Create data process object
        logger.debug("Process Initialization")
        p = Process(project_config)

        p.process()

    except Exception as ex:
        logger.exception(ex.args)

    except:
        logging.info('Unexpected error', exc_info=True)

    finally:
        logger.debug('Executing finally block')
        sys.exit()

# Entry point
if __name__ == '__main__':
    main()
