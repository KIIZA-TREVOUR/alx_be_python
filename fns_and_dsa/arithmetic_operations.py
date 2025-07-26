def perfom_operation(num1,num2, operation):
    """
    Perform arithmetic operations on two numbers.

    Parameters:
    num1 (int, float): The first number.
    num2 (int, float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    int, float: The result of the arithmetic operation.
    
    Raises:
    ValueError: If the operation is not recognized.
    ZeroDivisionError: If division by zero is attempted.
    """
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Operation not recognized. Use 'add', 'subtract', 'multiply', or 'divide'.")