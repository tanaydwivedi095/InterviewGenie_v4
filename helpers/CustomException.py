import traceback
import os

class CustomException(Exception):
    """Custom exception that includes filename and line number."""

    def __init__(self, original_exception):
        tb = traceback.extract_tb(original_exception.__traceback__)
        if tb:
            last_trace = tb[-1]
            file_name = os.path.basename(last_trace.filename)
            line_number = last_trace.lineno
        else:
            file_name = "unknown"
            line_number = "unknown"
        message = str(original_exception)
        formatted_message = f"Error in {file_name} on line [{line_number}]: {message}"
        super().__init__(formatted_message)