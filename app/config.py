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


DEBUG_MODE=os.getenv("DEBUG_MODE", False)

MUL_HOST=os.getenv('MUL_HOST', '0.0.0.0')

MUL_PORT=os.getenv('MUL_PORT', 8001)

SUM_HOST=os.getenv('SUM_HOST', '0.0.0.0')

SUM_PORT=os.getenv('SUM_PORT', 8002)