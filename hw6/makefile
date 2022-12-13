CXX := g++ -std=c++11
CXXFLAGS := -Wall -Wconversion -Wextra -Wpedantic
LDFLAGS := -ljpeg

main: main.cpp image.cpp hw6.cpp
	$(CXX) $(CXXFLAGS) -o main main.cpp image.cpp hw6.cpp -ljpeg

.PHONY: clean
clean:
	$(RM) main *.o