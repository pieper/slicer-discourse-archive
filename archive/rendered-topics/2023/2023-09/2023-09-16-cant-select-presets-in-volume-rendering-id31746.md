# Can't select presets in Volume Rendering

**Topic ID**: 31746
**Date**: 2023-09-16
**URL**: https://discourse.slicer.org/t/cant-select-presets-in-volume-rendering/31746

---

## Post #1 by @radiodid (2023-09-16 06:41 UTC)

<p>I want to create a 3D reconstruction for CBCT, but Slicer won’t let me choose a preset if I’ve already created segmentation. But if I run only the NRRD file without segmentations, everything works fine.<br>
What is the cause of the problem and how can it be solved?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce0fa3efda5bc6bbec798de1b910be8c5e1965cb.png" alt="image" data-base62-sha1="toTRPCQDmFW5lYl1a2hekQScLzl" width="589" height="140"></p>

---

## Post #2 by @slicer365 (2023-09-16 15:56 UTC)

<p>You should choose your Volume data first!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e47df6f93ecd5b7a06bffadf81edb81802f3fb30.jpeg" data-download-href="/uploads/short-url/wBkJYeagsqJVzvXB85dd26Rcovu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e47df6f93ecd5b7a06bffadf81edb81802f3fb30_2_517x201.jpeg" alt="image" data-base62-sha1="wBkJYeagsqJVzvXB85dd26Rcovu" width="517" height="201" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e47df6f93ecd5b7a06bffadf81edb81802f3fb30_2_517x201.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e47df6f93ecd5b7a06bffadf81edb81802f3fb30_2_775x301.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e47df6f93ecd5b7a06bffadf81edb81802f3fb30_2_1034x402.jpeg 2x" data-dominant-color="82817F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1221×475 96.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2023-09-16 19:24 UTC)

<p>If you load an image as a segmentation then you don’t need volume rendering module to show it in 3D. That’s why the segmentation is not showing up in the Volume Rendering module.  Instead, you can show a segmentation in 3D by going to the Segmentation module and clicking the “Show 3D” button.</p>

---

## Post #4 by @radiodid (2023-09-17 05:14 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="2" data-topic="31746" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>You should choose your Volume data first!</p>
</blockquote>
</aside>
<p>I did that and it still doesn’t help</p>

---

## Post #5 by @radiodid (2023-09-17 05:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="31746" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you load an image as a segmentation then you don’t need volume rendering module to show it in 3D. That’s why the segmentation is not showing up in the Volume Rendering module.  Instead, you can show a segmentation in 3D by going to the Segmentation module and clicking the “Show 3D” button.</p>
</blockquote>
</aside>
<p>I run Slicer’s MRML file, which opens CT and segmentation. Also, I know that the segmentations can be seen in the usual 3D mode. However, I have never had a problem before when trying to create 3D reconstructions in Volume Rendering with such CTs.<br>
It doesn’t have much clinical significance for me, but I wonder what could be causing it.</p>

---

## Post #6 by @chir.set (2023-09-17 11:03 UTC)

<p>Does it work with sample data?</p>
<p>It could be that your volume is too big for your GPU rendering capacities. Try to crop down your volume.</p>

---

## Post #7 by @radiodid (2023-09-17 15:53 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="31746" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It could be that your volume is too big for your GPU rendering capacities. Try to crop down your volume.</p>
</blockquote>
</aside>
<p>I`ve tried with other CTs of the same size and some of them work and some don’t. And there are also larger CTs that work without problems.</p>

---

## Post #8 by @lassoan (2023-09-17 19:15 UTC)

<p>If you can provide data and instructions that reproduce the issue then we can have a look.</p>

---
