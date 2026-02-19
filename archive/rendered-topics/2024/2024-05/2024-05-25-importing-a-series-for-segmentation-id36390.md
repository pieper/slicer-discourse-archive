---
topic_id: 36390
title: "Importing A Series For Segmentation"
date: 2024-05-25
url: https://discourse.slicer.org/t/36390
---

# Importing A Series for Segmentation

**Topic ID**: 36390
**Date**: 2024-05-25
**URL**: https://discourse.slicer.org/t/importing-a-series-for-segmentation/36390

---

## Post #1 by @Tinashe_Jambo (2024-05-25 14:48 UTC)

<p>I have been trying to import a series of Short axis MRI for a heart. There are 11 slices. I would like to segment these in 3D slicer and get a geometry. However When i import, it only imports 1 file in the series of 11. May you kindly assist. Here is a link to the files:  <a href="https://drive.google.com/drive/folders/1P73vX68TAMpn45BPVC3OUdR0k-eWhbL0?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">3D slicer - Google Drive</a></p>

---

## Post #2 by @pieper (2024-05-25 15:19 UTC)

<p>Thanks for sharing the anonymized data - I could replicate what you were seeing.  The issue is that each of the slices is a different dicom series, so Slicer doesn’t know to combine them.  I ran the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html">DICOMPatcher</a> with the option enabled to force the same series ID, and then I can load them:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73ba6543b709321feff8fd9eefbbe4e6d1f5a35a.jpeg" data-download-href="/uploads/short-url/gvMg6vjFjE2fOy2muxMIXmQbYqS.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73ba6543b709321feff8fd9eefbbe4e6d1f5a35a_2_690x411.jpeg" alt="image" data-base62-sha1="gvMg6vjFjE2fOy2muxMIXmQbYqS" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73ba6543b709321feff8fd9eefbbe4e6d1f5a35a_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73ba6543b709321feff8fd9eefbbe4e6d1f5a35a_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73ba6543b709321feff8fd9eefbbe4e6d1f5a35a_2_1380x822.jpeg 2x" data-dominant-color="9A9895"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1421×847 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note that there’s still some residual geometric inconsistency, so slicer warns and generates an acquisition transform to compensate.  You can examine the data and either use it without the transform or harden the transform.  It’s not clear to my eye which is more faithful to the anatomy.</p>
<p>Also note that there are 11 files in the directory you shared, but only 10 are images.</p>

---

## Post #3 by @Tinashe_Jambo (2024-05-27 05:41 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="36390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>faithful</p>
</blockquote>
</aside>
<p>Thank you so much, this will be helpful.</p>

---
