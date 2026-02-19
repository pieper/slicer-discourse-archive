---
topic_id: 29556
title: "Issue With Exporting Seg Dicom Files"
date: 2023-05-20
url: https://discourse.slicer.org/t/29556
---

# issue with exporting seg Dicom files 

**Topic ID**: 29556
**Date**: 2023-05-20
**URL**: https://discourse.slicer.org/t/issue-with-exporting-seg-dicom-files/29556

---

## Post #1 by @mustafa_magdy (2023-05-20 17:53 UTC)

<p>i downloaded Data from TCIA and its already have a seg results.</p>
<p>what i want to do is exporting the segmented lesion out of the whole volume as dicom file to start working on it.<br>
what i’m getting after exporting the file is the segmented area without any data only empty contour.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b350e585f6b76cb8c8aefd4d5fed415c7449f62.png" data-download-href="/uploads/short-url/d0R7ymKRwxEsOTA6Q5eBu0cfAPM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b350e585f6b76cb8c8aefd4d5fed415c7449f62_2_690x359.png" alt="image" data-base62-sha1="d0R7ymKRwxEsOTA6Q5eBu0cfAPM" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b350e585f6b76cb8c8aefd4d5fed415c7449f62_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b350e585f6b76cb8c8aefd4d5fed415c7449f62_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b350e585f6b76cb8c8aefd4d5fed415c7449f62.png 2x" data-dominant-color="535252"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×711 42.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-05-20 23:12 UTC)

<aside class="quote no-group" data-username="mustafa_magdy" data-post="1" data-topic="29556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mustafa_magdy/48/66028_2.png" class="avatar"> mustafa_magdy:</div>
<blockquote>
<p>what i want to do is exporting the segmented lesion out of the whole volume as dicom file to start working on it</p>
</blockquote>
</aside>
<p>What work would you like to do on it?<br>
I’m what software?<br>
What DICOM information objects that software can read - CT, Segmentation, RT structure set,…?</p>

---

## Post #3 by @mustafa_magdy (2023-05-20 23:42 UTC)

<p>i want to use it for ML for extracting the features of each voxel to make it able to differentiate tumors<br>
i’m runinng python script on juypter.</p>

---

## Post #4 by @lassoan (2023-05-21 00:09 UTC)

<p>DICOM is great as an archival and data exchange file format, but not as a working file format. To train an AI model you would normally convert input images from DICOM to NRRD or other research file formats that are simpler and more efficient than DICOM.</p>
<p>You don’t need to deal with DICOM until the very end of your project, when you deploy your tool to hospitals for clinical use. If you deploy your model using an application framework (such as 3D Slicer) then you don’t need to think about DICOM even then, aS the framework takes care of DICOM import/export.</p>

---

## Post #5 by @mustafa_magdy (2023-05-21 01:25 UTC)

<p>that’s great to know thank you for saving my time.<br>
but<br>
the issue remain that when i export nrrd i dont get info about the real lesion its just empty photos<br>
the pixels are 0 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bf0b73f96a6ee0b5eecc906dcd80203094ab706.png" data-download-href="/uploads/short-url/8yfTVk7WjRjr8vWWFAgecugrOIK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bf0b73f96a6ee0b5eecc906dcd80203094ab706_2_690x366.png" alt="image" data-base62-sha1="8yfTVk7WjRjr8vWWFAgecugrOIK" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bf0b73f96a6ee0b5eecc906dcd80203094ab706_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bf0b73f96a6ee0b5eecc906dcd80203094ab706_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bf0b73f96a6ee0b5eecc906dcd80203094ab706.png 2x" data-dominant-color="84848A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×725 54.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2023-05-21 03:33 UTC)

<p>Usually you use the original images and segmentations (that you call “empty photos” that contain discrete label values) as training data for your network.</p>

---
