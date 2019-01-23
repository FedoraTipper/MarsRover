import sys
import re

#List of movements
movementList = list()
#Where we can find the rovers
roverList = list()
finRoverList = list()


def Move(x, y, line):
	direction = plateau[x][y]
	for character in line:
		xMove = 0
		yMove = 0
		if character.lower() == "r": direction = (direction + 1) % 4
		elif character.lower() == "l": direction = (direction - 1) % 4
		else: 
			if direction % 2 == 0:
				yMove = 1 if direction != 2 else -1
			else:
				xMove = 1 if direction != 3 else -1
			xTemp = x + xMove
			yTemp = y + yMove
			if (xTemp >= 0 and xTemp <= length and yTemp >= 0 and yTemp <= height) and (plateau[xTemp][yTemp] == -1):
					plateau[x][y] = -1
					x = xTemp
					y = yTemp
		plateau[x][y] = direction
	finRoverList.append([x,y])

def Eliminate_Moves():
	for coords in roverList:
		if len(movementList) != 0: 
			move_line = movementList.pop(0)
			Move(coords[0], coords[1], move_line)


#Function to push all move input commands to a list
def push_to_moveList(line):
	#Format the line with regex
	sub_line = re.sub(r'[^MRL]+', '', line)
	movementList.append(sub_line)

#Create a rover on the map and push it to the rover list to track
def createRover(x, y, direction, num_direction = -1):
	if direction.lower() == "n":
		num_direction = 0
	elif direction.lower() == "e":
		num_direction = 1
	elif direction.lower() == "s":
		num_direction = 2
	else:
		num_direction = 3

	plateau[x][y] = num_direction
	roverList.append([x,y])

def InputCommands(line):
	match = re.match(r'\d\s\d\s[NnEeSsWw]', line)
	if bool(match) and len(line) == 6: 
		split = match.group(0).split(" ")
		createRover(int(split[0]),int(split[1]),split[2])
	else:
		push_to_moveList(line)

#Function used to initalise the size of the plateau
def initPlateau(line):
	match = re.match(r'\d\s\d', line)
	if bool(match) == False or len(line) != 4: print_command_help() 
	split = match.group(0).split(" ")
	global length, height
	length = int(split[0]) + 1
	height = int(split[1]) + 1
	return [[-1 for x in range(length)] for y in range(height)]

def main():
	if len(sys.argv) != 2:
		print_runtime_help()
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
		global plateau
		plateau = initPlateau(lines[0])
		for line in lines[1:]:
			InputCommands(line)
		Eliminate_Moves()
		print_results()


def print_results():
	for roverCoords in finRoverList:
		x = roverCoords[0]
		y = roverCoords[1]
		direction = ""
		if plateau[x][y] == 0:
			direction = " N"
		elif plateau[x][y] == 1:
			direction = " E"
		elif plateau[x][y] == 2:
			direction = " S"
		else:
			direction = " W"
		print(str(roverCoords[0]) + " " + str(roverCoords[1]) + direction)

def print_runtime_help():
	print("Run this python file with text file input as the single argument")
	print("python3 main.py ./dir/to/textfile")
	sys.exit(0)

def print_command_help():
	print("Setting map size requires two digits split by a space. Map sizing must be the first input")
	print("New rover creation input should follow two digits split by a space followed with 'Compass Direct'. e.g. 5 5 N")
	print("Movement input should follow single line of commands. R = Turn Right L = Turn Left and M = move")
	print("e.g. LMLMLMLMRMRMM")
	sys.exit(0)

if __name__ == "__main__":
	main()