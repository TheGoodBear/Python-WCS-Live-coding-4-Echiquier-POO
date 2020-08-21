# coding: utf-8

# imports
from Models.ChessPiece import ChessPiece

# model
class Tower(ChessPiece):
    """
        Tower model (inherits from ChessPiece)
    """

    def __init__(self,
        PosX,
        PosY):
        """
            Constructor
        """

        MovementX = "n"
        MovementY = "n"

        super().__init__("Tower", "T", PosY, PosX)

