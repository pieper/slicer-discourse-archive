---
topic_id: 36845
title: "Autoscoper Preprocessing For Volumes And Transforms"
date: 2024-06-17
url: https://discourse.slicer.org/t/36845
---

# Autoscoper PreProcessing for Volumes and Transforms

**Topic ID**: 36845
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/autoscoper-preprocessing-for-volumes-and-transforms/36845

---

## Post #1 by @Robert_Chauvet (2024-06-17 19:15 UTC)

<p>Hi,<br>
I have been working with Autoscoper for my PhD project, tracking foot and ankle bones using Biplane Fluoroscopy.<br>
I have been going through the process of tracking with Autoscoper, and am having trouble with the Pre Processing.<br>
The volumes are generated properly, and the tracking went well. My issue is with the cropping done to the volumes. The transform to get the tracked data in Autoscoper back into CT space requires a transform to account for the cropping. Visually this looks like a simple translation, and can be done using the new cropped volume origin. This I what I thought was being output into the transforms folder alongside the cropped volumes. The transforms being output do not match the origin and volume information if I look it up in Slicer. The outputted transform shows a stretch value in the z direction, which is a strange thing to have in a purely cropping step.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/910ee4e87b72bf29e4475614c19ab4e5615a144f.png" alt="image" data-base62-sha1="kHf8UTgrq8lJXcgDBy1ignu9D43" width="562" height="491"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7efaf253f6ba46da6762e0ad30339b1affe6d44.png" data-download-href="/uploads/short-url/x5NOD63wOK0H1XpJOvGdojWC6DG.png?dl=1" title="Transform2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7efaf253f6ba46da6762e0ad30339b1affe6d44.png" alt="Transform2" data-base62-sha1="x5NOD63wOK0H1XpJOvGdojWC6DG" width="690" height="138" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Transform2</span><span class="informations">758×152 2.74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a reason for this discrepancy between the transforms and volume information?<br>
If the ones that the pre processing module outputs are correct, what it the way to apply this to get the tracking data back into CT space (the link between Slicer and Autoscoper Space) ?</p>

---

## Post #2 by @Amy_Morton (2024-06-17 20:17 UTC)

<p>Hi Robert,</p>
<p>We are in the processes of implementing a regression in the code introduced a few months back - we apologize for the inconvenience!</p>
<p>That said, you are correct<br>
the.tfm written to the Transforms directory when processing your segmentation node into partial volumes contain the transform from your selected volume’s dicom origin to the corner of your tiff stack</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ca7f4196b77c8d05c39f645f41089f2f5f09121.png" data-download-href="/uploads/short-url/fvdp8VZ7Ar35ypuG1sN6lCxGlPP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6ca7f4196b77c8d05c39f645f41089f2f5f09121_2_690x271.png" alt="image" data-base62-sha1="fvdp8VZ7Ar35ypuG1sN6lCxGlPP" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6ca7f4196b77c8d05c39f645f41089f2f5f09121_2_690x271.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6ca7f4196b77c8d05c39f645f41089f2f5f09121_2_1035x406.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6ca7f4196b77c8d05c39f645f41089f2f5f09121_2_1380x542.png 2x" data-dominant-color="87858E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1880×740 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Autoscoper parses the tiff stacks in a flipped manner and this is captured in the tra output. One method for managing this flip is to create a flipped proxy surface file (stl, wrl etc)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c751e2ec5fcb5c52f24c03e134cf9260244251d.png" data-download-href="/uploads/short-url/hL084NN9eby6gCxhq6bqJ4gsNit.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c751e2ec5fcb5c52f24c03e134cf9260244251d_2_690x221.png" alt="image" data-base62-sha1="hL084NN9eby6gCxhq6bqJ4gsNit" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c751e2ec5fcb5c52f24c03e134cf9260244251d_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c751e2ec5fcb5c52f24c03e134cf9260244251d_2_1035x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c751e2ec5fcb5c52f24c03e134cf9260244251d_2_1380x442.png 2x" data-dominant-color="E5DCE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1558×501 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>for bn =1:length(bones)<br>
y_sz = size(bs.(bones{bn}).tif,1) * bs.(bones{bn}).tfmInv(1,1) ;<br>
% z_sz = size(bs.(bones{bn}).tif,3) * bs.(bones{bn}).tfmInv(3,3) ;<br>
CT_to_AUT_4x4 = RT_to_fX4(eul2rotm([0,0,pi]),[0 y_sz 0]);</p>
<pre><code>bs.(bones{bn}).AUT2ACS =    CT_to_AUT_4x4* bs.(bones{bn}).pvolCS ;
bs.(bones{bn}).ptsinPvolvf = RT_transform(bs.(bones{bn}).ptsinPvol, CT_to_AUT_4x4(1:3,1:3), CT_to_AUT_4x4(1:3,4),1);
</code></pre>
<p>end</p>
<p>Applying the output tra to each respective “autoscoper space” stl will give appropriate bone model placement in dicom space</p>
<p>Once the regression correction is commit to the main branch we will also have a more thorough readthedocs entry to aid in this post processing.</p>

---

## Post #3 by @Robert_Chauvet (2024-06-17 23:04 UTC)

<p>Thank you for the quick reply!</p>
<p>I have a couple of follow up clarifications on this.</p>
<ol>
<li>Since the Autoscoper space parses the images flipped, can the flip x/y/z function on the Autoscoper new trial window (or in the CFG file) be used? Would this flip the coordinates back into the proper DICOM space and undo the need for another transform?</li>
<li>Is the fix in the transform from the preprocessing to apply the origin as the z translation, and apply that to the flipped proxy surface (STL file) before applying the tracking?</li>
</ol>

---

## Post #4 by @Amy_Morton (2024-06-19 19:07 UTC)

<p>Hey Robert,</p>
<p>I’ve not tried to use the flip booleans to ease post-processing- I can attempt and get back to you on that.</p>
<p>When you segment the CT, the model is in DICOM space ( mc1 model/seg shown in yellow)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a0dee627ca7dcaafb79b628e742b56e14fb5997.jpeg" data-download-href="/uploads/short-url/cQEOPe2zkjxYbx6sT9uNPTrWnB5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a0dee627ca7dcaafb79b628e742b56e14fb5997_2_690x451.jpeg" alt="image" data-base62-sha1="cQEOPe2zkjxYbx6sT9uNPTrWnB5" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a0dee627ca7dcaafb79b628e742b56e14fb5997_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a0dee627ca7dcaafb79b628e742b56e14fb5997_2_1035x676.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a0dee627ca7dcaafb79b628e742b56e14fb5997.jpeg 2x" data-dominant-color="6D6D80"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1099×719 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The partial volumes tiff stacks are inherently without spatial resolution- the automatic tfm gives scale and translation info from image space to spatial coords (i.e. mm)</p>
<p>Without the tfm applied- the partial volume (shown in grayscale slices) is stretched inappropriately and index corner (0th row 0th colum and 0slice) is located at the origin.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b192bc0856c1470a162aa6c76d06bd571ce875e.png" data-download-href="/uploads/short-url/m83W3hwmL7uCZVwEdx6E6nqpTcy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b192bc0856c1470a162aa6c76d06bd571ce875e_2_690x307.png" alt="image" data-base62-sha1="m83W3hwmL7uCZVwEdx6E6nqpTcy" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b192bc0856c1470a162aa6c76d06bd571ce875e_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b192bc0856c1470a162aa6c76d06bd571ce875e_2_1035x460.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b192bc0856c1470a162aa6c76d06bd571ce875e_2_1380x614.png 2x" data-dominant-color="595A72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1776×791 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>WHen the tfm is applied (mc1_2) you’ll notice that the scale of the partial volume and it’s spatial resolution is identical to the segmented (yellow) mc1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef3c3a7ace2e3a699fa9b7a55f65b277af6fa087.png" data-download-href="/uploads/short-url/y8n9z0aCcwiTh6zwF1MX6IZk0Av.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef3c3a7ace2e3a699fa9b7a55f65b277af6fa087_2_690x295.png" alt="image" data-base62-sha1="y8n9z0aCcwiTh6zwF1MX6IZk0Av" width="690" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef3c3a7ace2e3a699fa9b7a55f65b277af6fa087_2_690x295.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef3c3a7ace2e3a699fa9b7a55f65b277af6fa087_2_1035x442.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef3c3a7ace2e3a699fa9b7a55f65b277af6fa087_2_1380x590.png 2x" data-dominant-color="5D5E75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1812×775 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The tricky bit concerns the red and green mc1. You’ll notice in the data node heirarchy, I’ve labeld the red mc1 with a Pvol prefix and the green with AUT</p>
<p>The red mc1 is the model you would get from the partial volume with properly scaled voxel information (0.39 0.39 0.625… ‘scale’ transfrom) , but corner indices still at 0,0,0.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/766317edf98c414419f7c4c2cdb5254aebb5604b.png" data-download-href="/uploads/short-url/gTiEc4YMA3SUM9LmIMDDCkbhVbl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/766317edf98c414419f7c4c2cdb5254aebb5604b_2_690x280.png" alt="image" data-base62-sha1="gTiEc4YMA3SUM9LmIMDDCkbhVbl" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/766317edf98c414419f7c4c2cdb5254aebb5604b_2_690x280.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/766317edf98c414419f7c4c2cdb5254aebb5604b_2_1035x420.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/766317edf98c414419f7c4c2cdb5254aebb5604b_2_1380x560.png 2x" data-dominant-color="5E6077"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1836×747 98.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The green is what AUT internally acts on (how it loads and stores the tiff - and what the tra operates on to</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #5 by @Robert_Chauvet (2024-06-20 22:41 UTC)

<p>Thank you, the stretch factor now makes sense.<br>
I have tried to replicate the yellow green and red models as in your photos. I have figured out the transform from the yellow to red. This is just the inverse of the transform automatically generated without the scaling factor.<br>
The issue seems to be the transform between the red and green models. I applied an x and z flip to the model : [-1,0,0;0,1,0;0,0,-1]. As this seems to match your images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/357ab647c5d264686f18a732bbe385b7c80275c4.png" data-download-href="/uploads/short-url/7D6dlqoWtLoORjiH6gpbW0bHC3q.png?dl=1" title="Image 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/357ab647c5d264686f18a732bbe385b7c80275c4_2_642x499.png" alt="Image 1" data-base62-sha1="7D6dlqoWtLoORjiH6gpbW0bHC3q" width="642" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/357ab647c5d264686f18a732bbe385b7c80275c4_2_642x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/357ab647c5d264686f18a732bbe385b7c80275c4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/357ab647c5d264686f18a732bbe385b7c80275c4.png 2x" data-dominant-color="9B9CC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 1</span><span class="informations">907×706 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I multiply the tra tracking data to these transformed green models (which should now match the autoscoper space), they do not seem to be matching up with the tracking I see in Autoscoper world view.  (I am doing TRA*GreenBoneModels).<br>
Can you see anything wrong with this approach?</p>

---

## Post #6 by @Amy_Morton (2024-06-24 16:38 UTC)

<p>Hey Robert, we’re still working through some fixes.<br>
Can you try updating the extension from the index and try again?</p>

---

## Post #7 by @Anthony.Lombardi (2024-06-25 17:56 UTC)

<p>Hi Robert.</p>
<p>Assuming your volume has its origin at (0,0,0) and the proper scaling has already been applied, you should be able to follow the following steps in order to move it into the optimized position from Autoscoper.</p>
<p>You will need to put together an Autoscoper2Slicer transform. This consists of two operations:</p>
<ul>
<li>A 180 degree rotation about the X-axis (L-R axis).</li>
<li>An Offset in the +X (R) direction computed by volDim * volSpacing for the x dimension.</li>
</ul>
<p>Once you have this you should be able to apply it to your volume then apply the tra file and your volume should be in the correct place. Please checkout <a href="https://github.com/BrownBiomechanics/SlicerAutoscoperM/issues/107#issuecomment-2189395255" rel="noopener nofollow ugc">this comment</a> on Github for a visual example.</p>
<p>Your transform hierarchy should look something like this once you are done (NOTE: I am using the inverse of a Slicer2Autoscoper transform for my Autoscoper2Slicer transform):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c653515cd4557cbc31735f432c56823160151ca.png" alt="image" data-base62-sha1="8Chu0vJhAgJWcLrW82lHy9a13Gq" width="422" height="186"></p>
<p>We are working on adding a feature to automatically export this transform to the <code>Transforms</code> directory. For the latest progress on integration, please checkout <a href="https://github.com/BrownBiomechanics/SlicerAutoscoperM/pull/109" rel="noopener nofollow ugc">PR #109</a> on Github.</p>
<p>Definitely let me know how this works for you!<br>
-Anthony</p>

---

## Post #8 by @Robert_Chauvet (2024-07-02 21:02 UTC)

<p>Hi,<br>
I have been playing around with the transforms you mentioned and it is still not quite working.<br>
The first image here shows the original CT segmented volume (yellow), the automatically generated volumes from the pre processing (stretched, but centered at the origin), and the centered bone models (Red).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f577dd8714eb3dbce915d205cc6829591fc2b3d.png" data-download-href="/uploads/short-url/92lwTdal05O3XQ4Sk1hhMboAL01.png?dl=1" title="T1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f577dd8714eb3dbce915d205cc6829591fc2b3d_2_384x500.png" alt="T1" data-base62-sha1="92lwTdal05O3XQ4Sk1hhMboAL01" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f577dd8714eb3dbce915d205cc6829591fc2b3d_2_384x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f577dd8714eb3dbce915d205cc6829591fc2b3d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f577dd8714eb3dbce915d205cc6829591fc2b3d.png 2x" data-dominant-color="8B809F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">T1</span><span class="informations">471×612 57.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The next step would be to apply the Autoscoper to Slicer transform.<br>
This was an x rotation, and a x translation (from the CT volume information - dimension*spacing)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/118249c0edb6e72ee47f4538a5a0ec68a1edbbf0.png" alt="T2" data-base62-sha1="2uTfZCdumKyQb7ancJrFEVgfNdu" width="567" height="227"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f36f2dff1e3ad35a54eb98d4e2294851c489d45d.png" alt="T3" data-base62-sha1="yJwe3kkm48CHM9c9JI6D8ZUis8J" width="410" height="318"><br>
This resulted in the bones being moved as expected, as shown in the green bones.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13b78a516237c0b4800654bbae3df03532705cf0.png" data-download-href="/uploads/short-url/2OqiVi84q62gjhfrnZlIYYDbXLa.png?dl=1" title="T4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13b78a516237c0b4800654bbae3df03532705cf0_2_569x500.png" alt="T4" data-base62-sha1="2OqiVi84q62gjhfrnZlIYYDbXLa" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13b78a516237c0b4800654bbae3df03532705cf0_2_569x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13b78a516237c0b4800654bbae3df03532705cf0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13b78a516237c0b4800654bbae3df03532705cf0.png 2x" data-dominant-color="9393BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">T4</span><span class="informations">767×673 58.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then the TRA file for each bone is applied to each bone. (Blue) This results in them being transformed, but not to the expected neutral position.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2627185b02f2c6b6acceab6fdeecefe634e5919a.png" data-download-href="/uploads/short-url/5rvU69flpl8WX48WoyJfCkoE2bE.png?dl=1" title="T5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2627185b02f2c6b6acceab6fdeecefe634e5919a_2_681x500.png" alt="T5" data-base62-sha1="5rvU69flpl8WX48WoyJfCkoE2bE" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2627185b02f2c6b6acceab6fdeecefe634e5919a_2_681x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2627185b02f2c6b6acceab6fdeecefe634e5919a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2627185b02f2c6b6acceab6fdeecefe634e5919a.png 2x" data-dominant-color="8787B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">T5</span><span class="informations">712×522 61.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For reference, this is how the bones look in Autoscoper World View.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7422eb996011430331f74ea7c8da9d5d2d27f963.png" data-download-href="/uploads/short-url/gzocAi0ZhooWKqcWFzornLmLSSL.png?dl=1" title="T6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7422eb996011430331f74ea7c8da9d5d2d27f963_2_672x500.png" alt="T6" data-base62-sha1="gzocAi0ZhooWKqcWFzornLmLSSL" width="672" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/7422eb996011430331f74ea7c8da9d5d2d27f963_2_672x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7422eb996011430331f74ea7c8da9d5d2d27f963.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7422eb996011430331f74ea7c8da9d5d2d27f963.png 2x" data-dominant-color="31475E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">T6</span><span class="informations">903×671 332 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure now which step is being applied wrong, but any advice would be helpful on how to make these transforms work.</p>
<p>Thanks,<br>
Robert</p>

---

## Post #9 by @Amy_Morton (2024-07-03 16:35 UTC)

<p>Robert, Would you be available to work one-on-one over zoom next week?</p>

---

## Post #10 by @Robert_Chauvet (2024-07-03 16:48 UTC)

<p>Yes - Absolutely.<br>
My email is robert.chauvet@ucalgary.ca if you want to schedule a meeting.<br>
Robert</p>

---

## Post #11 by @Robert_Chauvet (2024-07-19 20:42 UTC)

<p>Thanks Amy,<br>
I have gotten the Transforms to work in MATLAB properly.<br>
This involved importing the centered STL Files from SLICER (or the raw DICOM Positioned STL and translating it to the Origin in MATLAB)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aea65f3e96dc58bb07bafddb1f831667f95f91a1.png" alt="image" data-base62-sha1="oV1wSAbuCmErqvj1506GokXQyPL" width="385" height="483"></p>
<p>Applying a transformation matrix of the following:</p>
<p>Rot_Tibia=eul2rotm([0,0,pi]);<br>
Translation_Tibia=[0;46.898;0];<br>
TRANSFORM_Tibia=[Rot_Tibia,Translation_Tibia;0,0,0,1];</p>
<p>The 46.898 comes from the y volume spacing multiplied by the y volume dimension. This is a different value for each bone.<br>
This information can be found in the AUTOSCOPER pre processing module, in the Slicer2AUT transform.<br>
The rotation is not the same as the Slicer2AUT transform output, as the transform gives you a [-1,0,0;0,1,0;0,0,-1] rotation, where the rotation needed is a [1,0,0;0,-1,0;0,0,-1].<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a36d0aef71d4d583997cf160583227c98e439be.png" alt="image" data-base62-sha1="cS4pCIXwEoN9JtkJpNwIzTrhXnU" width="507" height="486"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60ec8722fba507ba33258dd22f26b4da5d01a1a4.png" data-download-href="/uploads/short-url/dPqAWgGku6qJTNq7WMCEj5Do9YE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60ec8722fba507ba33258dd22f26b4da5d01a1a4.png" alt="image" data-base62-sha1="dPqAWgGku6qJTNq7WMCEj5Do9YE" width="260" height="500" data-dominant-color="1B0319"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">262×502 5.42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Applying the TRA matrix to the bones, then positions the bones correctly as in the AUTOSCOPER space.<br>
Bone_model_Tracked.Tibia.vertices= (Tracking_matx.Tibia*Bone_model_Transformed.Tibia.vertices’)';</p>
<p>Bone_model_Tracked.Talus.vertices= (Tracking_matx.Talus*Bone_model_Transformed.Talus.vertices’)';<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39075bbad2bb379c8870ae69e51be8ae26ef41a7.png" alt="image" data-base62-sha1="88uYOK110spnUux51UGbcngdtFd" width="597" height="463"></p>

---
