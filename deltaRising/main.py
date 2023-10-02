import os, time, sys, pygame
from states.title import Title
from util.game import Game

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.gameLoop()
