# coding: utf-8

class Player():
    """
        Player model
    """

    def __init__(self,
        Name,
        Color,
        LineStart = 1,
        LineOffset = 1):
        """
            Constructor
        """
        super().__init__()
        
        # instance properties
        self.Name = Name
        self.Color = Color
        self.LineStart = LineStart
        self.LineOffset = LineOffset
        # collection of piece for this player
        self.ChessPieces = []

    
    def __str__(self):
        """
            Override the print method
        """
        return f"{self.Color}{self.Name}\033[0m"
