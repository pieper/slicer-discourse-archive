# How to perform 2d~3d registration

**Topic ID**: 28730
**Date**: 2023-04-03
**URL**: https://discourse.slicer.org/t/how-to-perform-2d-3d-registration/28730

---

## Post #1 by @zhang-qiang-github (2023-04-03 14:27 UTC)

<p>Does slicer provide a tool for 2d-3d registration?</p>
<p>I have a 3D CTA and a 2D US, and I want to perform a registration. Is it possible?</p>

---

## Post #2 by @lassoan (2023-04-03 15:54 UTC)

<p>Do you want to register a single ultrasound image or a translational or rotational sweep? Can you attach a position tracker (optical or electromagnetic, e.g., those that are supported by <a href="https://plustoolkit.github.io/features.html">Plus</a>/<a href="https://www.slicerigt.org/">SlicerIGT</a>) to your transducer?</p>

---

## Post #3 by @Nethrav22 (2024-04-11 21:30 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I wanted to bring up this discussion as I am trying to solve a similar problem. I have a 2D image and a 3D volume that I’m trying to register together. Similar anatomy is clearly visible in both of these inputs, so I’m trying to perform registration using some type of feature matching or using landmarks. I don’t have additional tracker information as of right now. Is this supported in 3D Slicer? I mostly saw 3D-3D methods available in the registration module. Thanks in advance!</p>

---

## Post #4 by @lassoan (2024-04-12 22:08 UTC)

<p>In Slicer, everything is 3D. A slice is just a single-slice 3D volume that has its position and orientation defined in 3D. Therefore, you can use all 3D/3D image registration methods. Just make sure that you pre-align the images reasonably well (no more than 10mm and 10deg misalignment) and use the single-slice image as fixed image.</p>

---

## Post #5 by @Nethrav22 (2024-04-18 01:44 UTC)

<p>Thanks for your answer. I was able to get some initial success with the IGT fiducial registration wizard by selecting 3 corresponding points. However, when I try to increase the number of points and happen to get a fairly good transform between my fixed image to volume, the transformed fixed image is not visualized correctly and appears as a line (shown in the picture attached below). I saw in some of the previous posts you suggested to ensure that the proper orientation is chosen in the volume reslice driver, but even with that it still shows up as a line and not the full image. More specifically, I chose the axial orientation in the red browser but after I apply the registration transform, the view is changed to reformat and the visualization of the image is gone. Additionally, I tried to use some other registration techniques like BRAINS and sometimes the image does not even show as one of the input volume options. Do you have any suggestions on what to do to improve my 2D-3D registration results?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2bcc123662cfc4be636aa46ed0ca594c51c3e10.png" alt="image" data-base62-sha1="wlOjoCLXPaC7MXGbJbZszUfwdOg" width="368" height="222"></p>

---

## Post #6 by @lassoan (2024-04-19 04:20 UTC)

<p>This is all good. If you apply a transform to the single-slice image or you change the orientation of the slice view then the image should show up as a single line. You can click “Rotate to volume plane” bitton in the slice view controller to snap the slice view to the image axes.</p>

---

## Post #7 by @Ontheroad123 (2024-12-11 09:27 UTC)

<aside class="quote no-group" data-username="Nethrav22" data-post="5" data-topic="28730">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nethrav22/48/68493_2.png" class="avatar"> Nethrav22:</div>
<blockquote>
<p>GT fiducial registration wizard</p>
</blockquote>
</aside>
<p>hi, i don’t know how to register 2D-3D, do you have any advice, thanks</p>

---

## Post #8 by @lassoan (2024-12-15 05:17 UTC)

<p>Fiducial Registration wizard should be fairly straightforward to use. Probably you can find many tutorials online (check out SlicerIGT and SlicerMorph tutorials and search on YouTube). You can always ask specific questions here (describe your overall goal, the steps you did, what you expected to happen, and what happened instead).</p>

---
