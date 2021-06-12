# SAMSUNG - 360tools - Helper

### This is helper code of [SAMSUNG 360tools](https://github.com/Samsung/360tools).


# Description

### Below are the steps that had been done on an image in this project :

## Projection

1. Input Image ERP image in JPG format

2. Convert ERP image in JPG format to ERP in YUV format

3. Use Samsung360 to convert ERP in YUV format to CMP in YUV format

4. Convert CMP image in YUV format to CMP in JPG format

## Splitting

1. Take input CMP image in JPG format (found from above point 4)

2. Divide the CMP image in JPG format into 6 patches as individual 2D images in JPG format.

## Joining

1. Take input all the 6 images obtained from above.

2. Combine the input 6 images into one CMP image (as same Projection, point 4 above). This would be in JPG.

## Back-Propagation

1. Convert the above CMP image in JPG format to YUV format

2. Use Samsung360 to convert CMP in YUV format to ERP in YUV format

3. Convert the above ERP image in YUV format to JPG format. This image should be the same as the image which was taken as input in Projection: step 1 (top).


### Before going to setup of this project make sure you have setup the [SAMSUNG 360tools](https://github.com/Samsung/360tools) if not proceed with the link and setup. 


# Setup

### **Python** is required for this project. if your system doesn't have python, install it from [here](https://www.python.org/)

After Executing make command __bin__ directory had been genrated in the root directory of that project. In that directory put this 2 things.
* `images` (Directory)
* `code.py` (File)

then open terminal/power-shell/cmd in the bin directory and run following command to install requirements:

* Windows

> pip install -r requirements.txt

* Linux

> pip3 install -r requirements.txt


After this you have to put all jpg images to images directory and run the python code with following command: 

* Windows

> python `code.py`

* Linux

> python3 `code.py`

After processing has been done, you will see two directory will genrated named as Forward and Backward in **bin** directory which will contain all diffrent types of images.


# Thanks For Your Time
