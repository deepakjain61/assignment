import logging
import os
import time


class Logger(object):
    def __init__(self, log_path="logs"):
        """

        :param log_path: Directory where logs are to be created.
        """
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        time_str = str(time.strftime("%Y%m%d-%H%M%S")) + ".log"
        log_path = os.path.join(log_path, time_str)
        logging.basicConfig(filename=log_path, level=logging.INFO, filemode='w', format='%(name)s - %(levelname)s - '
                                                                                        '%(message)s')
        self.log = logging
