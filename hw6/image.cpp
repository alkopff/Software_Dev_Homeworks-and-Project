# include <boost/multi_array.hpp>
# include <string>
# include <iostream>

#include "image.hpp"
#include "hw6.hpp"



image::image(std::string file) {
this-> input_filename = file;
ReadGrayscaleJPEG(file, this->input);
this->output.resize(boost::extents[input.shape()[0]][input.shape()[1]]);
this-> output = this->input;
}


void image::Save(std::string file) {
    WriteGrayscaleJPEG(file, this->output);
}

void image::BoxBlur(int kernel_size) {
    boost::multi_array<float,2> kernel(boost::extents[kernel_size][kernel_size]);
    float val = 1.f/(((float)kernel_size)*((float)kernel_size));
    for (int i = 0 ; i < kernel_size ; i++) {
    for (int j = 0 ; j < kernel_size ; j++) {
            kernel[i][j] = val;}
    }
    image::Convolution(input,output, kernel);
}


void image::Convolution(boost::multi_array<unsigned char,2>& input,
    boost::multi_array<unsigned char,2>& output,
    boost::multi_array<float,2>& kernel) {

    int nrows_input=(int)input.shape()[0];
    int ncols_input=(int)input.shape()[1];
    int nrows_output=(int)output.shape()[0];
    int ncols_output=(int)output.shape()[1];
    int nrows_kernel=(int)kernel.shape()[0];  
    int ncols_kernel=(int)kernel.shape()[1];

    if(nrows_input!=nrows_output) {
        std::cerr << "ERROR: different sizes for the input and output images" << std::endl;
    }

    if(ncols_input!=ncols_output) {
        std::cerr << "ERROR: different sizes for the input and output images" << std::endl;
    }

    if (nrows_kernel!=ncols_kernel) {
        std::cerr <<"ERROR: kernel is not a square matrix" << std::endl;
        exit(1);
    }
    
    if (((nrows_kernel)/2) == 0) {
        std::cerr <<"ERROR: kernel size is even" << std::endl;
        exit(1);        
    }        
    int med=(int) (nrows_kernel-1)/2;
    for (int x = 0 ; x < nrows_input ; x++) {
        for (int y = 0 ; y < ncols_input ; y++) {
            float temp = 0.f;
            for (int i = -med ; i <= med ; i++) {
                int r = x+i;
                if (r < 0) r = 0;
                if (r >= (int)nrows_input) r = nrows_input-1;
                for (int j = -med ; j<= med ; j++) {
                    int c = y+j;
                    if (c < 0) c = 0;
                    if (c >= (int)ncols_input) c = ncols_input-1;
                    temp += (float)input[r][c]*kernel[i+med][j+med];}
                } 
            if (temp<0) {
                temp=0; }
            if (temp>255) {
                temp=255;
            }
            output[x][y] = (unsigned char)temp;
            
        }
    }
} 


int image::Sharpness() {
	boost::multi_array<float,2> kernel(boost::extents[3][3]);
	kernel[0][0] = 0;
	kernel[0][1] = 1;
	kernel[0][2] = 0;
	kernel[1][0] = 1;
	kernel[1][1] = -4;
	kernel[1][2] = 1;
	kernel[2][0] = 0;
	kernel[2][1] = 1;
	kernel[2][2] = 0;

	auto temp = this->output;

	image::Convolution(this->output, temp, kernel);
	int sharp = *std::max_element(temp.origin(), temp.origin() + temp.num_elements());

	return sharp;
}

             

            
        
    
    

