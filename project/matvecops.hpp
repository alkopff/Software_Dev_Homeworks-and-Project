#ifndef MATVECOPS_HPP
#define MATVECOPS_HPP

#include <string>
#include <boost/multi_array.hpp>
#include <iostream>

 
/* Defining functions for usual operations on vectors and matrices: sum of two vectors, difference of two vectors, 
dot product of two vectors, scalar product, L2norm of a vector and matrix-vector product. 
These functions are called in the CGSolver.cpp file. */

std::vector<double> vec_sum(std::vector<double> &v1, std::vector<double> &v2);

std::vector<double> vec_diff(std::vector<double> &v1, std::vector<double> &v2);

double dot_prod(std::vector<double> &v1, std::vector<double> &v2);

std::vector<double> scalar_prod(std::vector<double> &v1, double &a);

double L2norm(std::vector<double> &v);


std::vector<double> matvecprod(std::vector<double> &values, std::vector<int> &rows, 
    std::vector<int> &cols, std::vector<double> &u);


# endif /* MATVECOPS HPP */
