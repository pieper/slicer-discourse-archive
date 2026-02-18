# Need to segment a hole

**Topic ID**: 19445
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/need-to-segment-a-hole/19445

---

## Post #1 by @jordanan (2021-08-31 18:12 UTC)

<p>I would like to segment a hole in a bone. Having no luck with thresholding is there another way that can allow me to do this quickly?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-08-31 18:14 UTC)

<p>It should be no problem to segment a hole using Segment Editor. If the hole is filled with fluid or soft tissue then contrast compared to the bone should be quite high, so thresholding should work well. You can attach an image to show us what kind of image you work with and why segmentation is challenging.</p>

---

## Post #3 by @jordanan (2021-09-03 15:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77811fa873ace25c89362e00f159a5d8c2da4640.jpeg" data-download-href="/uploads/short-url/h3bsQ49ZOzMDLZxHtuYuS79Xbfq.jpeg?dl=1" title="IMG_6187 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77811fa873ace25c89362e00f159a5d8c2da4640_2_582x499.jpeg" alt="IMG_6187 2" data-base62-sha1="h3bsQ49ZOzMDLZxHtuYuS79Xbfq" width="582" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77811fa873ace25c89362e00f159a5d8c2da4640_2_582x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77811fa873ace25c89362e00f159a5d8c2da4640_2_873x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77811fa873ace25c89362e00f159a5d8c2da4640_2_1164x998.jpeg 2x" data-dominant-color="686C6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_6187 2</span><span class="informations">1920×1649 299 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thresholding is difficult because it is a similar color to bone.</p>

---

## Post #4 by @muratmaga (2021-09-03 16:35 UTC)

<p>If the hole you want to segment is little circle in the red slice view, that should be no problem. There is a nice bright edge that should let you define a threshold that will pickup everything inside the hole, but not the edge. And then you can just use that as a masking value and point over the slices.</p>

---

## Post #5 by @jordanan (2021-09-03 17:43 UTC)

<p>Okay, can you explain further. When I try to just threshold that small circle it gets parts of the bone as well.</p>

---

## Post #6 by @muratmaga (2021-09-03 17:58 UTC)

<p>When you are in the threshold tool, you need to reduce the right hand side of the slide so that it is picking on the contents of the hole, but not the bone. The left hand side will be either at 0.</p>
<p>The click the use for masking, and then use the paint tool (with 3D option) to start painting inside the hole.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f724b1e88673a281ecdb625655b38c612fc09d92.png" data-download-href="/uploads/short-url/zgkykIMGYiNlDSQt7wbb9rKCNnI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f724b1e88673a281ecdb625655b38c612fc09d92_2_517x344.png" alt="image" data-base62-sha1="zgkykIMGYiNlDSQt7wbb9rKCNnI" width="517" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f724b1e88673a281ecdb625655b38c612fc09d92_2_517x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f724b1e88673a281ecdb625655b38c612fc09d92_2_775x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f724b1e88673a281ecdb625655b38c612fc09d92_2_1034x688.png 2x" data-dominant-color="4F5451"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1438×958 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jordanan (2021-09-07 13:47 UTC)

<p>Is their any way to do this more automatic using thresholding.</p>
<p>Is their a way to utilize the bright edge around the hole</p>

---

## Post #8 by @lassoan (2021-09-07 13:53 UTC)

<p>Yes, you can fully automate everything using Python scripting. You can find many examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-run-segment-editor-effects-from-a-script">script repository</a>.</p>
<p>However, probably you can segment a hole with semi-automatic tools in about 1 minute (after you have learned how to use the segment editor module), so you would only benefit of automation if you had to segment over a thousand or so data sets.</p>
<p>I would recommend to try the Local threshold effect. You can segment the hole with it by a couple of clicks:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cevlMLyhfK8" data-video-title='Segment Editor: New "Local threshold" effect' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cevlMLyhfK8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cevlMLyhfK8/maxresdefault.jpg" title='Segment Editor: New "Local threshold" effect' width="" height="">
  </a>
</div>


---

## Post #9 by @jordanan (2021-09-09 14:26 UTC)

<p>Thank you Local thresholding seems to work well.</p>
<p>In the top hole it is also segmenting outside the knee bone though. Is their a way to solve this, do I have to use the ROI?</p>

---

## Post #10 by @lassoan (2021-09-09 16:48 UTC)

<p>There are many ways to prevent leaking at the imaged region boundary (for example, you could crop the volume before segmentation; or define a free-form masking region), but defining a ROI for the local thresholding is probably the easiest to do.</p>

---

## Post #11 by @jordanan (2021-09-09 17:33 UTC)

<p>Okay good to hear. How do I define a masking region?</p>
<p>Also I tried to use the ROI but having trouble. From my understanding I have to have a local threshold segment, then create a new segment, press local threshold, create new ROI, an dc put it in my desired region. But how do I actually get it to create the segmentation, what button do I press?</p>

---

## Post #12 by @lassoan (2021-09-09 18:19 UTC)

<aside class="quote no-group" data-username="jordanan" data-post="11" data-topic="19445">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/94ad74/48.png" class="avatar"> jordanan:</div>
<blockquote>
<p>Okay good to hear. How do I define a masking region?</p>
</blockquote>
</aside>
<p>You can create a segment using any tools and then choose to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">use it as editable area</a>. However, as I wrote above, using a ROI should be simpler.</p>
<aside class="quote no-group" data-username="jordanan" data-post="11" data-topic="19445">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/94ad74/48.png" class="avatar"> jordanan:</div>
<blockquote>
<p>Also I tried to use the ROI but having trouble.</p>
</blockquote>
</aside>
<p>Define a ROI using the toolbar (choose to place ROI, drop two points, and adjust the ROI bounds as needed), then activate the Local threshold effect, define the intensity range (for example, by drawing a small region with a similar intensity range in one of the slice views), and then Ctrl+Click in a slice view to add that region to the segment.</p>

---
