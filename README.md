# MarsRover Challenge
Link: https://code.google.com/archive/p/marsrovertechchallenge/

# How to run:

Build an input file with any scenario you want - such as multiple rovers with plentiful moves.

A common input file may be found under /src, named input. 

To build your own, 
follow the given format:

"5 5" to give your plateau a size, in which rover's may travel on

"3 3 N" to create a rover at 3,3 facing North

"MMLMLMRMMRRL" and any movement you would like to give it.


Input of rovers and movement can be staggered, oh ever plateau input size needs to lead and follow the 2 digit format.

To run the MarsRover code:

python3 path/to/MarsRover.py path/to/inputfile

To run unit test file:

Be in the directory of the src folder

python3 -m unittest test__MarsRover.py 


