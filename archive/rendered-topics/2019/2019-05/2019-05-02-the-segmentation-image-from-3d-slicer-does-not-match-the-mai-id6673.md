# The segmentation image from 3D slicer does not match the main image in itk snap

**Topic ID**: 6673
**Date**: 2019-05-02
**URL**: https://discourse.slicer.org/t/the-segmentation-image-from-3d-slicer-does-not-match-the-main-image-in-itk-snap/6673

---

## Post #1 by @Shawn (2019-05-02 10:49 UTC)

<p>Operating system: win 10<br>
Slicer version: Slicer 4.11</p>
<p>Hi Everyone,</p>
<p>The segmentation image saved from 3D slicer does not match the main image in itk snap, but based on the same dicom images. How to fix it? i need the semi-auto segmation function of the 3D slicer.</p>
<p>Thank you all!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe05ecec4d05511332a122b0c1a24f84e14a7f64.jpeg" data-download-href="/uploads/short-url/AfbYjmc89p6bTyUydLCAWrEzUJm.jpeg?dl=1" title="3d%20slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe05ecec4d05511332a122b0c1a24f84e14a7f64_2_690x316.jpeg" alt="3d%20slicer" data-base62-sha1="AfbYjmc89p6bTyUydLCAWrEzUJm" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe05ecec4d05511332a122b0c1a24f84e14a7f64_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe05ecec4d05511332a122b0c1a24f84e14a7f64.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe05ecec4d05511332a122b0c1a24f84e14a7f64.jpeg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d%20slicer</span><span class="informations">714×328 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcd0f69f0611f393c211da733289161f25995b49.jpeg" alt="itk" data-base62-sha1="qWlsUN5uYHPicVVTRkYFM7NhXlv" width="502" height="399"></p>

---

## Post #2 by @cpinter (2019-05-02 13:30 UTC)

<p>Slicer saves a segmentation node in a 4D image, because all the segments are stored in one file. Other software expecting 3D images will not read it properly.</p>
<p>You can export the segments to labelmap nodes by right-clicking the segmentation in the Data module, and choose “Export visible segments to binary labelmap”. Then you can save these labelmaps in individual nrrd files. ITK-Snap can read these.</p>
<p>Just out of curiosity: why are you using ITK-Snap when you already use Segment Editor? My hunch is that everything you want to do can be done in Slicer. Please let us know.</p>

---

## Post #3 by @Shawn (2019-05-02 14:37 UTC)

<p>Thank you.You are right, and I have solved this problem.<br>
Because when I use another software to read the segmentation file from 3D slicer, it warning mismatch file size. Then I use itk snap to verify  this problem.</p>

---

## Post #4 by @cpinter (2019-05-02 15:14 UTC)

<p>I see. Yes, the 4D seg.nrrd files are a convenience format for Slicer-only. You need to split the segmentation to labelmaps and save those for interoperability.</p>

---

## Post #5 by @fedorov (2019-05-02 19:38 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="6673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>You need to split the segmentation to labelmaps and save those for interoperability.</p>
</blockquote>
</aside>
<p>You can also use the Segmentations module to export individual segments into labelmaps. If you specify our image volume as reference (as shown in the screenshot below), the geometry should match.</p>
<p>Note that some tools use very small default tolerance thresholds while determining if the geometry is identical, and may still complain about the inconsistency.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d45b72c660f0f885445ccece89455d0dd3e931b4.png" data-download-href="/uploads/short-url/uiB9m3suge6AEh8v1UCH190JS6M.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d45b72c660f0f885445ccece89455d0dd3e931b4_2_467x500.png" alt="image" data-base62-sha1="uiB9m3suge6AEh8v1UCH190JS6M" width="467" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d45b72c660f0f885445ccece89455d0dd3e931b4_2_467x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d45b72c660f0f885445ccece89455d0dd3e931b4_2_700x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d45b72c660f0f885445ccece89455d0dd3e931b4_2_934x1000.png 2x" data-dominant-color="BCBDC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">953×1020 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @asere (2020-11-03 01:20 UTC)

<p>Hello,</p>
<p>I was trying to obtain the 3D segmentations maps as well, with the same dimensions as my CT images.</p>
<p>As mentioned, I tried to export the visible segments to binary labelmap. However, the segmentation is still “cropped” and doesnt match the dimensions of the CT.</p>
<p>I also tried to “export” the individual segments into labelmaps, using the CT as a reference, however clicking on the export button I don’t get anything</p>
<p>Is there a way to save the segmentations having the same dimensions as the CT?</p>
<p>Thank you</p>

---

## Post #7 by @lassoan (2020-11-10 19:47 UTC)

<p>This should all work well in latest Slicer preview release. We don’t crop the segmentation to minimum necessary size by default anymore.</p>

---

## Post #8 by @KatnissSnow (2024-11-26 09:37 UTC)

<p>For old data (seg.nrrd files obtained from version 4.XX), what are good ways to resize it to the same dimensions as the reference volume using Python (outside of the Slicer environment)?I used sitk.ResampleImageFilter() to resize, but I got incorrect results when the spacing difference is large (resample.SetInterpolator(sitk.sitkNearestNeighbor)). Thank you for your help.</p>

---

## Post #9 by @lassoan (2024-11-26 15:17 UTC)

<p>You can load the segmentation and the reference volume then use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">“Specify Geometry” button in the Segment Editor to update the segmentation geometry</a>.</p>

---
