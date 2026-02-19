---
topic_id: 40349
title: "Scan Misaligned With Global Coordinate System"
date: 2024-11-23
url: https://discourse.slicer.org/t/40349
---

# Scan Misaligned with Global Coordinate System

**Topic ID**: 40349
**Date**: 2024-11-23
**URL**: https://discourse.slicer.org/t/scan-misaligned-with-global-coordinate-system/40349

---

## Post #1 by @ppech17 (2024-11-23 16:07 UTC)

<p>Hello,</p>
<p>I have a question regarding the following image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4428a0a174e3892a9023587a5635d2cbd2ea431a.jpeg" data-download-href="/uploads/short-url/9IXvJReA6Ppg1EKkUV2uHoy3DnA.jpeg?dl=1" title="example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4428a0a174e3892a9023587a5635d2cbd2ea431a_2_690x372.jpeg" alt="example" data-base62-sha1="9IXvJReA6Ppg1EKkUV2uHoy3DnA" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4428a0a174e3892a9023587a5635d2cbd2ea431a_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4428a0a174e3892a9023587a5635d2cbd2ea431a_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4428a0a174e3892a9023587a5635d2cbd2ea431a_2_1380x744.jpeg 2x" data-dominant-color="383841"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example</span><span class="informations">1500×809 75.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I load DICOM data, it is not aligned with the global coordinate system. I’m new to 3D Slicer and have looked at some yt videos about transforms but haven’t found a similar issue.<br>
Any help would be much appreciated!</p>

---

## Post #2 by @pieper (2024-11-23 16:15 UTC)

<p>That’s normal.  It just means the scan was acquired with a rotation to follow the anatomy.</p>

---

## Post #3 by @ppech17 (2024-11-24 08:57 UTC)

<p>Thank you very much for your reply. Is there a way to fix this misalignment?</p>

---

## Post #4 by @cpinter (2024-11-24 12:36 UTC)

<p>This is not a misalignment to fix, this is just how this dataset was acquired. Why do you want to rotate it?</p>

---
