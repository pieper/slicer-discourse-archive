# Convert vessel centerline model to image volume

**Topic ID**: 5906
**Date**: 2019-02-25
**URL**: https://discourse.slicer.org/t/convert-vessel-centerline-model-to-image-volume/5906

---

## Post #1 by @albert94 (2019-02-25 01:31 UTC)

<p>Hi all,</p>
<p>Is there a way to convert a 3D vessel centerline model into a 3D image volume? I segmented out the vascular centerline using 3D Slicer but I want to convert it into 3D image volume so that I could use use it in python as 3D array.<br>
Thanks a lot.</p>

---

## Post #2 by @lassoan (2019-02-25 03:14 UTC)

<p>You can access the centerline point positions from Python using <a href="http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util" rel="nofollow noopener"><code>slicer.util.arrayFromModelPoints()</code></a>.</p>
<p>To generate an image volume, you can create a tube model using “Markups to model” extension, import the generated model to a segmentation node, then export the segmentation to a labelmap volume node.</p>

---

## Post #3 by @albert94 (2019-02-26 09:39 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I appreciate your answer. But it seems that there’s something wrong.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fc4cb67c2138861fa58bd214a973a36c497d4eb.png" alt="1" data-base62-sha1="kvPUkStfSMB1yuiLy6PrpUlrTAv" width="439" height="261"><br>
As you can see the endpoints of these lines are connected in the generated model by “Markups to model” extension. But this is not I wanted. Did I miss something?</p>

---
