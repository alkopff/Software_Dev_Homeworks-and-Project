#include <iostream>
#include <fstream>
#include <string>

enum direction {
    right,
    left,
    down,
    up
};

int main (int argc, char *argv[]) {

	if (argc < 3) {
		std::cout << "Usage:" << std::endl;
		std::cout << "  " << argv[0] << " <maze file> <solution file>" << std::endl;
		return 0;
	}


	std::string maze_str = argv[1];
	std::string solution_str = argv[2];
    

    // create a static array with size the maximum of the maze sizes and initalizing all the values to 0
    int maze[201][201] = {{0}};

    std::ifstream maze_file(maze_str);
    int nrows=0;
    int ncols = 0;
    if (maze_file.is_open()){
        maze_file >> nrows >> ncols;
        int x, y;
        while (maze_file >> x >> y) {
            maze[x][y]=1;

        }
    }

    int entry=0;
    while (maze[0][entry]==1) {
        entry++;
        break;
    }

    std::ofstream sol_file(solution_str);
	if (sol_file.is_open()) {
        sol_file << 0 << " " << entry << std::endl;
    };

    direction dir=down;
    int pos_i=0;
    int pos_j=entry;
    
    while (pos_i<nrows-1){
        switch (dir) {
            case down:
            if (maze[pos_i][pos_j-1]==0) {
                pos_j=pos_j-1;
                dir=left;
                break;
            }
            else if (maze[pos_i+1][pos_j]==0) {
                pos_i++;
                dir=down;
                break;
            }
            else if (maze[pos_i][pos_j+1]==0) {
                pos_j++;
                dir=right;
                break;
            }
            else if (maze[pos_i-1][pos_j]==0) {
                pos_i=pos_i-1;
                dir=up;
                break;
            }
            case left:
            if (maze[pos_i-1][pos_j]==0) {
                pos_i--;
                dir=up;
                break;
            }
            else if (maze[pos_i][pos_j-1]==0) {
                pos_j--;
                dir=left;
                break;
            }
            else if (maze[pos_i+1][pos_j]==0) {
                pos_i++;
                dir=down;
                break;
            }
            else if (maze[pos_i][pos_j+1]==0) {
                pos_j++;
                dir=right;
                break;
            }
            case up:
            if (maze[pos_i][pos_j+1]==0) {
                pos_j=pos_j+1;
                dir=right;
                break;
            }
            else if (maze[pos_i-1][pos_j]==0) {
                pos_i=pos_i-1;
                dir=up;
                break;
            }
            else if (maze[pos_i][pos_j-1]==0) {
                pos_j=pos_j-1;
                dir=left;
                break;
            }
            else if (maze[pos_i+1][pos_j]==0) {
                pos_i=pos_i+1;
                dir=down;
                break;
            }
            case right:
            if (maze[pos_i+1][pos_j]==0) {
                pos_i=pos_i+1;
                dir=down;
                break;
            }
            else if (maze[pos_i][pos_j+1]==0) {
                pos_j++;
                dir=right;
                break;
            }
            else if (maze[pos_i-1][pos_j]==0) {
                pos_i=pos_i-1;
                dir=up;
                break;
            }
            else if (maze[pos_i][pos_j-1]==0) {
                pos_j=pos_j-1;
                dir=left;
                break;
            }
        }
    sol_file << pos_i << " " << pos_j << std::endl;
        
    }
    sol_file.close();
    return 0;
}
