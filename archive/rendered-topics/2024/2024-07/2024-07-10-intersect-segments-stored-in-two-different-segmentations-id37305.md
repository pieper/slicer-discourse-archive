# Intersect segments stored in two different segmentations

**Topic ID**: 37305
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/intersect-segments-stored-in-two-different-segmentations/37305

---

## Post #1 by @Noa (2024-07-10 14:38 UTC)

<p>Hello, I try to intersect two segmentations : tumor1 and tumor2, segmented from volume1 and volume2. I created a transform, 2to1, to overlay segment 2 on segment 1. How do I intersect these two segmentations?<br>
Thank you in advance.</p>

---

## Post #2 by @muratmaga (2024-07-10 16:49 UTC)

<p>SegmentEditot -&gt;Logical operators</p>

---

## Post #3 by @Noa (2024-07-10 18:33 UTC)

<p>Hello,<br>
I tried to use logical operators but I can’t do it with two different segmentations, and I need to keep them separated in order to save the transform. Moreover, I can’t seem to find the « multi select » in the segmentation module. I also tried CombineModels from the Sandbox extension but the python console says : error: bad shaped cells.<br>
Does someone knows how to solve this?<br>
Thank you for your replies.</p>

---

## Post #4 by @muratmaga (2024-07-10 18:34 UTC)

<p>You can copy segment(s) from a segmentation  to another segmentation. Look at the <code>Segmentation</code> module.</p>

---

## Post #5 by @lassoan (2024-07-10 19:10 UTC)

<aside class="quote no-group" data-username="Noa" data-post="3" data-topic="37305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/919ad9/48.png" class="avatar"> Noa:</div>
<blockquote>
<p>I need to keep them separated in order to save the transform</p>
</blockquote>
</aside>
<p>You can do the followings to keep the original segmentation but still have a transformed copy of the other segment:</p>
<ul>
<li>clone the segmentation (right-click on the segmentation in Data module and click <code>Clone</code>)</li>
<li>apply the same transform to the cloned segmentation as was applied to the original (right-click on the transformation column of the cloned segmentation and click on the appropriate transform)</li>
<li>harden the transformation (right-click on the transformation column of the cloned segmentation and click <code>Harden transform</code>)</li>
<li>drag the segment from the cloned segmentation to the other segmentation</li>
</ul>
<p>If you need to do this many times then you can automate it with a couple lines of Python script (most likely ChatGPT or Microsoft Copilot can generate the script).</p>

---

## Post #6 by @Noa (2024-07-10 19:31 UTC)

<p>thank you very much !</p>

---
