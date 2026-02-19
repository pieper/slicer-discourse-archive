---
topic_id: 4411
title: "Volume Rendering Of Binary Label Maps"
date: 2018-10-16
url: https://discourse.slicer.org/t/4411
---

# Volume rendering of binary label maps

**Topic ID**: 4411
**Date**: 2018-10-16
**URL**: https://discourse.slicer.org/t/volume-rendering-of-binary-label-maps/4411

---

## Post #1 by @katharina_hecker (2018-10-16 12:07 UTC)

<p>Hello everyone,</p>
<p>is it generally possible to use the volume rendering module for created binary label maps, which were originating from segmentations?</p>
<p>I was exporting my segments to binary label maps and were trying to visualize them as a volume rendering… it did not work. Is this not possible? And if yes, why not?</p>
<p>Might there be another solutions?</p>
<p>Thanks for all your inputs!</p>

---

## Post #2 by @cpinter (2018-10-16 14:16 UTC)

<aside class="quote no-group" data-username="katharina_hecker" data-post="1" data-topic="4411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>it did not work</p>
</blockquote>
</aside>
<p>We need a bit more information. What did you do? What did you expect? What happened instead? Thanks!</p>

---

## Post #3 by @katharina_hecker (2018-10-16 15:28 UTC)

<p>Hi,<br>
I was segmenting an nrrd file which contained a gray scale image stack.<br>
I was creating several different segments from blood vessels with different colors and exported them thereupon in the data module to a binary label map. This binary label map is in a volume format right?<br>
So I was hoping to generate a volume rendering (VTK GPU Ray Casting) out of this binary label map…</p>
<p>It would also help if I could use the Volume Rendering module for one segmentation, which was converted to a binary label map.</p>
<p>What not worked was that I could not visualize the binary label map as a volume rendering in the 3D view. I selected it as according volume and clicked on the eye icon but no 3D volume was visible (I tried also to change the Shift)…</p>

---

## Post #4 by @cpinter (2018-10-16 15:30 UTC)

<p>You said that volume rendering did not work, so it would be great if you explained what did it not work in <em>that</em>: What did you do? What did you expect? What happened instead?</p>
<p>Btw what Slicer version did you use? 4.8.1 is quite outdated especially in terms of Segment Editor and Volume Rendering, so if you used that then please install a recent nightly such as <a href="https://download.slicer.org/?date=2018-10-09">this</a>.</p>

---

## Post #5 by @katharina_hecker (2018-10-16 15:32 UTC)

<p>I explained it above again…<br>
I´m currently using 4.9.0…<br>
I will try it with the nightly version</p>

---

## Post #6 by @cpinter (2018-10-16 15:45 UTC)

<p>I understand what you want to do and why. Your way of creating the labelmap volume looks fine. But you didn’t describe what’s the problem with volume rendering, which is your question.</p>
<ol>
<li>Go to Volume Rendering module</li>
<li>Use GPU volume rendering</li>
<li>Turn on visibility for the labelmap volume</li>
<li>I expect to see X, but instead I see Y, see screenshot</li>
</ol>
<p>Something like this please.</p>

---

## Post #7 by @lassoan (2018-10-16 16:13 UTC)

<aside class="quote no-group" data-username="katharina_hecker" data-post="1" data-topic="4411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>And if yes, why not?</p>
</blockquote>
</aside>
<p>You can use volume rendering to show segments (you may need to adjust Scalar Color Mapping function to assign each color to map colors to voxel values 1.0, 2.0, …), however the result won’t be nice:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3112f69839848e4a6db02324aaf7876b441a81b8.png" data-download-href="/uploads/short-url/7081wKISAfURZAVBGnZlxsMcieI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3112f69839848e4a6db02324aaf7876b441a81b8_2_690x360.png" alt="image" data-base62-sha1="7081wKISAfURZAVBGnZlxsMcieI" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3112f69839848e4a6db02324aaf7876b441a81b8_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3112f69839848e4a6db02324aaf7876b441a81b8_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3112f69839848e4a6db02324aaf7876b441a81b8_2_1380x720.png 2x" data-dominant-color="6F6D6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1003 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can get the same look and just as good rendering speed by using “Show 3D” function with smoothing turned off.</p>
<p>If you smooth the volume to get a better look then you’ll have interpolation artifacts at the edges. A solution can be to use multi-volume rendering, but it is still experimental (no shading is available in multi-volume rendering mode).</p>
<p>Therefore, right now for 3D display of segments your best option is to click “Show 3D” button.</p>

---

## Post #8 by @katharina_hecker (2018-10-17 06:04 UTC)

<p>I was trying it again today with another version and now I can see the segmentation, thank you!</p>

---

## Post #9 by @katharina_hecker (2018-10-17 06:05 UTC)

<p>yes exactly, I tried the smoothing too. Thank you!</p>

---

## Post #10 by @eduardo.ecamargo (2021-02-08 18:38 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>. " however the result won’t be nice:". Could you tell me why? Or maybe point out some document with an explanation.</p>

---

## Post #11 by @lassoan (2021-02-08 18:53 UTC)

<p>See the image <a href="https://discourse.slicer.org/t/volume-rendering-of-binary-label-maps/4411/7">above</a>, you can barely make out the shape of the segment, even for a very simple shape.</p>
<p>By smoothing the labelmap, you can get visualization that is similar to surface rendering, like these:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdba75ac4c953af68712fd527842d38caa899636.png" data-download-href="/uploads/short-url/r4pJfIllZtQnZq5165l00aHqNQW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdba75ac4c953af68712fd527842d38caa899636_2_200x200.png" alt="image" data-base62-sha1="r4pJfIllZtQnZq5165l00aHqNQW" width="200" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdba75ac4c953af68712fd527842d38caa899636_2_200x200.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdba75ac4c953af68712fd527842d38caa899636_2_300x300.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdba75ac4c953af68712fd527842d38caa899636_2_400x400.png 2x" data-dominant-color="9999BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">579×559 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>A hybrid option exists, too, when you take the color from the segmentation but opacity from another volume (smoothed labelmap or the original input image):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97.jpeg" data-download-href="/uploads/short-url/x3tORNYZvwWMcQFoPQuTEVqgHuD.jpeg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97_2_690x494.jpeg" alt="" data-base62-sha1="x3tORNYZvwWMcQFoPQuTEVqgHuD" role="presentation" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97.jpeg 2x" data-dominant-color="13130F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">881×632 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>See more information about this option <a href="https://discourse.slicer.org/t/2021-01-19-hangout/15585/2">here</a>.</p>

---
