# coding: utf-8

class ChessPiece():
    """
        Chess piece model
    """

    def __init__(self,
        Name,
        Symbol,
        PosY,
        PosX):
        """
            Constructor
        """
        super().__init__()

        self.Name = Name
        self.Symbol = Symbol
        self.PosX = PosX
        self.PosY = PosY
        self.Movements = None


    def Move():
        """
            Move the piece
        """
        pass