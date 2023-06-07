#include <iostream>
#include "matvecops.hpp"
#include <fstream>
#include "COO2CSR.hpp"
#include "CGSolver.hpp"


int main (int argc, char *argv[]) {

    if (argc < 3) {
    std::cout << "Usage:" << std::endl;
    std::cout << "  " << argv[0] << " <matrix_file> <solution file>" << std::endl;
    return 0;
    }
    
    std::string matrix_file=argv[1];
    std::string solution_file=argv[2];
    double tol=0.00001;

     /*reading the matrix file and creating the COO form of the matrix*/
    std::ifstream input_file(matrix_file);
   
    unsigned int n_rows, n_cols;
    std::vector<int> rows;
    std::vector<int> cols;
    std::vector<double> vals;

    input_file >> n_rows >> n_cols;

    std::vector <double> b(n_rows,0);
    std::vector <double> x(n_cols,1);
    
    unsigned int row, col;
    double val;
    while (input_file >> row >> col >> val) {
        rows.push_back(row);
        cols.push_back(col);
        vals.push_back(val);
    } 

    input_file.close();

    /*converting the matrix from COO to CSR*/
    COO2CSR(vals, rows, cols);
    
    /*running the CGSolver with our CSR matrix*/
    int n_iter=CGSolver(vals, rows, cols, b, x, tol);

	if (n_iter == -1) {
		std::cout << "Solution does not converge" << std::endl;
		return 0;}


    /*writing the solution x of the CGSolver to the solution file*/
    std::ofstream file_output(solution_file);
    for(unsigned int i=0; i<x.size(); i++) {
        file_output.setf(std::ios::scientific, std::ios::floatfield);
        file_output.precision(3);
        file_output << x[i] << std::endl;
    }
    std::cout << "SUCCESS: CG solver converged in " << n_iter << " iterations." << std::endl;
}




