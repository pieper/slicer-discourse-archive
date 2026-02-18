# Mixed volume rendering and surface representation of segmentation has incorrect 3D appearance if segment is not fully opaque

**Topic ID**: 6532
**Date**: 2019-04-17
**URL**: https://discourse.slicer.org/t/mixed-volume-rendering-and-surface-representation-of-segmentation-has-incorrect-3d-appearance-if-segment-is-not-fully-opaque/6532

---

## Post #1 by @mikebind (2019-04-17 20:18 UTC)

<p>I am using volume rendering to view the air/non-air interface in a CT volume (only voxel values -600 to -300 HU are opaque, all others are transparent). In addition, I have segmented a tube which is in the airway, and created a closed surface representation of that segment which is visible in the 3D view.  As long as the segment is fully opaque, the rendering of the 3D view appears correct, like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2153d75897eedcd8d6150d0fb8f72dfc231c08d2.png" data-download-href="/uploads/short-url/4KPnTHpyEv1tbmYr6l2c15qbM0G.png?dl=1" title="1%204_17_2019%2012_51_00%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/2153d75897eedcd8d6150d0fb8f72dfc231c08d2_2_690x365.png" alt="1%204_17_2019%2012_51_00%20PM" data-base62-sha1="4KPnTHpyEv1tbmYr6l2c15qbM0G" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/2153d75897eedcd8d6150d0fb8f72dfc231c08d2_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/2153d75897eedcd8d6150d0fb8f72dfc231c08d2_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/2153d75897eedcd8d6150d0fb8f72dfc231c08d2_2_1380x730.png 2x" data-dominant-color="8F8C9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1%204_17_2019%2012_51_00%20PM</span><span class="informations">1920×1017 371 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, if the opacity of the tube segment is reduced at all, it is always rendered as if it were behind the volume rendering of the image volume data, like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c23e1b51c31539b8106a6e6c20a9c89961c6f775.png" data-download-href="/uploads/short-url/rIlGVaQQuiVTjht8Jsv63HtNpml.png?dl=1" title="1%204_17_2019%2012_51_12%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23e1b51c31539b8106a6e6c20a9c89961c6f775_2_690x365.png" alt="1%204_17_2019%2012_51_12%20PM" data-base62-sha1="rIlGVaQQuiVTjht8Jsv63HtNpml" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23e1b51c31539b8106a6e6c20a9c89961c6f775_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23e1b51c31539b8106a6e6c20a9c89961c6f775_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c23e1b51c31539b8106a6e6c20a9c89961c6f775_2_1380x730.png 2x" data-dominant-color="8F8C9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1%204_17_2019%2012_51_12%20PM</span><span class="informations">1920×1017 379 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is clearly a rendering error.  As the 3D view is rotated clearly physically impossible things happen and it is impossible to see any portion of the tube appear in front of any portion of the rendered image volume data.</p>
<p>Reducing the opacity of the image volume data does not mitigate the layering problem, the tube segment is eventually visible through the image volume data, but still always appears to be behind it, even when it should be in front.</p>
<p>The problem does not seem to be affected by changing the Rendering setting in the Volume Rendering  module between the CPU and GPU choices.</p>
<p>I assume this comes from a bug in the rendering code when it needs to handle mixing the image volume rendering and a closed surface representation, but it is well beyond my ability to figure out how to fix this bug.</p>
<p>Currently, I will work around the issue by always leaving my closed surface object fully opaque, but it would be nice to be able to use a partially transparent representation as well in the future.</p>

---

## Post #2 by @lassoan (2019-04-17 20:54 UTC)

<p>To render semi-transparent models correctly, you need to enable depth peeling.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/0649f4eba08584f8999dda46f9f5e3f9dfecbeab.png" alt="image" data-base62-sha1="TDjC6IDg7pslwyKFWgQGYQelTR" width="494" height="180"></p>
<p>You can enable depth peeling by default in menu: Edit / Application settings / Views / 3D viewer defaults / Use depth peeling - then restart Slicer.</p>

---

## Post #3 by @mikebind (2019-04-17 21:43 UTC)

<p>Thanks, I hadn’t noticed this option before.  However, this results in the segmented tube being semi-transparently rendered <strong>in front of</strong> the volume rendered image volume. Looks like this with depth peeling on:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cace14ecabcead486f4b18efe94d9d88fb566ea5.jpeg" data-download-href="/uploads/short-url/sW5YA1JwYD1m6eRnIX6LKJSmEsJ.jpeg?dl=1" title="1%204_17_2019%202_40_03%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cace14ecabcead486f4b18efe94d9d88fb566ea5_2_690x365.jpeg" alt="1%204_17_2019%202_40_03%20PM" data-base62-sha1="sW5YA1JwYD1m6eRnIX6LKJSmEsJ" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cace14ecabcead486f4b18efe94d9d88fb566ea5_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cace14ecabcead486f4b18efe94d9d88fb566ea5_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cace14ecabcead486f4b18efe94d9d88fb566ea5_2_1380x730.jpeg 2x" data-dominant-color="9E9AA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1%204_17_2019%202_40_03%20PM</span><span class="informations">1920×1017 498 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>(The tube should disappear from view as it enters the nose, hidden by the rendered image volume, as in the very first image attached above for the fully opaque image)</p>
<p>So, this changes, but <strong>does not resolve the issue</strong>. Thanks for the response, I very much appreciate it.</p>

---

## Post #4 by @lassoan (2019-04-17 22:32 UTC)

<p>GPU ray casting should work well with depth peeling and usually it is also magnitudes faster than CPU ray casting.</p>
<p>If you use a step-function-like scalar opacity transfer function in the volume renderer (as you do in the attached screenshot) then you may just as well apply the same threshold range in segment editor to create an opaque surface mesh. You can then visualize everything without the need for volume rendering.</p>

---

## Post #5 by @mikebind (2019-04-17 23:29 UTC)

<p>Thanks again. It does work with GPU ray casting and depth peeling. I will also experiment with using surface models instead of volume rendering.  The appeal of the volume rendering was the ease of working with 4D data, as the volume is cycled through the time steps, the volume-rendered representation naturally changes with the image volume.  To do the same with surface models, I need to generate surface models for each frame (of which there are 39 in this case), assemble them into a sequence, and put the sequence into the same sequence browser.  These are all doable steps, and I am going to need to do them for the tube anyway (which needs to be segmented), but there was significant appeal in just keeping the volume rendering for the air interface, which works out of the box with the preset I created and automatically handles 4D displays. Also, I liked that it was easy to create a representation where it was trivial to tell which side of the surface was facing air, and which side was facing non-air by putting two different colors on either end of my step function.  I think to do the same using surface models I would need to generate two surfaces slightly apart from one another, and depending on how they got smoothed, etc., they might accidentally intersect, and there would also be a visible gap between them if I tried to use clipping planes to provide similar functionality to the clipping ROI in the volume rendering module, not to mention having to synchronize the clipping planes between the two surface models.  All of that is much easier if I can stick with the volume rendering module, which is very easy and intuitive to use.</p>
<p>Thanks again for your help.  Slicer is an amazing tool, and the community support is second to none!</p>

---
