# Homework 5
## C++

### Description of the problem
Given a file containing the coordinates of the walls of a maze, 
we want to make an algorithm that finds the solution path to this maze 
and writes it to a solution file. We are using the right-hand method 
to find the path from the entrance to the exit.

### Description of my C++ mazesolver code
I have used a switch and each case represents each direction we can be facing 
while walking through the maze. 
For each direction, we first check if we can move to the right, 
then forward, then left, then backwards. 
We update our current position and the direction we are facing 
and we iterate until we haven't reached
the last row (the exit of the maze).
We write each position we walk through in the solution file.

### Description of my checksoln.py code
I put the maze and the solution file in np.arrays to facilitate the check. 
Then I first verify if the entry point is correct,
then if the exit point is correct,
then if we move one step at a time,
then if we don't go through a wall
and then if we stay in the boundaries of the maze.
The order is arbitrary and in case the solution is wrong for many reasons,
I decided to only print one of the reasons (first one that the program will detect)
We could have printed all the reasons by deleting the sys.exit(0) everywhere



