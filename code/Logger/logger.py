from csv_logger import CsvLogger
import logging
from time import sleep

filename = 'logs/Pattern_log.csv'
delimiter = "|\t"
level = logging.INFO
custom_additional_levels = ['logs_p']
fmt = f'%(asctime)s{delimiter}%(levelname)s{delimiter}%(message)s'
datefmt = '%d/%m/%Y %H:%M:%S'
max_size = 10485760  # 1 Megabyte
max_files = 1  # 1 rotating files
header = ['Date', 'Level', 'Shape', 'Color']

# Creat logger with csv rotating handler
csvlogger = CsvLogger(filename=filename,
                      delimiter=delimiter,
                      level=level,
                      add_level_names=custom_additional_levels,
                      add_level_nums=None,
                      fmt=fmt,
                      datefmt=datefmt,
                      max_size=max_size,
                      max_files=max_files,
                      header=header)

