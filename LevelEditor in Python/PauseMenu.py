import sys
import pygame

from DataHandler import DataHandler

class PauseMenu:
    def __init__(self, screen, level_map, settings) -> None:
        # Get external screen
        self.screen = screen        
        
        # Get external data
        self.level_map = level_map
        self.settings = settings

        # Init menu surface
        self.SURFACE_WIDTH = 400
        self.SURFACE_HEIGHT = 400
        self.surface = pygame.Surface((400, 400))
        self.font = pygame.font.SysFont(None, 36)

        # Position relatively to main screen
        self.surface_position = (self.screen.get_width() // 2 - self.SURFACE_WIDTH // 2, 
                         self.screen.get_height() // 2 - self.SURFACE_HEIGHT // 2)

        # Define menu text buttons
        self.option1 = self.font.render("Save as lvl", True, (255, 255, 255))
        self.option2 = self.font.render("Save as map", True, (255, 255, 255))
        self.option3 = self.font.render("Exit (save as lvl)", True, (255, 255, 255))

        self.option1_pos = (self.SURFACE_WIDTH // 2 - self.option1.get_width() // 2, 100)
        self.option2_pos = (self.SURFACE_WIDTH // 2 - self.option2.get_width() // 2, 200)
        self.option3_pos = (self.SURFACE_WIDTH // 2 - self.option3.get_width() // 2, 300)

        self.option1_rect = self.option1.get_rect()
        self.option1_rect.move_ip((self.option1_pos[0] + self.surface_position[0],
                                    self.option1_pos[1] + self.surface_position[1]))
        self.option2_rect = self.option2.get_rect()
        self.option2_rect.move_ip((self.option2_pos[0] + self.surface_position[0],
                                    self.option2_pos[1] + self.surface_position[1]))
        self.option3_rect = self.option3.get_rect()
        self.option3_rect.move_ip((self.option3_pos[0] + self.surface_position[0],
                                    self.option3_pos[1] + self.surface_position[1]))

    def _handle_event(self, event):
        """Handle event"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.option1_rect.collidepoint(mouse_pos):
                data_handler = DataHandler()
                data_handler.save_level(self.level_map, self.settings)
            elif self.option2_rect.collidepoint(mouse_pos):
                data_handler = DataHandler()
                data_handler.save_map(self.level_map)
            elif self.option3_rect.collidepoint(mouse_pos):
                # Save and exit
                data_handler = DataHandler()
                data_handler.save_level(self.level_map, self.settings)
                pygame.quit()
                sys.exit()

    def _render(self):
        """Draw everything"""
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.option1, self.option1_pos)
        self.surface.blit(self.option2, self.option2_pos)
        self.surface.blit(self.option3, self.option3_pos)
        self.screen.blit(self.surface, self.surface_position)
        pygame.display.flip()

    def run(self):
        """Menu loop"""
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return # Resume
                else:
                    self._handle_event(event)

            # Draw menu
            self._render()
                        
