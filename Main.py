# coding: utf-8

# imports
import sys, os

import Variables as Var
from Models.Player import Player
from Models.ChessPiece import ChessPiece
from Models.Tower import Tower
from Models.Knight import Knight
from Models.Bishop import Bishop
from Models.King import King
from Models.Queen import Queen
from Models.Pawn import Pawn

# functions
def Main():
    """
        Main entry
    """

    # add players to collection
    Var.Players.append(Player("Guillaume", "\033[34m"))
    Var.Players.append(Player("Alex", "\033[31m", 8, -1))
    
    # # print players
    # print(Var.Players)
    # for MyPlayer in Var.Players:
    #     print(MyPlayer)
    #     print(MyPlayer.Name)

    # Pieces = []
    # print("\n\n")
    # MyTower = Tower(1, 1)
    # Pieces.append(Tower(1, 1))
    # print(f"{MyTower.Name} ({MyTower.Symbol}) - Y={MyTower.PosY}, X={MyTower.PosX}")
    # print("\n\n")
    # Pieces.append(Tower(1, 8))
    # for MyPiece in Pieces:
    #     print(f"{MyPiece.Name} ({MyPiece.Symbol}) - Y={MyPiece.PosY}, X={MyPiece.PosX}")

    print("\n\n")


    # add pieces to players
    for MyPlayer in Var.Players:
        Y = MyPlayer.LineStart
        MyPlayer.ChessPieces.extend((Tower(Y, 1), Tower(Y, 8)))
        MyPlayer.ChessPieces.extend((Knight(Y, 2), Knight(Y, 7)))
        MyPlayer.ChessPieces.extend((Bishop(Y, 3), Bishop(Y, 6)))
        MyPlayer.ChessPieces.append(King(Y, 4))
        MyPlayer.ChessPieces.append(Queen(Y, 5))
        for X in range(1, 9):
            MyPlayer.ChessPieces.append(Pawn(Y + MyPlayer.LineOffset, X))
  
    # print players with pieces
    for MyPlayer in Var.Players:
        print(MyPlayer)
        # print(MyPlayer.Name)
        for MyPiece in MyPlayer.ChessPieces:
            print(f"    {MyPiece.Name} ({MyPiece.Symbol}) - Position {MyPiece.PosY}, {MyPiece.PosX}")



def ClearConsole():
    """
        Clear the console depending on OS
    """
    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")


def DrawChessBoard(width, height, char, char_2 = " "):
    """
        Draw board
    """
    # for each even line
    for line in range(round(height / 2)):
        # print alternatively black and white square on even line
        print((char + char_2) * round(width / 2))
        # print alternatively white and black square on odd line
        print((char_2 + char) * round(width / 2))


def DrawPieces():
    """
        Draw pieces on chess board
    """
    # for each player
    for Player in Var.Players:
        # on defini la couleur du player
        color = Player.Color
        # for each piece
        for Piece in Player.ChessPieces:
            StringToPrint = (f"{Var.Position.replace('{Line}', str(Piece.PosX)).replace('{Column}', str(Piece.PosY))}{color}{Piece.Symbol}{Var.ColorReset}")
            print(StringToPrint, end="")



# code entry
if __name__ == "__main__":
    Main()
    input()    
    ClearConsole()
    DrawChessBoard(8, 8, "█")
    DrawPieces()
    input()    