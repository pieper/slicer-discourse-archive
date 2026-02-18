# Segmentation operation takes too long for virtual reality

**Topic ID**: 8394
**Date**: 2019-09-11
**URL**: https://discourse.slicer.org/t/segmentation-operation-takes-too-long-for-virtual-reality/8394

---

## Post #1 by @Netta_Z (2019-09-11 20:25 UTC)

<p>Hi, I’m having the same issue on my end where virtual reality screen goes into a loading screen when the subtract logical operator is activated to remove the overlapping segmentation (the rendered model from imaging and the controller model). Smoothing has been turned off and the update rate in Virtual Reality module has been set to the the fastest speed, and yet the loading screen still appears for 3s before the updated model is shown, about the same duration as before the parameters were changed. Could you give me some advice as to how to avoid this? I would like to see the pre-rendered model in virtual reality even when it’s rendering slowly, but a shorter rendering time would be ideal.</p>
<p>Running on slicer 4.10.2!</p>

---

## Post #2 by @lassoan (2019-09-12 01:46 UTC)

<p>If model generation takes 3 seconds without smoothing then most probably you have complex segments. Certain operations, such as thresholding tend to generate very complex segments because it creates thousands of tiny speckles and uneven edges. You can remove these by using the Smoothing effect / Median method before creating 3D models.</p>
<p>You may also improve overall performance by cropping and/or downsampling the master volume.</p>
<p>Also, try recent preview versions of Slicer, there may have been performance improvements that are relevant for you.</p>
<p>In the future, we might consider off-loading 3D model generation to a background thread to improve responsiveness of the application, but since updates are already quite fast (when surface smoothing is disabled), this task does not have very high priority.</p>

---

## Post #3 by @lassoan (2019-09-16 01:41 UTC)

<p>4 posts were split to a new topic: <a href="/t/segment-resolution-changes-after-subtraction/8439">Segment resolution changes after subtraction</a></p>

---
