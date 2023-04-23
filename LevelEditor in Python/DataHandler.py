import json

from Settings import Settings

class DataHandler:
    def __init__(self) -> None:
        pass

    def save_map(self, level_map):
        path = "Maps/map1.json"
        with open(path, 'w') as file:
            json.dump(level_map, file)

    def save_level(self, level_map, settings):
        path = "Levels/level1.json"
        data = {"level_matrix": level_map, 
                "settings": settings.to_dict()}
        with open(path, 'w') as file:
            json.dump(data, file)

    def load_level(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
            level_map = data["level_matrix"]
            settings = Settings(data["settings"])
            return (settings, level_map)
        
        
