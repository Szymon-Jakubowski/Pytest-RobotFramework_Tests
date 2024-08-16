class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def __init__(self, initial_value: float = 0.0):
        """
        Initialize the calculator with an initial value.

        :param initial_value: The starting value of the calculator.
        """
        self.value = initial_value

    def add(self, number: float) -> float:
        """
        Add a number to the current value.

        :param number: The number to add.
        :return: The new current value.
        """
        self.value += number
        return self.value

    def subtract(self, number: float) -> float:
        """
        Subtract a number from the current value.

        :param number: The number to subtract.
        :return: The new current value.
        """
        self.value -= number
        return self.value

    def multiply(self, number: float) -> float:
        """
        Multiply the current value by a number.

        :param number: The number to multiply by.
        :return: The new current value.
        """
        self.value *= number
        return self.value

    def divide(self, number: float) -> float:
        """
        Divide the current value by a number.

        :param number: The number to divide by.
        :return: The new current value.
        :raises ValueError: If trying to divide by zero.
        """
        if number == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= number
        return self.value

    def get_value(self) -> float:
        """
        Get the current value of the calculator.

        :return: The current value.
        """
        return self.value

    def reset(self) -> None:
        """
        Reset the calculator value to zero.

        :return: None
        """
        self.value = 0.0