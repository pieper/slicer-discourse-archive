# Resolution of segmentations change after saving. 

**Topic ID**: 31191
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/resolution-of-segmentations-change-after-saving/31191

---

## Post #1 by @austingrove (2023-08-17 07:40 UTC)

<p>Hello,</p>
<p>After saving segmentations and labels, I have noticed that sometimes certain structures change to a lower resolution. Not all segmentations change to a lower resolution, just some, but it is always the same structures. I am wondering if anyone knows why this is or if anyone has tips or suggestions to prevent this.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-08-17 07:55 UTC)

<p>In a segmentation with binary labelmap representation, each layer is allowed to have different geometry (origin, spacing, axis directions, extents) temporarily - to allow moving segments between segmentations without unnecessary quality loss (each resampling of a binary labelmap can lead to slight changes). All layers are forced to have the same geometry during certain editing operations and when the segmentation is saved to file.</p>

---

## Post #3 by @mikebind (2023-08-17 22:11 UTC)

<p>I didn’t know this.  Is it documented under what conditions this happens?  Since uniformity is forced on saving, shouldn’t it be forced when a segment is transferred into a different segmentation?  What is the use case where allowing the temporary altered resolution, but forcing it on saving, avoids unnecessary resampling? The only case I can think of is if you have a high resolution segment in segmentation A, copy it to lower resolution segmentation B, and then copy it again from segmentation B to segmentation C, which has a different low resolution, but I’m not sure when someone would routinely be doing that.</p>

---

## Post #4 by @lassoan (2023-08-18 21:09 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="31191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Is it documented under what conditions this happens?</p>
</blockquote>
</aside>
<p>It is described <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#binary-labelmap-representation">here</a>, but not in more detail than in my above post. It should not matter, because when you need segments to have the same geometry then the resampling happens automatically.</p>
<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="31191">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>The only case I can think of is if you have a high resolution segment in segmentation A, copy it to lower resolution segmentation B, and then copy it again from segmentation B to segmentation C, which has a different low resolution, but I’m not sure when someone would routinely be doing that.</p>
</blockquote>
</aside>
<p>This is a good example but there are many more. Resampling is performed using “lazy” strategy (i.e., as late as possible), to avoid any <em>unnecessary</em> loss of detail.</p>

---
