---
topic_id: 28135
title: "Using Paint Or Smoothing Tool Spoils The Segment"
date: 2023-03-02
url: https://discourse.slicer.org/t/28135
---

# Using Paint or Smoothing tool spoils the segment

**Topic ID**: 28135
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/using-paint-or-smoothing-tool-spoils-the-segment/28135

---

## Post #1 by @radiodid (2023-03-02 06:35 UTC)

<p>I recently ran with a problem in Slicer when I try to use Paint to edit a segment and segment immediately spoils on the first contact with the study. Pixels become huge, contours are rough, neighboring structures are layered with each other, and on 3D reconstructions, everything looks as if I did not use smoothing, but built a reconstruction in Minecraft.<br>
Smoothing has the same problem when using a sphere brush in Median mode. Instead of smoothing the area of interest, it immediately makes the entire segment untidy and crooked.<br>
Sometimes the problem with the segment can only be seen when you rerun a saved study.<br>
Sometimes it helps to delete the segmentation and create a new one with the old segment.</p>
<p>What could be the reason for this Slicer’s behavior? Maybe the problem is in the segments or segmentations themselves and how can I find out it?</p>

---

## Post #2 by @lassoan (2023-03-02 06:43 UTC)

<p>Everything works as intended. Your segmentation used closed surface or ribbon representation (e.g., because you loaded the segmentation from a model or a DICOM RT structure set). When you performed an editing operation, the source representation is atuomatically switched to binary labelmap, which is indeed “blocky” (it is made up of discrete voxels). See more information <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a>.</p>
<p>If you find that the binary labelmap representation is not sufficiently detailed then you can change the segmentation’s geometry as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---

## Post #3 by @radiodid (2023-03-02 09:09 UTC)

<p>Thanks, Andras<br>
I understand that blocks may appear during editing, but not sure that this size of “blocks” are fine. I had such a problem for the first time.<br>
On the other hand, I noticed that the size of some segmentations is different from the size of the original studies. Maybe the Slicer itself is trying to fit the segment to the basic CT size?<br>
BUT! For example, I run a few segmentations that differ in size from the original CT. Why most of them do not have such a problem, and some begin to have such a blocky appearance?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4fdc88c1fba29983dadc86b75836d71da8f5ae1.png" alt="image" data-base62-sha1="nxA24Z6DTzOo9shRSoJfVQOU5BT" width="376" height="460">       <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/323f2f2409a200e0191918f0ee1e39d13cae069a.png" alt="image" data-base62-sha1="7avfbuH2J59Wq7AOnsW0t0KtKno" width="302" height="466"></p>

---

## Post #4 by @lassoan (2023-03-02 12:54 UTC)

<aside class="quote no-group" data-username="radiodid" data-post="3" data-topic="28135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9e8a1a/48.png" class="avatar"> radiodid:</div>
<blockquote>
<p>Maybe the Slicer itself is trying to fit the segment to the basic CT size?</p>
</blockquote>
</aside>
<p>Yes. The default voxel size of the binary labelmap representation is set to be the same as the source volume that is selected when the segmentation is created. You can change the geometry as described in the Segment Editor documentation section that I linked above.</p>

---

## Post #5 by @radiodid (2023-03-02 16:39 UTC)

<p>But then why Slicer doesn’t try to adapt all the segments to suit the original size? The part works fine. So, for example, I have a CT with a size of 626x626x626 and 4 segments with a size of 333x333x333, but one of them will have structures with blocky pixels, and the other 3 are ideal <img src="https://emoji.discourse-cdn.com/twitter/man_shrugging.png?v=12" title=":man_shrugging:" class="emoji" alt=":man_shrugging:" loading="lazy" width="20" height="20"><br>
Sorry to bother you with these questions, but I’m curious to know how it works.</p>

---

## Post #6 by @lassoan (2023-03-02 17:35 UTC)

<p>To minimize the number of labelmap resampling operations (resampling is a lossy operation), resampling is only done when it is needed - for example when the segmentation is edited or written to file. Until then each segment keeps its own geometry, which may be different from the other segments (for example if the segment was copied from another segmentation). If you create a new segment then the reference geometry of the segmentation is used, which comes from the geometry of the source volume that was selected first when the segmentation was created.</p>
<p>This default behavior does not require any input from users and it does what users expect most of the time. If this is not ideal for your use case then you can set the segmentation geometry explicitly as described at the link above.</p>

---
