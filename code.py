import subprocess
import glob
import cv2
import numpy as np

# All Images Path
all_files_path = "./images/*.jpg"

# Taking all Images
files = glob.glob(all_files_path)

# Making Directories
subprocess.run(["mkdir", "Forward"])
subprocess.run(["mkdir", "Forward/YUV_ERP",
                "Forward/YUV_CMP", "Forward/CMP_Images", "Forward/Splited_Images"])

subprocess.run(["mkdir", "Backward"])
subprocess.run(["mkdir", "Backward/YUV_ERP",
                "Backward/YUV_CMP", "Backward/ERP_Images", "Backward/Joined_Images"])

# Processing Files
for aFile in files:

    file_name = aFile[9:-4]
    image = cv2.imread(aFile)

    yuv_erp_path = "./Forward/YUV_ERP/{}.yuv".format(file_name)

    # JPG to YUV
    # ERP FILE
    subprocess.run(
        ["ffmpeg", "-i", aFile, "-pix_fmt", "yuv420p", yuv_erp_path])

    yuv_cmp_path = "./Forward/YUV_CMP/{}.yuv".format(file_name)

    # Converting ERP(YUV) to CMP(YUV)
    subprocess.run(["./360tools_conv", "-i",
                    yuv_erp_path, "-w", str(image.shape[1]), "-h", str(image.shape[0]), "-x", "1", "-y", "1", "-l",  "4000", "-m", "3000", "-o", yuv_cmp_path, "-f", "3"])

    cmp_path = "./Forward/CMP_Images/{}.jpg".format(file_name)

    # CMP(YUV) to JPG
    # Containg 6 Patches
    subprocess.run(["ffmpeg", "-y", "-s", "4000x3000",
                   "-i", yuv_cmp_path, cmp_path])

    # Saving 6 Diffrent Patches
    cmp_read = cv2.imread(cmp_path)

    wi = [1000, 0, 1000, 2000, 3000, 1000]
    wj = [2000, 1000, 2000, 3000, 4000, 2000]

    hi = [0, 1000, 1000, 1000, 1000, 2000]
    hj = [1000, 2000, 2000, 2000, 2000, 3000]

    # Differentiating 6 Patches and Saving
    for j in range(1, 7):

        path = "./Forward/Splited_Images/{}".format(file_name)

        path += "_CMP_"
        path += str(j)
        path += ".jpg"

        img = cmp_read[hi[j - 1]: hj[j - 1], wi[j - 1]: wj[j - 1]]
        cv2.imwrite(path, img)


#
#
#   ---------------------------------------------------------------------
#                                  SECOUND PART
#   ---------------------------------------------------------------------
#

    split_image = "./Forward/Splited_Images/{}_CMP_".format(file_name)

    # Blank image with Dimension(4000, 3000)
    canvas = np.zeros((3000, 4000, 3), dtype="uint8")

    # Reading Splited images
    for j in range(1, 7):

        img = split_image + str(j) + ".jpg"

        imgr = cv2.imread(img)
        canvas[hi[j-1]:hj[j-1], wi[j-1]:wj[j-1]] = imgr

    join_img = "./Backward/Joined_Images/{}.jpg".format(file_name)

    # Saving after joining(CMP)
    cv2.imwrite(join_img, canvas)

    cmp_yuv = "./Backward/YUV_CMP/{}.yuv".format(file_name)

    # CMP(JPG) to CMP(YUV)
    subprocess.run(["ffmpeg", "-i", join_img, "-pix_fmt", "yuv420p", cmp_yuv])

    erp_yuv = "./Backward/YUV_ERP/{}.yuv".format(file_name)

    # CMP(YUV) to ERP(YUV)
    subprocess.run(["./360tools_conv", "-i",
                    cmp_yuv, "-w", "4000", "-h", "3000", "-x", "1", "-y", "1", "-l", str(image.shape[1]), "-m", str(image.shape[0]), "-o", erp_yuv, "-f", "4"])

    erp_path = "./Backward/ERP_Images/{}.jpg".format(file_name)
    Width = image.shape[1]
    Height = image.shape[0]

    Dimension = str(Width) + "x" + str(Height)

    # ERP(YUV) to ERP(JPG)
    subprocess.run(["ffmpeg", "-y", "-s", Dimension,
                   "-i", erp_yuv, erp_path])
