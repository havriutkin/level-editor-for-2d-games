import sys
import pygame

from Settings import Settings
from LevelEditor import LevelEditor
from DataHandler import DataHandler

class StartMenu:
    def __init__(self) -> None:
        # Init pygame
        pygame.init()

        # Init screen
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.font = pygame.font.SysFont(None, 48)

        # Define menu text buttons
        self.option1 = self.font.render("Create new empty level", True, (255, 255, 255))
        self.option2 = self.font.render("Load existing level", True, (255, 255, 255))
        self.option3 = self.font.render("Exit", True, (255, 255, 255))

        self.option1_pos = (self.SCREEN_WIDTH // 2 - self.option1.get_width() // 2, 200)
        self.option2_pos = (self.SCREEN_WIDTH // 2 - self.option2.get_width() // 2, 300)
        self.option3_pos = (self.SCREEN_WIDTH // 2 - self.option3.get_width() // 2, 400)

        self.option1_rect = self.option1.get_rect()
        self.option1_rect.move_ip(self.option1_pos)
        self.option2_rect = self.option2.get_rect()
        self.option2_rect.move_ip(self.option2_pos)
        self.option3_rect = self.option3.get_rect()
        self.option3_rect.move_ip(self.option3_pos)

    def _handle_event(self, event):
        """Handle event"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.option1_rect.collidepoint(mouse_pos):
                pygame.quit()
                editor = LevelEditor(None, None)
                editor.run()
            elif self.option2_rect.collidepoint(mouse_pos):
                data_handler = DataHandler()
                settings, level_map = data_handler.load_level("Levels/level1.json")
                editor = LevelEditor(settings, level_map)
                editor.run()
            elif self.option3_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    def _render(self):
        """Draw everything"""
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.option1, self.option1_pos)
        self.screen.blit(self.option2, self.option2_pos)
        self.screen.blit(self.option3, self.option3_pos)
        pygame.display.flip()

    def run(self):
        """Menu loop"""
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    self._handle_event(event)
            
            # Draw menu
            self._render()

            




