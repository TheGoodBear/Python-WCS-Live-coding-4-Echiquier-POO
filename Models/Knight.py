# coding: utf-8

# imports
from Models.ChessPiece import ChessPiece

# model
class Knight(ChessPiece):
    """
        Knight model (inherits from ChessPiece)
    """

    def __init__(self,
        PosX,
        PosY):
        """
            Constructor
        """

        MovementX = "n"
        MovementY = "n"

        super().__init__("Knight", "N", PosY, PosX)

