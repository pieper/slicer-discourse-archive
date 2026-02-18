# Dicom Volume Render an unmatched series

**Topic ID**: 4732
**Date**: 2018-11-12
**URL**: https://discourse.slicer.org/t/dicom-volume-render-an-unmatched-series/4732

---

## Post #1 by @epdawson (2018-11-12 17:50 UTC)

<p>I have an ultrasound data set that has been converted to individual dicom files. However, these files have no reference to each other, so in Slicer they all are loaded as individual volumes. Is there a way to combine these in an efficient manner (talking about 300+ images) through slicer, or must this happen previously in Matlab by correctly giving each file the necessary metadata attached?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-11-12 17:55 UTC)

<p>What would you like to do with the images? Replay them as a time sequence, reconstruct into a 3D volume, …?</p>

---

## Post #3 by @epdawson (2018-11-12 18:40 UTC)

<p>Sorry for the vagueness. I would like to reconstruct them as a volume, and then be able to export that Volume as a single Dicom if possible.</p>
<p>Thanks for the reply!</p>

---

## Post #4 by @lassoan (2018-11-12 19:37 UTC)

<p>Have you used position tracker (optical or electromagnetic tracker, etc) to track the ultrasound probe’s position?</p>
<p>Did you use <a href="http://plustoolkit.org">Plus toolkit</a> for data acquisition? If yes, you can do real-time volume reconstruction in Slicer, using <a href="http://www.slicerigt.org">SlicerIGT extension</a> - see details in SlicerIGT tutorials.</p>

---

## Post #5 by @epdawson (2018-11-15 19:20 UTC)

<p>This is all post-processed data. I am not interested in doing live acquisiton. My question is what does Slicer need to know in metadata to load a Dicom Volume? I have a dicom file that contains 1 study, 1 series, and 255 instances, but when loaded in Slicer nothing registers. No error comes up, but no confirmation either. Simply nothing. What is going on here?</p>

---

## Post #6 by @lassoan (2018-11-15 19:47 UTC)

<aside class="quote no-group" data-username="epdawson" data-post="5" data-topic="4732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/ebca7d/48.png" class="avatar"> epdawson:</div>
<blockquote>
<p>My question is what does Slicer need to know in metadata to load a Dicom Volume?</p>
</blockquote>
</aside>
<p>All the required UIDs (patient name, ID, study UID, series instance UID) must be there, image position patient, image orientation patient must be present and consistent, pixel spacing is required, too.</p>
<p>It is complicated. So, if you don’t already have a DICOM image then I would not recommend to attempt to create a valid DICOM image. Instead, you can write it to a nrrd file using <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">nrrdwrite.m</a>. Or, even better, let Slicer handle all the Matlab communication (send/receive images, transforms, points, etc.) using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge extension.</a></p>

---

## Post #7 by @epdawson (2018-11-16 22:05 UTC)

<p>Andras,</p>
<p>I am sticking with the metadata approach, and have been able to construct a single volume series from all of my images. It appears though that Slicer is having an issue with loading order, as you can see below in the screenshot. There is no reason for this to be happening from a metadata standpoint. Any thoughts?</p>
<p>Thanks for you time and support!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6effdf639bde85154f4f9633f8a27fe1ca340f.png" data-download-href="/uploads/short-url/oKgpTJvH8N2luu9wuoPS3KorfWv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad6effdf639bde85154f4f9633f8a27fe1ca340f_2_685x500.png" alt="image" data-base62-sha1="oKgpTJvH8N2luu9wuoPS3KorfWv" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad6effdf639bde85154f4f9633f8a27fe1ca340f_2_685x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6effdf639bde85154f4f9633f8a27fe1ca340f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6effdf639bde85154f4f9633f8a27fe1ca340f.png 2x" data-dominant-color="EBEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1026×748 57.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2018-11-18 15:36 UTC)

<blockquote>
<p>I am sticking with the metadata approach</p>
</blockquote>
<p>We can help you find a solution to any problem, but if you don’t follow our advice then you make this hard.</p>
<blockquote>
<p>It appears though that Slicer is having an issue with loading order</p>
</blockquote>
<p>If you set DICOM metadata correctly then Slicer reads all the slices into a single 3D volume. Order of file names does not matter, slices order is computed based on image position and orientation tags.</p>

---
