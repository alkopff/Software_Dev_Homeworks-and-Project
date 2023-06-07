#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
#include "matvecops.hpp"

using namespace std;

/* Defining functions for usual operations on vectors and matrices: sum of two vectors, difference of two vectors, 
dot product of 2 vectors, scalar product, L2norm of a vector and matrix-vector product  */

std::vector<double> vec_sum(std::vector<double> &v1, std::vector<double> &v2) {

    if(v1.size()!= v2.size()) {
        std::cerr<<"ERROR: can't sum two vectors with different sizes"<<std::endl;
    }

    std::vector<double> v3(v1.size());
    for(unsigned int i=0;i<v1.size(); i++) {
        v3[i]=v1[i]+v2[i];
    }
    return v3;
}

std::vector<double> vec_diff(std::vector<double> &v1, std::vector<double> &v2) {

    if(v1.size()!= v2.size()) {
        std::cerr<<"ERROR: can't diff two vectors with different sizes"<<std::endl;
    }

    std::vector<double> v3(v1.size());
    for(unsigned int i=0;i<v1.size(); i++) {
        v3[i]=v1[i]-v2[i];
    }
    return v3;
}


double dot_prod(std::vector<double> &v1, std::vector<double> &v2) {

    if(v1.size()!= v2.size()) {
        std::cerr<<"ERROR: can't compute the dot product of vectors with different sizes"<<std::endl;
    }
    double val=0;
    for(unsigned int i=0;i<v1.size(); i++) {
        val+=v1[i]*v2[i];
    }
    return val;
}

std::vector<double> scalar_prod(std::vector<double> &v1, double &a) {
    std::vector<double> v3(v1.size());
    for(unsigned int i=0;i<v1.size(); i++) {
        v3[i]=a*v1[i];
    }
    return v3;
}

double L2norm(std::vector<double> &v) {
    return std::sqrt(dot_prod(v,v));

}

std::vector<double> matvecprod(std::vector<double> &values,
    std::vector<int>    &rows,
    std::vector<int>    &cols,
    std::vector<double> &u) {

    std::vector<double> result;
    for (int i = 0; i < (int)rows.size()-1; i++) {
        double sum = 0.0;
        for (int j = (int)rows[i]; j < (int)rows[i+1]; j++) {
            sum += u[cols[j]] * values[j];
        }
        result.push_back(sum);
    }
    return result;
}