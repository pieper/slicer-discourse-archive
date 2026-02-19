---
topic_id: 10356
title: "3D Label Map And The 3D View Of Segmentation Mismatch"
date: 2020-02-19
url: https://discourse.slicer.org/t/10356
---

# 3D label map and the 3D view of segmentation mismatch

**Topic ID**: 10356
**Date**: 2020-02-19
**URL**: https://discourse.slicer.org/t/3d-label-map-and-the-3d-view-of-segmentation-mismatch/10356

---

## Post #1 by @Mohammad_Tanjib_Rahm (2020-02-19 21:53 UTC)

<p>Hi all,<br>
I am trying to do segmentation using MRI data. After completing the segmentation I saved it as a label map to view it as voxels instead of tetrahedral meshes. The problem is there are small holes at the bottom of the segmentation (missing voxels) when I visualize the segmentation in Paraview. However, in the 3D view of the segmentation in slicer there are no holes and it’s a closed contour. So, I have the following questions:</p>
<ol>
<li>Why is this happening?</li>
<li>Can I render the 3D view in slicer as voxels instead of tetrahedrons? Or if I can do the segmentation using rectangular meshes instead of tetrahedral mesh?</li>
</ol>
<p>I am using Slicer 4.10.2</p>

---

## Post #2 by @Juicy (2020-02-20 03:09 UTC)

<p>You could try going to the “Show 3d” button which is found toward the top of the segment editor module. There is a drop down arrow next to the button, click this and untick surface smoothing. You should now be able to visualise the voxels in the 3d view.</p>

---

## Post #3 by @lassoan (2020-02-20 04:58 UTC)

<aside class="quote no-group" data-username="Mohammad_Tanjib_Rahm" data-post="1" data-topic="10356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammad_tanjib_rahm/48/5934_2.png" class="avatar"> Mohammad_Tanjib_Rahm:</div>
<blockquote>
<p>After completing the segmentation I saved it as a label map to view it as voxels instead of tetrahedral meshes</p>
</blockquote>
</aside>
<p>Segmentations and Segment Editor modules do not generate tetrahedral meshes. You can convert segmentations to tetrahedral meshes using SegmentMesher extension.</p>
<aside class="quote no-group" data-username="Mohammad_Tanjib_Rahm" data-post="1" data-topic="10356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammad_tanjib_rahm/48/5934_2.png" class="avatar"> Mohammad_Tanjib_Rahm:</div>
<blockquote>
<p>The problem is there are small holes at the bottom of the segmentation (missing voxels) when I visualize the segmentation in Paraview</p>
</blockquote>
</aside>
<p>Do you see small holes in an exported surface mesh? How did you create the mesh and how did you save it? (I would recommend to use <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Export to files</a> feature)</p>
<aside class="quote no-group" data-username="Mohammad_Tanjib_Rahm" data-post="1" data-topic="10356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammad_tanjib_rahm/48/5934_2.png" class="avatar"> Mohammad_Tanjib_Rahm:</div>
<blockquote>
<p>I am using Slicer 4.10.2</p>
</blockquote>
</aside>
<p>Slicer Preview Release is stable and contains many fixes and improvements compared to the Stable Release, so if you encounter any problems, try if the preview release works better.</p>

---

## Post #4 by @Mohammad_Tanjib_Rahm (2020-02-20 16:04 UTC)

<p>Yes. I have done that. But when I export it out as a binary labelmap I see some missing pixels in the bottom which cannot be seen on the 3D model. I am attaching an image to clarify what I am talking about. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c2e6a64106862e832585ca977ab7fa2c6b02a2f.jpeg" data-download-href="/uploads/short-url/d9tn4P8gsH8AVZVdisZAvTAfXn9.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_690x305.jpeg" alt="Capture.PNG" data-base62-sha1="d9tn4P8gsH8AVZVdisZAvTAfXn9" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_1380x610.jpeg 2x" data-dominant-color="5E6384"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">2249×995 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
On the left is the segmentation loaded as a .obj file and on the right the binary labelmap saved as .vtk and visualized in paraview. Please note that the 3D model generated inside slicer 3D corroborates to the exported .obj model.</p>

---

## Post #5 by @Mohammad_Tanjib_Rahm (2020-02-20 16:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="10356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Segmentations and Segment Editor modules do not generate tetrahedral meshes. You can convert segmentations to tetrahedral meshes using SegmentMesher extension.</p>
</blockquote>
</aside>
<p>I am sorry if I was unclear before or if I did not word it correctly. My goal is not to create a tetrahedral mesh. Rather I want to import it out as a binary labelmap and visualize it as voxelized 3D model. I am able to do that. But the issue is that the model generated inside 3D slicer and the binary labelmap do not match exactly. I am wondering if that is because slicer 3D uses tetrahedrons as elements for 3D models and when these tetrahedrons are converted to cubes I am losing some data. I am attaching an image for clarification:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c2e6a64106862e832585ca977ab7fa2c6b02a2f.jpeg" data-download-href="/uploads/short-url/d9tn4P8gsH8AVZVdisZAvTAfXn9.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_690x305.jpeg" alt="Capture.PNG" data-base62-sha1="d9tn4P8gsH8AVZVdisZAvTAfXn9" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c2e6a64106862e832585ca977ab7fa2c6b02a2f_2_1380x610.jpeg 2x" data-dominant-color="5E6384"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">2249×995 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The left one is the .obj file of the segmentation. If you notice carefully, I used the cell selection tool of Paraview to mark couple cells on the left image. These cells are all triangular/tetrahedrons. Also in the right image you can see the missing voxels/holes I am talking about.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="10356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer Preview Release is stable and contains many fixes and improvements compared to the Stable Release, so if you encounter any problems, try if the preview release works better.</p>
</blockquote>
</aside>
<p>I will try this and see if this yields better results.</p>

---

## Post #6 by @lassoan (2020-02-20 16:27 UTC)

<aside class="quote no-group" data-username="Mohammad_Tanjib_Rahm" data-post="4" data-topic="10356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammad_tanjib_rahm/48/5934_2.png" class="avatar"> Mohammad_Tanjib_Rahm:</div>
<blockquote>
<p>when I export it out as a binary labelmap I see some missing pixels in the bottom</p>
</blockquote>
</aside>
<p>It seems like Paraview struggles with correctly displaying binary image data. You can report the error to Paraview developers. In general, Paraview is great for mesh visualization and processing but extremely limited and not very robust for image data.</p>
<aside class="quote no-group" data-username="Mohammad_Tanjib_Rahm" data-post="5" data-topic="10356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammad_tanjib_rahm/48/5934_2.png" class="avatar"> Mohammad_Tanjib_Rahm:</div>
<blockquote>
<p>issue is that the model generated inside 3D slicer and the binary labelmap do not match exactly</p>
</blockquote>
</aside>
<p>Normally you would not want them to match exactly but to reconstruct a surface mesh that matches the real shape of the objects (without staircase artifacts. If you turn of smoothing as <a class="mention" href="/u/juicy">@juicy</a> suggested above then you’ll have exact match.</p>

---
