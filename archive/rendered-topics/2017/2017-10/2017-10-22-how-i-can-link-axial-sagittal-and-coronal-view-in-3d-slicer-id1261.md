---
topic_id: 1261
title: "How I Can Link Axial Sagittal And Coronal View In 3D Slicer"
date: 2017-10-22
url: https://discourse.slicer.org/t/1261
---

# How I can link axial, sagittal, and coronal view in 3d slicer

**Topic ID**: 1261
**Date**: 2017-10-22
**URL**: https://discourse.slicer.org/t/how-i-can-link-axial-sagittal-and-coronal-view-in-3d-slicer/1261

---

## Post #1 by @a.mortazi (2017-10-22 01:17 UTC)

<p>Operating system:Ubuntu 14<br>
Slicer version:4.6</p>
<p>Assume I am scrolling through slices in the axial view and I want to know the position of current slice in the sagittal or coronal view (i.e as a line).<br>
Any help is appreciated.</p>

---

## Post #2 by @pieper (2017-10-22 23:36 UTC)

<p>It sounds like you want to turn on the Slice Intersections option:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Crosshair_Options" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Crosshair_Options</a></p>

---

## Post #3 by @lassoan (2017-10-23 01:39 UTC)

<p>Also note that for linked movement of all slices, you need to hold down Shift key while moving the mouse over a slice viewer.</p>

---

## Post #4 by @a.mortazi (2017-10-23 02:38 UTC)

<p>Thanks, that was exactly what I looked for.</p>

---

## Post #5 by @jcfr (2017-10-23 05:11 UTC)

<p>For reference, I just updated the wiki page associated with the link posted by <a class="mention" href="/u/pieper">@pieper</a></p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="2" data-topic="1261" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It sounds like you want to turn on the Slice Intersections option:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Crosshair_Options" class="inline-onebox">Documentation/4.8/SlicerApplication/MainApplicationGUI - Slicer Wiki</a></p>
</blockquote>
</aside>
<p>to reference the comment of <a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1261" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Also note that for linked movement of all slices, you need to hold down Shift key while moving the mouse over a slice viewer.</p>
</blockquote>
</aside>

---

## Post #6 by @cphillips (2018-07-09 13:51 UTC)

<p>I’m so happy I found this feature. Is there anyway to just link TWO of the views (axial and coronal), and remove the sagittal (yellow lines)?</p>

---

## Post #7 by @cphillips (2018-07-09 14:03 UTC)

<p>Is there anyway to just link TWO of the views (axial and coronal), and remove the sagittal (yellow lines)?</p>

---

## Post #8 by @lassoan (2018-07-09 16:54 UTC)

<p>Linking of views are always happen for all the views in the same view group. To exclude yellow view from linking, change its view group ID in <em>View controllers</em> module, <em>Advanced</em> section, <em>View group</em>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fa37c8809b82a7ea9cde61265fc4f428136f366.png" data-download-href="/uploads/short-url/id8UdWjH1iLBemvB7Qdfl0og1Qa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fa37c8809b82a7ea9cde61265fc4f428136f366_2_484x500.png" alt="image" data-base62-sha1="id8UdWjH1iLBemvB7Qdfl0og1Qa" width="484" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fa37c8809b82a7ea9cde61265fc4f428136f366_2_484x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fa37c8809b82a7ea9cde61265fc4f428136f366_2_726x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fa37c8809b82a7ea9cde61265fc4f428136f366_2_968x1000.png 2x" data-dominant-color="F7F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1176×1213 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @cphillips (2018-07-10 13:48 UTC)

<p>Thank you. Also, is there anyway to see, say, ALL the lines (corresponding to all of the coronal slices) on each slice of the axial view? I.e. if there are 8 coronal slices, 8 lines would be visible on each axial slice?</p>

---

## Post #11 by @lassoan (2018-07-10 14:06 UTC)

<p>Yes. You see the lines for all slices in the same group. If there are 8 coronal slices in the same view group, you’ll see 8 intersection lines.</p>

---

## Post #12 by @cphillips (2018-07-10 14:24 UTC)

<p>The issue is that there are 2 volumes I have loaded: one that contains all the coronal slices, which I can scroll through using the slicer slider in the red window, and another that contains all the axial slices, which I can scroll through using the slicer slider in the yellow window. As I scroll through the coronal slices, only one red line appears on the axial slice currently being shown (I want to see all 8 red lines at once). I can’t seem to separate out the slices into different view groups when they are part of the same volume.</p>

---

## Post #13 by @cphillips (2018-07-10 14:25 UTC)

<p>The issue is that there are 2 volumes I have loaded: one that contains all the coronal slices, which I can scroll through using the slicer slider in the red window, and another that contains all the axial slices, which I can scroll through using the slicer slider in the yellow window. As I scroll through the coronal slices, only one red line appears on the axial slice currently being shown (I want to see all 8 red lines at once). I can’t seem to separate out the slices into different view groups when they are part of the same volume.</p>

---

## Post #14 by @lassoan (2018-07-10 14:35 UTC)

<blockquote>
<p>As I scroll through the coronal slices, only one red line appears on the axial slice currently being shown</p>
</blockquote>
<p>The red line indicates the current red slice location. There are not 8 red lines (unless you have 8 slice viewers). What would you expect to see? Can you attach an annotated sketch/photoshopped image of what you would like to get? What is the end goal/clinical use?</p>

---

## Post #16 by @cphillips (2018-07-10 14:49 UTC)

<p>Yes, but I am wondering if I can view more than just the current red slice location. Right now, I only see the current coronal slice on the axial image.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b289245186afa1655e0756fe728f34e39dbedef.png" alt="bad" data-base62-sha1="m8AVLly8ew63xXA446RGkg0Ozkr" width="347" height="221"></p>
<p>Since there are 8 coronal slices total, I want to see something that looks like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e243592c1e14f2436479fb4c8ba2da264a57b97.png" alt="slice_planning" data-base62-sha1="6AbxA5c6VxE7ZsukzxF3bPMi1Gn" width="393" height="226"></p>
<p>I am attempting to see how much of the total brain volume of an MRI scan was captured with the coronal scan, for research purposes.</p>

---

## Post #17 by @lassoan (2018-07-10 15:03 UTC)

<p>Thanks for the clarification. If you don’t see multiple lines then maybe you use a lightbox view. Since all slice and 3D views dynamic (you can easily scroll through the volume, cross-reference different slice view directions and reconstructed 3D views, etc.) lightbox views have fallen out of favor. We have not removed them from the application yet, but probably will at the next major release (maybe we’ll add a module instead that can generate a large, static image, similar to radiography films that used to be printed and hung over a lightbox).</p>
<p>I would recommend to try to move away from static 2D slices and use the application interactively.</p>
<p>If that’s not an option for now, you can use “Four by three slice” layout (it creates a separate view for each slice instead of just a single slice view with a lightbox mode). it is slightly inconvenient that you need to position the slice view sliders manually, but you can write a few-line Python script that can do it automatically.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63d0aaf2234f50dcac051a8833e4f2c59169be6d.jpeg" data-download-href="/uploads/short-url/ef0kXYlKRDvnmwtQY9qdxnyh4IZ.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d0aaf2234f50dcac051a8833e4f2c59169be6d_2_577x500.jpg" alt="image" data-base62-sha1="ef0kXYlKRDvnmwtQY9qdxnyh4IZ" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d0aaf2234f50dcac051a8833e4f2c59169be6d_2_577x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d0aaf2234f50dcac051a8833e4f2c59169be6d_2_865x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63d0aaf2234f50dcac051a8833e4f2c59169be6d_2_1154x1000.jpg 2x" data-dominant-color="585858"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1950×1688 866 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #18 by @cphillips (2018-07-10 15:17 UTC)

<p>Many thanks. I am trying the “Four by three” slice layout for now and am not able to get windows 4-12 to display their lines on the green image (no blue/gray lines are visible). The green window, and all of the windows from 4-12 are all part of the same view group.</p>

---

## Post #19 by @cphillips (2018-07-10 15:17 UTC)

<p>Many thanks. I am trying the “Four by three” slice layout for now and am not able to get windows 4-12 to display their lines on the green image (no blue/gray lines are visible). The green window, and all of the windows from 4-12 are all part of the same view group.</p>

---

## Post #20 by @lassoan (2018-07-10 15:19 UTC)

<p>By default all the grey views are set to the same slice. You need to adjust the slice positions with the sliders to spread them out. As I described above, it is inconvenient, but if needed often then it can be automated using a short Python script.</p>

---

## Post #21 by @cphillips (2018-07-10 15:20 UTC)

<p>I have spread them out, they are positioned to different slices. But, the lines are still not appearing on the green image.</p>

---

## Post #22 by @lassoan (2018-07-10 15:21 UTC)

<p>Have you enabled display of slice intersections?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d953a56f5402ef54e75bb1b1798bc2ac59c2026c.png" data-download-href="/uploads/short-url/v0yOYXbcwH76ujIIHkp8bpfunH6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d953a56f5402ef54e75bb1b1798bc2ac59c2026c.png" alt="image" data-base62-sha1="v0yOYXbcwH76ujIIHkp8bpfunH6" width="380" height="500" data-dominant-color="E0E3EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">509×668 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @cphillips (2018-07-10 15:25 UTC)

<p>Yes, I have. Not sure why it is not working</p>

---

## Post #26 by @cphillips (2018-07-10 15:26 UTC)

<p>I think I figured it out–disabled and then enabled Slice Intersections seemed to do the trick. Many thanks again!</p>

---

## Post #27 by @cphillips (2018-07-10 19:21 UTC)

<p>I have written a custom python script to do this (saved as a .py file, which I wrote in Notepad) but have not had luck running it with 3D Slicer. I added the path for the directory it is in to Edit–&gt;Application Settings–&gt;Modules and reset Slicer, but I don’t see it under the Examples menu.</p>

---

## Post #28 by @lassoan (2018-07-10 20:29 UTC)

<p>See explanation in Slicer Python programming tutorial: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial</a></p>
<p>There is also a brand new option of running <a href="https://discourse.slicer.org/t/jupyter-notebooks-are-now-usable-in-3d-slicer/3438">Slicer Python scripts from Jupyter notebooks</a>.</p>

---

## Post #29 by @cphillips (2018-07-11 13:27 UTC)

<p>I have followed the steps in the tutorial exactly, but I get an error when I try to add the module to the extension.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2b33a78490ab7200015a6936383cef19c443cf6.png" alt="error_message" data-base62-sha1="yD1xEZ5DxLdIJimiHtMV5J85SUm" width="510" height="118"></p>

---

## Post #31 by @lassoan (2018-07-11 13:46 UTC)

<p>Check if the error log contains more details. Maybe module class name does not match exactly the .py file name.</p>

---

## Post #32 by @cphillips (2018-07-18 17:09 UTC)

<p>Hello again, I have an additional question about this feature. Right now, I am attempting to calculate the total brain volume of a rat (excluding the cerebellum) from an MRI scan, using segmentation. I do this by creating a new segment, and painting the brain volume on each coronal slice (shown as lines against the oval-shaped axial cut below). I use the Segment Statistics module to view the total volume calculation (including all the slices) in mm^3.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3237f5bb943edb14d7edbb95bd052c1dbbb57789.png" alt="regular" data-base62-sha1="7afLyvpP9BvfnhRZke05g5IkCVz" width="364" height="279"></p>
<p>My question is, how does Slicer calculate the total volume? If it starts from the top of the image and works downwards, I would imagine that the image below is a good representation of what is part of the volume calculation, with each of the lines representing the top edge of a given slice. Each rectangle is the width of the slice thickness, and I have left slight gaps to represent the gaps between the slices, which are not included in the volume calculation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc79143a76aa65cb230f9c6d1d5aa51049a01ccc.png" alt="top_down" data-base62-sha1="A1tJsenCYpV47HW2bqmfK5STO8c" width="408" height="301"></p>
<p>On the other hand, it could start from the bottom and work up, as shown below:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f9a67b8979715937baad5fd6f61c2735ceeabd5.png" alt="bottom_up" data-base62-sha1="2e1Ymt5LOOvNNtB7V7qayLzY8nP" width="394" height="319"></p>
<p>It is important for me to know how the volume is being calculated, as I need to know whether the slices include the cerebellum (at the bottom of the brain).</p>

---

## Post #33 by @pieper (2018-07-18 20:48 UTC)

<p>Just look at the segmentation in the other orthogonal views and see what is included in the segmentation.  By default the segmentations will be binary labelmaps that fill the voxels of the master volume and there wouldn’t be any gap.</p>

---

## Post #34 by @cphillips (2018-07-19 14:13 UTC)

<p>Thank you. One point of confusion still: as per the DICOM header, my slice thicknesses are 1mm, and the spacing between slices is 2mm. This means that there is a gap between slices of 1mm. Does the volume calculation done by the statistics module include this gap as part of the calculation? I had asked this question before and was assured that only the slice thickness (not the gap) was part of the volume calculation, but the 3D rendering of the segment appears to fill in the gap as well.</p>

---

## Post #35 by @cphillips (2018-07-19 14:13 UTC)

<p>Thank you. One point of confusion still: as per the DICOM header, my slice thicknesses are 1mm, and the spacing between slices is 2mm. This means that there is a gap between slices of 1mm. Does the volume calculation done by the statistics module include this gap as part of the calculation? I had asked this question before and was assured that only the slice thickness (not the gap) was part of the volume calculation, but the 3D rendering of the segment appears to fill in the gap as well.</p>

---

## Post #36 by @pieper (2018-07-20 12:27 UTC)

<p>Hi <a class="mention" href="/u/cphillips">@cphillips</a> -</p>
<p>Perhaps it was misstated or unclear, but actually the the spacing between slices is the thing that Slicer uses for calculating volumes.  The gap is not part of the calculation in the sense that Slicer is interpolating between slices and does not take into account the thickness and gap information.</p>
<p>To put it another way, Slicer constructs a volume which has a matrix IJKToRAS that maps from index space (IJK) to patient space (RAS).  There’s no concept of a voxel being larger or smaller than the spacing.  That is, if the thickness were larger than the slice spacing the slices would overlap.  If it were smaller there would be a gap, but this is not directly represented.</p>

---

## Post #37 by @lassoan (2018-07-20 13:33 UTC)

<p>Slice thickness indicates the quality of the imaging system - how well it can focus on a slice. The thickness value should not matter, unless extreme cases, e.g. if it is larger than the slice spacing or the size of the objects that you want to quantify.</p>

---
