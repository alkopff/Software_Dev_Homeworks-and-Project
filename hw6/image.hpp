#ifndef IMAGE_HPP
#define IMAGE_HPP

# include <string>
#include <boost/multi_array.hpp>


class image {


    boost::multi_array<unsigned char, 2> input;
    boost::multi_array<unsigned char, 2> output;
    std::string input_filename;

    public:
    /* constructor of the image class that reads the image and converts it to a boost array*/
    image(std::string input_filename);

    /* blurs the image using the Convolution method. 
    The kernel size argument defines how blurry the ouptut picture will be. */
	void BoxBlur(int kernel_size);

    /*returns the sharpness of the image, using the Convolution method and a specific kernel*/
	int Sharpness();

    /*computes the convolution of a kernel and a matrix and puts the result in an output boost array*/
    void Convolution(boost::multi_array<unsigned char,2>& input,
    boost::multi_array<unsigned char,2>& output,
    boost::multi_array<float,2>& kernel);

    /*converts a boost array into an image and saves it in a file*/
    void Save(std:: string file);

};


# endif /* IMAGE_ HPP */