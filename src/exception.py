import logging
import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script: {0}, line number: {1}, error message: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        self.error_message = error_message_detail(error, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    # Configure logging to file
    logging.basicConfig(
        filename='example.log',  # Specify the log file path
        format="[%(asctime)s] %(levelname)s: %(message)s",
        level=logging.INFO
    )
    

