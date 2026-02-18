# Saving a select view as a DICOM file

**Topic ID**: 24227
**Date**: 2022-07-07
**URL**: https://discourse.slicer.org/t/saving-a-select-view-as-a-dicom-file/24227

---

## Post #1 by @beginl22 (2022-07-07 16:47 UTC)

<p>I am working with CT scans of metatarsals and I am looking at the anterior to posterior configuration (cross section of diaphysis). But when I go to save the view as a DICOM, it just ends up saving a DICOM file of the inferior to superior view (like a normal CT scan). Any help with saving the select A/P view, as well as figuring out what exact slice I am looking at in the data set.<br>
Thank you!</p>

---

## Post #2 by @lassoan (2022-07-07 16:58 UTC)

<p>Changing the slice view orientation just changes how the image is displayed and will not modify the image.</p>
<p>You can reslice the volume, for example using Crop volume module. You can enable rotation of the cropping region (ROI) in Markups module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5142cc2d2f9e6b397a3c6264386b1ba2c5a8db1.jpeg" data-download-href="/uploads/short-url/pPTE5o8y4iFWdhtztnOx2biplPb.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5142cc2d2f9e6b397a3c6264386b1ba2c5a8db1_2_690x360.jpeg" alt="image" data-base62-sha1="pPTE5o8y4iFWdhtztnOx2biplPb" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5142cc2d2f9e6b397a3c6264386b1ba2c5a8db1_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5142cc2d2f9e6b397a3c6264386b1ba2c5a8db1_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5142cc2d2f9e6b397a3c6264386b1ba2c5a8db1_2_1380x720.jpeg 2x" data-dominant-color="B7B6B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1004 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Why would you like to export the resliced image to DICOM? Would you like to do some additional processing in some other software? Why would you like to export to DICOM format instead of a simpler research format, such as NRRD?</p>

---

## Post #4 by @beginl22 (2022-07-07 17:46 UTC)

<p>Looking to export A/P view of metatarsals for cross-sectional bone model. The bone modeling code only accepts DICOM. Is it not possible to just export the A/P view?</p>

---

## Post #5 by @lassoan (2022-07-07 17:55 UTC)

<p>Would you like to simulate an X-ray image from a CT?</p>

---

## Post #6 by @beginl22 (2022-07-07 18:05 UTC)

<p>No, I am importing a normal CT scan. Then I was looking at trying to save the anterior/posterior view of the foot to use for a bone model. But it does not seem like 3D Slicer allows me to save any variations of the CT scan, other than the original superior/inferior as a DICOM</p>

---

## Post #7 by @lassoan (2022-07-07 18:14 UTC)

<aside class="quote no-group" data-username="beginl22" data-post="6" data-topic="24227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/beginl22/48/15915_2.png" class="avatar"> beginl22:</div>
<blockquote>
<p>But it does not seem like 3D Slicer allows me to save any variations of the CT scan, other than the original superior/inferior as a DICOM</p>
</blockquote>
</aside>
<p>I just described above how one way to do it. There are many other options how to get a single slice or many slices or a projection or average of slices in any orientation.</p>
<aside class="quote no-group" data-username="beginl22" data-post="6" data-topic="24227">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/beginl22/48/15915_2.png" class="avatar"> beginl22:</div>
<blockquote>
<p>Then I was looking at trying to save the anterior/posterior view of the foot to use for a bone model</p>
</blockquote>
</aside>
<p>Do you want to save a single reformatted slice of the 3D image as a new DICOM image? Or do you want to show a 3D rendering? If it is hard to explain then post a few images of what you want to get.</p>

---

## Post #8 by @beginl22 (2022-07-07 18:18 UTC)

<p>Preferably, I would like to save one single slice from the A/P display as a DICOM file. Just a single slice of interest showing the cross sections of the metatarsals.</p>

---

## Post #9 by @beginl22 (2022-07-07 19:26 UTC)

<p>I cant seem to get my cross sectional slice. Is there any other way of going about selecting a specific slice? I tried to use your method but cant seem to get it. This is my first time working with 3D Slicer and I am just trying to import a normal CT, and export a single slice of the A/P view.</p>

---

## Post #10 by @lassoan (2022-07-07 19:50 UTC)

<p>What you want to do is highly unusual (why would you need to extract a single slice, why it is a problem that there are other slices in the image; why that software cannot reslice the volume; why a bone modeling software care about how the voxel grid is oriented - it should work in physical space), so the soution may not be very easy or convenient.</p>
<p>If you need to do this only for a handful of cases, without any Python scripting, then you can create a ROI and rotate and reslice it like this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="eW3XIYnI6Ok" data-video-title="How to extract a single slice using Slicer GUI" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=eW3XIYnI6Ok" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/eW3XIYnI6Ok/maxresdefault.jpg" title="How to extract a single slice using Slicer GUI" width="" height="">
  </a>
</div>


---

## Post #11 by @beginl22 (2022-07-07 19:56 UTC)

<p>I figured out how to extract the view that I want as DICOM files. Where in 3D slicer though does it tell you what # slice you are looking at? Rather than exporting a single slice, I have exported the entire A/P view, but now I have to choose my slice of interest for the bone model, but I do not see anywhere in 3D Slicer what the exact number slice I am looking at in the CT file. The entire CT is 512 slices so I am just trying to figure out where I can see what number slice I am looking at.</p>
<p>My apologies if this is all confusing, I am new to 3D Slicer and I also am struggling with how to explain my exact problems.</p>

---

## Post #12 by @lassoan (2022-07-07 20:44 UTC)

<p>Slicer performs all analysis and visualizations in 3D, so image data is not organized into slices but managed as one single 3D array. There are no slice indices until the data is actually exported to DICOM.</p>
<p>However, since most DICOM exporter choose to reslice the volume along the third axis, you can get the slice index by adding 1 to the third voxel coordinate that is shown in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#data-probe">Data Probe</a>. You need to add 1 because in DICOM the slice index usually starts from 1, while 3D coordinates start from 0.</p>

---
