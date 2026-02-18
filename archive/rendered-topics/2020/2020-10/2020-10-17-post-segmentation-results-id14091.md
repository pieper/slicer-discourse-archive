# Post segmentation results

**Topic ID**: 14091
**Date**: 2020-10-17
**URL**: https://discourse.slicer.org/t/post-segmentation-results/14091

---

## Post #1 by @sarvpriya1985 (2020-10-17 01:16 UTC)

<p>Hi,</p>
<p>I am facing an issue in segmentation that i is quite weird. Not sure what is going wrong. I segmented cervical vessels and after growing from seeds, I am getting some blobs only but not full volume. I did this three times- same result.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed165b7bef1c56de1581ec9839b10c3bd0291ea3.jpeg" data-download-href="/uploads/short-url/xPn3MaGVzN62m1HZymnolGhWmxd.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed165b7bef1c56de1581ec9839b10c3bd0291ea3_2_690x406.jpeg" alt="Capture" data-base62-sha1="xPn3MaGVzN62m1HZymnolGhWmxd" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed165b7bef1c56de1581ec9839b10c3bd0291ea3_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed165b7bef1c56de1581ec9839b10c3bd0291ea3_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed165b7bef1c56de1581ec9839b10c3bd0291ea3_2_1380x812.jpeg 2x" data-dominant-color="94989C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1919×1130 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Can someone pls tell me what is going wrong!</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-10-17 01:48 UTC)

<p>The blobs that you see in 3D are the seeds that you painted. If you want to see preview of the grown segmentation in 3D then check the Grow from seeds -&gt; Display -&gt; results - &gt; Show 3D checkbox.</p>

---

## Post #3 by @sarvpriya1985 (2020-10-17 01:57 UTC)

<p>Thanks Andras. Somehow i was clicking the show 3D button at top but it was not doing anything. But then i checked display (show 3D) and its working now.<br>
Thanks again!</p>

---
