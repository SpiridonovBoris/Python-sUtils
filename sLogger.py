#!/usr/bin/env python

# file_name
# 11.03.2026 [ru_RU]
# Boris Spiridonov
# Editor: Boris Spiridonov
# Last Modified: 01.06.2026 00:50:51

import logging
import os

class sLogger:
    """
    @brief Logger class for logging messages to console, file, and/or socket.
    """
    def __init__(
            self, 
            name = 'sLogger', 
            log_file = 'log.log', 
            log_level = logging.INFO, 
            log_format = '%(asctime)s - %(levelname)s - %(message)s', 
            is_log_to_console = False, 
            is_log_to_file = False, 
            is_log_to_socket = False, 
            socket_host = '127.0.0.1', 
            socket_port = 9999,
            logger = None):
        """
        @brief Initialize the logger with specified parameters.

        @param name: Name of the logger.
        @param log_file: Path to the log file.
        @param log_level: Logging level (e.g., logging.INFO, logging.ERROR).
        @param log_format: Format of the log messages.
        @param is_log_to_console: Boolean indicating if logs should be sent to the console.
        @param is_log_to_file: Boolean indicating if logs should be sent to a file.
        @param is_log_to_socket: Boolean indicating if logs should be sent to a socket.
        @param socket_host: Host for the socket handler.
        @param socket_port: Port for the socket handler.
        @param logger: The external logger instance.
        """
        self.name = name
        self.log_file = os.path.expanduser(log_file)
        self.log_level = log_level
        self.log_format = log_format
        self.is_log_to_console = is_log_to_console
        self.is_log_to_file = is_log_to_file
        self.is_log_to_socket = is_log_to_socket
        self.socket_host = socket_host
        self.socket_port = socket_port
        self.logger = logger

        self.setup_logging()

    def setup_logging(self):
        """
        @brief Set up the logging configuration based on the initialized parameters.
        """
        formatter = logging.Formatter(self.log_format)

        if not self.logger:
            self.logger = logging.getLogger(self.name)

        self.logger.setLevel(self.log_level)

        self.clear_handlers()

        handlers = []

        if self.is_log_to_console:
            handlers.append(self.setup_console_handler(formatter))

        if self.is_log_to_file:
            handlers.append(self.setup_file_handler(formatter))

        if self.is_log_to_socket:
            handlers.append(self.setup_socket_handler(formatter))

        self.add_handlers_to_logger(handlers)

        return self

    def clear_handlers(self):
        """
        @brief Clears existing handlers from the logger.
        """
        if self.logger.handlers:
            for handler in self.logger.handlers[:]:
                self.logger.removeHandler(handler)
                handler.close()

        return self

    def setup_console_handler(self, formatter):
        """
        @brief Sets up the console handler.
        @param formatter: The formatter to use for the console handler.
        @return: The configured console handler.
        """
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        return console_handler

    def setup_file_handler(self, formatter):
        """
        @brief Sets up the file handler.
        @param formatter: The formatter to use for the file handler.
        @return: The configured file handler.
        """
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, mode = 0o755 , exist_ok = True)

        file_handler = logging.FileHandler(self.log_file, mode='a')
        file_handler.setFormatter(formatter)

        return file_handler

    def setup_socket_handler(self, formatter):
        """
        @brief Sets up the socket handler.
        @param formatter: The formatter to use for the socket handler.
        @return: The configured socket handler.
        """
        try:
            socket_handler = logging.handlers.SocketHandler(
                self.socket_host, 
                self.socket_port)
            socket_handler.setFormatter(formatter)
        except Exception as e:
            peint(f"Failed to set up socket handler: {e}")

        return socket_handler

    def add_handlers_to_logger(self, handlers):
        for handler in handlers:
            self.logger.addHandler(handler)

        return self

    def info(self, message):
        """
        @brief Log an info message.

        @param message: The message to log.
        """
        self.logger.info(message)

        return self

    def warning(self, message):
        """
        @brief Log a warning message.

        @param message: The message to log.
        """
        self.logger.warning(message)

        return self

    def error(self, message):
        """
        @brief Log an error message.

        @param message: The message to log.
        """
        self.logger.error(message)

        return self
