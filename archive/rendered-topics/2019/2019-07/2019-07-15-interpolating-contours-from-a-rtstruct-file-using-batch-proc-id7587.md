---
topic_id: 7587
title: "Interpolating Contours From A Rtstruct File Using Batch Proc"
date: 2019-07-15
url: https://discourse.slicer.org/t/7587
---

# Interpolating contours from a RTSTRUCT file using batch processing

**Topic ID**: 7587
**Date**: 2019-07-15
**URL**: https://discourse.slicer.org/t/interpolating-contours-from-a-rtstruct-file-using-batch-processing/7587

---

## Post #1 by @Shekhar (2019-07-15 13:10 UTC)

<p>Hello,</p>
<p>I have an RTSTRUCT file (.dcm) and its reference files (ultrasound images in dicom format). RTSTRUCT file contains contour data for ROI at some slice locations, I would like to interpolate the contour data to all the slices using batch processing in 3D slicer or Platimatch.</p>
<p>I have done this manually in 3D Slicer manually and saved them to label maps for each ROI, since 3D slicer interpolated the contour data automatically. I would like to know how to interpolate the contour to all slices and save them as label maps using batch processing.</p>
<p>Thank you in advance for your help.</p>
<p>Regards,<br>
Shekhar</p>

---

## Post #2 by @cpinter (2019-07-15 13:51 UTC)

<p>Please try the BatchProcessing module that does just this:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/1325988?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="128" height="128">

<h3><a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT</a></h3>

<p>Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @Shekhar (2019-07-15 14:43 UTC)

<p>Hello Csaba,</p>
<p>I have my RTSTRUCT file and reference files in the same folder, but when I run the script as you suggested it gives the following error. The output folder is empty.</p>
<p>Script Used:</p>
<p>Slicer.exe --no-main-window --python-script BatchStructureSetConversion.py --input-folder Dir/RTandImages --output-folder /Output</p>
<p>Error Message:<br>
No reference volume found for segmentation RTSTRUCT: RTSTRUCT</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2630f097a212091ca40ceb0e8db15ab8ff1a9c56.png" data-download-href="/uploads/short-url/5rQZOfLHWkyCukfVKpkjNh0k754.png?dl=1" title="error-python" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2630f097a212091ca40ceb0e8db15ab8ff1a9c56.png" alt="error-python" data-base62-sha1="5rQZOfLHWkyCukfVKpkjNh0k754" width="690" height="162" data-dominant-color="F7FAF7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error-python</span><span class="informations">1778×420 26.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regards,<br>
Shekhar</p>

---

## Post #4 by @cpinter (2019-07-15 15:31 UTC)

<p>The CT does not just need to be in the same folder, but needs to be referenced from the RT structure set via DICOM to be considered reference. The reason for this is that you can have multiple structure sets and CTs in the input folder and they are paired automatically using this method. Most TPSs where you can export RTSTRUCT from create this link. How do you get the RTSTRUCT file?</p>

---
