---
topic_id: 39855
title: "Converting Stl File To Tiff Stack"
date: 2024-10-25
url: https://discourse.slicer.org/t/39855
---

# Converting STL file to TIFF stack

**Topic ID**: 39855
**Date**: 2024-10-25
**URL**: https://discourse.slicer.org/t/converting-stl-file-to-tiff-stack/39855

---

## Post #1 by @nagda95 (2024-10-25 03:29 UTC)

<p>Hello,</p>
<p>I am attempting to convert an STL file containing spherical-like particles into a stack of TIFF image files using the code provided by <a class="mention" href="/u/lassoan">@lassoan</a> in this thread discussion:</p><aside class="quote quote-modified" data-post="8" data-topic="15949">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-stl-file-to-high-resolution-tiff-stack/15949/8">Convert STL file to high-resolution TIFF stack</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    By default, when you import a module, the image extents are increased to include the entire model, essentially undoing the limit that you set on the reference geometry. You can disable this by changing a conversion parameter. 
After some cleanup and simplification of the code, here is a complete working version: 
inputModelFile = r"c:\Users\andra\OneDrive\SpinePhantom2Model.stl"
outputDir = r"c:\tmp\20210211-model-rasterization"
outputVolumeLabelValue = 255
inPlaneResolutionDpi = 400
planeThickn…
  </blockquote>
</aside>

<p>I was able to run the code in 3D Slicer’s Python console without any errors (except for a few warnings that I think can be ignored). However, the resulting TIFF images are completely black. Could someone please take a look and help me figure out what might be going wrong?</p>
<p>Warning message:<br>
[VTK] Warning: In vtkSegmentation.h, line 504<br>
[VTK] vtkSegmentation (000001B935AC77D0): vtkSegmentation::SetMasterRepresentationName() method is deprecated, please use SetSourceRepresentationName method instead</p>
<p>I had really appreciate your time and assistance.</p>
<p>Thank you for your support.</p>
<p>Best Regards,<br>
Vinit Nagda</p>
<p>Link to my stl file:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1iqxlyHix88lmC4Uh7CzYYYY9j4L9q9WH/view?usp=drive_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1iqxlyHix88lmC4Uh7CzYYYY9j4L9q9WH/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1iqxlyHix88lmC4Uh7CzYYYY9j4L9q9WH/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1iqxlyHix88lmC4Uh7CzYYYY9j4L9q9WH/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">Multiple_Particles3D.stl</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2024-10-25 17:54 UTC)

<p>The images are not all black. Outside the spheres pixel values are all 0, inside the pixel value is 255. If you open the image in any scientific imaging software then you will see the difference.</p>
<p>Most consumer image viewers probably scale the entire range of the 16-bit image to the displayed range, so you would barely see the difference between 0 and 255 value. I’ve updated the script now to use 8-bit TIFFs, which basic viewers should be able to handle better.</p>
<p>I would recommend to not use consumer imaging software. Scientific software not just supports larger scalar range but it can also use 3D image file formats, so you would not slow things down by reading/writing hundreds or thousands of files, and you would preserve the 3D image geometry (origin, spacing, axis directions) that you lose when you export to separate slices.</p>

---

## Post #3 by @nagda95 (2024-10-31 09:37 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> very much for your response and the code update. I truly appreciate all your efforts.<br>
Thanks again for your time!</p>

---
