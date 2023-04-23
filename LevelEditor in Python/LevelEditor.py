import sys
import os

import pygame

from Menu import Menu
from Plot import Plot
from Settings import Settings
from PauseMenu import PauseMenu

class LevelEditor:
    def __init__(self, settings, level_map) -> None:
        # Load settings
        if settings == None:
            self.settings = Settings(None)
        else:
            self.settings = settings

        # Init pygame
        pygame.init()
        pygame.display.set_caption("Level Editor")

        # Load tiles
        self.load_tiles()

        # Set up screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.plot = Plot(self.tiles, level_map, self.settings)
        self.menu = Menu(self.tiles, self.settings)

    def load_tiles(self):
        """Load tiles"""
        self.tiles = {}
        index = 1
        for filename in os.listdir(self.settings.path_to_tiles):
            self.tiles[index] = pygame.image.load(os.path.join(self.settings.path_to_tiles, filename))
            self.tiles[index] = pygame.transform.scale(self.tiles[index], 
                                                       (self.settings.tile_size, self.settings.tile_size))
            index += 1
        self.settings.set_amount_of_tiles(len(self.tiles))

    def handle_event(self, event):
        """Handle given event"""
        if event.type == pygame.KEYDOWN:
            self._handle_keydown(event)
        elif event.type == pygame.KEYUP:
            self._handle_keyup(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self._handle_mousebuttonup(event)

    def _handle_keydown(self, event):
        """Handle keydown event"""
        if event.key == pygame.K_UP:
            if not self.menu.scroll_down:
                self.menu.scroll_up = True
        elif event.key == pygame.K_DOWN:
            if not self.menu.scroll_up:
                self.menu.scroll_down = True
        elif event.key == pygame.K_w:
            if not self.plot.scroll_down:
                self.plot.scroll_up = True
        elif event.key == pygame.K_s:
            if not self.plot.scroll_up:
                self.plot.scroll_down = True
        elif event.key == pygame.K_a:
            if not self.plot.scroll_right:
                self.plot.scroll_left = True
        elif event.key == pygame.K_d:
            if not self.plot.scroll_left:
                self.plot.scroll_right = True
        elif event.key == pygame.K_ESCAPE:
            pygame.time.wait(100)
            menu = PauseMenu(self.screen, self.plot.level_matrix, self.settings)
            menu.run()

    def _handle_keyup(self, event):
        """Handle keyup event"""
        if event.key == pygame.K_UP:
            self.menu.scroll_up = False
        elif event.key == pygame.K_DOWN:
            self.menu.scroll_down = False
        elif event.key == pygame.K_w:
            self.plot.scroll_up = False
        elif event.key == pygame.K_s:
            self.plot.scroll_down = False
        elif event.key == pygame.K_a:
            self.plot.scroll_left = False
        elif event.key == pygame.K_d:
            self.plot.scroll_right = False

    def _handle_mousebuttonup(self, event):
        """Handle mousebuttonup event"""
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Click was inside menu
        if self.menu.rect.collidepoint(mouse_pos):
            if event.button == 1:
                self.menu.set_active_tile(mouse_pos)
        # Click was inside plot
        elif self.plot.surface.get_rect().collidepoint(mouse_pos):
            if event.button == 1:
                self.plot.add_tile(mouse_pos, self.menu.active_tile)  # Add tile
            elif event.button == 3:
                self.plot.delete_tile(mouse_pos)  # Delete tile

    def update(self):
        """Update everything"""
        self.menu.update()
        self.plot.update()

    def render(self):
        """Draw everything"""
        self.plot.render()
        self.menu.render()
        
        self.screen.blit(self.plot.surface, self.plot.pos, area=self.plot.get_scroll_rect())
        self.screen.blit(self.menu.surface, self.menu.pos, area=self.menu.get_scroll_rect())

        pygame.display.flip()

    def run(self):
        """Main loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.handle_event(event)
            self.update()
            self.render()
            
        # Quit the app
        pygame.quit()