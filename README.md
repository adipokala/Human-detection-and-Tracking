# Human detection and Tracking

## Introduction
_In this project we have worked on the problem of human detection,face detection, face recognition and tracking an individual. Our project is capable of detecting a human and its face in a given video and storing Local Binary Pattern Histogram (LBPH) features of the detected faces. LBPH features are the key points extracted from an image which is used to recognize and categorize images. Once a human is detected in video, we have tracked that person assigning him a label. We have used the stored LBPH features of individuals to recognize them in any other videos. After scanning through various videos our program gives output like- person labeled as subject1 is seen in video taken by camera1, subject1 is seen in video by camera2. In this way we have tracked an individual by recognizing him/her in the video taken by multiple cameras. Our whole work is based on the application of machine learning and image processing with the help of [openCV](http://opencv.org)._**This code is built on opencv 3.1.1, python 3.4 and C++, other versions of opencv are NOT SUPPORTED.**
## Requirements
* **opencv [v3.1.1]**
	* **Installation in linux:**
			For complete installation of opencv in ubuntu you can refer [here](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/).
	* **Installation in windows**
			For complete installation of opencv in windows you can refer [here](https://putuyuwono.wordpress.com/2015/04/23/building-and-installing-opencv-3-0-on-windows-7-64-bit/)
* **python3**
	* In Ubuntu python 3.4 can be installed via terminal with the command given below:
		`sudo apt-get install python3`
* **python libraries:**
	Here is a list of all the python dependencies 
	* Python Image Library (PILLOW)
	* Imutils
	* numpy

* **C++**

## Approach
* The code follows the steps given below:
	1. First it reads a video and process each frame one by one.
	2. For each frame it tries to detect a human. If a human is detected it draws a rectangle around it.
	3. after completing step 2 it tries to detect human face.
	4. if a human face is detected it tries to recognize it with a pre-trained model file.
	5. If human face is recognized it puts the label on that human face else it moves to step 2 again for next frame 
* The repository is structured as follows:
	* `recognition/` : This directory contains face recognition algorithm and script to create model
	* `main.py` : This is the main python file that detects and recognizes humans.
	* `main.cpp` : This is the main C++ file that detects and recognizes humans.
	* `model.yaml` : This file contains trained model for given data. This trained model contains LBPH features of each and every face for given data.
	* `face_cascades/` : This directory contains sample data for testing our codes. This data is prepared by extracting face images of a praticular person from some videos.
	* `scripts/` : This directory contains some useful scripts that we used to work on different problems.
	* `video/` : This directory contains some of the videos that we used to while testing.

## Installation 

## Python
Don't forget to install the necessary libraries described in the install paragraph above.

First you need to run the encode script in recognition folder to create a model
* In the recognition folder run 
	* See README in recogniton folder for steps 
* To run the python version of the code you have to put all the input videos in one folder and then provide the path of that folder as command line argument:
```sh
python3 main.py -v /path/to/input/videos/  
```
Example- for our directory structure it is: 
```sh
 python3 main.py -v /video 
```

## C++ (Did not test)
* To compile the C++ version of the code with openCV the command is:
```sh
 g++ -ggdb `pkg-config --cflags opencv` -o `basename name_of_file.cpp .cpp` name_of_file.cpp `pkg-config --libs opencv` 
```
Example- for our directory structure it is: 
```sh
 g++ -ggdb `pkg-config --cflags opencv` -o `basename main.cpp .cpp` main.cpp `pkg-config --libs opencv` 
```  
* To run the C++ version of the code you have to put all the input videos in one folder and then provide the path of that video as command line argument:
```sh
./name_of_file /path/to/input/video_file 
```  
Example- for our directory structure it is: 
```sh
 ./main /video/2.mp4
```

## Performance of code
* Since this is a computer vision project it requires a lot of computation power and performance of the code is kind of an issue here.
* The code was tested on two different machines to analyse performace. The input was 30fps 720p video.
	* On a machine with AMD A4 dual-core processor we got an output of 4fps which is quite bad.
	* on a machine with Intel i5 quad-core processor we got an output of 12fps.
