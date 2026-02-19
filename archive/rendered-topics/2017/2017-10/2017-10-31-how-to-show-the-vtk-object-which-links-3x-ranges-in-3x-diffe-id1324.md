---
topic_id: 1324
title: "How To Show The Vtk Object Which Links 3X Ranges In 3X Diffe"
date: 2017-10-31
url: https://discourse.slicer.org/t/1324
---

# How to show the vtk object which links 3x ranges in 3x different slices?

**Topic ID**: 1324
**Date**: 2017-10-31
**URL**: https://discourse.slicer.org/t/how-to-show-the-vtk-object-which-links-3x-ranges-in-3x-different-slices/1324

---

## Post #1 by @spring (2017-10-31 06:20 UTC)

<p>Hi Slicer Experts:</p>
<pre><code>Background is: we have one CT image in Slicer,and we want to draw 3x ranges(with rectangle format ) in 3x different slices,then we want to link these 3x ranges and show it as cuboid.
Now we can get the start point and end point for each rectangles,but we dont know how to link them.
</code></pre>
<p>Any suggestions would be appreciated.</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #2 by @pieper (2017-10-31 12:08 UTC)

<p>Hi Chunbo -</p>
<p>Can you explain a bit more what you mean by “3x ranges” and what you mean by linking them?  Maybe you could draw a picture of what you have in mind?</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2017-10-31 12:54 UTC)

<p><a class="mention" href="/u/spring">@spring</a> Do you mean you would need something like annotation ROI box?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddea94956a768c9920b50a08d53f2764b3a4ca3d.jpeg" data-download-href="/uploads/short-url/vFa6DXkTNcbvYeBRIEtCqQlTD8p.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ddea94956a768c9920b50a08d53f2764b3a4ca3d_2_690x373.jpg" alt="image" data-base62-sha1="vFa6DXkTNcbvYeBRIEtCqQlTD8p" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ddea94956a768c9920b50a08d53f2764b3a4ca3d_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ddea94956a768c9920b50a08d53f2764b3a4ca3d_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ddea94956a768c9920b50a08d53f2764b3a4ca3d_2_1380x746.jpg 2x" data-dominant-color="A3989E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 526 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @spring (2017-11-01 06:51 UTC)

<p>Hi Steve,</p>
<p>Thanks for your reply.</p>
<p>Below screenshot can show our requirement.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50d15f9efebdbbd657b6f8283ec22395059e5eab.png" alt="image" data-base62-sha1="bwWMfUCxbqI6XIDo5e1VwNqB9nt" width="567" height="447"></p>
<p>There are 3x slices which located at different positions, we want to link them as one cuboid,and use  interpolation to show the middle slices.<br>
It seems we should create one specific vtk object to contain it. Could you share some suggestions?</p>
<p>Thanks and Regards,<br>
Chunbo</p>

---

## Post #5 by @spring (2017-11-01 07:16 UTC)

<p>Thanks Lasso,</p>
<p>Yes,the ROI box can create the similar ranges.</p>
<p>The only one difference is:ROI box was based on the specific slice,and the box’s depth is fixed.We want to create one object likes vtk’s cuboid to connect those 3x different slices.</p>

---

## Post #6 by @lassoan (2017-11-01 11:44 UTC)

<p>To achieve that, create vtkMRMLTransformNode to your scene and set a <a href="https://www.vtk.org/doc/nightly/html/classvtkGridTransform.html">vtkGridTransform</a> with 2x2x3 points. Each point specifies how each slice corner point is displaced relative to original corner point position.</p>

---
