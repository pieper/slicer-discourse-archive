---
topic_id: 25935
title: "Get Rotation Angles From Transform Matrix"
date: 2022-10-27
url: https://discourse.slicer.org/t/25935
---

# Get rotation angles from transform matrix

**Topic ID**: 25935
**Date**: 2022-10-27
**URL**: https://discourse.slicer.org/t/get-rotation-angles-from-transform-matrix/25935

---

## Post #1 by @domP (2022-10-27 15:12 UTC)

<p>Operating system: Windows 11 Home<br>
Slicer version: 5.0.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello everybody,<br>
I’m in trouble with the module ‘Transforms’ in 3D Slicer. My goal is to compare the transform matrix obtained after a “Landmarks Registration” with the one obtained with a manual registration in terms of Eulero angles and translations.<br>
However, these values are not congruent with a visual aligment because transform matrix, as I read in the documentation, is composed by concatenated rotations etc.<br>
So, is there a way to know the “real” transform matrix (i.e. the overall Eulero angles and translations needed to align two volumes ) from the one showed in 3D Slicer?</p>

---

## Post #2 by @pieper (2022-10-27 16:50 UTC)

<p>It’s not clear what you mean by “real” here, since Euler angles are not uniquely defined for any given rotation matrix.  The Transform matrix is the ‘real’ transform.  If you want the pure rotation you could decompose the rotation into a unit quaternion.</p>

---

## Post #3 by @lassoan (2022-10-27 23:41 UTC)

<p><a href="https://github.com/PerkLab/SlicerSandbox#Characterize-transform-matrix">Characterize Transform Matrix module</a> in Sandbox extension can provide one such decomposition.</p>

---

## Post #4 by @domP (2022-10-28 11:16 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
let me explain better. The goal for my project is to quantify the Landmarks registration’s result as compared to a manual registration’s one.<br>
The Landmarks registration’s transform is:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15ae382573f34fd974938558c68d2e3c42530807.png" alt="transform_reg" data-base62-sha1="35NhYY2XqLidU6JEQi5Mk81XbYr" width="527" height="143"></p>
<p>while the manual’s one is:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6cccb20f9d63905bbf7eca441742fcbb2817aaa.png" alt="transform_manual" data-base62-sha1="q57FoizthqpbT2DngylG2FU8cwq" width="522" height="120"></p>
<p>So I decided to compute the difference between the two transform matrix.<br>
This is the result in Eulero Angles’ terms and translations computed in Matlab:</p>
<ul>
<li>Eulero angles: [3.1972   ,  3.4554   ,   2.1101] in degree [°] (absolute values)</li>
<li>Translation: [155.3490   , 18.5039  ,  54.7138] in [mm] (absolute values)</li>
</ul>
<p>However, it seems that these values are incogruent with the the visual alignment.<br>
Below an example of overlap of the two volumes. In the foreground visualization there’s the US volume while in the background visualization the CT one. The first row refers to landmarks registration, the second row refers to manual registration.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb0f224af3446bf97d306c8e97a9c33a318ca31c.jpeg" data-download-href="/uploads/short-url/sYllKG0Wj30zyyMp2BmsDufL6zi.jpeg?dl=1" title="reg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb0f224af3446bf97d306c8e97a9c33a318ca31c_2_689x423.jpeg" alt="reg" data-base62-sha1="sYllKG0Wj30zyyMp2BmsDufL6zi" width="689" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb0f224af3446bf97d306c8e97a9c33a318ca31c_2_689x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb0f224af3446bf97d306c8e97a9c33a318ca31c_2_1033x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb0f224af3446bf97d306c8e97a9c33a318ca31c.jpeg 2x" data-dominant-color="363534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">reg</span><span class="informations">1371×842 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to solve this ambiguity?</p>
<p>Thanks.</p>

---

## Post #5 by @lassoan (2022-10-28 12:42 UTC)

<p>You cannot characterize registration quality by analyzing the registration transforms or the difference between the transforms. The Eluer angles are only meaningful if you have one large rotation angle (there can be a second angle close to zero, and a third angle very close to zero). The translation component does not mean much if there is rotation because the actual position difference depends a lot on distance from the center of rotation and the rotation angles.</p>
<p>Instead, the most commonly used clinically relevant registration evaluation metric is target registration error (TRE) computed from average distance of clearly identifiable landmark points near the region of interest. For 3D cardiac echo to CT/MRI registration you can use the commissure points along the annulus. For a tricuspid valve it would give you 3 points, which is sufficient. For a bicuspid valve you would only get 2 commissure points, so you would need to identify at least one more point along the annulus, approximately halfway between the commissures.</p>
<aside class="quote no-group" data-username="domP" data-post="4" data-topic="25935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/domp/48/17086_2.png" class="avatar"> domP:</div>
<blockquote>
<p>The first row refers to landmarks registration, the second row refers to manual registration.</p>
</blockquote>
</aside>
<p>What do you mean by “manual registration”? Iteratively translating rotating one image to try to visually align with the other? That’s just a very time-consuming, tedious, and inaccurate procedure that should not be even considered for 3D registration. Such manual visual alignment procedure works well for 2D images, because it is a direct method (or just requires very few iterations) in 2D and you need to look at only one image. However, visual alignment usually requires many iterations in 3D, because translation has 3 axes instead of 2, and rotation has 3 axes instead of just 1, and you need to keep looking at least two views in different orientations and may even need to scroll through them for each iteration, and there is no guarantee that your results get better with each iteration.</p>

---
