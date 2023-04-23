import pygame

from Settings import Settings

class Plot:
    def __init__(self, tiles, level_map, settings) -> None:
        # Load settings 
        self.settings = settings

        # Define size
        self.width = self.settings.plot_width
        self.height = self.settings.plot_height
        self.pos = self.settings.plot_pos

        # Create surface
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect()
        self.rect.move_ip(self.pos)

        # Scrolling params
        self.scroll_x = 0
        self.scroll_y = 0
        self.scroll_speed = 3
        self.scroll_up = False
        self.scroll_down = False
        self.scroll_left = False
        self.scroll_right = False

        # Tiles
        self.tiles = tiles
        if level_map == None:
            self.reset_level_matrix()
        else:
            self.level_matrix = level_map

    def reset_level_matrix(self):
        """Define empty level matrix"""
        width = self.width // self.settings.tile_size
        height = self.height // self.settings.tile_size

        self.level_matrix = [[0 for j in range(height)] for i in range(width)]

        # Fill level matrix with zeros
        for i in range(width):
            for j in range(height):
                self.level_matrix[i][j] = 0 

    def add_tile(self, pos, tile_number):
        """Adding tile to level map based on mouse position"""
        x, y = ((pos[0] + self.scroll_x) // self.settings.tile_size, 
                (pos[1] + self.scroll_y) // self.settings.tile_size)
        self.level_matrix[x][y] = tile_number

    def delete_tile(self, pos):
        """Delete tile from level map based on mouse position"""
        x, y = ((pos[0] + self.scroll_x) // self.settings.tile_size, 
                (pos[1] + self.scroll_y) // self.settings.tile_size)      
        self.level_matrix[x][y] = 0
        
    def draw_gird(self):
        """Draw grid"""
        for x in range(0, self.width, self.settings.tile_size):
            pygame.draw.line(self.surface, (128, 128, 128), (x, 0), (x, self.height))
        for y in range(0, self.height, self.settings.tile_size):
            pygame.draw.line(self.surface, (128, 128, 128), (0, y), (self.width, y))

    def draw_tiles(self):
        """Draw all tiles based on level map"""
        width = self.width // self.settings.tile_size
        height = self.height // self.settings.tile_size

        for i in range(width):
            for j in range(height):
                index = self.level_matrix[i][j]
                x = (i * self.settings.tile_size)
                y = (j * self.settings.tile_size)
                if index != 0:
                    self.surface.blit(self.tiles[index], (x , y))

    def get_scroll_rect(self):
        """Return visible part of plot"""
        scroll_rect = pygame.Rect(self.scroll_x, 
                                  self.scroll_y, 
                                  self.settings.visible_plot_width, 
                                  self.settings.visible_plot_height) 
        return scroll_rect

    def update(self):
        """Update plot position"""
        if self.scroll_up and self.scroll_y - self.scroll_speed >= 0:
            self.scroll_y -= self.scroll_speed

        if self.scroll_down and self.scroll_y + self.scroll_speed + self.settings.visible_plot_height <= self.height:
            self.scroll_y += self.scroll_speed

        if self.scroll_left and self.scroll_x - self.scroll_speed >= 0:
            self.scroll_x -= self.scroll_speed

        if self.scroll_right and self.scroll_x + self.scroll_speed + self.settings.visible_plot_width <= self.width / 2:
            self.scroll_x += self.scroll_speed

    def render(self):
        """Draw plot"""
        self.surface.fill((255, 255, 255))
        self.draw_tiles()
        self.draw_gird()
        