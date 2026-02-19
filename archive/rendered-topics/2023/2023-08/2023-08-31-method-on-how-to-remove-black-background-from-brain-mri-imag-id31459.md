---
topic_id: 31459
title: "Method On How To Remove Black Background From Brain Mri Imag"
date: 2023-08-31
url: https://discourse.slicer.org/t/31459
---

# Method on how to remove black background from Brain MRI images

**Topic ID**: 31459
**Date**: 2023-08-31
**URL**: https://discourse.slicer.org/t/method-on-how-to-remove-black-background-from-brain-mri-images/31459

---

## Post #1 by @Alvi_Rahman (2023-08-31 06:57 UTC)

<p>My aim is to remove the black ground from each brain MRI slice. I want to achieve this using Python.</p>
<p>I have given my code below:</p>
<pre><code class="lang-auto">import os
import numpy as np
import SimpleITK as sitk
from PIL import Image
from skimage.measure import find_contours
from skimage.draw import polygon2mask
import cv2
import pydicom



# Input Folder

input_directory = r"/home/braillic/Braillic/Segmentation to remove black background/Otsu_Thresholding/Original Images/BRAINIX/Gardner_Paul_Raymond_Randsley/Head_Brain_Sth - MR20210802080844/t1_mprage_sag_p2_09__FA_12_brain_14"

#input_directory = r"X:\Braillic\Otsu_Thresholding\Original Images\CT2"

dicom_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory)]


# Output Folder where images will be saved

output_base_folder = r"/home/braillic/Braillic/Segmentation to remove black background/Otsu_Thresholding/Segmentated Images"
#output_base_folder = r"X:\Braillic\Otsu_Thresholding\Segmentated Images"

path_parts = input_directory.split(os.sep)
output_file_name =path_parts[-1]

output_folder = os.path.join(output_base_folder,output_file_name)


# Create folder if does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Read DICOM files
dicom_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory)]
dicom_files.sort()  # Ensure files are in the correct order

# Initialize an empty list to store the image data
img_list = []

# Read DICOM files
for file in dicom_files:
    try:
        ds = pydicom.dcmread(file)
        img = ds.pixel_array

        # Add each DICOM image to a list
        img_list.append(img)

    except Exception as error:
        print(f"An unexpected error happened: {error}")

# Stack all 2D images into a single 3D image
volume_img = np.stack(img_list)

# Normalize the Image
normalize = volume_img / np.iinfo(volume_img.dtype).max

# Transpose the 3D image for different planes
axial_img = np.transpose(normalize, (0, 1, 2))
sagittal_img = np.transpose(normalize, (2, 0, 1))
coronal_img = np.transpose(normalize, (2, 1, 0))

# Process slices and save them for each plane
for plane_name, plane_img in zip(['Axial', 'Sagittal', 'Coronal'], [axial_img, sagittal_img, coronal_img]):
    output_folder = os.path.join(output_folder, plane_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for i in range(plane_img.shape[0]):
        slice_img = plane_img[i, :, :]

        # Convert the normalized image to 8-bit
        slice_img_8bit = cv2.normalize(slice_img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

        # Apply Gaussian blur
        slice_img_blur = cv2.GaussianBlur(slice_img_8bit, (1, 1), 0)

        # Otsu's thresholding
        _, img_thresh = cv2.threshold(slice_img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Morphological operations
        kernel = np.ones((10, 10), np.uint8)
        img_open = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

        # Find largest contour
        contours, _ = cv2.findContours(img_open, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contours were found
        if contours:
            cnt = max(contours, key=cv2.contourArea)

            # Create mask
            mask = np.zeros_like(slice_img_8bit)
            cv2.drawContours(mask, [cnt], -1, (255), thickness=cv2.FILLED)

            # Convert mask to PIL Image for easier manipulation
            mask = Image.fromarray(mask)
            foreground = Image.new("RGBA", slice_img.shape, (0, 0, 0, 0))  # Create new blank (transparent) image
            image_pil = Image.fromarray(slice_img_8bit).convert("RGBA")  # Convert the normalized image to RGBA
            foreground.paste(image_pil, mask=mask)  # Paste in the segmented part using the mask

            # Save the segmented slice
            foreground.save(os.path.join(output_folder, f'{plane_name}_{i:03d}_segmented.png'))
        else:
            print(f"No contours found in slice {i} of {plane_name} plane.")

print("Processing done ....")
</code></pre>
<p>This code basically reads the dicom files, applies blurring, otsu thresholding and fill contours to generate masks and then just get the MRI image without the background.</p>
<p>I would like to know if I can achieve this using the ‘slicer’ module in python.</p>
<p>In addition, I would be grateful if anyone can suggest alternative methods to achieve my end goal.</p>
<p>Thank you.</p>

---

## Post #2 by @Alvi_Rahman (2025-08-06 06:22 UTC)

<p><a class="mention-group notify" href="/groups/moderators">@moderators</a><br>
Kindly remove the  above post.<br>
My team has asked me to remove it.</p>

---
