# Segmentation Not Centering

**Topic ID**: 36504
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/segmentation-not-centering/36504

---

## Post #1 by @MPARHAM (2024-05-30 19:57 UTC)

<p>Hi everyone,</p>
<p>I wanted to ask the community is familiar with a issue I am facing in 3D Slicer.<br>
Currently I am trying to continue my segmentation, but having troubles with viewing in the 3D space. With my segmentation, I initially open and the segmentation appears in the bottom-left corner. However, after hitting “center view” to center the model, the model instead goes to the upper right corner and shrinks. The segmentation in the other 3 axes do not shift and the pixels segmented remains, I believe it is a visual error.</p>
<p>Any help or discussion in troubleshooting this, would be very appreciative.</p>
<p>Thank you,<br>
Melton</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ce2ee3fcc6c1b5ac890a66077f1a730341604a.png" alt="Segmentation_Uncenetered" data-base62-sha1="rEtTCOfUUhJGLALWyrXGSL0D03E" width="528" height="324"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3766be93c4c263222ebc73eedac1a4b088f04e0.png" alt="Segmentation_Cornered" data-base62-sha1="pBBbpVfF91NB2z2Z4Z7OIFa92ne" width="573" height="362"></p>

---

## Post #2 by @lassoan (2024-05-31 00:15 UTC)

<p>The behavior looks correct. The view is centered on the segments visible in the 3D view. You can choose any other point as camera focus (center of rotation) by right-clicking in any slice or 3D view anywhere and then selecting “Refocus camera on this point” in the menu.</p>

---

## Post #3 by @MPARHAM (2024-05-31 05:44 UTC)

<p>Hi Iassoan,</p>
<p>I might be misinterpreting the software, but I do not think this is correct behavior. I usually press center view and the 3D model goes to the center of the box regardless of the position. As seen here. In the above situation, after I pressed that same button, the model moved to the upper corner<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c186810bcad0083768b419c97f793b1c79a2c604.png" alt="Centered" data-base62-sha1="rC0kb79Iis6jjUrQ3UsDnG4gckY" width="343" height="310"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c395280b66ca6c0f817ea8d1e165b2d7b94c4a8.png" alt="Uncentered" data-base62-sha1="fronvICBUNV0CUKFqh4d6RCq1Mk" width="684" height="448"></p>

---

## Post #4 by @lassoan (2024-05-31 21:07 UTC)

<p>The box includes the volume currently displayed in slice views.</p>

---

## Post #5 by @MPARHAM (2024-06-12 19:04 UTC)

<p>This issue may be solved in the following post: <a href="https://discourse.slicer.org/t/error-in-opening-files-using-slicer-5-6-2/36611/3" class="inline-onebox">Error in Opening Files using Slicer 5.6.2 - #3 by MPARHAM</a></p>

---
