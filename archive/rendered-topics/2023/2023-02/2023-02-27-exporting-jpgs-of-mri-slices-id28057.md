---
topic_id: 28057
title: "Exporting Jpgs Of Mri Slices"
date: 2023-02-27
url: https://discourse.slicer.org/t/28057
---

# Exporting jpgs of MRI slices

**Topic ID**: 28057
**Date**: 2023-02-27
**URL**: https://discourse.slicer.org/t/exporting-jpgs-of-mri-slices/28057

---

## Post #1 by @hchattaway (2023-02-27 03:34 UTC)

<p>I am looking to do the following… I can write the Python code, but I am new to the 3d-slicer API and just need some guidance…<br>
I want to:</p>
<ol>
<li>Load up a folder(s) of nii image files into 3d-slicer… I’ve done this part and since they are loaded into a listbox I assume(?) there is a reference to this.</li>
<li>Iterate over this list of files.</li>
<li>For each nii file, select either the sagittal, coronal or transverse view.</li>
<li>Then for the selected view, cycle through each slice for that view and export each slice as a jpg/png file.</li>
</ol>
<p>The goal of this is to extract these to be used as images to train a machine learning model…</p>
<p>I’ve looked over the API and there are SO many methods!  if anyone has done this before as a module or can point out the relevant API calls, it would be greatly appreciated!</p>
<p>Thank you!<br>
Harold Chattaway</p>

---

## Post #2 by @pieper (2023-02-27 20:39 UTC)

<p>First, we understand that some machine learning examples are hard-coded to handle only jpg or png, but converting the original data to an 8 bit format truncates the dynamic range and is probably a bad idea.</p>
<p>That out of the way, you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html">ScreenCapture</a> module’s slice sweep mode to catpure the images.  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#capture-a-slice-view-sweep-into-a-series-of-png-files">Here’s an example</a> doing this from a python script.</p>
<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#batch-processing">batch processing</a> examples will get you started applying this to a set of images.</p>

---

## Post #3 by @hchattaway (2023-02-28 15:54 UTC)

<p>This looks like it will be a great help, thanks… I am not using anything hard coded for just jpgs etc… I am writing the app using YOLO/PyTorch so I have control over the image format…</p>
<p>I figured something like this had to have been done before…<br>
Thank you!<br>
Harold</p>

---
