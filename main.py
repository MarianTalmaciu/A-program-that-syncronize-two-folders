from dirsync import sync
import logging


source_path = 'D:/PythonProjects/A program that syncronize two folders/source/'
replica_path = 'D:/PythonProjects/A program that syncronize two folders/replica/'


sync(source_path, replica_path, "sync")


logger = logging.getLogger('my.logger')
# logging.basicConfig(level=logging.DEBUG)

file_log_handler = logging.FileHandler('logfile.log')
logger.addHandler(file_log_handler)

stderr_log_handler = logging.StreamHandler()
logger.addHandler(stderr_log_handler)

# output format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log_handler.setFormatter(formatter)
stderr_log_handler.setFormatter(formatter)

logger.info('This is an info message')
logger.error('This is an error message')
