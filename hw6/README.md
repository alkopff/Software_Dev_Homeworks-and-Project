# CME 211 - Homework 6

## Goal of the assignment
The goal of the assignment is to implement a code to blur an image with a chosen intensity of blurring and to compute the sharpness of an image. The main function blurs the stanford.jpg image and saves the successive blurred pictures in different files. It also prints the sharpness of each blurred picture.

## Description of the code
I decomposed my code in one main function that calls the methods of the image class defined in the image.cpp file. In this file, I defined my image class, built a constructor that loads the image and converts it to an boost array, and defined 4 methods.

### Convolution 
It computes the convolution of a kernel and an array. It will be used to blur the images. It could have been defined outside the image class since it takes two arrays and the kernel as arguments but I kept it in the image class.

### BoxBlur  
It blurs the image with a chosen intensity represented by the kernel_size argument by calling the convolution function and using a specific kernel. 

### Sharpness
It computes the sharpness of the image using the convolution function and a specific kernel and returns the sharpnes.

### Save
It converts a boost array into an image.


