#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <boost/multi_array.hpp>

#include "image.hpp"
#include "hw6.hpp"


int main() {
	std::string inputname = "stanford.jpg";
    image myImage = image(inputname);
    std::cout << "Original Image: "<< myImage.Sharpness() << std::endl;
    
    int k_size = 3;
	while (k_size < 28) {
		image myImage = image(inputname);
		myImage.BoxBlur(k_size);
		std::cout << "BoxBlur(" << k_size << "): " << myImage.Sharpness() << std::endl;

		//syntax found on Stackoverflow
		std::ostringstream oss;
		oss << "BoxBlur" << k_size << ".jpeg";
		std::string var = oss.str();
		myImage.Save(var);
		k_size += 4;

	}
}