"""Module A"""


class Animal:  # pylint: disable=too-few-public-methods
    """This is Animal class <3"""

    def __init__(self, color: int) -> None:
        """Animal init function

        Args:
            color (int): color parameter
        """
        self.color = color

    def change_colors(self, another_color: int) -> int:
        """Change color func
        Args:
            another_color (int): New color parameter

        Returns:
            int: Return changed color
        """

        self.color = another_color
        return self.color
