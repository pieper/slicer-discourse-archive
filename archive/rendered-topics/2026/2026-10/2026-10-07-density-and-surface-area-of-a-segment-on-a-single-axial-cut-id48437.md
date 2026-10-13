---
topic_id: 48437
title: "Density and surface area of a segment on a single axial cut"
date: 2026-10-07
url: https://discourse.slicer.org/t/48437
last_bumped: 2026-10-13T02:15:38.364Z
---

# Density and surface area of a segment on a single axial cut

**Topic ID**: 48437
**Date**: 2026-10-07
**URL**: https://discourse.slicer.org/t/density-and-surface-area-of-a-segment-on-a-single-axial-cut/48437

---

## Post #1 by @Mahdi_H (2026-10-07 19:56 UTC)

<p>Hello everyone!</p>
<p>I am new to the 3d slicer software and its powerful features.</p>
<p>I am currently planning a research project and have been successful in running totalsegmentator to segment tissues I am interested in. I have now to get the density and surface area of the segmented tissues I generate on a single axial cut. Can anyone please provide with simple, beginner-level, instructions on how to do so?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @Esteban_Barreiro (2026-10-08 15:59 UTC)

<p>Hi! You can run “Segment Statistics” for your quantification based on label maps, the corresponding Scalar Volume and Closed Surface.<br>
documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" rel="noopener nofollow ugc">Segment statistics — 3D Slicer documentation</a><br>
Hope this help.</p>

---

## Post #3 by @Mahdi_H (2026-10-11 10:33 UTC)

<p>Hello!</p>
<p>Thank you so much for your reply!<br>
It really means a lot.</p>
<p>I checked the link and the segment statistics extension. However, it gives values for the whole segment, while what I need are surface area and density for the segment on a <strong>single axial slice</strong>.</p>
<p>To note, the link mentions, <code>Segment Cross-Section Area</code> module in Sandbox extension for the cross sectional area of a segment on axial images, which is fair because I tried it and it works. However, is there any similar thing for the density?</p>
<p>Thanks in advance.</p>

---

## Post #4 by @bjmufffff (2026-10-12 09:18 UTC)

<p>Hello, you can try SementGeometry mudule(which also has cross-sectional area included) to compute Mean brightness of each slice of a segmentation.</p>

---

## Post #5 by @Mahdi_H (2026-10-12 20:03 UTC)

<p>Thank you again for your reply!</p>
<p>The issue with SegmentGeometry is that it generates the information for each segment alone. Is there a way to generate the density for multiple segments at once (like in the Segment Cross-Section area module)?</p>

---

## Post #6 by @bjmufffff (2026-10-13 02:15 UTC)

<p>Hi, don’t know if there is such a module that meets your needs. The method I can think of is to merge all the segments into one (using the Logical Operators tool in the Segment Editor) , or, if possible, do some Python programming to perform the measurement.</p>

---
