import sys
import re

valid_chars = "0123456789MRLNWSE"
#List of movements
movementList = list()
#Where we can find the rovers
roverList = list()
finRoverList = list()

platue = None

def moveRover(line):

#Function used to initalise the size of the platue
def initPlatue(line):
	match = re.search(r'\d\s\d', line)
	if bool(match) == False or len(line) != 4: print_command_help() 
	split = match.group(0).split(" ") 
	return [[-1 for x in range(int(split[0]))] for y in range(int(split[1]))]


def createRover(x, y, dir):


def stackCommands(line):


def main():
	if len(sys.argv) != 2:
		print_runtime_help()
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
		platue = initPlatue(lines[0])
		for line in lines[1:]:
			stackCommands(line)

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