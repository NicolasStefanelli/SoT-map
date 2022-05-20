class Tile:

    def __init__(self,name="water",type="water",marker="."):
        self.name = name
        self.type = type
        self.marker = marker
    
    def get_marker(self):
        return self.marker
    
    def get_type(self):
        return self.type
    
    def get_name(self):
        return self.name
