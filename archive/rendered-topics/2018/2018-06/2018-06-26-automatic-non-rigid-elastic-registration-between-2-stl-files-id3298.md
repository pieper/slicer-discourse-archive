# Automatic non-rigid (elastic) registration between 2 stl files

**Topic ID**: 3298
**Date**: 2018-06-26
**URL**: https://discourse.slicer.org/t/automatic-non-rigid-elastic-registration-between-2-stl-files/3298

---

## Post #1 by @DavideBassano (2018-06-26 10:26 UTC)

<p>Hello,</p>
<p>I have 2 .stl volumes (let’s call them fixed and moving).<br>
I would like to warp the moving volume above the fixed volume with an automatic registration (so without fiducials, landmarks, … or with a very small number of points).<br>
These 2 volumes are already aligned and overlapped, so I just need to warp the moving volume to fit (or adapt) the fixed volume.</p>
<p>Does exist a way I can do it?</p>
<p>Thanks,</p>
<p>Davide Bassano</p>

---

## Post #2 by @timeanddoctor (2018-06-26 11:36 UTC)

<p>you can transform under 3d view with handly and the models should be transparent.</p>

---

## Post #3 by @cpinter (2018-06-26 11:52 UTC)

<p>If you have anatomical volumes as well, you can use the SegmentRegistration extension. You need to load the STLs as segmentations, not models. You can change it in the loading screen.</p>
<p>If you only have the STLs then you can use the ModelRegistration module in the SlicerIGT extension.</p>
<p>Let us know how it goes.</p>

---

## Post #4 by @DavideBassano (2018-06-26 12:34 UTC)

<p>Thanks for your fast reply.</p>
<p>I only have the STLs, so I used the ModelRegistration Module in IGT.<br>
The problem is that it only gives linear transformations as output, but I need to warp/adapt my moving volume to the fixed one, so I’d like a non-linear transformation because I’m trying to do a non-rigid registration.<br>
How can I do?</p>
<p>Thanks</p>
<p>Davide</p>

---

## Post #5 by @cpinter (2018-06-26 15:10 UTC)

<p>Good point. In this case the only way I can think of is to create two volumes for each model, and use Segment Registration. You only need the volumes to have a grid that the volume-based distance map registration can use.</p>
<p>I don’t have time now but the first idea that comes to mind is to load a sample dataset, and move it to overlap the models (create transform, set as parent, show volume in volume rendering, show ROI, see if it overlaps). Then harden the transform, clone that volume in Data module, and use those two for Segment Registration.</p>
<p>I’m in the process of implementing an easy way to specify volume geometry from segmentations/models/etc, but it’s not ready yet and will be even more time before we can use it to create empty reference volumes, so for the time being we have to use an existing volume for example as I described above.</p>
<p>Others feel free to chime in.<br>
Good luck!</p>

---

## Post #6 by @DavideBassano (2018-06-26 15:24 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="3298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>create two volumes</p>
</blockquote>
</aside>
<p>I have a problem when importing .stl files as “volume”: I can select “volume” when importing, but then they don’t appear in the Data Module, thus in Volume Rendering Module I can’t select them. If I import them as module, instead, it works.<br>
Why does this happen?</p>
<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="3298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>to load a sample dataset,</p>
</blockquote>
</aside>
<p>With “dataset” you mean the stl files?</p>
<p>Thank you</p>
<p>Davide</p>

---

## Post #7 by @cpinter (2018-06-26 15:41 UTC)

<p>You cannot open STL as volume, as they are surface meshes. You can only open them as model or segmentation. When I said sample dataset I meant volumes from the Sample Data module (you can find it in the Welcome module too).</p>

---

## Post #8 by @jkearns (2021-06-23 04:45 UTC)

<p>Davide,</p>
<pre><code> Did you ever come to a resolution for this problem? I am interested in a mapping that is similar to what you describe (I believe) so that I can get a series of transformation coordinates to inform the moving mesh of a simulation of the Left Ventricle in COMSOL. 

 I am a new user to this software, so any guidance is greatly appreciated. 
</code></pre>
<p>Cheers,<br>
John</p>

---

## Post #9 by @lassoan (2021-06-23 13:05 UTC)

<p>Once you loaded the STL file as segmentation, you can convert it to a volume by two clicks in Data module (right-click and choose to convert to labelmap).</p>

---
