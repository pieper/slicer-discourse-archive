---
topic_id: 15598
title: "Ct Scan Problem As Shown In The Image"
date: 2021-01-19
url: https://discourse.slicer.org/t/15598
---

# CT scan problem, as shown in the image

**Topic ID**: 15598
**Date**: 2021-01-19
**URL**: https://discourse.slicer.org/t/ct-scan-problem-as-shown-in-the-image/15598

---

## Post #1 by @Moeka_Chan (2021-01-19 22:12 UTC)

<p>Hello,<br>
I install the latest Slicer. I loaded the CT scan images. They look somehow as follows… This problem happens after I used the new Slicer… How to edit the data in Slicer and make the image show correctly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20273bdbbf9ceb375a3aed93ff5c386368473f01.jpeg" data-download-href="/uploads/short-url/4ArkTVwc7lNrd9D2vmjQhXNXcYN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20273bdbbf9ceb375a3aed93ff5c386368473f01_2_690x326.jpeg" alt="image" data-base62-sha1="4ArkTVwc7lNrd9D2vmjQhXNXcYN" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/20273bdbbf9ceb375a3aed93ff5c386368473f01_2_690x326.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20273bdbbf9ceb375a3aed93ff5c386368473f01.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20273bdbbf9ceb375a3aed93ff5c386368473f01.jpeg 2x" data-dominant-color="2E2F2D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">983×465 69.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-19 22:13 UTC)

<p>You need to load DICOM images using the DICOM module as described here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene</a></p>

---
