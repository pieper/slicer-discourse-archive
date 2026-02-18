# Image Registration microCT image to STL file 

**Topic ID**: 27820
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/image-registration-microct-image-to-stl-file/27820

---

## Post #1 by @elrond11 (2023-02-15 06:41 UTC)

<p>I have an STL file that I used to 3D print bone samples. I then scanned those 3D printed bone samples and converted those files to nii files. I am trying to run image registration in Slicer to evaluate the quality of the 3D printing, but I am not sure how to register a surface mesh and a 3D image. I would like to run a simple rigid transformation using BRAINS and a linear transform.</p>
<p>I was able to get a linear transform to work using the original image file that I used to make the STL file but that is not quite what was 3D printed. As there is mesh operations that would slightly change this. Is there an easy way to convert the STL file to a nii or nrrd for example?</p>

---

## Post #2 by @lassoan (2023-02-15 06:47 UTC)

<p>You lose some accuracy if you rasterize the surface mesh into a binary labelmap, so probably you can get more accurate results if you segment the CT scans and compare them to the original surface meshes (STL files) using ModelToModelDistance extension. You can align the meshes before the comparison using <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#model-registration">model registration</a>.</p>

---

## Post #3 by @elrond11 (2023-02-15 06:57 UTC)

<p>I have segmentations of the CT scans, but I was thinking segmentation could introduce other errors into the image. Noise or loss of connectivity in the structures of the sample.</p>
<p>Could you provide some documentation about rasterizing the surface mesh into a binary labelmap? Additonally, I am confused on how to resample an image in Slicer. I would like for the CT image and the STL file to be of the same image size.</p>

---

## Post #4 by @lassoan (2023-02-15 07:07 UTC)

<aside class="quote no-group" data-username="elrond11" data-post="3" data-topic="27820">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elrond11/48/18421_2.png" class="avatar"> elrond11:</div>
<blockquote>
<p>Could you provide some documentation about rasterizing the surface mesh into a binary labelmap?</p>
</blockquote>
</aside>
<p>I mean importing a model (surface mesh) into binary labelmap representation in a segmentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file" class="inline-onebox">Segmentations — 3D Slicer documentation</a></p>
<aside class="quote no-group" data-username="elrond11" data-post="3" data-topic="27820">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elrond11/48/18421_2.png" class="avatar"> elrond11:</div>
<blockquote>
<p>I am confused on how to resample an image in Slicer. I would like for the CT image and the STL file to be of the same image size.</p>
</blockquote>
</aside>
<p>CT imaging, segmentation, all import/export operations, etc. all maintain the correct physical size. All processing and comparison methods in Slicer operate in physical space (image resolution does not matter). Therefore, there should be ne need for resizing or resampling for any comparison.</p>
<p>If you want to resample images anyway then you can use resampling modules, such as “Resample Scalar/Vector/DWI Volume” module.</p>

---

## Post #5 by @elrond11 (2023-02-15 18:29 UTC)

<p>I am still having some issues with resampling and the image sizes. Can I provide you with the images so you can understand what the issue is?</p>

---

## Post #6 by @lassoan (2023-02-15 20:53 UTC)

<p>Yes, sure, you can upload the images anywhere (dropbox, onedrive, google drive, etc.) and post the download link here. Make sure the image do not contain patient health information (anonymize or use public or non-human data).</p>

---
