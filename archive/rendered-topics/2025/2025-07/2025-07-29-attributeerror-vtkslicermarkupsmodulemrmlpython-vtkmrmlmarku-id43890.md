---
topic_id: 43890
title: "Attributeerror Vtkslicermarkupsmodulemrmlpython Vtkmrmlmarku"
date: 2025-07-29
url: https://discourse.slicer.org/t/43890
---

# AttributeError: 'vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsClo' object has no attribute 'GetImageData'

**Topic ID**: 43890
**Date**: 2025-07-29
**URL**: https://discourse.slicer.org/t/attributeerror-vtkslicermarkupsmodulemrmlpython-vtkmrmlmarkupsclo-object-has-no-attribute-getimagedata/43890

---

## Post #1 by @Gruoss (2025-07-29 17:37 UTC)

<p>Hi, I’m new to Slicer (version 5.8.1 on Windows 11 Pro) and would like to calculate radiomics features from native 2D DICOM images. I’m trying this code in the Python-Slicer terminal:</p>
<p><em>import slicer<br>
import numpy as np<br>
import SimpleITK as sitk<br>
from radiomics import featureextractor<br>
def calculate_2d_radiomics(image_node, segmentation_node, label_value=1, force_2d=True, force_2d_dimension=0):<br>
extractor = featureextractor.RadiomicsFeatureExtractor()<br>
extractor.settings[‘label’] = label_value<br>
extractor.settings[‘force2D’] = force_2d<br>
extractor.settings[‘force2Ddimension’] = force_2d_dimension<br>
image_sitk = sitk.GetImageFromArray(slicer.util.arrayFromVolume(image_node))<br>
segmentation_sitk = sitk.GetImageFromArray(slicer.util.arrayFromVolume(segmentation_node))</em></p>
<p><em>segmentation_sitk = sitk.Cast(segmentation_sitk, sitk.sitkUInt8)<br>
try:<br>
results = extractor.execute(image_sitk, segmentation_sitk)<br>
return results<br>
except Exception as e:<br>
print(f"Error during feature extraction: {e}“)<br>
return None</em></p>
<p><em>image_node = slicer.util.getNode(“DCM_IMG”)<br>
segmentation_node = slicer.util.getNode(“SEG_IMG”)</em></p>
<p><em>if image_node and segmentation_node:<br>
radiomics_results = calculate_2d_radiomics(image_node, segmentation_node, label_value=1, force_2d=True, force_2d_dimension=0)<br>
if radiomics_results:<br>
for key, value in radiomics_results.items():<br>
if key.startswith(‘original’):<br>
print(f”{key}: {value}")<br>
else:<br>
print(“Error: Please load an image and segmentation with specified names.”)</em></p>
<p>I’m getting this error:</p>
<p><em>AttributeError: ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsClo’ object has no attribute ‘GetImageData’</em></p>
<p>I’ve also tried different ROI segmentations: “closed curve,” “ROI,” etc.</p>
<p>Do you have some suggestions?<br>
Thanks in advance for your help.</p>

---

## Post #2 by @cpinter (2025-07-31 12:28 UTC)

<p>What is happening is that your code is trying to call <code>GetImageData</code> on a node type that is not an image (a closed curve markups node).</p>
<p>You need to make sure you’re using the proper data types for your calculation. I’d suggest that you read on <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">segmentations in Slicer</a> a bit, because from your last sentence it seems that you are confusing various node types with segmentations.</p>
<p>Also next time please format the code you paste as code, because it is very hard to read Python code without indentation. Thanks!</p>

---

## Post #3 by @Gruoss (2025-08-01 09:20 UTC)

<p>Sorry, maybe I didn’t express myself clearly. I tried both the Segmentation and ROI tools. In the meantime, I’ve solved the problem. I get radiomic features from a 2D image (for example, just an MRI slide) but not from native 2D scintigraphy scans. The error is this:</p>
<p><em>ValueError: Image/Mask geometry mismatch. Potential fix: increase tolerance using geometryTolerance, see Documentation:Usage:Customizing the Extraction:Settings:geometryTolerance for more information</em></p>
<p>I read that this problem could be solved with “correctMask: True”,  but it doesn’t work for me.</p>
<p>Do you have any suggestions? Thanks a lot!</p>

---

## Post #4 by @cpinter (2025-08-05 11:32 UTC)

<p>This is a completely different problem, and not even in Slicer core, so please open a new topic for it.</p>
<p>Also please describe the solution you found for the original issue, so that others have the opportunity to learn from it.</p>
<p>Thank you!</p>

---
