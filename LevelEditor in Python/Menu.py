import pygame

from Settings import Settings

class Menu:
    def __init__(self, tiles, settings) -> None:
        # Load settings
        self.settings = settings

        # Define size
        self.width = self.settings.menu_width
        self.height = self.settings.menu_height
        self.pos = self.settings.menu_pos

        # Create surface
        self.surface = pygame.Surface((self.width, self.height))

        self.rect = self.surface.get_rect()
        self.rect.move_ip(self.pos)

        # Scrolling params
        self.scroll_y = 0
        self.scroll_speed = 5
        self.scroll_up = False
        self.scroll_down = False

        # Get tiles
        self.tiles = tiles
        self.active_tile = 1    # ID of active tile

    def get_scroll_rect(self):
        """Return visible part of menu"""
        scroll_rect = pygame.Rect(0, 
                                  self.scroll_y, 
                                  self.settings.visible_menu_width, 
                                  self.settings.visible_menu_height) 
        return scroll_rect

    def set_active_tile(self, pos):
        """Change active tile based on mouse position"""
        y = (pos[1] + self.scroll_y) / 2
        new_index = (y // self.settings.tile_size) + 1
        if new_index <= len(self.tiles):
            self.active_tile = new_index

    def draw_tiles(self):
        """Draw all tiles that was loaded"""
        tile_size = self.settings.tile_size

        # Draw the tiles
        for i in range(len(self.tiles)):
            tile = self.tiles[i + 1]

            self.surface.blit(tile, (tile_size, i*tile_size*2))

            if i + 1 == self.active_tile:
                rect = pygame.Rect(self.settings.tile_size, 
                                   i*self.settings.tile_size*2, 
                                   self.settings.tile_size, 
                                   self.settings.tile_size)
                pygame.draw.rect(self.surface, (255, 0, 0), rect, 1)        

    def update(self):
        """Update menu position"""
        if self.scroll_up and self.scroll_y - self.scroll_speed >= 0:
            self.scroll_y -= self.scroll_speed

        if self.scroll_down and self.scroll_y + self.scroll_speed <= self.height / 2:
            self.scroll_y += self.scroll_speed

    def render(self):
        """Draw menu"""
        self.surface.fill((255, 255, 255))
        self.draw_tiles()

