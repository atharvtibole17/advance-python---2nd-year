
import logging

# Create logger
logger = logging.getLogger("AppLogger")
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="w")

# Set handler levels
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create formatters
console_format = logging.Formatter(
    "%(levelname)s - %(message)s"
)

file_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Attach formatters
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log messages
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")

# Handle exception
try:
    result = 10 / 0

except ZeroDivisionError:
    logger.exception("Division failed")

# Close handlers
for handler in logger.handlers:
    handler.close()

logger.handlers.clear()

# OUTPUT
INFO - This is an INFO message
WARNING - This is a WARNING message
ERROR - This is an ERROR message
CRITICAL - This is a CRITICAL message
ERROR - Division failed
Traceback (most recent call last):
  File "your_file.py", line 35, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero

2026-11-25 12:30:00,000 - AppLogger - DEBUG - This is a DEBUG message
2026-11-25 12:30:00,000 - AppLogger - INFO - This is an INFO message
2026-11-25 12:30:00,000 - AppLogger - WARNING - This is a WARNING message
2026-11-25 12:30:00,000 - AppLogger - ERROR - This is an ERROR message
2026-11-25 12:30:00,000 - AppLogger - CRITICAL - This is a CRITICAL message
2026-11-25 12:30:00,000 - AppLogger - ERROR - Division failed
Traceback (most recent call last):
  File "your_file.py", line 35, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
