import sys
import re

def Move(x, y, line, plateau, height, length):
    direction = plateau[x][y]
    for character in line:
        xMove = 0
        yMove = 0
        if character.lower() == "r":
            direction = (direction + 1) % 4
        elif character.lower() == "l":
            direction = (direction - 1) % 4
        else:
            if direction % 2 == 0:
                yMove = 1 if direction != 2 else -1
            else:
                xMove = 1 if direction != 3 else -1
            xTemp = x + xMove
            yTemp = y + yMove
            if ((xTemp >= 0 and xTemp + 1 <= length and yTemp >=0 
            	and yTemp + 1 <= height) and (plateau[xTemp][yTemp] == -1)):
                plateau[x][y] = -1
                x = xTemp
                y = yTemp
        plateau[x][y] = direction
    return([x, y], plateau)

def Eliminate_Moves(roverList, movementList, plateau, height, length):
    for i, coords in enumerate(roverList):
        if len(movementList) != 0:
            move_line = movementList.pop(0)
            newCoords, plateau = Move(coords[0], coords[1], move_line,
                                      plateau, height, length)
            roverList[i] = newCoords
        else:
            # Break out of the for loop when there's no more movement lines
            break
    return roverList, plateau

# Function to format the move command input by removing all illegal characters
def format_move_input(line):
    # Format the line with regex
    return(re.sub(r'[^MRL]+', '', line))

# Create a rover on the map and push it to the rover list to track
def createRover(x, y, direction, plateau, num_direction=-1):
    num_direction = 'nesw'.index(direction.lower())
    plateau[x][y] = num_direction
    return [x, y], plateau

def InputCommands(line, roverList, movementList, plateau, height, length):
    match = re.match(r'\d\s\d\s[NnEeSsWw]', line)
    if bool(match) and len(line) == 5:
        split = match.group(0).split(" ")
        if(int(split[0]) >= 0 and int(split[0]) <= length and
           int(split[1]) >= 0 and int(split[1]) <= height):
            coords, plateau = createRover(int(split[0]), int(split[1]),
                                          split[2], plateau)
            roverList.append(coords)
    else:
        movementList.append(format_move_input(line))
    return roverList, movementList

# Function used to initalise the size of the plateau
def initPlateau(line):
    match = re.match(r'\d\s\d', line)
    if not bool(match) or len(line) != 3:
        print_command_help()
    split = match.group(0).split(" ")
    length = int(split[0]) + 1
    height = int(split[1]) + 1
    return [[-1 for x in range(length)] for y in range(height)], height, length

def main(args, test=0):
    if len(args) != 2:
        print_runtime_help()
    with open(args[1], 'r') as file:
        roverList = list()
        movementList = list()
        lines = file.readlines()
        if len(lines) == 0:
            print_file_error()
        plateau, height, length = initPlateau(lines[0].replace("\n", ""))
        for line in lines[1:]:
            roverList, movementList = InputCommands(
                line.replace("\n", ""), roverList, 
                movementList, plateau, height,
                length)
        if len(roverList) == 0:
            print("There are no rovers on the plateau")
            sys.exit(0)
        finRoverList, plateau = Eliminate_Moves(
            roverList, movementList, plateau, 
            height, length)
        results = print_results(finRoverList, plateau)
        if test == 1:
            return results
        else:
            print(results)

def print_results(finRoverList, plateau, result=None):
    for roverCoords in finRoverList:
        if result is not None:
            result += "\n"
        else:
            result = ""
        x = roverCoords[0]
        y = roverCoords[1]
        direction = "NESW"[plateau[x][y]]
        result += '%d %d %s' % (x,y,direction)
    return result

def print_runtime_help():
    print("Run this python file with text file input as the single argument")
    print("python3 MarsRover.py ./dir/to/textfile\nUtilisation of commands:\n")
    print_command_help()

def print_command_help():
    print("Setting map size requires two digits split by a space. \nMap sizing must be the first input in the textfile")
    print("New rover creation input should contain two digits split by a space followed with 'Compass Direction'. e.g. 5 5 N")
    print("Movement input should follow single line/string of commands. R = Turn Right L = Turn Left and M = move")
    print("e.g. LMLMLMLMRMRMM")
    sys.exit(0)

def print_file_error():
    print("Input file is empty\n")
    print_runtime_help()

if __name__ == "__main__":
    main(sys.argv)