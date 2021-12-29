import logging
import logging.handlers

import puncher.cnsts as cnsts


class Log(logging.Logger):
    # noinspection PyMissingConstructor
    def __init__(self):
        super(Log, self).__init__("log")
        self.setLevel(cnsts.LOG_DEFAULT_LEVEL)
        self.formatter = logging.Formatter(cnsts.LOG_DEFAULT_FORMAT, cnsts.LOG_DEFAULT_DATE_FORMAT)
        self.console_log_handler = logging.StreamHandler()
        self.console_log_handler.setFormatter(self.formatter)
        self.console_log_handler.setLevel(cnsts.LOG_DEFAULT_CONSOLE_LEVEL)
        self.file_log_handler = logging.handlers.TimedRotatingFileHandler(cnsts.LOG_DEFAULT_PATH,
                                                                          when=cnsts.LOG_DEFAULT_ROTATE_TIME,
                                                                          interval=cnsts.LOG_DEFAULT_ROTATE_INTERVAL,
                                                                          backupCount=
                                                                          cnsts.LOG_DEFAULT_ROTATE_BACKUP_COUNT,
                                                                          atTime=cnsts.LOG_DEFAULT_ROTATE_AT_TIME)
        self.file_log_handler.setFormatter(self.formatter)
        self.addHandler(self.console_log_handler)
        self.addHandler(self.file_log_handler)
