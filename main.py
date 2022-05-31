import tile
import numpy as np

def convert_letter_to_num(letter):
    """
    Convert the letter to a number coord.
    @param letter - the letter to be converted
    """
    letter = letter.lower()
    letter_dict = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    return letter_dict[letter]

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

    #add islands to the map
    infile = open(filename,"r")
    map_date = infile.readline() # read through header
    for line in infile:
        coords = line.split(",")
        col = convert_letter_to_num(coords[0])
        row = int(coords[1]) - 1
        name = coords[2]
        type = coords[3]
        sot_map[col][row] = tile.Tile(name,type,tile.choose_marker(type))

    
    print_map(sot_map)

    return sot_map

def print_map(map_to_print):
    print("  ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    count = 0
    for i in range(0,len(map_to_print)):
        new_row = ""
        count += 1
        if count <= 9:
            new_row = new_row + " " +str(count)
        else:
            new_row = new_row + str(count)
        for j in range(0,len(map_to_print[i])):
            new_row = new_row + map_to_print[i][j].get_marker()
        print(new_row) 
    return 0

def chart_course(sot_map,destination_list):
    instructions = ""
    instructions += "Start at " + str(destination_list[0]) + "."
    return instructions
def main():
    
    #generate the map representation
    filename = input("Please enter the name of the map file: ")
    sot_map = create_map(filename)
    destination = ""
    
    """
    #get the list of islands that need to be in the path
    destination_list = []
    first_island = True
    while destination != "E":
        if first_island == True:
            destination = input("Please enter the start of the path: ")
            first_island = False
        else:
            destination = input("Please enter the next island in the path or enter E if there are no more islands in the path: ")
        
        if destination != "E":
            destination_list.append(destination)
    
    #chart the course and return the results to the user
    if len(destination_list) > 0:
        course_instructions = chart_course(sot_map,destination_list)
    else:
        course_instructions = "No locations entered."
    
    print(course_instructions)
    """


main()

