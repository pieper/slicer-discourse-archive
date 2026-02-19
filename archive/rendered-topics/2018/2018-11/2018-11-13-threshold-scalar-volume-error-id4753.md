---
topic_id: 4753
title: "Threshold Scalar Volume Error"
date: 2018-11-13
url: https://discourse.slicer.org/t/4753
---

# Threshold scalar volume error

**Topic ID**: 4753
**Date**: 2018-11-13
**URL**: https://discourse.slicer.org/t/threshold-scalar-volume-error/4753

---

## Post #1 by @kayarre (2018-11-13 22:04 UTC)

<p>I have a signed distance field that  I am thresholding to a label map volume, everything below zero should be identified as the segmentation that I am interested in, however when I do this the returned mask is larger than expected.</p>
<p>Thresholding with <strong>below</strong> and  <strong>-0.01</strong> values one can see that the data probe (arrow missing in screenshot) is on the blue edge next to pink region is segmented but the levelset background image is positive. So somehow the region is growing by a layer of voxels?</p>
<p>Is there something I am doing wrong, or is this a bug? the levetset is of type float.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/0600f10f6386c9ba35ea26dc15b60ce16b50d681.png" data-download-href="/uploads/short-url/R6SHtSpzAijjFzK0uFaPSRAcpj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0600f10f6386c9ba35ea26dc15b60ce16b50d681_2_690x223.png" alt="image" data-base62-sha1="R6SHtSpzAijjFzK0uFaPSRAcpj" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0600f10f6386c9ba35ea26dc15b60ce16b50d681_2_690x223.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0600f10f6386c9ba35ea26dc15b60ce16b50d681_2_1035x334.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0600f10f6386c9ba35ea26dc15b60ce16b50d681_2_1380x446.png 2x" data-dominant-color="D3CCCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1647×534 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-11-14 05:39 UTC)

<p>How did you threshold the distance field to a labelmap?<br>
Does the labelmap, the distance map, the segmentation master volume, and the segmentation’s internal binary labelmap representation has the same geometry (origin, spacing, axis directions)?</p>

---

## Post #3 by @pieper (2018-11-14 15:15 UTC)

<p><a class="mention" href="/u/kayarre">@kayarre</a> to facilitate investigation it would help if you can provide a sample dataset and sequence of steps to replicate where you see the inconsistency.</p>

---

## Post #4 by @kayarre (2018-11-15 00:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> threshold scalar volume, same origin, spacing and directions)</p>
<p><a class="mention" href="/u/pieper">@pieper</a>: see steps below, also give me a place to upload the image data and I will.</p>
<ol>
<li>load levelset image (same origin, spacing, and directions as source image. type float)</li>
<li>threshold scalar volume
<ul>
<li>input volume: 1.</li>
<li>output volume: set to label map (create new)</li>
<li>Type: Below, Threshold Value: -0.01, Outside Value: 1.0</li>
<li>Apply</li>
</ul>
</li>
<li>observe weird behavior described above where the label map covers positive values of the levelset</li>
</ol>

---

## Post #5 by @lassoan (2018-11-15 00:48 UTC)

<p>I’ve tested thresholding of a distance map IN Segment Editor and it worked perfectly. Have you tried that?</p>
<p>Could you share a scene where you can reproduce your problem?</p>

---

## Post #6 by @kayarre (2018-11-15 18:20 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Yep that works, <img src="https://emoji.discourse-cdn.com/twitter/man_facepalming.png?v=6" title=":man_facepalming:" class="emoji" alt=":man_facepalming:"><br>
is the scene the xml file that slicer always is wanting me to save?</p>

---

## Post #7 by @lassoan (2018-11-15 18:34 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="6" data-topic="4753">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>is the scene the xml file that slicer always is wanting me to save?</p>
</blockquote>
</aside>
<p>Yes, the .mrml file stores the scene (state of all MRML nodes).</p>

---

## Post #8 by @kayarre (2018-11-15 19:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> here is the scene<br>
<a href="https://gist.github.com/kayarre/1889a1be1a1b65d5f93548eb3be77381" rel="nofollow noopener">https://gist.github.com/kayarre/1889a1be1a1b65d5f93548eb3be77381</a></p>

---

## Post #9 by @lassoan (2018-11-15 19:16 UTC)

<p>The scene file does not contain any bulk data (images, etc.). To share a scene with someone, the easiest is to click on the small “giftbox” icon to create a .mrb file that saves the scene file and all data in a single file.</p>

---

## Post #10 by @kayarre (2018-11-15 22:15 UTC)

<p>That is fancy!</p>
<p><a href="https://drive.google.com/file/d/1o5lUg39ZLmI2dimYRKtwavGZgbd_30Mp/view?usp=sharing" rel="nofollow noopener">shared file from googel drive </a></p>

---

## Post #11 by @lassoan (2018-11-16 04:02 UTC)

<p>I’ve tested “Threshold Scalar Volume” module with your data set and it works as intended.</p>
<p>You might have though that thresholding binarizes the image, while it is not. It changes values below/above/outside the specified range and leaves other values unchanged. You see the “band” because you’ve created a labelmap volume for storing the output, which discretizes the output to integer values.</p>
<p>To get a binary volume, you can do it by running thresholding twice (once with “Negate threshold” disabled, then enabled) as shown below. However, you can binarize the image much more easily by using Segment Editor’s Threshold effect or Simple Filter module’s BinaryThresholdImageFilter.</p>
<p>Binarizing an image using Threshold Scalar Volume effect:</p>
<p><strong>Step 1:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40933e59ee36caaf835c6118a6e6b8ef673dfd1.png" data-download-href="/uploads/short-url/pGFF0vzMzoYn7suVTWkmF8OtqVz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b40933e59ee36caaf835c6118a6e6b8ef673dfd1_2_690x384.png" alt="image" data-base62-sha1="pGFF0vzMzoYn7suVTWkmF8OtqVz" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b40933e59ee36caaf835c6118a6e6b8ef673dfd1_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40933e59ee36caaf835c6118a6e6b8ef673dfd1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40933e59ee36caaf835c6118a6e6b8ef673dfd1.png 2x" data-dominant-color="F6F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×534 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Step 2:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd793b102a7d9ad82e9b8f9a4fcea515e0a04440.png" data-download-href="/uploads/short-url/vBffUhZGNHJ62CYrgTdDooCTune.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd793b102a7d9ad82e9b8f9a4fcea515e0a04440.png" alt="image" data-base62-sha1="vBffUhZGNHJ62CYrgTdDooCTune" width="690" height="378" data-dominant-color="F6F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">963×528 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @kayarre (2018-11-16 19:57 UTC)

<p>That makes a lot more sense. thank you.</p>

---
