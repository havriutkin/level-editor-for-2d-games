import pygame

from StartMenu import StartMenu
from LevelEditor import LevelEditor
from Menu import Menu
from Plot import Plot
from Settings import Settings

def main():
    start_menu = StartMenu()
    start_menu.run()

if __name__ == '__main__':
    main()
