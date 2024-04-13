import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='appLog.log', encoding="utf8", level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
