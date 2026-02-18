# Automatic point setting of bone structures in DICOMs

**Topic ID**: 15125
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/automatic-point-setting-of-bone-structures-in-dicoms/15125

---

## Post #1 by @DICOMonist (2020-12-17 22:11 UTC)

<p>Hey there,<br>
Someone in here editing DICOMs? I want to determine the lowest point of the mandibular ramus (gradient = 0) in a 3D-reconstruction DICOM file.<br>
So I already seperarated the section of the ramus via python in a converted DICOM (512/512 pixel) file to make it a bit easier, because now there’s just one curve (the ramus) in there to analyze.<br>
But I didn’t find out how to program an algorithm to automatically get the lowest point in the curve.<br>
I know its a bit specific, but maybe someone here managed to detect a specific point in a (bone) structure already. It would help a lot.<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2020-12-17 23:10 UTC)

<aside class="quote no-group" data-username="DICOMonist" data-post="1" data-topic="15125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/7feea3/48.png" class="avatar"> DICOMonist:</div>
<blockquote>
<p>Someone in here editing DICOMs?</p>
</blockquote>
</aside>
<p>Yes, most of us here do.</p>
<aside class="quote no-group" data-username="DICOMonist" data-post="1" data-topic="15125">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/7feea3/48.png" class="avatar"> DICOMonist:</div>
<blockquote>
<p>I want to determine the lowest point of the mandibular ramus (gradient = 0) in a 3D-reconstruction DICOM file.</p>
</blockquote>
</aside>
<p>Gradient would be 0 for all the local minima and would not be robust on a noisy, imperfect mesh or curve. A simpler way to get minimum point position by getting the minimum coordinate value along a selected axis.</p>
<p>You can get all coordinates of points of a model node using <code>slicer.util.arrayFromModelPoints()</code>. You can then use standard numpy operations to get the position of the “lowest” point:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np
points = slicer.util.arrayFromModelPoints(modelNode)
minZ = points[:,2].min()
minIndex = np.where(points[:,2]==minZ)[0]
minPoint = points[minIndex]
print(minPoint)
</code></pre>
<p>If you did not segment the image but just specified a curve then you can get its points by calling <code>points=slicer.util.arrayFromMarkupsCurvePoints(curveNode)</code>.</p>

---

## Post #3 by @DICOMonist (2020-12-18 09:27 UTC)

<p>Hello,<br>
First of all thanks for your quick response.<br>
This is great!<br>
But Im still not sure how to select one ramus out of the sector.<br>
I added some images to show you my problem.<br>
The sticking point is the red cross (3rd picture) on the ramus I posted in the first picture (I managed to seperate this ramus as you see in the second picture). Maybe this helps a bit.</p>
<p>Kind regards.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19c0865f0f8906b6058ec78af55ccfc47669bdf7.jpeg" data-download-href="/uploads/short-url/3FOq0ifT2paDCk9KJbwMDXfTEjB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19c0865f0f8906b6058ec78af55ccfc47669bdf7_2_231x500.jpeg" alt="image" data-base62-sha1="3FOq0ifT2paDCk9KJbwMDXfTEjB" width="231" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19c0865f0f8906b6058ec78af55ccfc47669bdf7_2_231x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19c0865f0f8906b6058ec78af55ccfc47669bdf7_2_346x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19c0865f0f8906b6058ec78af55ccfc47669bdf7_2_462x1000.jpeg 2x" data-dominant-color="B7A896"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">828×1792 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
!<br>
<a href="/uploads/short-url/rJDgb2Mc7foH4zcmliEIBwi8nJN.jpeg">Test|690x403</a> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc1317f677f7a9502770399002dad111fd3728e.jpeg" data-download-href="/uploads/short-url/8wC5j307GoWuFYAKG0QH4p9pOzA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bc1317f677f7a9502770399002dad111fd3728e_2_231x500.jpeg" alt="image" data-base62-sha1="8wC5j307GoWuFYAKG0QH4p9pOzA" width="231" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bc1317f677f7a9502770399002dad111fd3728e_2_231x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bc1317f677f7a9502770399002dad111fd3728e_2_346x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bc1317f677f7a9502770399002dad111fd3728e_2_462x1000.jpeg 2x" data-dominant-color="BDB0A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">828×1792 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-12-19 06:11 UTC)

<p>If you are looking for the most distal point along an arbitrary measurement axis then probably the easiest solution is to transform the curve to a coordinate system where that arbitrarily oriented axis is the z axis (you can create the transform similarly as in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials">this example</a>, but instead of passing the plane normal and planeX direction to SetSliceToRASByNTP, you would put them in columns of a homogeneous transformation matrix). You can then get the minimum z value (as I described above) to get the lowest position along the measurement axis.</p>
<p>Can you write a bit more about your clinical application? What is your end goal? Do you segment the bone or just draw markups on the volume-rendered surface?</p>

---

## Post #5 by @DICOMonist (2020-12-19 11:43 UTC)

<p>Hello,<br>
So the goal is to know the lowest point of the mandibular ramus in every DICOM I want to analyze to find out what type of fracture (AO-Classification-System) it is. Therefor you have to know 1. The lowest point of the ramus Id showed in the picture 2. The outermost point of the lower (bigger) ramus (it is the lowest cross in the picture) and a second point of the ramus to draw a tangent. I marked three Red Cross in the picture: top left (this is the one we need to find out with help of the program because its the most difficult one to find out with the naked eye and its the most important one), bottom right (the lower outermost point of the ramus to draw the tangent) and any 3rd point at the ramus (3rd cross top right) to finish the tangent.<br>
Then we connect the 1st cross with the tangent (90°) and I can classify the fracture history and plan how to operate this type of fracture at the end.</p>

---

## Post #6 by @DICOMonist (2020-12-19 11:48 UTC)

<p>So first step: The 3D Slicer need to detect the right ramus to calculate the lowest point of it. And that’s my problem, because I don’t know to mark this specific ramus in a DICOM with lots of curves, angles …<br>
I hope its understandable for you, I do my really best.</p>

---

## Post #7 by @lassoan (2020-12-19 21:28 UTC)

<p>You can display the volume in 3D using Volume Rendering (it will look similar to your screenshots above) and draw curves and lines on it. All quantifications (getting intersection points, extrém, etc) should be easily doable by a short Python script. Would this work for you?</p>

---

## Post #8 by @DICOMonist (2020-12-19 22:50 UTC)

<p>Yeah this would be really great! So how do we want to do this?<br>
I have a series of 50 original DICOMs and 49 (somehow I couldn’t convert the last picture) Python-converted DICOMs (the separated section of the ramus) (+Python and 3D-Slicer).<br>
Perhaps the best thing would be to show you the DICOMs if it is possible. What is the easiest way to try out for you? I am pretty open.<br>
Thank you very much in advance.<br>
I am very grateful for your help.</p>

---
