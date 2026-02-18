# How to slice along a curve and display it in 2D view in real time

**Topic ID**: 30711
**Date**: 2023-07-20
**URL**: https://discourse.slicer.org/t/how-to-slice-along-a-curve-and-display-it-in-2d-view-in-real-time/30711

---

## Post #1 by @slicer365 (2023-07-20 17:25 UTC)

<p>In the video, I need to constantly rotate the yellow line to make sure that the yellow line is basically perpendicular to the curve, and then I can see the result I want in the sagittal view.<br>
Is there any way to automatically set the yellow line to slide along the curve instead of a fixed straight line?<br>
If there is a way, I can write a small script or module, but I don’t know how to implement it now.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5de1fc82108ae7928cac05813f8a5562c6bf5d2f.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5de1fc82108ae7928cac05813f8a5562c6bf5d2f.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5de1fc82108ae7928cac05813f8a5562c6bf5d2f.mp4</a>
    </video>
  </div><p></p>

---

## Post #2 by @chir.set (2023-07-20 19:42 UTC)

<p>You might be looking for ‘Cross-section analysis’ module in SlicerVMTK extension. It can take an open curve as single input and reslice a specified slice view perpendicular to the curve.</p>

---
