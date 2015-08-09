import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('application.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logging.Formatter.converter = time.gmtime
handler.setFormatter(formatter)

logger.addHandler(handler)