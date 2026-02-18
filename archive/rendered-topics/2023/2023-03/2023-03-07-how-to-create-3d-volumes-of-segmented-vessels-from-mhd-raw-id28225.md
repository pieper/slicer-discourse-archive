# How to create 3D volumes of segmented vessels from .mhd/.raw?

**Topic ID**: 28225
**Date**: 2023-03-07
**URL**: https://discourse.slicer.org/t/how-to-create-3d-volumes-of-segmented-vessels-from-mhd-raw/28225

---

## Post #1 by @hoppymop (2023-03-07 17:38 UTC)

<p>Hej,</p>
<p>My aim is to create 3D volumes of .mhd/.raw-files of segmented abdomen vessels (CT-images) and eventually extract the center-lines. The 3D volume of the segmented vessels looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6a3f0000c34a2900870c10ea1b5d9054b94c609.jpeg" data-download-href="/uploads/short-url/uCNpC9zPdaDILx5RaQ62ME8p0ud.jpeg?dl=1" title="23027a52-2c93-4156-b3cf-d65d23e965fe" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6a3f0000c34a2900870c10ea1b5d9054b94c609_2_310x500.jpeg" alt="23027a52-2c93-4156-b3cf-d65d23e965fe" data-base62-sha1="uCNpC9zPdaDILx5RaQ62ME8p0ud" width="310" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6a3f0000c34a2900870c10ea1b5d9054b94c609_2_310x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6a3f0000c34a2900870c10ea1b5d9054b94c609_2_465x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6a3f0000c34a2900870c10ea1b5d9054b94c609.jpeg 2x" data-dominant-color="2D332E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">23027a52-2c93-4156-b3cf-d65d23e965fe</span><span class="informations">482×776 68.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There is one CT-data set with segmented vessels in the same color, where I can easily use thresholding to create a 3D volume. The other CT-data set shows different colors for the vessel segmentation as shown in the image above.</p>
<p>How can I create 3D volumes of segmented vessels (.mhd/.raw) with different colors?</p>
<p>Thank you so much for your help!</p>
<p>How can I create a 3D volume of these differently colored segmented vessels?</p>

---

## Post #2 by @lassoan (2023-03-08 03:51 UTC)

<aside class="quote no-group" data-username="hoppymop" data-post="1" data-topic="28225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hoppymop/48/18682_2.png" class="avatar"> hoppymop:</div>
<blockquote>
<p>How can I create 3D volumes of segmented vessels (.mhd/.raw) with different colors?</p>
</blockquote>
</aside>
<p>You can use the Segment Editor module for this.</p>
<aside class="quote no-group" data-username="hoppymop" data-post="1" data-topic="28225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hoppymop/48/18682_2.png" class="avatar"> hoppymop:</div>
<blockquote>
<p>How can I create a 3D volume of these differently colored segmented vessels?</p>
</blockquote>
</aside>
<p>If you save the segmentation then you get exactly that, a volume where each segment is represented by a different label (color).</p>

---

## Post #3 by @hoppymop (2023-03-08 05:55 UTC)

<p>Which tool should I use in segment editor? That’s my problem. I can use threshold, but it allowed me to choose one label (color) at a time. I couldn’t choose all labels at once.</p>

---

## Post #4 by @muratmaga (2023-03-08 06:42 UTC)

<p><a class="mention" href="/u/hoppymop">@hoppymop</a><br>
Threshold the entire network as one segment.</p>
<p>Create blank segments for each of those branches.</p>
<p>Set the active segment to a blank one.</p>
<p>use the scissors tool in the fill mode, and set the editable area Inside Segment_1 (or the name of the segment that contains the full network).</p>
<p>With scissors highlight the branch you want to separate in one cursor movement.<br>
Now that section will be in the new segment’s color.</p>
<p>Repeat for each of the branches.</p>

---
