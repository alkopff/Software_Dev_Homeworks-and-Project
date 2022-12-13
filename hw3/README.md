# CME 211 Homework 3

## Brief description of the program
The goal is to print a table with the lift coefficient
and the stagnation point of an airfoil, 
which data (geometry and pressure coef for different angles of attack) 
is described in a certain directory.

## Description of the class Airfoil
### Methods
For this, I created a class Airfoil in the file airfoil.py 
with repr method so that the print of an instance of the class Airfoil 
in the main.py program prints this table. 
The class is decomposed in 4 methods (+ the init one):
    -load_and_read_data
    -compute_foil_length
    -compute_cl
    -repr
They represent different steps that we needed to take before printing our table.

### Attributes
An instance of the class Airfoil has different attributes, created by calling the methods:
    -self.alpha_files
    -self.pressure_dic
    -self.coordinates
    -self.foil_length
    -self.cl_dict
    -self.stagnation_points
They all describe the data found in the input directory 
and are useful to create our table.

### Errors raised
The program is able to detect if the input directory does not contain
the files we need to print our table. Error raised if:
    -the directory has less 0 or 1 file (meaning we are missing 
    either the coordinates file or the pressure coef files)
    -the directory doesn't have a coordinates file for the geometry airfoil
    -the directory doesn't have any alpha files 
    -wrong format was detected in any of these files
