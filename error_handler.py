import logging
import sys
from typing import Any, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class CustomError(Exception):
    """Base class for custom exceptions"""
    def __init__(self, message: str, error_code: Optional[int] = None):
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()
        super().__init__(self.message)

class ValidationError(CustomError):
    """Raised when input validation fails"""
    pass

class DatabaseError(CustomError):
    """Raised when database operations fail"""
    pass

class ErrorHandler:
    """Utility class for handling and logging errors"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def handle_error(self, error: Exception, context: Optional[dict] = None) -> dict:
        """Handle different types of errors and log them appropriately
        
        Args:
            error: The exception that was raised
            context: Optional dictionary with additional context
            
        Returns:
            dict: Error details including type, message, and timestamp
        """
        error_details = {
            'error_type': error.__class__.__name__,
            'message': str(error),
            'timestamp': datetime.now().isoformat(),
            'context': context or {}
        }

        if isinstance(error, CustomError):
            error_details['error_code'] = error.error_code

        # Log different error types appropriately
        if isinstance(error, ValidationError):
            self.logger.warning(f'Validation error: {error}', extra=error_details)
        elif isinstance(error, DatabaseError):
            self.logger.error(f'Database error: {error}', extra=error_details)
        else:
            self.logger.error(f'Unexpected error: {error}', extra=error_details)

        return error_details

    def safe_execute(self, func: callable, *args: Any, **kwargs: Any) -> Any:
        """Execute a function with error handling
        
        Args:
            func: Function to execute
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
            
        Returns:
            The result of the function if successful
            
        Raises:
            CustomError: If an error occurs during execution
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_details = self.handle_error(e, {
                'function': func.__name__,
                'args': args,
                'kwargs': kwargs
            })
            raise CustomError(
                f'Error executing {func.__name__}: {str(e)}',
                error_code=getattr(e, 'error_code', None)
            ) from e

# Example usage
def example_usage():
    error_handler = ErrorHandler()
    
    # Example of handling a validation error
    try:
        raise ValidationError('Invalid input data', error_code=400)
    except Exception as e:
        error_handler.handle_error(e, {'user_id': 123})
    
    # Example of safe execution
    def risky_operation(x: int) -> int:
        if x < 0:
            raise ValueError('Number must be positive')
        return x * 2
    
    try:
        result = error_handler.safe_execute(risky_operation, -1)
    except CustomError as e:
        print(f'Caught error: {e}')

if __name__ == '__main__':
    example_usage()