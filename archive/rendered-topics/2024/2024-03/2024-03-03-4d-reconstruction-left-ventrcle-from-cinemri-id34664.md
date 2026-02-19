---
topic_id: 34664
title: "4D Reconstruction Left Ventrcle From Cinemri"
date: 2024-03-03
url: https://discourse.slicer.org/t/34664
---

# 4D reconstruction left ventrcle from cineMRI

**Topic ID**: 34664
**Date**: 2024-03-03
**URL**: https://discourse.slicer.org/t/4d-reconstruction-left-ventrcle-from-cinemri/34664

---

## Post #1 by @Antonio_Tirotta (2024-03-03 03:13 UTC)

<p>Good evening,<br>
I am trying to reconstruct a 4D view of a ventricle given some medicals cineMRI.<br>
The files are in a DICOM format.<br>
I have 14 different slices each one containing 30 frames but they are separated in 14 different groups (1 for each slice).<br>
My idea is to perform a segmentation for each time frame, but in order to do that, I need images to be grouped in space for each time instance. By the way, the files are grouped in time for each space location.<br>
Moreover, in a previous discussion, the different slices of a cineMRI were grouped all together in a unique file, while in my case they are not. Is it possible to group them? If so, how?</p>
<p>About the 4D reconstruction, I don’t know if there are more efficient method to perform the desired task. I am open to any suggestion.<br>
Thank you in advance for your time</p>

---

## Post #2 by @pieper (2024-03-05 23:51 UTC)

<p>You could look at <a href="https://github.com/Slicer/Slicer/blob/ea595e64de26fa455c7d2e02a5dfc071409d955a/Modules/Scripted/DICOMPlugins/DICOMImageSequencePlugin.py#L32-L214">the logic</a> of the loader and see how that maps to your data.  You can right-click in the dicom browser to look at the dicom headers for your data to see what tags are changing.</p>

---

## Post #3 by @Antonio_Tirotta (2024-03-06 10:33 UTC)

<p>Thank you very much for your help.<br>
There is a way to change how they are stored (I was thinking to take from each of the 14 slices the frame at the same time and collect them together in order to be able then, to do a reconstruction in space for each time instant)</p>

---

## Post #4 by @pieper (2024-03-06 13:05 UTC)

<p>There are many ways that dicom files may be organized so the slices form volumes and timepoints.  If your data doesn’t match the current heuristics you may need to either write a pydicom script like the dicom patcher module to set the headers according to the current heuristic or maybe tweak the sequence loader to recognize your data.</p>

---
