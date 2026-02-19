---
topic_id: 17498
title: "Accurate Way Of Measuring The Distance Of Tooth Cusp To Cej"
date: 2021-05-07
url: https://discourse.slicer.org/t/17498
---

# Accurate way of measuring the distance of tooth cusp to CEJ

**Topic ID**: 17498
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/accurate-way-of-measuring-the-distance-of-tooth-cusp-to-cej/17498

---

## Post #1 by @lazymark2 (2021-05-07 01:22 UTC)

<p>Hi everyone, recently I need to perform gingivoplasty to a patient with severe gingival hyperplasia. But the first thing I should do before the actual surgery is to mark the CEJ (cement-enamel-joint) on patient’s gingiva. As the image shows, I decide to measure the distance of tooth cusp to CEJ.<br>
For each tooth, I measured 6 points (buccal and palatal, mesial/middle/distal).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6799caad89148f41ebfc0cb4e1e0e038ffd3c5a.png" data-download-href="/uploads/short-url/nKHOnuMmSP0BhQoEz5jEVYAzU6u.png?dl=1" title="0210507085733" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6799caad89148f41ebfc0cb4e1e0e038ffd3c5a_2_650x500.png" alt="0210507085733" data-base62-sha1="nKHOnuMmSP0BhQoEz5jEVYAzU6u" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6799caad89148f41ebfc0cb4e1e0e038ffd3c5a_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6799caad89148f41ebfc0cb4e1e0e038ffd3c5a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6799caad89148f41ebfc0cb4e1e0e038ffd3c5a.png 2x" data-dominant-color="895F64"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0210507085733</span><span class="informations">768×590 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But when I tried to used the above data to perform surgery, I found out for the posterior teeth, the actual distance between the tooth cusp to CEJ is greater(1~2mm) to what I measured in the slicer 3D software. I think it might be caused by the curved surface. So I wonder if there is a more accurate way of measuring this kind of distance.</p>

---

## Post #2 by @lassoan (2021-05-21 18:19 UTC)

<p>If you want to measure distance along a curved surface then you can place a curve (with multiple points along the curved surface). Instead of placing points along a straight line manually, you can place a curve with just two points and then resample it on a surface using Markups module / Resample (set “Constrain points to surface” to the model node that you exported from the segmentation).</p>
<p>How did you measure the distance during surgery? Instead of making point measurements, using the Segment Editor module you could design a 3D-printable marking guide that you can snap to the teeth of the patient and would only leave the enamel part exposed.</p>

---
