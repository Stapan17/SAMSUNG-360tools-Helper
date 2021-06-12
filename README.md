# SAMSUNG-360tools-Helper

### Below are the steps that have been done on one image:

## Projection:
1. Input Image ERP image in JPG format
2. Convert ERP image in JPG format to ERP in YUV format
3. Use Samsung360 to convert ERP in YUV format to CMP in YUV format
4. Convert CMP image in YUV format to CMP in JPG format

## SPLITTING:
1. Take input CMP image in JPG format (found from above point 4)
2. Divide the CMP image in JPG format into 6 patches as individual 2D images in JPG format.
 
## JOINING:
1. Take input all the 6 images obtained from above.
2. Combine the input 6 images into one CMP image (as same Projection, point 4 above). This would be in JPG.

## Back-propagation:
1. Convert the above CMP image in JPG format to YUV format
2. Use Samsung360 to convert CMP in YUV format to ERP in YUV format
3. Convert the above ERP image in YUV format to JPG format. This image should be the same as the image which was taken as input in Projection: step 1 (top).
