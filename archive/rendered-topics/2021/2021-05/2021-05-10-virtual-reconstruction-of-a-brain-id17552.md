---
topic_id: 17552
title: "Virtual Reconstruction Of A Brain"
date: 2021-05-10
url: https://discourse.slicer.org/t/17552
---

# Virtual reconstruction of a brain

**Topic ID**: 17552
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/virtual-reconstruction-of-a-brain/17552

---

## Post #1 by @Marta_Fernandez (2021-05-10 21:50 UTC)

<p>Hi.<br>
I would like to create a brain from a skull. The problem is that the object is an STL and I cant create a volume from it.<br>
Someone know how can I create a virtual brain from it?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b47fb9164090ecc2d7e0b9b8c3f0985bd38ef70.png" alt="image" data-base62-sha1="8sqomvC9DyzdJUUhjf7eJZSWYSY" width="302" height="337"></p>
<p>Thanks in advice for the answer</p>

---

## Post #2 by @lassoan (2021-05-11 04:05 UTC)

<p>You can extract a closed brain volume despite the missing cranium pieces, by following these steps:</p>
<ul>
<li>Install WrapSolidify extension from Extensions Manager.</li>
<li>Load the STL file as segmentation (drag-and-drop the STL file to the Slicer application window and select “Segmentation” in “Description” column)</li>
<li>Go to Segment Editor module and generate a master volume (click specify geometry - button next to master volume selector, select the segmentation node as “Source geometry”, specify spacing -probably something between 0.2-1.0mm will work, and click OK).</li>
<li>Switch to “Wrap Solidify” effect, choose Region → Largest cavity, Output → New segment, and click Apply. =&gt; this will extract the largest cavity enclosed in the convex hull of the model, fully automatically</li>
</ul>

---
