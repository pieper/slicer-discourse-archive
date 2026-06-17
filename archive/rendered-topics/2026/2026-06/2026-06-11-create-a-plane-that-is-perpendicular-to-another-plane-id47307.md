---
topic_id: 47307
title: "Create a plane that is perpendicular to another plane"
date: 2026-06-11
url: https://discourse.slicer.org/t/47307
last_bumped: 2026-06-16T16:36:24.262Z
---

# Create a plane that is perpendicular to another plane

**Topic ID**: 47307
**Date**: 2026-06-11
**URL**: https://discourse.slicer.org/t/create-a-plane-that-is-perpendicular-to-another-plane/47307

---

## Post #1 by @jsguerra (2026-06-11 01:30 UTC)

<p>I’ve created a best fit plane from a point list in the Markups module and I would like to create a second plane perpendicular to the best fit plane. Attached is an example using one of the mouse crania from the SlicerMorph sample data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66aebfd139c911afb3b74b05d30295140cc17683.jpeg" data-download-href="/uploads/short-url/eEn6eIYAsoZorY91dwFXhqhQxcD.jpeg?dl=1" title="example plane" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aebfd139c911afb3b74b05d30295140cc17683_2_665x500.jpeg" alt="example plane" data-base62-sha1="eEn6eIYAsoZorY91dwFXhqhQxcD" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aebfd139c911afb3b74b05d30295140cc17683_2_665x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aebfd139c911afb3b74b05d30295140cc17683_2_997x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66aebfd139c911afb3b74b05d30295140cc17683_2_1330x1000.jpeg 2x" data-dominant-color="9E9DB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example plane</span><span class="informations">1920×1443 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here, I created a best fit plane (Plane A)  using landmarks 13,14,15,28,54, and 55. I would like to create a second perpendicular plane (Plane B) so that Plane A represents the X-axis and Plane B represents a Y-Axis.</p>
<p>I looked over the documentation and scripts repository but I’m also not well versed in python so I’m not sure what to look for. Any help would be appreciated.</p>

---

## Post #2 by @ThomasVanParys (2026-06-11 09:25 UTC)

<p>Could you not also set Plane B using the Markups module? You only need two landmarks. I think you can set the plane normal constrained relative to Plane A or the plane origin at a landmark/centroid?</p>

---

## Post #3 by @Philippe_Pellerin (2026-06-11 12:40 UTC)

<p>It is very easy, have a look at this tutorial to see how to create orthogonal planning.<a href="https://youtu.be/Bs4GWLrFQfA" rel="noopener nofollow ugc">https://youtu.be/Bs4GWLrFQfA</a></p>

---

## Post #4 by @jsguerra (2026-06-11 13:29 UTC)

<p>Yes, the idea would be to add a second plane in the Markups module, but where I’m having issues is figuring out how to constrain it to be perpendicular relative to plane A.</p>

---

## Post #5 by @chir.set (2026-06-11 14:47 UTC)

<p>If you don’t want to use python scripting, you may consider the Reslice functions in <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/ManyThingsToolBar?ref_type=heads" rel="noopener nofollow ugc">this</a> project.</p>
<ul>
<li>Reslice a view be perpendicular to that plane (choose Binormal or Tangent).</li>
<li>Place a second plane markups node in the latter slice view.</li>
<li>Restore the orientation of the slice view.</li>
</ul>

---

## Post #7 by @jsguerra (2026-06-11 17:49 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> Thanks for sharing. I installed the tool but I’m only working with surface PLY files, so I dont have slices.</p>
<p>Also, I’m not opposed to using python, I just don’t know how to use python but I’m willing to learn.</p>

---

## Post #8 by @jsguerra (2026-06-11 17:56 UTC)

<p>Thank you for sharing. That is quite easy however I’m only working with surface PLY files, not CT/DICOM files.</p>

---

## Post #9 by @chir.set (2026-06-11 18:27 UTC)

<p>You don’t need a volume for that. The slice views can be empty. You don’t even need a model.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/649f4227c2384ce42e43c75b7bb3fb74b5af5126.png" data-download-href="/uploads/short-url/em8XjiKl9Njc3MfJSbcUhxQbmjI.png?dl=1" title="NoVolumeNeeded" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/649f4227c2384ce42e43c75b7bb3fb74b5af5126.png" alt="NoVolumeNeeded" data-base62-sha1="em8XjiKl9Njc3MfJSbcUhxQbmjI" width="690" height="487" data-dominant-color="170D0C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NoVolumeNeeded</span><span class="informations">757×535 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @jsguerra (2026-06-12 01:33 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> Got it, thanks for the clarification. I was using a 3D only view and was confused why nothing seemed to be happening. Just tried it again and it works remarkably well!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9aeca4c2e170171dfc6d79948374d365fc8aebee.jpeg" data-download-href="/uploads/short-url/m6wxij859M3OLvXYhLC6LTK90iq.jpeg?dl=1" title="perpendicular planes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aeca4c2e170171dfc6d79948374d365fc8aebee_2_690x443.jpeg" alt="perpendicular planes" data-base62-sha1="m6wxij859M3OLvXYhLC6LTK90iq" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aeca4c2e170171dfc6d79948374d365fc8aebee_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aeca4c2e170171dfc6d79948374d365fc8aebee_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aeca4c2e170171dfc6d79948374d365fc8aebee_2_1380x886.jpeg 2x" data-dominant-color="746859"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">perpendicular planes</span><span class="informations">1920×1233 360 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I did notice that because the my surface is not aligned along the axis, I had to rotate the new plane created (Plane B; Green) along the one axis to get it to run along the direction I’m interested in (Plane B - Rotated; Blue). Is there a way to accomplish this without having to manually rotate it?</p>

---

## Post #11 by @chir.set (2026-06-12 08:59 UTC)

<aside class="quote no-group" data-username="jsguerra" data-post="10" data-topic="47307">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/919ad9/48.png" class="avatar"> jsguerra:</div>
<blockquote>
<p>Is there a way to accomplish this without having to manually rotate it?</p>
</blockquote>
</aside>
<p>You can proceed this way:</p>
<ul>
<li>Check ‘Orthogonal intersection’ when you orient a slice view to be parallel to your first plane node (use Normal).</li>
<li>Activate ‘Slice intersections’ in the slice view (right click).</li>
<li>Rotate the other slice views in it, by ‘Ctrl+Alt+Mouse move’ or by checking ‘Interaction’ to activate the handles; rotate so that one of the views is as you want (see the line colour in the slice view).</li>
<li>In the target slice view (line colour in the source slice view), place a new plane markups node.</li>
<li>Optionally restore the orientation slice views.</li>
</ul>

---

## Post #12 by @jsguerra (2026-06-16 16:36 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="11" data-topic="47307">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>You can proceed this way:</p>
<ul>
<li>Check ‘Orthogonal intersection’ when you orient a slice view to be parallel to your first plane node (use Normal).</li>
<li>Activate ‘Slice intersections’ in the slice view (right click).</li>
<li>Rotate the other slice views in it, by ‘Ctrl+Alt+Mouse move’ or by checking ‘Interaction’ to activate the handles; rotate so that one of the views is as you want (see the line colour in the slice view).</li>
<li>In the target slice view (line colour in the source slice view), place a new plane markups node.</li>
<li>Optionally restore the orientation slice views</li>
</ul>
</blockquote>
</aside>
<p>This worked perfectly, thank you!</p>

---
