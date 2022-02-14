import os
import  logging
import sys 


FORMAT = "%(asctime)s - (%(name)s) - %(levelname)s - %(message)s"

logging.basicConfig(format=FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
for handler in logger.handlers:
    logger.removeHandler(handler)

logger.addHandler(handler)




MUL_HOST=os.getenv('MUL_HOST', '0.0.0.0')

SUM_HOST=os.getenv('SUM_HOST', '0.0.0.0')