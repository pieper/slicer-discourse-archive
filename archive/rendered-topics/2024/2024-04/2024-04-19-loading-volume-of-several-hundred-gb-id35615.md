---
topic_id: 35615
title: "Loading Volume Of Several Hundred Gb"
date: 2024-04-19
url: https://discourse.slicer.org/t/35615
---

# Loading volume of several hundred GB

**Topic ID**: 35615
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/loading-volume-of-several-hundred-gb/35615

---

## Post #1 by @cpinter (2024-04-19 11:37 UTC)

<p>Hi all,</p>
<p>I feel like this topic should have come up over the years but I couldn’t find anything (search on discourse is awful…).</p>
<p>What options do we have in Slicer if we want to load a volume of industrial CT that is several hundred GB large? Typically these images are stored as TIFF stacks with some metadata. It is possible to pack that much memory in the computer, but what if we don’t have all the memory?</p>
<p>Thank you very much!</p>

---

## Post #2 by @lassoan (2024-04-19 12:39 UTC)

<p>ImageStacks module can handle such images: it can load the entire volume at lower resolution so that the user can choose the region of interest and load that ROI at full resolution. The main limitation is usability (requires a several clicks and some wait each time the user wants to inspect another ROI) and that preview image quality is not optimal (because downsampling is done without a low-pass filter).</p>
<p>These limitations could be addressed by using a multiresolution file format. BigImage extension is a prototype that demonstrates how easy it is to implement panning/zooming of arbitrarily large images in Slicer using Zarr. It would not be that hard to implement a similar mechanism for volume rendering (request resolution and image region from Zarr depending on what part of the volume is visible; all can be implemented in Python, without any Slicer core change).</p>
<p>ITK has increasingly better support for reading/writing/processing of such images, so some processing operations may be feasible, too.</p>

---

## Post #3 by @cpinter (2024-04-19 12:43 UTC)

<p>Thank you very much Andras for the super quick answer!</p>

---

## Post #4 by @muratmaga (2024-04-19 22:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would not be that hard to implement a similar mechanism for volume rendering (request resolution and image region from Zarr depending on what part of the volume is visible; all can be implemented in Python, without any Slicer core change).</p>
</blockquote>
</aside>
<p>What about the segmentation of such datasets?</p>

---

## Post #5 by @lassoan (2024-04-19 23:56 UTC)

<p>Most common segmentation representations are labelmap and closed surface. Both can be rendered very quickly if stored in a multiresolution format. The challenging part is the processing: how to quickly modify a multiresolution labelmap image and create closed surface mesh from it.</p>
<p>In 2D it is trivial, as you can simply store segmentations in polygons. But I am not sure if there is a simple general solution in 3D. Maybe displaying the segmentation in 3D using volume rendering would simplify things, but then we would need to be able to solve the problem of computing smooth gradients for labelmaps.</p>

---

## Post #6 by @muratmaga (2024-04-20 02:24 UTC)

<p>I meant more in context of actual segmentation and memory consumption. Would you create the closed surface representation at the finest resolution the multiscale provides, or at the level data shown on the screen? If the user zooms in to the next level, does the labelmap automatically resample? If so, what will happen to the memory usage? Does the labelmap will be written to the disk and streamed (as opposed to stored in the memory as a single numpy array)</p>

---

## Post #7 by @lassoan (2024-04-21 12:15 UTC)

<p>Ultimately, all modifications would be saved at the ground truth level. For performance and design simplification reasons it may be easier to update segmentation at the current level and write it to the ground truth level in background processing thread.</p>
<p>Only the displayed regions would be in memory, only at the relevant resolution. This would take care of memory usage.</p>
<p>Processing would need to be done in the background and may require streaming. Both ITK and VTK filters support streaming, but it is only implemented for some of the filters. Some algorithms would be difficult to adapt to streaming (e.g., region growing).</p>

---

## Post #8 by @cpinter (2024-04-22 13:43 UTC)

<p>I assume lots of this is not yet in place. It is possible that once the first phase of the project in terms of which I encountered this challenge is finished, there will be a need for a more integrated solution using multi-resolution images. If this occurs, I’ll let you know <a class="mention" href="/u/muratmaga">@muratmaga</a>, maybe with joint efforts it could be done faster. My guess is that we’ll know this in a few months.</p>

---
