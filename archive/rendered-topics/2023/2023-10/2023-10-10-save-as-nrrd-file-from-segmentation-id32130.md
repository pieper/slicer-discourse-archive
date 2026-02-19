---
topic_id: 32130
title: "Save As Nrrd File From Segmentation"
date: 2023-10-10
url: https://discourse.slicer.org/t/32130
---

# Save as nrrd file from segmentation

**Topic ID**: 32130
**Date**: 2023-10-10
**URL**: https://discourse.slicer.org/t/save-as-nrrd-file-from-segmentation/32130

---

## Post #1 by @Chuan (2023-10-10 09:06 UTC)

<p>Dear community,</p>
<p>I would like to report a problem related to export nrrd file from segmentation.<br>
When I open the saved nrrd file, all the CT value information are lost (either 1 or 0).<br>
See as figure below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/877fcd10d2f880bdb19cbc2c82e30119b9572034.png" data-download-href="/uploads/short-url/jkGgNC8cpUQLuYTp9ORfqHpjJwE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877fcd10d2f880bdb19cbc2c82e30119b9572034_2_690x207.png" alt="image" data-base62-sha1="jkGgNC8cpUQLuYTp9ORfqHpjJwE" width="690" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877fcd10d2f880bdb19cbc2c82e30119b9572034_2_690x207.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/877fcd10d2f880bdb19cbc2c82e30119b9572034_2_1035x310.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/877fcd10d2f880bdb19cbc2c82e30119b9572034.png 2x" data-dominant-color="8F8F8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×348 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I use is shown below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6ac80eb826710ee92c80149014f0e85da966a3.jpeg" data-download-href="/uploads/short-url/oSXRcAcptLF6FGJSPod0sRTKb0n.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae6ac80eb826710ee92c80149014f0e85da966a3_2_679x500.jpeg" alt="image" data-base62-sha1="oSXRcAcptLF6FGJSPod0sRTKb0n" width="679" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae6ac80eb826710ee92c80149014f0e85da966a3_2_679x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae6ac80eb826710ee92c80149014f0e85da966a3_2_1018x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae6ac80eb826710ee92c80149014f0e85da966a3.jpeg 2x" data-dominant-color="A5A19C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×978 90.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone meet the same problem as me?</p>
<p>Thank you very much in advance for any kinds of discussion and help</p>
<p>Best, Chuan</p>

---

## Post #2 by @Chuan (2023-10-10 09:07 UTC)

<p>I also try to add the reference volume, but still the original CT value information are missed</p>

---

## Post #3 by @lassoan (2023-10-10 10:28 UTC)

<p>The segmentation only stores labels. If you want to blank out regions of the original CT by segments then you can use the “Mask Volume” effect in Segment Editor.</p>

---

## Post #4 by @Chuan (2023-10-11 11:54 UTC)

<p>Thanks Lassoan, that works!</p>

---
