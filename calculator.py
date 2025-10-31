# Стало
def calculate(a, b, operation):
    """Выполняет арифметическую операцию над двумя числами."""
    operations = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y if y != 0 else 0,
    }
    return operations.get(operation, lambda *_: None)(a, b)
