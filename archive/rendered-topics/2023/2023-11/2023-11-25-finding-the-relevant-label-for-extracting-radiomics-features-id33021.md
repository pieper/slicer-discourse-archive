---
topic_id: 33021
title: "Finding The Relevant Label For Extracting Radiomics Features"
date: 2023-11-25
url: https://discourse.slicer.org/t/33021
---

# Finding the relevant label for extracting radiomics features

**Topic ID**: 33021
**Date**: 2023-11-25
**URL**: https://discourse.slicer.org/t/finding-the-relevant-label-for-extracting-radiomics-features/33021

---

## Post #1 by @Toni_Tannoury (2023-11-25 17:59 UTC)

<p>Hello , I am a software engineer working as a research fellow at an hospital in beirut where we started diving into radiomics. I am currently working on a script that extracts radiomic features from a folder containing multiple CT images for the patient and another file in RTSTRUCT for the contours . These images where downloaded from the cancer imaging archive.The issue i am facing is  that i am getting the below error  File “C:\Users\toni\AppData\Local\Programs\Python\Python310\lib\site-packages\radiomics\imageoperations.py”, line 51, in getMask<br>
raise ValueError(‘Label (%g) not present in mask. Choose from %s’ % (label, labels[labels != 0]))<br>
ValueError: Label (1) not present in mask. Choose from [         2          4          5          8          9         10<br>
11         13         14         16         17         18<br>
19         20         21         22         23         24<br>
25         26         27         28         29         30<br>
31         32         33         34         35         36<br>
4294967267 4294967268 4294967269 4294967270 4294967271 4294967272<br>
4294967273 4294967274 4294967275 4294967276 4294967277 4294967278<br>
4294967279 4294967280 4294967281 4294967282 4294967283 4294967284<br>
4294967285 4294967286 4294967287 4294967288 4294967292 4294967293] even tho I am only passing the contour for the tumor .I think the issue is not specifying the label in my main file here results = extractor.execute(image, mask ,return_labels=True).GetLabels() (Code will be provided at the end ) but i do not know how to choose the appropriate label.<br>
Help would be very much appreciated and a huge help for our radiomics studies.<br>
Thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Python Code :import os<br>
import matplotlib.pyplot as plt<br>
import numpy as np<br>
import SimpleITK as sitk<br>
import pydicom<br>
from radiomics import featureextractor</p>
<p>def load_dicom_series(directory):<br>
reader = sitk.ImageSeriesReader()<br>
dicom_names = reader.GetGDCMSeriesFileNames(directory)<br>
reader.SetFileNames(dicom_names)<br>
return reader.Execute()</p>
<p>def load_rtstruct(file_path):<br>
rtstruct = pydicom.read_file(file_path)<br>
return rtstruct</p>
<p>def extract_radiomic_features(image, mask):<br>
parameters =[<br>
25,<br>
[1, 1, 1]<br>
# Add any other parameters you want to customize<br>
]</p>
<pre><code>lsif = sitk.LabelStatisticsImageFilter()
extractor = featureextractor.RadiomicsFeatureExtractor(parameters)

results = extractor.execute(image, mask ,return_labels=True).GetLabels()
imageNode, maskNode = extractor.loadImage(image, mask)

lsif.Execute(imageNode, maskNode)
counter = 0
for result in results:
    counter +=1
    # if result == 0 :
    #     continue
    if counter != 3:
        continue
    boundingBox = np.array(lsif.GetBoundingBox(result))

    ndims = np.sum((boundingBox[1::2] - boundingBox[0::2] + 1) &gt; 1)
    if ndims &gt; 1 :
        results = extractor.execute(image, mask ,result)
        break
    raise Exception("No labels picked")
return results
</code></pre>
<p>def main():<br>
# Replace these paths with the actual paths to your DICOM and RTSTRUCT files<br>
dicom_directory = r’C:\Users\toni\Desktop\manifest-1700734196925\4D-Lung\115_HM10395\04-26-2000-NA-p4-06742\1.000000-P4P115S300I00007 Gated 30.0A-41594’<br>
file_path = os.path.join(<br>
“C:\Users\toni\Desktop\manifest-1700734196925\4D-Lung\115_HM10395\04-26-2000-NA-p4-06742\1.000000-P4P115S300I00007 Gated 30.0A-734.4\1-1.dcm”)<br>
rtstruct = pydicom.read_file(file_path)<br>
tumor_id = None<br>
contours_list = rtstruct.StructureSetROISequence._list</p>
<pre><code>for contour in contours_list:
    if "tumor" in contour.ROIName.casefold():
        tumor_id = contour.ROINumber
# Load DICOM series
image = load_dicom_series(dicom_directory)

# Load RTSTRUCT

# Assuming the RTSTRUCT refers to the first frame in the DICOM series
contours_list = rtstruct.ROIContourSequence._list
contour_sequence = list(filter(lambda element: element.ReferencedROINumber == tumor_id, contours_list))[
    0].ContourSequence
# print(rtstruct.ROIContourSequence[3])
# contour_sequence = rtstruct.ROIContourSequence[3].ContourSequence
num_slices = len(contour_sequence)
contour_data_reshaped = []

# Find the maximum number of elements in contour data
max_contour_elements = max(len(seq.ContourData) for seq in contour_sequence)

for i in range(num_slices):
    contour_data = contour_sequence[i].ContourData
    # Convert MultiValue to list and pad with zeros to make it consistent
    contour_data_list = list(contour_data) + [0.0] * (max_contour_elements - len(contour_data))
    contour_data_padded = np.array(contour_data_list).reshape((-1, 3))
    contour_data_reshaped.append(contour_data_padded)

# Convert the reshaped array to SimpleITK image
mask = sitk.GetImageFromArray(np.array(contour_data_reshaped))
mask.SetSpacing((1.0, 1.0, 1.0))

# Resample the mask to match the size of the original image
resampler = sitk.ResampleImageFilter()
resampler.SetSize(image.GetSize())
resampler.SetOutputSpacing(image.GetSpacing())
resampler.SetOutputOrigin(image.GetOrigin())
resampler.SetOutputDirection(image.GetDirection())
mask = resampler.Execute(mask)
# Extract radiomic features using the 3D mask
print(image.GetSize())
print(mask.GetSize())
features = extract_radiomic_features(image, mask)

# Print the extracted features
for key, value in features.items():
    print(f"{key}: {value}")
</code></pre>
<p>if <strong>name</strong> == “<strong>main</strong>”:<br>
main()</p>

---
