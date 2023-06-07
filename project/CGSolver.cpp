#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "matvecops.hpp"

using namespace std;

int CGSolver(std::vector<double> &val,
             std::vector<int>    &row_ptr,
             std::vector<int>    &col_idx,
             std::vector<double> &b,
             std::vector<double> &x,
             double              tol) {

    int n_iter_max = (int)x.size();

    std::vector<double> Au0 = matvecprod(val, row_ptr, col_idx, x);
    std::vector<double> r0 = vec_diff(b, Au0);

    double L2normr0 = L2norm(r0);
    std::vector<double> pn = r0;

    int n_iter = 0;

    while (n_iter <= n_iter_max) {
        n_iter++;

        std::vector<double> Apn = matvecprod(val, row_ptr, col_idx, pn);
        double alpha = dot_prod(r0, r0) / dot_prod(pn, Apn);

        std::vector<double> alpha_pn = scalar_prod(pn, alpha);
        std::vector<double> un = vec_sum(x, alpha_pn);

        std::vector<double> alpha_A_pn = scalar_prod(Apn, alpha);
        std::vector<double> r_update = vec_diff(r0, alpha_A_pn);

        double l2normr = L2norm(r_update);
        if ((l2normr / L2normr0) < tol) {
            
            x = un;
            return n_iter; // return n_iter
            std::cout << "SUCCESS: CG solver converged in " << n_iter << "iterations" << std::endl;
        }

        double beta_n = dot_prod(r_update, r_update) / dot_prod(r0, r0);

        std::vector<double> beta_n_pn = scalar_prod(pn, beta_n);
        std::vector<double> p_update = vec_sum(r_update, beta_n_pn);

        r0 = r_update;
        pn = p_update;
        x = un;
        }

    if (n_iter <= n_iter_max) return n_iter;
    else return -1;

}