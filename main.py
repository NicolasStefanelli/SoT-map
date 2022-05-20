import tile

def convert_letter_to_num(letter):
    """
    Convert the letter to a number coord.
    @param letter - the letter to be converted
    """
    letter = letter.lower()
    letter_dict = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    return letter_dict[letter]

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
    else:
        return "I"


def create_map(filename):
    """
    Generates a representation of the map of Sea of Thieves based off the provided text file. More info on how this text file needs to be structured is contained in the README.
    @param filename - the name of the text file
    """
    
    #create map
    sot_map = []
    water_tile = tile.Tile()
    blank_row = [water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,water_tile,]
    for i in range(0,26,1):
        sot_map.append(blank_row)
        print(i)

    #add islands to the map
    infile = open(filename,"r")
    for line in infile:
        coords = line.split(",")
        col = convert_letter_to_num(coords[0])
        row = int(coords[1])
        name = coords[2]
        type = coords[3]
        sot_map[col][row] = tile.Tile(name,type,choose_marker(type))

    return sot_map

def main():
    filename = input("Please enter the name of the map file: ")
    sot_map = create_map(filename)

