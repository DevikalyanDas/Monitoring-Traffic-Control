import matplotlib.pyplot as plt
import cv2
from glob import glob
import os
import shutil

inputPath = '/home/akshay/workspace/saarland/sem2/DS/Project/trafficnet_dataset_v1/train/accident'
outputPath = inputPath
sparseOutputPath = os.path.join(outputPath, 'sparse_traffic')
denseOutputPath = os.path.join(outputPath, 'dense_traffic')
emptyOutputPath = os.path.join(outputPath, 'empty_traffic')
if not os.path.isdir(sparseOutputPath):
    os.mkdir(sparseOutputPath)
if not os.path.isdir(denseOutputPath):
    os.mkdir(denseOutputPath)
if not os.path.isdir(emptyOutputPath):
    os.mkdir(emptyOutputPath)

images = sorted(glob(inputPath+ "/*.jpg"))

image_index = 0

while image_index < len(images):
    image_path = images[image_index]
    img = cv2.imread(image_path)
    cv2.imshow('img',img)
    k = cv2.waitKey(0)

    if k==27:    # Esc key to stop
        print("Program stopped by user.")
        break
    if k == ord('s'):
        print("ANNOTATION: sparse traffic image.")
        shutil.copy2(image_path, sparseOutputPath)
        image_index += 1
    if k == ord('d'):
        print("ANNOTATION: dense traffic image.")
        shutil.copy2(image_path, denseOutputPath)
        image_index += 1
    if k == ord('e'):
        print("ANNOTATION: empty traffic image.")
        shutil.copy2(image_path, emptyOutputPath)
        image_index += 1
    if k == ord('p'):
        print("Re-annotate previous image.")
        image_index -= 1
        #delete the previous annotation first
        last_img = images[image_index]
        last_img_name = os.path.basename(last_img)
        last_annotation_path = os.path.join(sparseOutputPath, last_img_name)
        if os.path.exists(last_annotation_path):
            os.remove(last_annotation_path)
        else:
            last_annotation_path = os.path.join(denseOutputPath, last_img_name)
            if os.path.exists(last_annotation_path):
                os.remove(last_annotation_path)
            else:
                print("Could not locate last file.") 
