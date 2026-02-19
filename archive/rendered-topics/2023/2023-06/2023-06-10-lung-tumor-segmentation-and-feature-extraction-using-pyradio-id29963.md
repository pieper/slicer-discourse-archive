---
topic_id: 29963
title: "Lung Tumor Segmentation And Feature Extraction Using Pyradio"
date: 2023-06-10
url: https://discourse.slicer.org/t/29963
---

# Lung tumor segmentation and feature extraction using pyradiomics and python

**Topic ID**: 29963
**Date**: 2023-06-10
**URL**: https://discourse.slicer.org/t/lung-tumor-segmentation-and-feature-extraction-using-pyradiomics-and-python/29963

---

## Post #1 by @Ridwanur_Rahman (2023-06-10 15:16 UTC)

<p>Hello Altruists,</p>
<p>I’m doing a project on tumor segmentation of the lung. I’ve got only the Dicom images. My job is the find the ROI to segment only the tumor part and extract features using pyradiomics, later run ML model to determine stage, therapeutic success, and survival rate. But I’m having difficulties of how do I do the segmentation using code. I’ve found a thresholding technique to segment which I’m about to explore. If you have any helpful tips for doing this, would be really appreciated.</p>

---

## Post #2 by @rbumm (2023-06-10 17:47 UTC)

<p>Hi,</p>
<p>That sounds like an interesting project. Unfortunately, there is no established code-based technique that fits all needs of lung tumor segmentation in 3D Slicer yet. The situation is similar if you look at commercial solutions.</p>
<p>I am sure you have consulted ChatGPT.</p>
<ol>
<li>
<strong>Manual Segmentation</strong>: Manual segmentation allows you to draw the boundaries of the tumor slice by slice. This can be time-consuming and requires a high level of skill and knowledge, but it can yield accurate results, especially for small or irregularly shaped tumors.</li>
<li>
<strong>Threshold Segmentation</strong>: This is a basic form of automated segmentation. By setting a range of intensities (thresholds), all voxels with values within the specified range are assigned to the segmentation. This works well when the tumor has significantly different intensity values than the surrounding tissues.</li>
<li>
<strong>Region Growing Segmentation</strong>: In this method, you select a seed point within the tumor and the algorithm will include adjacent voxels that have similar intensities. This method can work well if the tumor has homogenous intensity.</li>
<li>
<strong>Semi-automatic Segmentation</strong>: 3D Slicer has a number of advanced semi-automatic segmentation methods available in the “Segment Editor” module, such as ‘Grow from Seeds’, ‘Watershed’, and ‘Fast Marching’. These methods allow you to provide some input (like seeds or markers), and then the algorithm will do the rest based on the rules of the method.</li>
<li>
<strong>Deep Learning-Based Segmentation</strong>: Recently, deep learning-based segmentation techniques have become increasingly popular. They have the potential to provide highly accurate segmentations with less user input. However, they require a large amount of annotated training data, and are more complex to set up. As of my (GPT)  knowledge cut-off in September 2021, such methods are not built into 3D Slicer, but could potentially be implemented through Python scripting or by using an external package.</li>
</ol>
<p>I can recommend “Local Threshold” as part of the “Segment Editor Extra Effects” package for tumor registration.</p>
<p>There is a lung tumor ct detection AI tool in NVIDIA´s <a href="https://monai.io/model-zoo.html">model zoo</a> that you could try out and train.</p>
<p>Or contact Johannes Hofmanninger from contextflow in Vienna, I know they work on a promising  AI tool for this purpose.</p>

---

## Post #3 by @Rabbito22 (2024-10-16 19:16 UTC)

<p>Hi <a class="mention" href="/u/ridwanur_rahman">@Ridwanur_Rahman</a> did u figure it out how to do caz I’m having a same project but due to the scarcity of previous works I’m not able to find any good approximate solution.</p>

---
