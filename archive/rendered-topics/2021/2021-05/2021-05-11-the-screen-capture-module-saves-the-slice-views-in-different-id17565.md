---
topic_id: 17565
title: "The Screen Capture Module Saves The Slice Views In Different"
date: 2021-05-11
url: https://discourse.slicer.org/t/17565
---

# The screen capture module saves the slice views in different directions

**Topic ID**: 17565
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/the-screen-capture-module-saves-the-slice-views-in-different-directions/17565

---

## Post #1 by @pranaysingh (2021-05-11 08:06 UTC)

<p>Hi,</p>
<p>We stumbled upon a problem with screen capture module. After loading the data in 3D slicer, we wanted to save the R, G and Y view planes that we set into the system. We used Screen capture module, but noticed that the resolution of the images being saved depends upon screen size of my 3D slicer app window, or the view window inside the app itself, how much I have expanded or shrinked that particular view. This creates a problem of reproducibility.<br>
We are trying to extract slices from our CT volumetric data along different planes set at arbitrary normals and center points. As we find a suitable plane along a normal and we can subsequently view them in slicer views, we were trying to save them. But looks we have to remember a constant window size at which all the slices were saved using screen capture so that, in order to reproduce them anytime.<br>
Why are they not saved at the resolution of original dicom files ? Am I saving it the wrong way ?<br>
Also, we would prefer if we avoid saving it as PNG images as it compresses the images down to 8 bit depth while my original dicom images are of 16 bit depth per pixel, may be saving as numpy would be better ?</p>
<p>Kindly guide to fix the issue. Would be lot helpful.<br>
Thanks,<br>
Pranay</p>

---

## Post #2 by @lassoan (2021-05-13 06:32 UTC)

<aside class="quote no-group" data-username="pranaysingh" data-post="1" data-topic="17565">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pranaysingh/48/10876_2.png" class="avatar"> pranaysingh:</div>
<blockquote>
<p>Why are they not saved at the resolution of original dicom files</p>
</blockquote>
</aside>
<p>Screen capture module is mean for making presentations and youtube videos. It is not meant for data extraction for deep learning.</p>
<p>DICOM files typically have anisotropic resolution and you lose data when you reslice along an arbitrary orientation, so you need to choose an output resolution that makes sense for your application (probably a bit higher than the average resolution).</p>
<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume">this code snippet</a> to get images at arbitrary orientation and resolution.</p>
<aside class="quote no-group" data-username="pranaysingh" data-post="1" data-topic="17565">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pranaysingh/48/10876_2.png" class="avatar"> pranaysingh:</div>
<blockquote>
<p>Why are they not saved at the resolution of original dicom files ? Am I saving it the wrong way ?<br>
Also, we would prefer if we avoid saving it as PNG images as it compresses the images down to 8 bit depth while my original dicom images are of 16 bit depth per pixel, may be saving as numpy would be better ?</p>
</blockquote>
</aside>
<p>Except very rare cases (e.g., dry bone CT), 8 bits are insufficient for CT image storage. Saving it as nrrd or numpy should work. If you save as numpy then you need to save somewhere your image geometry (origin, spacing, and axis directions), while nrrd can store all these essential information in the file header.</p>
<p>Have a look at torchio and monai for ideas of preparing deep learning training data from 3D medical images.</p>

---
