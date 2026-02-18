# Create new series based on orientation

**Topic ID**: 39497
**Date**: 2024-10-02
**URL**: https://discourse.slicer.org/t/create-new-series-based-on-orientation/39497

---

## Post #1 by @mohammed_alshakhas (2024-10-02 15:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
i waste so much time going back and forth playing with orientation of slices e.g parasagitaal 30 20 etc.</p>
<p>i need to review images for both sides and different anlge serve different purposes . some purposes related to better view of  anatomy other for surgical reasons .</p>
<p>it would be a game changer to my workflow that i can do an orientation then save as new series.</p>
<p>please add it pleaaaase <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2024-10-02 16:49 UTC)

<p>This is already available. You can resample an image using Crop volume module (with a rotated ROI) or any of the volume resample modules and then export the new volume as a new DICOM series.</p>

---

## Post #3 by @mohammed_alshakhas (2024-10-03 04:24 UTC)

<p>i coulnt understand how to use resampling .</p>
<p>the crop+ oriented ROI is good but takes some steps . is there faster way i can use.</p>
<p>this is already good just trying to be more efficient</p>

---
