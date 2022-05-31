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
    
def choose_marker(type_of_island):
    """
    Return the appropriate marker based on the type of island
    @param type_of_island - the type of island 
    """
    type_of_island = type_of_island.lower()
    if type_of_island == "fort":
        return "F"
    elif type_of_island == "fortress":
        return "f"
    elif type_of_island == "shrine":
        return "S"
    elif type_of_island == "outpost":
        return "O"
    elif type_of_island == "tradepost":
        return "T"
    else:
        return "I"
