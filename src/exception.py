import sys
import logging
# sys library: manipulate Python runtime env
# contains things for exception handling

def error_message_detail(error, error_detail:sys):
    # error_detail present in sys
    _,_,exc_tb=error_detail.exc_info()
    # .exc_info() -> gives execution info, 3rd thing gives detail on file, line num, etc
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    # gets specific filename from the error detail
    # can check in python custom exception handling documentation

    error_message = 'Error occurred in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    # inherits from parent Exception
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=='__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.info('Divide by 0')
        raise CustomException(e, sys)