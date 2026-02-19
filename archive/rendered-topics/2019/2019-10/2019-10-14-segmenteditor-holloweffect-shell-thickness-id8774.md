---
topic_id: 8774
title: "Segmenteditor Holloweffect Shell Thickness"
date: 2019-10-14
url: https://discourse.slicer.org/t/8774
---

# SegmentEditor HollowEffect - Shell thickness

**Topic ID**: 8774
**Date**: 2019-10-14
**URL**: https://discourse.slicer.org/t/segmenteditor-holloweffect-shell-thickness/8774

---

## Post #1 by @YsrH (2019-10-14 15:46 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1</p>
<p>As I was trying to understand the parameters (especially the shell thickness) of the HollowEffect. I created a cube of 7x7x7 and applied the effect with a 3x3x3 kern size (2-4 mm). I am sure that the kern size is the smallest one, but the result had a thickness of 1 pixel (1 mm and not 2-4 mm). and as well if I determine the shell thickness between 4 and 6 mm, I get a cube with a thickness of 2 mm (2 pixels).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec4bc334d6a2e7f13aee49b21c8fe91476f76282.png" data-download-href="/uploads/short-url/xIn0dp5Gf4tCryq3gIIMhdIWgzU.png?dl=1" title="after%20Hollow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4bc334d6a2e7f13aee49b21c8fe91476f76282_2_628x500.png" alt="after%20Hollow" data-base62-sha1="xIn0dp5Gf4tCryq3gIIMhdIWgzU" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4bc334d6a2e7f13aee49b21c8fe91476f76282_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4bc334d6a2e7f13aee49b21c8fe91476f76282_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec4bc334d6a2e7f13aee49b21c8fe91476f76282_2_1256x1000.png 2x" data-dominant-color="2C2D37"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after%20Hollow</span><span class="informations">1313×1044 23.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am useing a segment’s spacing of 1 mm per pixel.</p>
<p>may I politely say that maybe the “shellThicknessMm” should be by 2 divided, if it’s not the case, could you please explain the results to me.</p>
<p>I am thankful for your answer</p>

---

## Post #2 by @lassoan (2019-10-14 22:05 UTC)

<p>Thanks for reporting this. Indeed, while the used kernel size was correctly displayed, it was not the closest match to what was requested. I’ve fixed this now. The fix is available in Slicer Preview Release that you download tomorrow or later (revision 28547 or above).</p>

---
