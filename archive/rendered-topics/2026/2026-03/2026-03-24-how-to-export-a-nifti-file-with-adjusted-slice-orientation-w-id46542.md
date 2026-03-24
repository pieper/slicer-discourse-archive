---
topic_id: 46542
title: "How To Export A Nifti File With Adjusted Slice Orientation W"
date: 2026-03-24
url: https://discourse.slicer.org/t/46542
---

# How to export a NIfTI file with adjusted slice orientation while keeping the original origin?

**Topic ID**: 46542
**Date**: 2026-03-24
**URL**: https://discourse.slicer.org/t/how-to-export-a-nifti-file-with-adjusted-slice-orientation-while-keeping-the-original-origin/46542

---

## Post #1 by @Ronald_Lu (2026-03-24 02:02 UTC)

<p>Hello everyone,</p>
<p>I am using 3D Slicer and would like to rotate the slice views (coordinate axes) to a specific orientation that better matches my anatomical reference. My goal is to export a new .nii file that preserves this adjusted orientation, while keeping the original coordinate origin unchanged.</p>
<p>Specifically:</p>
<ul>
<li>
<p>I used tools such as Toggle Slice Intersection Visibility and manual slice rotation to obtain the desired orientation.</p>
</li>
<li>
<p>Now I would like to save this orientation change into the NIfTI file, so that when the file is opened again (in Slicer or other software), the image appears in the same rotated coordinate system.</p>
</li>
<li>
<p>Importantly, I would like the world coordinate origin to remain unchanged, only the orientation should be updated.</p>
</li>
</ul>
<p>My core issue is:</p>
<ol>
<li>
<p>What is the correct workflow to save the adjusted orientation into the NIfTI file?</p>
</li>
<li>
<p>Should this be done using the Transforms module (e.g., hardening a transform)?</p>
</li>
<li>
<p>Are there any recommended best practices to avoid unintended changes in spacing, origin, or header information?</p>
</li>
</ol>
<p>Thank you very much for your help!</p>
<p>Best regards</p>
<p>This is the original orientation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a106c4fde126dfc5d0c6bcf5c85ab19da4e19b7.jpeg" data-download-href="/uploads/short-url/3IzBevjfQjhVvq2ue5YQ1GZhzIX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a106c4fde126dfc5d0c6bcf5c85ab19da4e19b7_2_645x500.jpeg" alt="image" data-base62-sha1="3IzBevjfQjhVvq2ue5YQ1GZhzIX" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a106c4fde126dfc5d0c6bcf5c85ab19da4e19b7_2_645x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a106c4fde126dfc5d0c6bcf5c85ab19da4e19b7_2_967x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a106c4fde126dfc5d0c6bcf5c85ab19da4e19b7_2_1290x1000.jpeg 2x" data-dominant-color="424148"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1413×1095 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This the orientation I would like to adjust</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87eca1079888aff0a69e98347025d076fec60dce.jpeg" data-download-href="/uploads/short-url/jorqTJbqNIpQsPIbmC7ZEn6mtBk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87eca1079888aff0a69e98347025d076fec60dce_2_646x500.jpeg" alt="image" data-base62-sha1="jorqTJbqNIpQsPIbmC7ZEn6mtBk" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87eca1079888aff0a69e98347025d076fec60dce_2_646x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87eca1079888aff0a69e98347025d076fec60dce_2_969x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87eca1079888aff0a69e98347025d076fec60dce_2_1292x1000.jpeg 2x" data-dominant-color="403F45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1413×1092 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
