# How can I crop some CT data into same region?

**Topic ID**: 16863
**Date**: 2021-03-31
**URL**: https://discourse.slicer.org/t/how-can-i-crop-some-ct-data-into-same-region/16863

---

## Post #1 by @hir (2021-03-31 03:35 UTC)

<p>Hi, I’m new to 3D slicer.</p>
<p>I have several series of CT data, like day0,1,… for each mouse.<br>
I want to compare bone volume change over time.</p>
<p>I use “Expert Automated Registration” to align the orientations.</p>
<p>Then, I want to crop same region like below image.<br>
Which tool is appropriate?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56276271937914525664bbf2f5efe226b2d7523d.jpeg" data-download-href="/uploads/short-url/ci9ruEwhUt7NvP0e4ZEjKC3BU0l.jpeg?dl=1" title="スクリーンショット 2021-03-31 12.31.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56276271937914525664bbf2f5efe226b2d7523d_2_509x500.jpeg" alt="スクリーンショット 2021-03-31 12.31.06" data-base62-sha1="ci9ruEwhUt7NvP0e4ZEjKC3BU0l" width="509" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56276271937914525664bbf2f5efe226b2d7523d_2_509x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56276271937914525664bbf2f5efe226b2d7523d_2_763x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56276271937914525664bbf2f5efe226b2d7523d_2_1018x1000.jpeg 2x" data-dominant-color="82869F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2021-03-31 12.31.06</span><span class="informations">1336×1310 502 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
blue:     day0<br>
yellow:  day1<br>
red:       day2<br>
green:   day3<br>
black line: some regions I want to crop.(I will do it more accurately.)</p>

---

## Post #2 by @timeanddoctor (2021-03-31 04:29 UTC)

<p>you can crop it with the same ROI box.</p>

---

## Post #3 by @hir (2021-03-31 05:39 UTC)

<p>Thank you for replying.</p>
<p>I tried that and I can.<br>
Now my procedure is below.</p>
<p>Load series of DICOM data.<br>
→ Use “Expert Automated Registration”, fix:day0 move:day1,2,3<br>
→ Make Segmentations to see bone volumes(like the photo above.)<br>
→ make ROI box and rotate it with “Transform”<br>
→ Apply ROI box to original volume data with “Crop Volume”<br>
→ Make Segmentations of cropped Volume.<br>
→Calculate segment Volume with “Segment statistics”</p>
<p>It takes much time. Can I shorten these steps?<br>
Also, is it possible to apply scissor tool(free form) simultaneously to these Segmentations?</p>
<p>thanks.</p>

---

## Post #4 by @lassoan (2021-04-03 02:25 UTC)

<p>You can write a short Python code snippet that performs all the steps automatically. You can run the code snippet using a keyboard shortcut (or if you want to have a more convenient GUI then create a Python scripted module). See lots of examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">the script repository</a>. You can learn about basics of Slicer programming from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">developer tutorials</a>.</p>

---

## Post #5 by @chir.set (2021-04-03 08:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="16863">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>create a Python scripted module</p>
</blockquote>
</aside>
<p>As far as ‘crop some CT data into same region’ is concerned, you may get some insight from this <a href="https://github.com/chir-set/TemplateROICrop" rel="noopener nofollow ugc">module</a>. It applies saved ROIs to crop CT volumes of known dimensions. You will obviously need more scripting for your requirements.</p>

---

## Post #6 by @hir (2021-04-05 00:56 UTC)

<p>Thanks a lot!<br>
I will try to make python scripts.</p>

---
