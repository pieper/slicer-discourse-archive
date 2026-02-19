---
topic_id: 1898
title: "2 Mri To Compare And Highlight The Different Region"
date: 2018-01-22
url: https://discourse.slicer.org/t/1898
---

# 2 MRI to compare and highlight the different region

**Topic ID**: 1898
**Date**: 2018-01-22
**URL**: https://discourse.slicer.org/t/2-mri-to-compare-and-highlight-the-different-region/1898

---

## Post #1 by @MRI23D (2018-01-22 14:15 UTC)

<p>I have 2 MRI docomdat to compare.<br>
My Goal is identifying in the 3D window which part of brain is damaged.</p>
<ol>
<li>Is there any convenient way to see these two?</li>
<li>is there any way to overlap and detect the different region to high light as a damaged  area?</li>
</ol>
<p>One mri is before hypoxic and the other is after.<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2018-01-23 01:15 UTC)

<p>If you can segment these regions using Segment Editor module, then you can get basic statistics from Segment Statistics module and compare segments using Segment Comparison module (in SlicerRT extension).</p>

---

## Post #3 by @MRI23D (2018-01-31 04:29 UTC)

<p>What are these of “these regions?”</p>
<p>Also unfortunately the alignment of one MRI is slanted the patient head was a bit slanted.</p>
<p>To compare I think the slanted to be corrected.<br>
Huh… how… using 3d slicer as a newbie …<br>
I am lost.</p>

---

## Post #4 by @lassoan (2018-01-31 14:53 UTC)

<p>You can align the two images using “General registration (BRAINS)” or “General registration (Elastix)” modules (to see the latter, you need to install SlicerElastix extension).</p>
<p>If you just need visual comparison (fade between the two volumes) then you can choose one volume as foreground and the other as background and fade between them. You can then also go to <code>Compare volumes</code> module and activate <code>Reveal cursor</code> to explore the changes.</p>
<p>For quantitative comparison, you need to segment lesions using Segment Editor module and then get basic statistics from Segment Statistics module and compare segments using Segment Comparison module (in SlicerRT extension).</p>

---
