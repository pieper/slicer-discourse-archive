---
topic_id: 20518
title: "Reduction In The Number Of T A C Cuts"
date: 2021-11-07
url: https://discourse.slicer.org/t/20518
---

# Reduction in the number of t.a.c. cuts

**Topic ID**: 20518
**Date**: 2021-11-07
**URL**: https://discourse.slicer.org/t/reduction-in-the-number-of-t-a-c-cuts/20518

---

## Post #1 by @Carota1965 (2021-11-07 16:03 UTC)

<p>hello everyone for a sufficient segmentation not all the files produced by the rx exam are needed.<br>
i am trying to selectively reduce the number of files<br>
and I wanted to know if 3d slicer does it automatically<br>
francesco</p>

---

## Post #2 by @lassoan (2021-11-07 16:12 UTC)

<p>Can you tell what you mean by “rx exam”?</p>
<p>Does it provide a series of parallel cross-sectional slices in DICOM format, one file per slice? If yes, then you can pick and choose to use any files. If you skip slices from the begin ijg or end then the imported image region will be smaller. You can even skip slices in the middle and then Slicer will interpolate between slices to fill in the gaps.</p>

---

## Post #3 by @Carota1965 (2021-11-07 16:19 UTC)

<p>first question: t.a.c. cone beam<br>
second question: a good cone beam machine produces 400 cuts which correspond to 400 dicom files are too many to segment manually.<br>
some software like mimics for example allow to reduce the number of files<br>
one yes and three no … for example</p>

---

## Post #4 by @Carota1965 (2021-11-07 16:25 UTC)

<p>automatically of course.<br>
because selecting files in a folder would take a long time</p>

---

## Post #5 by @lassoan (2021-11-07 17:08 UTC)

<aside class="quote no-group" data-username="Carota1965" data-post="3" data-topic="20518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/7ea924/48.png" class="avatar"> Carota1965:</div>
<blockquote>
<p>t.a.c. cone beam</p>
</blockquote>
</aside>
<p>It seems that you are from a different field than most other users because I have not heard any of the acronyms you use. What do you mean by “t.a.c”?</p>
<aside class="quote no-group" data-username="Carota1965" data-post="3" data-topic="20518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/7ea924/48.png" class="avatar"> Carota1965:</div>
<blockquote>
<p>good cone beam machine produces 400 cuts which correspond to 400 dicom files are too many to segment manually.</p>
</blockquote>
</aside>
<p>Segmenting each slice manually (using Paint/Draw/Erase effects) is possible, but it is only done as a last resort. Normally you use semi-automatic methods.</p>
<p>For the easiest segmentation tasks a global thresholding (using Threshold effect) can be a good start. For most cases a single global threshold is not suitable, so you would use “Grow from seeds” effect instead. For the most challenging cases, where boundary of segments are actually not visible (and only the operator can draw it manually based on his prior knowledge about the expected shape) you can use “Fill between slices” effect: you segment one out of every 5 to 50 slices and boundaries are smoothly interpolated between them.</p>
<p>If you want fully automatic segmentation then probably training a neural network is the best solution. You can create your own model using <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a> extension. It also has a number of pre-trained models for some common clinical segmentation tasks.</p>
<p>To get started with segmentation in 3D Slicer, check out <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this page</a>.</p>
<p>What structures would you like to segment?</p>

---

## Post #6 by @Carota1965 (2021-11-08 09:46 UTC)

<p>I thank you but that’s not the problem</p>

---

## Post #7 by @lassoan (2021-11-08 13:04 UTC)

<p>I’m not sure what the problem is, but let us know if we can help with anything. Since Slicer relies on very powerful libraries and has been developed by many people for decades, it can do almost everything, but it is not always easy to find and figure out how to use all its features.</p>

---

## Post #8 by @Carota1965 (2021-11-08 14:19 UTC)

<p>I send you a picture<br>
This is an example for teeth segmentation<br>
Left no right ok</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f005cb2ee2ff01ace6569e1b1e0cb8e059d9c587.jpeg" data-download-href="/uploads/short-url/yfl0mmNS2TublydRfwZZ7DUQ40T.jpeg?dl=1" title="image0.jpeg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f005cb2ee2ff01ace6569e1b1e0cb8e059d9c587_2_375x500.jpeg" alt="image0.jpeg" data-base62-sha1="yfl0mmNS2TublydRfwZZ7DUQ40T" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f005cb2ee2ff01ace6569e1b1e0cb8e059d9c587_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f005cb2ee2ff01ace6569e1b1e0cb8e059d9c587.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f005cb2ee2ff01ace6569e1b1e0cb8e059d9c587.jpeg 2x" data-dominant-color="9E9281"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image0.jpeg</span><span class="informations">480×640 82.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @jamesobutler (2021-11-08 14:32 UTC)

<p>You are looking for <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#fill-between-slices" rel="noopener nofollow ugc">Fill between slices</a> segment editor effect which allows you to manually segment at larger discrete offsets and then interpolate the segmentation in between those locations. This allows you to get your segmentation quicker.</p>

---

## Post #10 by @mau_igna_06 (2021-11-08 15:39 UTC)

<p>I think you need to use the resample volume module to downsample your CT. And then export the scalar volume of the CT as DICOM.</p>
<p>Hope it helps</p>

---

## Post #11 by @lassoan (2021-11-08 17:15 UTC)

<p>I agree, that “Fill between slices” seems to be the most relevant tool if you only need to segment one or few tooth in an image. If you need to segment hundreds of teeth or you want to fully automate the process then it may worth training a neural network using MONAILabel.</p>
<p>I see that <a class="mention" href="/u/carota1965">@Carota1965</a> is thinking about downsampling the CT but that would not be a good solution, as he would lose information without any gaining anything. There is no need to downsample the CT just to reduce the number of slices to draw contours on.</p>

---
