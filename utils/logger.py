import logging
import logging.handlers
import os

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Logger configuration
logger = logging.getLogger("AIA_Logger")
logger.setLevel(logging.DEBUG)  # Capture all levels DEBUG and above

# Formatter for log messages
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# File handler - rotates logs after reaching 5MB, keeps 5 backups
file_handler = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8"
)
file_handler.setLevel(logging.INFO)  # Log INFO+ to file
file_handler.setFormatter(formatter)

# Console handler - logs WARNING+ to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Convenience functions for logging
def log_debug(msg):
    logger.debug(msg)

def log_info(msg):
    logger.info(msg)

def log_warning(msg):
    logger.warning(msg)

def log_error(msg):
    logger.error(msg)

def log_critical(msg):
    logger.critical(msg)

# Example usage:
if __name__ == "__main__":
    log_info("Logger initialized and ready.")
    log_debug("This is a debug message.")
    log_warning("This is a warning.")
    log_error("This is an error message.")
