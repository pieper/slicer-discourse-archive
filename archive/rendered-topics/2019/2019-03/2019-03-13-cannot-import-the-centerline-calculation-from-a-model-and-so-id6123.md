---
topic_id: 6123
title: "Cannot Import The Centerline Calculation From A Model And So"
date: 2019-03-13
url: https://discourse.slicer.org/t/6123
---

# Cannot import the centerline calculation from a model and some other problems

**Topic ID**: 6123
**Date**: 2019-03-13
**URL**: https://discourse.slicer.org/t/cannot-import-the-centerline-calculation-from-a-model-and-some-other-problems/6123

---

## Post #1 by @cduque (2019-03-13 02:41 UTC)

<p>Dear community,</p>
<p>I am trying to obtain the centerline from a model.</p>
<p>First, I imported my dataset (It is a nrrd file created in Fiji from a ome tiff file from a lightsheet stack, as previously somebody recommended in this forum). Here, the first problem arrived: I had to downsample my dataset (originally 2540x1956x454, 16 bits) to 1000x700x227, 8 bits, because otherwise Slicer was crashing.</p>
<p>Then, I applied a median filter and threshold segmentation to create the model. I use the VMTK centerline calculation module, so I selected the feducials for the starting and endpoints. I clicked in Preview and the centerline was nicely calculated. However, in an attempt to extract it either as a binary image or a point list, I clicked in Start and Slicer crashed again.</p>
<p>Does anybody has any suggestion for extracting the centerline or any other alternative module to calculate and export the centerline of a model?</p>
<p>I really appreciate your help.</p>
<p>Best,</p>
<p>Carlos</p>

---

## Post #2 by @lassoan (2019-03-13 03:00 UTC)

<aside class="quote no-group" data-username="cduque" data-post="1" data-topic="6123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f14d63/48.png" class="avatar"> cduque:</div>
<blockquote>
<p>I had to downsample my dataset (originally 2540x1956x454, 16 bits) to 1000x700x227, 8 bits, because otherwise Slicer was crashing.</p>
</blockquote>
</aside>
<p>How much RAM do you have. Slicer should not crash unless you run out of memory. For dealing with a 4.5GB image you need to have about 40-50GB memory space available (preferably physical RAM).</p>
<aside class="quote no-group" data-username="cduque" data-post="1" data-topic="6123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f14d63/48.png" class="avatar"> cduque:</div>
<blockquote>
<p>However, in an attempt to extract it either as a binary image or a point list, I clicked in Start and Slicer crashed again.</p>
</blockquote>
</aside>
<p>Which module did you use for computing the centerline? Did you get the centerline as a model node? Can you attach a screenshot?</p>
<aside class="quote no-group" data-username="cduque" data-post="1" data-topic="6123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f14d63/48.png" class="avatar"> cduque:</div>
<blockquote>
<p>Does anybody has any suggestion for extracting the centerline or any other alternative module to calculate and export the centerline of a model?</p>
</blockquote>
</aside>
<p>“Extract skeleton” module is much simpler and robust way of computing centerline. It works by gradually peeling off layers from the input labelmap, so the thicker the structure is, the longer it takes. For faster extraction, you can resample the input image to make the vessel diameter about 5 voxels.</p>

---

## Post #3 by @cduque (2019-03-13 10:36 UTC)

<p>Dear Andras,</p>
<p>Thanks for your time and reply</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How much RAM do you have. Slicer should not crash unless you run out of memory. For dealing with a 4.5GB image you need to have about 40-50GB memory space available (preferably physical RAM).</p>
</blockquote>
</aside>
<p>I have 128 GB RAM. I post this problem some time ago in the forum: <a href="https://discourse.slicer.org/t/fail-to-load-a-big-tiff-stack/4832" class="inline-onebox">Fail to load a big tiff stack </a></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which module did you use for computing the centerline? Did you get the centerline as a model node? Can you attach a screenshot?</p>
</blockquote>
</aside>
<p>The VMTK (Vascular modelling toolkit).  I attach a screenshot of the “Data” tab and of the “Centerline calculation”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed179f6a15245f87b604ca1b350ed2fd04844538.png" data-download-href="/uploads/short-url/xPpLRhcw7Ucm34hBdd0ayfwlBDW.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed179f6a15245f87b604ca1b350ed2fd04844538_2_650x500.png" alt="grafik" data-base62-sha1="xPpLRhcw7Ucm34hBdd0ayfwlBDW" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed179f6a15245f87b604ca1b350ed2fd04844538_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed179f6a15245f87b604ca1b350ed2fd04844538_2_975x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed179f6a15245f87b604ca1b350ed2fd04844538.png 2x" data-dominant-color="B2B3CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1280×984 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48d2003c99fdf34ca68211c52ff2df070b1e8c79.png" data-download-href="/uploads/short-url/aociLSAB4Fl4HIfsylMa8lJgJ8B.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48d2003c99fdf34ca68211c52ff2df070b1e8c79_2_650x500.png" alt="grafik" data-base62-sha1="aociLSAB4Fl4HIfsylMa8lJgJ8B" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48d2003c99fdf34ca68211c52ff2df070b1e8c79_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48d2003c99fdf34ca68211c52ff2df070b1e8c79_2_975x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48d2003c99fdf34ca68211c52ff2df070b1e8c79.png 2x" data-dominant-color="B4B5CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1280×984 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>“Extract skeleton” module is much simpler and robust way of computing centerline. It works by gradually peeling off layers from the input labelmap, so the thicker the structure is, the longer it takes. For faster extraction, you can resample the input image to make the vessel diameter about 5 voxels.</p>
</blockquote>
</aside>
<p>I will try. Thanks!</p>

---

## Post #4 by @lassoan (2019-03-13 13:10 UTC)

<aside class="quote no-group" data-username="cduque" data-post="1" data-topic="6123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f14d63/48.png" class="avatar"> cduque:</div>
<blockquote>
<p>I had to downsample my dataset (originally 2540x1956x454, 16 bits) to 1000x700x227, 8 bits, because otherwise Slicer was crashing.</p>
</blockquote>
</aside>
<p>I have no problem loading and saving a 5GB nrrd image using Slicer-4.10.1. What operation caused the crash? Was it a crash or a hang? Can you get a stack trace?</p>

---

## Post #5 by @cduque (2019-03-13 13:19 UTC)

<p>I clicked on import data, clicked on Choos fiel to add, clicked on the file, it appeared in the window “Add data into scene” as volume and then click on. Then, it hang and had to close it through the Task Manager, because was totally irresponsive. I try waiting up to half an hour, and it kept being irresponsive.</p>

---

## Post #6 by @lassoan (2019-03-13 13:27 UTC)

<p>Try to leave it there for an hour and see if it loads the data eventually. Loading/saving may be much faster if the data is not compressed.</p>
<p>For me, <a href="https://1drv.ms/u/s!Arm_AFxB9yqHt4IFKkn6T01kBYTbWQ" rel="nofollow noopener">this 5GB dataset</a> loads within a few minutes. Can you try to load it and see if it works for you?</p>

---

## Post #7 by @cduque (2019-03-14 09:42 UTC)

<p>Yes, I could load it in roughly 2 minutes. I will try to save the stack as .MHD and try to load</p>

---
