# -*- coding: utf-8 -*-
from .loggers import LOGGING_CONFIG_CONSOLE, LOGGING_CONFIG_FILE
from logging.config import dictConfig

dictConfig(LOGGING_CONFIG_CONSOLE)  ##