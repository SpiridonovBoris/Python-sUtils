#!/usr/bin/env python

# s_logger.py
# 11.03.2026 [ru_RU]
# Boris Spiridonov
# Last Modified: 12.03.2026 14:51:16

import logging

class s_Logger:
    """
    @brief Logger class for logging messages to console, file, and/or socket.
    """
    def __init__(
            self, 
            name = 's_Logger', 
            log_file = 'log.log', 
            log_level = logging.INFO, 
            log_format = '%(asctime)s - %(levelname)s - %(message)s', 
            is_log_to_console = False, 
            is_log_to_file = False, 
            is_log_to_socket = False, 
            socket_host = '127.0.0.1', 
            socket_port = 9999):
        """
        Initialize the logger with specified parameters.

        :param name: Name of the logger.
        :param log_file: Path to the log file.
        :param log_level: Logging level (e.g., logging.INFO, logging.ERROR).
        :param log_format: Format of the log messages.
        :param is_log_to_console: Boolean indicating if logs should be sent to the console.
        :param is_log_to_file: Boolean indicating if logs should be sent to a file.
        :param is_log_to_socket: Boolean indicating if logs should be sent to a socket.
        :param socket_host: Host for the socket handler.
        :param socket_port: Port for the socket handler.
        """
        self.name = name
        self.log_file = log_file
        self.log_level = log_level
        self.log_format = log_format
        self.is_log_to_console = is_log_to_console
        self.is_log_to_file = is_log_to_file
        self.is_log_to_socket = is_log_to_socket
        self.socket_host = socket_host
        self.socket_port = socket_port
        self.setup_logging()

    def setup_logging(self):
        """
        Set up the logging configuration based on the initialized parameters.
        """
        formatter = logging.Formatter(self.log_format)
        handlers = []

        if self.is_log_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            handlers.append(console_handler)

        if self.is_log_to_file:
            file_handler = logging.FileHandler(self.log_file, mode = 'a')
            file_handler.setFormatter(formatter)
            handlers.append(file_handler)

        if self.is_log_to_socket:
            try:
                socket_handler = logging.handlers.SocketHandler(
                    self.socket_host, 
                    self.socket_port)
                socket_handler.setFormatter(formatter)
                handlers.append(socket_handler)
            except Exception as e:
                peint(f"Failed to set up socket handler: {e}")

        logger = logging.getLogger(self.name)
        logger.setLevel(self.log_level)
        for handler in handlers:
            logger.addHandler(handler)

        self.logger = logger

    def info(self, message):
        """
        Log an info message.

        :param message: The message to log.
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Log a warning message.

        :param message: The message to log.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Log an error message.

        :param message: The message to log.
        """
        self.logger.error(message)
