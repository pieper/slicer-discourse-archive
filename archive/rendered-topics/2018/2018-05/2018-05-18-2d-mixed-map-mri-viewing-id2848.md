---
topic_id: 2848
title: "2D Mixed Map Mri Viewing"
date: 2018-05-18
url: https://discourse.slicer.org/t/2848
---

# 2D Mixed Map MRI Viewing

**Topic ID**: 2848
**Date**: 2018-05-18
**URL**: https://discourse.slicer.org/t/2d-mixed-map-mri-viewing/2848

---

## Post #1 by @cphillips (2018-05-18 13:45 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am attempting to view a 2D Mixed Map MRI scan in Slicer, but the slicer slider appears to be non-functional. Granted, there is only 1 slice in this scan, but the nature of 2D Mixed Map is that multiple different types of images of the same region are taken, and I am only able to view one of them in Slicer (as opposed to all of them in PHILIPS DICOM Viewer).</p>
<p>Any insight on how to view 2D Mixed Map scans would be helpful. Thank you!</p>

---

## Post #2 by @pieper (2018-05-18 15:33 UTC)

<p>Depending on what DICOM tags differentiate the types of images you may be able load them as independent volumes using the Advanced mode of the <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/DICOM">DICOM Module</a></p>
<p>Check the Advanced box in the lower right, select your series and pick Examine and then it will show what options it discovers.  You can also use the Metadata dialog to scroll through the images to see what tags are changing for the different images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5972aa0536798a0a6d5a378bcc12562201574b4.png" data-download-href="/uploads/short-url/nCSEDgneD0FxKY04cL58FZ5THEw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5972aa0536798a0a6d5a378bcc12562201574b4_2_690x418.png" alt="image" data-base62-sha1="nCSEDgneD0FxKY04cL58FZ5THEw" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5972aa0536798a0a6d5a378bcc12562201574b4_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5972aa0536798a0a6d5a378bcc12562201574b4_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5972aa0536798a0a6d5a378bcc12562201574b4.png 2x" data-dominant-color="EBECEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1111×674 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
