# Slice Interpolation

**Topic ID**: 2808
**Date**: 2018-05-11
**URL**: https://discourse.slicer.org/t/slice-interpolation/2808

---

## Post #1 by @cphillips (2018-05-11 16:28 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1<br>
Expected behavior: 3D Slicer should show the exact number of slices as appear in a DICOM viewer<br>
Actual behavior: 3D Slicer shows extra (and I cannot find a “match” for some of the correct slices shown in DICOM)</p>
<p>I am working with MRI data. When I load it into 3D Slicer, it often adds extra slices than what are actually present (i.e. one scan has 8 slices, which I verified with the PHILIPS DICOM viewer, but in 3D slicer, the data shows up as having 13 slices). Now, sliding the slider at the top of each frame definitely interpolates between slices, but I am wondering if interpolation also occurs when I am using the arrow keys, which usually just navigates slice by slice. The reason I am wondering this is that I tried to match the slices I was seeing in the DICOM viewer with what I was seeing in 3D slicer, to filter out the extra, non-matching slices in Slicer, but some of the slices from the DICOM viewer are not precisely matched anywhere in what 3D slicer showed me. This error is present whether I load in the data in DICOM or NIFTY (.nii) form.</p>
<p>Any insights are much appreciated! Thank you.</p>

---

## Post #2 by @lassoan (2018-05-11 16:38 UTC)

<p>3D Slicer reconstructs 3D volumes from the input 2D image slices and no reference is kept to 2D slice indexes. However, you may find that one of the voxel indexes that slicer displays in the Data Probe section in the lower-left corner correlate with DICOM slice index (most likely there will be an offset of 1, since DICOM usually start the numbering at 1 instead of 0).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f825a5c4a09d42f0cf365204b7fb0d3f6b5f98e3.png" alt="image" data-base62-sha1="zpd4thXpHmurXuYxqcMPPt1ULSz" width="484" height="210"></p>

---

## Post #3 by @cphillips (2018-05-11 17:36 UTC)

<p>Sorry, I don’t think I was clear enough in my previous post. When I import the DICOM data itself into 3D Slicer, the some problem arises as with the NIFTY data. I am comparing the 2D slices as shown in 3D slicer to the 2D slices as shown in a different DICOM viewer software. How does 3D Slicer decide which slices to show? Are they an exact match to the “real” slices, or no?</p>

---

## Post #4 by @pieper (2018-05-11 17:51 UTC)

<p>Slicer displays patient spact by default.  Your images might have been acquired on a tilted plane, in which case you could see the discussion here (look for “Rotate to volume plane”)</p>
<aside class="quote" data-post="2" data-topic="546">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/display-issue-with-rt-structs-and-mr-volume/546/2">Display issue with RT structs and MR volume</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello Yannick, 
It looks like there is a problem with the planar contour to closed surface conversion. 
If you could send me an email with the data, I will see if I can figure out what the problem is. 
I will message you with my email. 
Thanks! 
Kyle
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2018-05-11 18:50 UTC)

<aside class="quote no-group" data-username="cphillips" data-post="3" data-topic="2808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/848f3c/48.png" class="avatar"> cphillips:</div>
<blockquote>
<p>Are they an exact match to the “real” slices, or no?</p>
</blockquote>
</aside>
<p>You always see the real image. The coordinates (both the anatomical/patient coordinates and voxel coordinates) are also all real and correct. You may turn off interpolation (Volumes module / Display / Interpolate checkbox) if you want to make sure that at a certain position in the image you see the contribution of exactly one pixel of the image slices.</p>
<p>If you could tell what your application (anatomy, procedure, imaging modality, etc) and your concerns are then we could give more specific answer.</p>

---

## Post #6 by @ihnorton (2018-05-11 19:58 UTC)

<p>If I understand correctly, I think the request is for the spacing mode <code>vtkMRMLSliceNode::PrescribedSliceSpacingMode</code> (“manual spacing”) to automatically match the volume spacing along the corresponding axis.</p>

---

## Post #7 by @cphillips (2018-05-11 20:19 UTC)

<p>Thank you, rotating to the volume axis really helped. The application is research (calculating the volume of stroke lesions). Would having interpolate on or off have a big difference on the accuracy in this case (I doubt it would…)?</p>

---

## Post #8 by @lassoan (2018-05-11 21:41 UTC)

<p>Interpolation has no effect on anything but how smooth the image appears (if you see boundary of individual voxels or the transition is continuous).</p>
<p>Slice step size is already the same as the volume spacing along the corresponding axis, but this step size is not used when you browse slices using the slider above the viewer (only when mouse wheel or arrow keys are used).</p>

---

## Post #9 by @Yong_Wang (2019-06-13 18:50 UTC)

<p>HI Lassoan,<br>
Thank you for the information. We are looking for the algorithm that this interpolation checkbox triggered. Is it linear or B-spline based interpolation? Is there code that we can refer to for this interpolation function?</p>
<p>It looks like the interpolation dramatically increase the spatial resolution and smooth the image with very smooth boundaries.</p>
<p>Thank you very much!<br>
Yong</p>

---

## Post #10 by @lassoan (2019-06-13 19:38 UTC)

<p>It is linear interpolation, implemented in <a href="https://vtk.org/doc/nightly/html/classvtkImageReslice.html" rel="nofollow noopener">vtkImageReslice</a> filter.</p>
<p>Note that this interpolation does not increate resolution, it just displays the continuous signal reconstructed from samples (instead of showing discrete samples).</p>

---

## Post #11 by @Yong_Wang (2019-06-13 21:39 UTC)

<p>Thank you very much!</p>
<p>How can we know the values of the reconstructed continuous signals?</p>
<p>Yong</p>

---

## Post #12 by @lassoan (2019-06-14 04:01 UTC)

<p>You can <a href="https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem" rel="nofollow noopener">reconstruct a continuous signal from discrete samples</a>. For typical medical images, linear interpolation results are usually indiscernible from the optimal reconstruction results.</p>

---

## Post #13 by @zxy630 (2023-07-28 07:16 UTC)

<p>If I want to export dicom after interpolation, can you give me some guidance？</p>

---

## Post #14 by @lassoan (2023-07-29 20:25 UTC)

<p>See how to export images to DICOM in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">Slicer documentation</a>.</p>

---
