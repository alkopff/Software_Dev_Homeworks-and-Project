import sys
import numpy as np
from scipy.sparse import csr_matrix

if len(sys.argv) < 3:
    print('Usage:')
    print('  python3 {} <maze file> <solution file>'.format(sys.argv[0]))
    sys.exit(0)

maze_file=sys.argv[1]
solution_file=sys.argv[2]

data = np.loadtxt(maze_file, dtype=np.int16)
maze_shape=data[0,:]
maze = csr_matrix((np.ones(data[1:,:].shape[0], dtype=np.int8), (data[1:,0], data[1:,1])), shape=maze_shape, dtype=np.int8)
solution = np.loadtxt(solution_file, dtype=np.int16)


if solution[0,0]!=0:
    print("Solution is not valid: wrong entrance point")
    sys.exit(0)

if solution[-1,0]!=maze_shape[0]-1:
    print("Solution is not valid: wrong exit point")
    sys.exit(0)


for i,not_used_variable in enumerate(solution[:-1,:]):
	if np.linalg.norm(solution[i,:]-solution[i+1,:]) != 1:
		print("Solution is not valid : moving more than one step at a time")
		sys.exit(0)
	if maze[tuple(solution[i,:])] == 1:
		print("Solution is not valid: going through a wall")
		sys.exit(0)


for j in range(maze_shape[1]):
    if solution[i,:][0]<0 or solution[i,:][0]>maze_shape[0]-1:
        print("Solution is not valid: row index is out of bounds")
        sys.exit(0)
    if solution[i,:][1]<0 or solution[i,:][1]>maze_shape[0]-1:
        print("Solution is not valid: column index is out of bounds")
        sys.exit(0)


print("Solution is valid :-) ")
            
    

    