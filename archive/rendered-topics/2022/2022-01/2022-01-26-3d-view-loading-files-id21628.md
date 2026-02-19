---
topic_id: 21628
title: "3D View Loading Files"
date: 2022-01-26
url: https://discourse.slicer.org/t/21628
---

# 3D view / Loading files

**Topic ID**: 21628
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/3d-view-loading-files/21628

---

## Post #1 by @Vaughanbj (2022-01-26 06:25 UTC)

<p>Operating system:win10<br>
Slicer version:latest<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @Vaughanbj (2022-01-26 06:29 UTC)

<p>Why is my 3D view opposite to the other views i.e. when Im editing the top view segments the cursor appears on the opposite side of the 3d view to what it should…<br>
Also when saving, 3 files are saved… nrrd, segmentation and something else… but how do I reload these same files to continue editing? I closed rhe program and now can only reload one at a time…</p>

---

## Post #3 by @lassoan (2022-01-27 06:07 UTC)

<aside class="quote no-group" data-username="Vaughanbj" data-post="2" data-topic="21628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/8e8cbc/48.png" class="avatar"> Vaughanbj:</div>
<blockquote>
<p>Why is my 3D view opposite to the other views</p>
</blockquote>
</aside>
<p>You can rotate all the views (both slice and 3D) any way you need. By default 3D view is not opposite as slice views.</p>
<p>The orientation of slice views is not very easy to change (for example, you need to go to Reformat module), so there is an option in application settings to choose “patient right” direction to be “screen right” or “screen left”. In contrast, 3D views are very easy to reorient (just click-and-drag), so the default orientation is always “patient superior” is “screen up”; “patient right” is “screen left”.</p>
<aside class="quote no-group" data-username="Vaughanbj" data-post="2" data-topic="21628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/8e8cbc/48.png" class="avatar"> Vaughanbj:</div>
<blockquote>
<p>Also when saving, 3 files are saved… nrrd, segmentation and something else… but how do I reload these same files to continue editing?</p>
</blockquote>
</aside>
<p>Probably these files are saved:</p>
<ul>
<li>nrrd: segmented image</li>
<li>seg.nrrd: segmentation</li>
<li>mrml: workspace file, stores display settings, view arrangement, etc.</li>
</ul>
<p>You can click on the “package” icon to save everything in a single file.</p>
<aside class="quote no-group" data-username="Vaughanbj" data-post="2" data-topic="21628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/8e8cbc/48.png" class="avatar"> Vaughanbj:</div>
<blockquote>
<p>I closed rhe program and now can only reload one at a time…</p>
</blockquote>
</aside>
<p>After you saved the files, you can restore the workspace by opening the .mrml file (e.g., drag-and-drop it to the Slicer screen).</p>

---

## Post #4 by @Vaughanbj (2022-01-27 06:37 UTC)

<p>Soory, i dont think you understand my situation regarding the 3D view…<br>
I am working on a cervical spine. Top left is the birdseye view. Anterior is to the bottom of the screen, when im working on the left side of the spine the cursor is on the mirrored side of the 3D view ( also in the same petspective looking away from me). When i move the cursor everything is moving opposite on the 3D view, its very difficult to coordinate where i want to edit when everything is moving like im looking in a mirror.</p>

---

## Post #5 by @lassoan (2022-01-27 06:52 UTC)

<p>This is how views are set up by default in current Slicer version:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/406614d2d92c9042b49efe87c45d7447176dc2df.jpeg" data-download-href="/uploads/short-url/9bHgvWQacgI7CuJjVwCVOC4ofkb.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406614d2d92c9042b49efe87c45d7447176dc2df_2_643x499.jpeg" alt="image" data-base62-sha1="9bHgvWQacgI7CuJjVwCVOC4ofkb" width="643" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406614d2d92c9042b49efe87c45d7447176dc2df_2_643x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406614d2d92c9042b49efe87c45d7447176dc2df_2_964x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406614d2d92c9042b49efe87c45d7447176dc2df_2_1286x998.jpeg 2x" data-dominant-color="8A888E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1565×1216 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can see, slice views are all aligned patient right is screen left, patient superior is screen up, patient anterior is left. You can now rotate the 3D view with one mouse drag or cicking on the <code>L</code>, <code>I</code>, or <code>A</code> buttons in the 3D view controller to view the patient from the left, inferior, or anterior directions to match the 3D view direction with any of the slice views.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffde2ed974a21a42be3457a380aef51500f9896e.jpeg" data-download-href="/uploads/short-url/AvvMlM92BWs6m2EfHCY0EXu8vMi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffde2ed974a21a42be3457a380aef51500f9896e_2_690x492.jpeg" alt="image" data-base62-sha1="AvvMlM92BWs6m2EfHCY0EXu8vMi" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffde2ed974a21a42be3457a380aef51500f9896e_2_690x492.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffde2ed974a21a42be3457a380aef51500f9896e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffde2ed974a21a42be3457a380aef51500f9896e.jpeg 2x" data-dominant-color="AAA4BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">847×605 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you do this then the cursor will move in the same direction in the 3D view as in the corresponding slice view.</p>

---

## Post #6 by @Vaughanbj (2022-01-27 08:05 UTC)

<p>Thanks, ill try that</p>

---
