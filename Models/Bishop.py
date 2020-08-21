# coding: utf-8

# imports
from Models.ChessPiece import ChessPiece

# model
class Bishop(ChessPiece):
    """
        Bishop model (inherits from ChessPiece)
    """

    def __init__(self,
        PosX,
        PosY):
        """
            Constructor
        """

        MovementX = "n"
        MovementY = "n"

        super().__init__("Bishop", "B", PosY, PosX)

