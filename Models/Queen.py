# coding: utf-8

# imports
from Models.ChessPiece import ChessPiece

# model
class Queen(ChessPiece):
    """
        Queen model (inherits from ChessPiece)
    """

    def __init__(self,
        PosX,
        PosY):
        """
            Constructor
        """

        MovementX = "n"
        MovementY = "n"

        super().__init__("Queen", "Q", PosY, PosX)

