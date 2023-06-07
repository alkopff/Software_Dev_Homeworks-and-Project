main: main.cpp matvecops.cpp matvecops.hpp CGSolver.cpp CGSolver.hpp COO2CSR.cpp COO2CSR.hpp
	g++ -std=c++11 -Wall -Wextra -Wconversion -o main main.cpp CGSolver.cpp matvecops.cpp COO2CSR.cpp

.PHONY: clean
clean:
	$(RM) main main.o CGSolver.o matvecops.o COO2CSR.o