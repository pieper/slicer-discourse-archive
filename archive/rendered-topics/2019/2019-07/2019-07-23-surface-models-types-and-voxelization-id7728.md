---
topic_id: 7728
title: "Surface Models Types And Voxelization"
date: 2019-07-23
url: https://discourse.slicer.org/t/7728
---

# Surface models types and voxelization

**Topic ID**: 7728
**Date**: 2019-07-23
**URL**: https://discourse.slicer.org/t/surface-models-types-and-voxelization/7728

---

## Post #1 by @Alessandro_Piol (2019-07-23 16:12 UTC)

<p>Hi all!</p>
<p>I have to convert a surface model stl into a voxelized mask, with 1s inside and 0s outside. It is important that the mask has the same dimensions and voxel size as another volume I want to register with. In Matlab the available functions don’t allow to specify voxel size and this is very important for me. Getting inspired by this post: <a href="https://discourse.slicer.org/t/voxelization-of-mesh/4942">Voxelization of mesh</a>, I follow these steps:</p>
<ol>
<li>Import stl and convert into segmentation node by right clicking on the model entry in the data module.</li>
<li>Import the other volume, and in the volume section specify the voxel size and center it.</li>
<li>Go to the transform model, and create a new transformation which moves the segmentation so that the crucial parts of it overlap the other volume. This step may not be needed.</li>
<li>Go to the Segmentation Module, and select export the segmentation as a labelmap, indicating as reference volume the other one, so that the output voxelized mask has the same dimensions and voxel size.</li>
<li>Then, go to the volume section, select the just created volume, and convert to scalar volume.</li>
</ol>
<p>I’d like to know if these steps are well or if there is another way to do it better. The stl model sometimes appears to be bigger than the object in the other volume, when it shouldn’t be. And other thing: should the stl model have some basis features (i.g. closed surface, filled inside etc.)?</p>

---

## Post #2 by @lassoan (2019-07-23 17:50 UTC)

<aside class="quote no-group" data-username="Alessandro_Piol" data-post="1" data-topic="7728">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alessandro_piol/48/4218_2.png" class="avatar"> Alessandro_Piol:</div>
<blockquote>
<p>I’d like to know if these steps are well or if there is another way to do it better.</p>
</blockquote>
</aside>
<p>The steps are correct.</p>
<p>You can write a script that performs all the steps without the need to use the GUI (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a>).</p>
<aside class="quote no-group" data-username="Alessandro_Piol" data-post="1" data-topic="7728">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alessandro_piol/48/4218_2.png" class="avatar"> Alessandro_Piol:</div>
<blockquote>
<p>The stl model sometimes appears to be bigger than the object in the other volume, when it shouldn’t be.</p>
</blockquote>
</aside>
<p>We test all the conversions very thoroughly and we are not aware any shift or scale issues. If you have doubts then send a data set (upload somewhere and post the link here) and explanation of what you expect and what you find instead.</p>
<aside class="quote no-group" data-username="Alessandro_Piol" data-post="1" data-topic="7728">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alessandro_piol/48/4218_2.png" class="avatar"> Alessandro_Piol:</div>
<blockquote>
<p>should the stl model have some basis features (i.g. closed surface, filled inside etc.)?</p>
</blockquote>
</aside>
<p>Surface to labelmap conversion is guaranteed to work if the surface is closed (watertight). STL is a surface mesh, so it cannot be filled inside. If the surface is not closed then it will be made a solid, watertight object “randomly”: the surface is sliced along the z axis and filled in line by line, so what parts and how will be filled depend on the object shape and orientation.</p>

---
