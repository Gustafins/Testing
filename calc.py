def add(x, y, z):
    """Add Function"""
    return x + y + z


def subtract(x, y, z):
    """Subtract Function"""
    return x - y - z


def multiply(x, y, z):
    """Multiply Function"""
    return x * y * z


def divide(x, y, z):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y / z