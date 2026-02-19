---
topic_id: 12025
title: "Centerline Computation"
date: 2020-06-15
url: https://discourse.slicer.org/t/12025
---

# Centerline Computation

**Topic ID**: 12025
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/centerline-computation/12025

---

## Post #1 by @Deepa (2020-06-15 04:30 UTC)

<p>Hello Everyone,</p>
<p>I’m using VMTK module in Slicer to run Centerline Computation for <a href="https://github.com/DeepaMahm/misc/blob/master/Segment2.zip" rel="noopener nofollow ugc">this</a> model input using the latest Preview release.</p>
<p>The task has run for nearly 10 hours but it was unsuccessful.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae77744ff1aa504dfb71711a5724484c9eab8725.jpeg" data-download-href="/uploads/short-url/oTp0AWINkdeo6uKCReFcqC0uU1T.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae77744ff1aa504dfb71711a5724484c9eab8725_2_345x148.jpeg" alt="Untitled" data-base62-sha1="oTp0AWINkdeo6uKCReFcqC0uU1T" width="345" height="148" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae77744ff1aa504dfb71711a5724484c9eab8725_2_345x148.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae77744ff1aa504dfb71711a5724484c9eab8725_2_517x222.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae77744ff1aa504dfb71711a5724484c9eab8725_2_690x296.jpeg 2x" data-dominant-color="A8A8B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1905×821 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The notice that the endpoints are correctly computed and I think the actual problem is while writing the<br>
centerline properties. CellId and Radius was written to the file, but the other properties are not written to the properties table.</p>
<p>Could someone give this a try? I would like to know if it is successful.</p>
<p>In <a href="https://pubmed.ncbi.nlm.nih.gov/11678637/" rel="noopener nofollow ugc">this</a> paper by Luca Antiga, skeletonization of a large network takes 50 seconds.</p>

---

## Post #2 by @muratmaga (2020-06-15 05:13 UTC)

<p>again, the issue is reported in the error message (bad_alloc). You are running out of memory.</p>
<p>The paper you cite says</p>
<blockquote>
<p>“Thanks  to  the  regularity  of  the  capillary  lumenboundary shape, and in order to shorten the comput-ing  time,  the  images  were  resized  at  a  resolution  of 300x300 pixels with bicubic interpolation.”</p>
</blockquote>
<p>How big is your volume?</p>

---

## Post #3 by @Deepa (2020-06-15 05:18 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="12025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>again, the issue is reported in the error message (bad_alloc). You are running out of memory.</p>
</blockquote>
</aside>
<p>Yes, I am running this on a server and I am not sure how much of memory is required for this task.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="12025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>How big is your volume?</p>
</blockquote>
</aside>
<p>I have used segment editor to extract a subvolume from the original volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/133ac2455dd74f2708cfa894b17442cb2e2f9779.png" alt="Untitled" data-base62-sha1="2K6XEQtV7fRhq0e6QMz0bldV6hr" width="279" height="87"></p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="12025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Thanks to the regularity of the capillary lumenboundary shape, and in order to shorten the comput-ing time, the images were resized at a resolution of 300x300 pixels with bicubic interpolation.</p>
</blockquote>
</aside>
<p>Thanks a lot for pointing this out. I am not sure how to do this.<br>
Instead, I tried to use decimation in Surface Toolbox to reduce the number of points. This didn’t help because Centerline Computation could not be initiated using decimated model.</p>

---

## Post #4 by @muratmaga (2020-06-15 05:55 UTC)

<p>Your dataset is way larger than what they used.</p>
<p>I am not familiar with VMTK, or the centerline computation. If that’s a multithreaded task, you can try to find a powerful computer with dozens of cores, and hundreds of GBs of RAM. That will definitely speed up the task.</p>
<p>Otherwise, you can use <code>Crop Volume</code> to downsample your images prior to segmentation.</p>

---

## Post #5 by @Deepa (2020-06-15 06:15 UTC)

<p>Thank you.</p>
<p>First I’d like to try <code>Crop Volume</code> with the following settings. I’m using the output volume obtained after segmentation as an input here. I hope this is OK.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e02d966e3a497a0033489f4c7884b12e6f10b3c.png" data-download-href="/uploads/short-url/8QzHS2wCNzvmttesl0wUsJAUubW.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e02d966e3a497a0033489f4c7884b12e6f10b3c_2_201x250.png" alt="Untitled" data-base62-sha1="8QzHS2wCNzvmttesl0wUsJAUubW" width="201" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e02d966e3a497a0033489f4c7884b12e6f10b3c_2_201x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e02d966e3a497a0033489f4c7884b12e6f10b3c_2_301x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e02d966e3a497a0033489f4c7884b12e6f10b3c_2_402x500.png 2x" data-dominant-color="F4F4F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">620×768 33.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2020-06-15 15:47 UTC)

<p>I am not sure if Crop Volume works with the segmentation nodes directly. I would probably reduce the original volume and redo the segmentation at low resolution. Alternatively, if you don’t want to redo the segmentation, you can export your existing segment as a label map and reduce that (for that make sure to choose the interpolator as nearest neighbors).</p>
<p>Another option I think is to use the segmentation geometry and use a coarser resolution than the master volume.</p>
<p>I honestly do not know which one of these would give you the best fidelity with respect to the original high-resolution volume at reasonable volume sizes. <a class="mention" href="/u/lassoan">@lassoan</a> and others may have some other suggestion.</p>

---

## Post #7 by @muratmaga (2020-06-15 15:48 UTC)

<p><a class="mention" href="/u/deepa">@Deepa</a> nevermind, I think you are doing it right. I guess your master volume is a masked volume from the original data. So it  should be fine…</p>

---

## Post #8 by @Deepa (2020-06-15 16:45 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="12025">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Alternatively, if you don’t want to redo the segmentation, you can export your existing segment as a label map and reduce that (for that make sure to choose the interpolator as nearest neighbors).</p>
</blockquote>
</aside>
<p>Thank you, I’ll try with nearest neighbors. I did the same steps but used b-spline for interpolator and the cropped volume wasn’t created successfully.</p>

---

## Post #9 by @Deepa (2020-06-15 17:12 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a><br>
I am using nearest neighbors  this time<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad3d4d288e0ad8bbe709f6d931fe9939c336f865.jpeg" data-download-href="/uploads/short-url/oIxWhtQU87eOue2HSXlNgV3Nvoh.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad3d4d288e0ad8bbe709f6d931fe9939c336f865_2_345x139.jpeg" alt="Untitled" data-base62-sha1="oIxWhtQU87eOue2HSXlNgV3Nvoh" width="345" height="139" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad3d4d288e0ad8bbe709f6d931fe9939c336f865_2_345x139.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad3d4d288e0ad8bbe709f6d931fe9939c336f865_2_517x208.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad3d4d288e0ad8bbe709f6d931fe9939c336f865_2_690x278.jpeg 2x" data-dominant-color="C7C9E1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1643×663 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
For some reason, I find that the cubic box is not fit around 3D vessel segments before cropping.  I’m<br>
not sure if this will affect cropping.</p>

---

## Post #10 by @muratmaga (2020-06-15 17:16 UTC)

<p>You can modify where the ROI is set. Did you try the fit to volume option?</p>

---

## Post #11 by @Deepa (2020-06-15 17:45 UTC)

<p>Thank you. Yes, I tried <code>Fit to Volume</code>. Unfortunately, it didn’t help</p>

---
