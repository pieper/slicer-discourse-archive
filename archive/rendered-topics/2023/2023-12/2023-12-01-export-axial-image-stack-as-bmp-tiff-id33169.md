# Export axial image stack as BMP/TIFF

**Topic ID**: 33169
**Date**: 2023-12-01
**URL**: https://discourse.slicer.org/t/export-axial-image-stack-as-bmp-tiff/33169

---

## Post #1 by @snehak (2023-12-01 19:42 UTC)

<p>I am working on a project that involves loading DICOMM images into 3D slicer, cropping the image into 2 layers, performing re-orientation of the sagittal plane (using reformat), adjusting window leveling, and then exporting the modified axial image stack as .BMP files. How can I export the axial image stack as BMP files (or TIFF files)?</p>
<p>There was another thread on this forum that used a python script to convert an STL segmentation file to BMP, but I don’t use segmentation in my process. If possible, I would prefer to use the GUI to accomplish all my tasks, but I can use a Python script if necessary. Thank you!</p>

---

## Post #2 by @tsehrhardt (2023-12-04 16:50 UTC)

<p>What I have done is exported the new dicom images using “Create a DICOM series” then used the batch convert function in Irfanview to convert them to a different format. You might need to download an extension for Irfanview to read the DICOMs but the batch conversion is fast.</p>

---

## Post #3 by @muratmaga (2023-12-04 17:08 UTC)

<aside class="quote no-group" data-username="snehak" data-post="1" data-topic="33169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/snehak/48/68555_2.png" class="avatar"> snehak:</div>
<blockquote>
<p>performing re-orientation of the sagittal plane (using reformat), adjusting window leveling, and then exporting the modified axial image stack as .BMP files.</p>
</blockquote>
</aside>
<p>FYI, All of these are lossy operations if you export them as a BMP stack (you will resample the image, change bit depth etc). Is there a reason why you are doing this? Quite a bit of the Slicer infrastructure is actually designed to avoid this type of lossy operations (e.g., use space directions as part of the image header to reorient the image as opposed to resample).</p>

---
