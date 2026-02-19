---
topic_id: 22881
title: "Remove Unwanted Region From Slices To Create 3D Model"
date: 2022-04-09
url: https://discourse.slicer.org/t/22881
---

# Remove unwanted region from slices to create 3D Model

**Topic ID**: 22881
**Date**: 2022-04-09
**URL**: https://discourse.slicer.org/t/remove-unwanted-region-from-slices-to-create-3d-model/22881

---

## Post #1 by @bhowmisp (2022-04-09 10:17 UTC)

<p>Hi,</p>
<p>I am new to Slicer, I am using the Visible Human project data Cryosection images to build a 3D model with all the possible anatomical details.</p>
<p>The problem is, each slice is placed in a bounded region/platform, which are obviously being transferred to the 3D model when I stack up the images(Vector to Scalar volume conversion). It is creating an issue and frankly defeats the purpose. I can remove some parts of it by clipping of the edges of the volume, but I guess that’s only for visualization purposes.</p>
<p>Can you please guide me on how to totally remove them?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85df84edb52457526e8398f411be97ea86b8a4d2.jpeg" data-download-href="/uploads/short-url/j6iognLcST1ZHRwD46ZCNoW4oUy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85df84edb52457526e8398f411be97ea86b8a4d2_2_690x454.jpeg" alt="image" data-base62-sha1="j6iognLcST1ZHRwD46ZCNoW4oUy" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85df84edb52457526e8398f411be97ea86b8a4d2_2_690x454.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85df84edb52457526e8398f411be97ea86b8a4d2_2_1035x681.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85df84edb52457526e8398f411be97ea86b8a4d2.jpeg 2x" data-dominant-color="424046"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1365×900 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-04-09 12:06 UTC)

<p>You can blank out regions in a volume using “Mask volume” effect in Segment Editor, but I’m not completely sure if this is what you need.</p>
<aside class="quote no-group" data-username="bhowmisp" data-post="1" data-topic="22881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e5b9ba/48.png" class="avatar"> bhowmisp:</div>
<blockquote>
<p>is creating an issue and frankly defeats the purpose</p>
</blockquote>
</aside>
<p>Can you explain what issue it creates? What is the purpose that it defeats?</p>
<aside class="quote no-group" data-username="bhowmisp" data-post="1" data-topic="22881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e5b9ba/48.png" class="avatar"> bhowmisp:</div>
<blockquote>
<p>build a 3D model with all the possible anatomical details</p>
</blockquote>
</aside>
<p>I’m afraid that this is an impossible task. There is no such thing as a perfect segmentation. You need a very specific goal of exactly what details you need to extract, with what accuracy. If you don’t have a well-defined stopping criteria (what is good enough) then you take on a never-ending job.</p>
<p>I see that how the Visible Human data sets could appear as the ultimate atlas, but the images are too low quality for most applications. Its the resolution is very low by today’s standards and they lack details that you can get from more specialized imaging protocols.</p>
<p>There are a few segmentations of the data set, for example by <a href="https://www.voxel-man.com/segmented-inner-organs-of-the-visible-human/">Voxel-Man</a>. If you find that the Visible Human data sets are good enough for you then you might use the voxel-man segmentation as a starting point (although there could be limitations due to licensing).</p>

---

## Post #3 by @bhowmisp (2022-04-09 19:35 UTC)

<p>Hi,</p>
<p>Sorry for the confusion.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127affa3561ba39c7db9f15c87618a0f325795be.jpeg" data-download-href="/uploads/short-url/2Du7iwM5n3oONMqobVv8KcnczO6.jpeg?dl=1" title="Issues.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/127affa3561ba39c7db9f15c87618a0f325795be_2_690x454.jpeg" alt="Issues.PNG" data-base62-sha1="2Du7iwM5n3oONMqobVv8KcnczO6" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/127affa3561ba39c7db9f15c87618a0f325795be_2_690x454.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/127affa3561ba39c7db9f15c87618a0f325795be_2_1035x681.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127affa3561ba39c7db9f15c87618a0f325795be.jpeg 2x" data-dominant-color="434046"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Issues.PNG</span><span class="informations">1365×900 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I want to specifically remove the red marked regions in the 3D view so that the body becomes visible. If you see in the 2D slice, the green encircled body slice is my only area of interest, I don’t want the other area outside of that(possibly the platform in which the body was kept) to stack up as well. This translates to the shaded regions, encircled in red, in the 3D model. Let me know if that made sense.</p>
<p>My end goal is clear, I want to extract the Vertebrae, Spinal cord and its corresponding roots and dorsal root ganglion at every level. I realize what you mean by the VHP images being too low in resolution, when I cut sections in this 3D model, the roots were barely visible.</p>
<p>I appreciate you pointing me towards any better resource regarding this. It would be of great help.</p>

---

## Post #4 by @lassoan (2022-04-09 21:15 UTC)

<p>You can blank out those image regions using Mask volume effect:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="bhowmisp" data-post="3" data-topic="22881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e5b9ba/48.png" class="avatar"> bhowmisp:</div>
<blockquote>
<p>My end goal is clear, I want to extract the Vertebrae, Spinal cord and its corresponding roots and dorsal root ganglion at every level. I realize what you mean by the VHP images being too low in resolution, when I cut sections in this 3D model, the roots were barely visible.</p>
</blockquote>
</aside>
<p>Vertebrae can be best segmented on high-resolution CT images. Nerves might be sufficiently visible on these images (depending on how far you need to go), but probably for best results some optimized MRI protocols would work best.</p>
<p>I would recommend to contact leading research groups for collaboration and data sharing. Maybe <a class="mention" href="/u/ron">@Ron</a> or <a class="mention" href="/u/pieper">@pieper</a> has some leads.</p>

---

## Post #5 by @bhowmisp (2022-04-10 02:25 UTC)

<p>Thank you for the solution!</p>
<p>I was indeed looking for open source Spine MRI datasets and thus came up with the VHP, I suspect they might not be that helpful.</p>
<p>I appreciate any help from <a class="mention" href="/u/Ron">@Ron</a> and <a class="mention" href="/u/pieper">@pieper</a> .</p>

---

## Post #6 by @pieper (2022-04-10 14:14 UTC)

<p>I’m not aware of any open source datasets of spine images focused on the nerves, but some cancer images might also include spines in the field of view and that might be helpful.  See <a href="https://www.cancerimagingarchive.net/">TCIA</a>.</p>

---
