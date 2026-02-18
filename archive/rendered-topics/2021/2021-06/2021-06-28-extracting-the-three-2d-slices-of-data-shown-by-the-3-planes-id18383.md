# Extracting the three 2d slices of data shown by the 3 planes defined in 3d Slicer

**Topic ID**: 18383
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/extracting-the-three-2d-slices-of-data-shown-by-the-3-planes-defined-in-3d-slicer/18383

---

## Post #1 by @elarson (2021-06-28 19:31 UTC)

<p>I can manipulate the 3 2d planes in 3d slicer and visualize the the planes of data I want to extract.  The data is 3d+t ultrasound data.  Ideally I would like to export the data as 2d ultrasound multi-frame data to 3 separate DICOM files.  Is there a way to do this within 3D Slicer GUI or with an extension (SlicerHeart perhaps)?</p>
<p>Simply put, I want to export the data I see presented on the screen for each plane without diving into python coding.  Am I missing something obvious?  If I have to use python then how would I get the data for each of the planes shown in 3D Slicer?</p>

---

## Post #2 by @lassoan (2021-06-29 00:08 UTC)

<p>If it is just for creating a list of images or video for a powerpoint presentation then you can use Screen Capture module for this.</p>
<p>If it is for exporting training data for deep learning or other analysis or processing then you need to somehow specify what you need. The easiest is to express this using Python scripting. For example, you can get access to the entire volume sequence as a 4D numpy array (see example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-voxels-of-a-4d-volume-as-a-single-numpy-array">here</a>) and then you can extract any data from it, any way you need.</p>

---

## Post #3 by @elarson (2021-06-29 13:59 UTC)

<p>I need the data for analysis purposes.</p>
<p>I have found an example of how to get the 4d array of data in python.</p>
<p>Now I want to extract the data as the axial, sagittal, and coronal slices defined by the user.  Since the 4d array isn’t aligned with the user defined slices/orientations, what python code would get me the interpolated data along the user defined slices?</p>

---

## Post #4 by @elarson (2021-06-29 18:05 UTC)

<p>More precisely, I want the “Reformat” view for the red, green, and yellow slices.</p>

---

## Post #5 by @lassoan (2021-06-30 01:43 UTC)

<p>Do you need this for data augmentation for deep learning?</p>

---

## Post #6 by @elarson (2021-06-30 15:14 UTC)

<p>I want to extract standard AP4, AP2, AP3, and SAX 2d ultrasound clips from a 3d data set for input to another software analysis tool that only accepts 2d ultrasound clips.  I probably should have stated the problem this way from the start, but I tend to have bottom up view of things…</p>

---

## Post #7 by @lassoan (2021-07-09 15:14 UTC)

<p>You can create a markups ROI node, make it so thin that it only extracts a single slice, then use Crop volume sequence module to extract that slice from all the volumes in the sequence. If you get stuck at any of these steps then let us know.</p>

---
