# Editing existing atlas/point cloud

**Topic ID**: 8493
**Date**: 2019-09-19
**URL**: https://discourse.slicer.org/t/editing-existing-atlas-point-cloud/8493

---

## Post #1 by @Yaqub_Jonmohamadi (2019-09-19 03:22 UTC)

<p>Operating system: Ubuntu 16<br>
Slicer version: 4.10.2 r28257</p>
<p>Hi there,<br>
I am pretty new to the 3D Slicer.</p>
<p>I have two questions:</p>
<ol>
<li>
<p>I have a point cloud that I created using my stereo endoscope and I would like to modify it using the Slicer, specifically using the scissor. How can I do that? I just managed to upload and show it in the Slicer, but couldn’t figure out how to use the editing tools.</p>
</li>
<li>
<p>My second question is similar to the first, I have downloaded the knee atlas (KneeAtlas-2015Sept-Slicer4-4Version.mrb) and I would like to modify some of the segments in that atlas. Again I couldn’t figure out how to use the scissor or other editing tools. They just don’t turn on and are all off when I select segments of the atlas.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abf914ac56816427025e595d0aebcbe096d795ca.jpeg" data-download-href="/uploads/short-url/oxliD89EeN8V0C1hPaTlIwy23Sq.jpeg?dl=1" title="Screenshot%20from%202019-09-19%2011-55-50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf914ac56816427025e595d0aebcbe096d795ca_2_690x425.jpeg" alt="Screenshot%20from%202019-09-19%2011-55-50" data-base62-sha1="oxliD89EeN8V0C1hPaTlIwy23Sq" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf914ac56816427025e595d0aebcbe096d795ca_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf914ac56816427025e595d0aebcbe096d795ca_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abf914ac56816427025e595d0aebcbe096d795ca_2_1380x850.jpeg 2x" data-dominant-color="A5A5B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-09-19%2011-55-50</span><span class="informations">1463×903 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>Thank you for your time.<br>
Yaqub</p>

---

## Post #2 by @lassoan (2019-09-19 03:31 UTC)

<aside class="quote no-group" data-username="Yaqub_Jonmohamadi" data-post="1" data-topic="8493">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yaqub_jonmohamadi/48/4774_2.png" class="avatar"> Yaqub_Jonmohamadi:</div>
<blockquote>
<p>I have a point cloud that I created using my stereo endoscope and I would like to modify it using the Slicer, specifically using the scissor. How can I do that? I just managed to upload and show it in the Slicer, but couldn’t figure out how to use the editing tools.</p>
</blockquote>
</aside>
<p>Segment Editor is developed for editing solid objects (closed surfaces) and some effects require an underlying volumetric image. If you only have surface patches from an endoscope then your editing options are quite limited. What would you like to do?</p>
<aside class="quote no-group" data-username="Yaqub_Jonmohamadi" data-post="1" data-topic="8493">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yaqub_jonmohamadi/48/4774_2.png" class="avatar"> Yaqub_Jonmohamadi:</div>
<blockquote>
<p>I have downloaded the knee atlas (KneeAtlas-2015Sept-Slicer4-4Version.mrb) and I would like to modify some of the segments in that atlas.</p>
</blockquote>
</aside>
<p>Import the models into a segmentation node to edit them using Segmentations module (Import/export section).</p>

---

## Post #3 by @Yaqub_Jonmohamadi (2019-09-19 04:44 UTC)

<p>Hi Andras,</p>
<p>Thanks for the reply.</p>
<p>I believe I already did import (atlas) models into the Segmentation Node. You can see in the screenshot that I attached in the original question it is showing the Segmentation Editor window. When I click on the Segments I expect the editing tools become activated but that does not happen.</p>
<p>Regarding the endoscope point cloud, I would like to register it to the MRI images (the endoscope is capturing parts of the femur). It looks like that I should convert my point cloud (.ply) to other formats in order to be able to do that, is that right?</p>
<p>Thanks for your time.<br>
Yaqub</p>

---

## Post #4 by @lassoan (2019-09-19 12:35 UTC)

<aside class="quote no-group" data-username="Yaqub_Jonmohamadi" data-post="3" data-topic="8493">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yaqub_jonmohamadi/48/4774_2.png" class="avatar"> Yaqub_Jonmohamadi:</div>
<blockquote>
<p>When I click on the Segments I expect the editing tools become activated but that does not happen.</p>
</blockquote>
</aside>
<p>Thanks for the clarification. As the message in the module shows, you need to “Select master volume to enable editing”. See instructions here: <a href="https://discourse.slicer.org/t/issue-during-voxelization-of-a-model-stl/7687/2" class="inline-onebox">Issue during voxelization of a model stl - #2 by lassoan</a></p>
<aside class="quote no-group" data-username="Yaqub_Jonmohamadi" data-post="3" data-topic="8493">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yaqub_jonmohamadi/48/4774_2.png" class="avatar"> Yaqub_Jonmohamadi:</div>
<blockquote>
<p>I would like to register it to the MRI images (the endoscope is capturing parts of the femur)</p>
</blockquote>
</aside>
<p>You can register surface of a segmented image with a surface scan using modules in SlicerIGT extension. You can either specify landmark points manually and compute registration using in Fiducial registration wizard module. You may also try to use Surface registration module to match surfaces automatically: for this you need a good initial position and surface model that does not have any extra/incorrect surface patches.</p>

---
