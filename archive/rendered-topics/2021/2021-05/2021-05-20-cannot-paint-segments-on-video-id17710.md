---
topic_id: 17710
title: "Cannot Paint Segments On Video"
date: 2021-05-20
url: https://discourse.slicer.org/t/17710
---

# Cannot paint segments on video

**Topic ID**: 17710
**Date**: 2021-05-20
**URL**: https://discourse.slicer.org/t/cannot-paint-segments-on-video/17710

---

## Post #1 by @caesarsalad (2021-05-20 08:18 UTC)

<p>Hello,</p>
<p>I am very new to this software and it seems like I’m having a similar issue.<br>
However, the painting doesn’t work either. Whenever I draw/paint then let go, the drawn area just disappears.<br>
Should probably let you know that the files I’m working with have an error " Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>
<p>Reference image in series does not contain geometry information. Please use caution."</p>
<p>I don’t know if this is what’s making the annotations disappear. If you have any ideas on why this may be that would be great.</p>
<p>Below is a screenshot of the issue (I can draw/paint, but once I release the mouse or right click, the area doesn’t get shaded but just disappears)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa7cbce10aff6c586a1fdc8d253cd860df4fbc16.jpeg" data-download-href="/uploads/short-url/okcq0yr2D1cjiURq5KC6L0y5wfY.jpeg?dl=1" title="Screen Shot 2021-05-20 at 5.21.52 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa7cbce10aff6c586a1fdc8d253cd860df4fbc16_2_573x499.jpeg" alt="Screen Shot 2021-05-20 at 5.21.52 PM" data-base62-sha1="okcq0yr2D1cjiURq5KC6L0y5wfY" width="573" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa7cbce10aff6c586a1fdc8d253cd860df4fbc16_2_573x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa7cbce10aff6c586a1fdc8d253cd860df4fbc16_2_859x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa7cbce10aff6c586a1fdc8d253cd860df4fbc16_2_1146x998.jpeg 2x" data-dominant-color="694139"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-05-20 at 5.21.52 PM</span><span class="informations">1530×1334 607 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2021-05-20 12:13 UTC)

<p>Do you see any errors or warnings in the application log?</p>
<p>If not, then most probably the segmentation’s geometry does not overlap with the image. This happens for example, when you create the segmentation with a different image than the one that you are trying to segment. You can fix it as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a> or re-create the segmentation (for example, save the image as nrrd, restart the application, load that saved nrrd, then go to Segment Editor).</p>
<p>Can you share a sample data so that we can investigate the DICOM import?</p>
<p>If you just need 2D area measurement then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#place-new-markups">placing closed curve markups</a> and enabling area measurement might be easier than creating segmentation.</p>

---
