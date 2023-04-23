class Settings:
    """Class for global constants"""
    def __init__(self, settings_dict) -> None:
        if settings_dict == None:
            self.tile_size = 32
            self.amount_of_tiles = 40

            self.screen_width = self.tile_size * 38
            self.screen_height = self.tile_size * 25
            
            self.plot_width = self.tile_size * 38
            self.plot_height = self.tile_size * 25
            self.visible_plot_width = self.tile_size * 35
            self.visible_plot_height = self.screen_height
            self.plot_pos = (0, 0)

            self.menu_width = self.tile_size * 3
            self.menu_height = self.tile_size * self.amount_of_tiles * 3
            self.visible_menu_width = self.tile_size * 3
            self.visible_menu_height = self.tile_size * 35
            self.menu_pos = (self.visible_plot_width, 0)

            self.path_to_tiles = "/Users/piton/Desktop/Karazin University/Java/Platform Game/JavaPlatformer/res/Egypt/tileset/craftpix-891121-free-2d-rpg-desert-tileset/PNG/"
        else:
            self.tile_size = settings_dict["tile_size"]
            self.amount_of_tiles = settings_dict["amount_of_tiles"]

            self.screen_width = settings_dict["screen_width"]
            self.screen_height = settings_dict["screen_height"]
            
            self.plot_width = settings_dict["plot_width"]
            self.plot_height = settings_dict["plot_height"]
            self.visible_plot_width = settings_dict["visible_plot_width"]
            self.visible_plot_height = settings_dict["visible_plot_height"]
            self.plot_pos = settings_dict["plot_pos"]

            self.menu_width = settings_dict["menu_width"]
            self.menu_height = settings_dict["menu_height"]
            self.visible_menu_width = settings_dict["visible_menu_width"]
            self.visible_menu_height = settings_dict["visible_menu_height"]
            self.menu_pos = settings_dict["menu_pos"]

            self.path_to_tiles = settings_dict["path_to_tiles"]

    def set_amount_of_tiles(self, amount):
        self.amount_of_tiles = amount
        self.menu_height = self.tile_size * self.amount_of_tiles * 3

    def to_dict(self):
        return {
            "tile_size": self.tile_size,
            "amount_of_tiles": self.amount_of_tiles,
            "screen_width": self.screen_width,
            "screen_height":  self.screen_height,
            "plot_width": self.plot_width,
            "plot_height": self.plot_height,
            "visible_plot_width": self.visible_plot_width,
            "visible_plot_height": self.visible_plot_height,
            "plot_pos": self.plot_pos,
            "menu_width": self.menu_width,
            "menu_height": self.menu_height,
            "visible_menu_width": self.visible_menu_width,
            "visible_menu_height": self.visible_menu_height,
            "menu_pos": self.menu_pos,
            "path_to_tiles": self.path_to_tiles,
        }

        