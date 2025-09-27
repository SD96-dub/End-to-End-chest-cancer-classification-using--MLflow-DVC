import os
import sys

# add 'src' folder to system path
sys.path.append(os.path.join(os.getcwd(), "src"))

from cnnClassifier import logger
logger.info("welcome to cnnClassifier!")