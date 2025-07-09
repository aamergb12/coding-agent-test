def validate_number(value):
    """
    Validate if the input can be converted to a float number.
    
    Args:
        value: Input value to validate
        
    Returns:
        float: Converted number if valid
        
    Raises:
        ValueError: If the input cannot be converted to a float
    """
    try:
        return float(value)
    except ValueError:
        raise ValueError("Invalid number input")

def validate_operator(operator):
    """
    Validate if the operator is supported.
    
    Args:
        operator: Mathematical operator to validate
        
    Returns:
        str: Validated operator
        
    Raises:
        ValueError: If the operator is not supported
    """
    valid_operators = ['+', '-', '*', '/', '**']
    if operator not in valid_operators:
        raise ValueError(f"Invalid operator. Supported operators are: {', '.join(valid_operators)}")
    return operator

def format_result(result):
    """
    Format the calculation result to handle special cases.
    
    Args:
        result: The calculation result
        
    Returns:
        str: Formatted result
    """
    if isinstance(result, float):
        # Convert to integer if the float is a whole number
        if result.is_integer():
            return str(int(result))
        # Limit decimal places for float results
        return f"{result:.6f}".rstrip('0').rstrip('.')
    return str(result)

def divide_numbers(a, b):
    """
    Safely perform division and handle division by zero.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        float: Division result
        
    Raises:
        ValueError: If attempting to divide by zero
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b