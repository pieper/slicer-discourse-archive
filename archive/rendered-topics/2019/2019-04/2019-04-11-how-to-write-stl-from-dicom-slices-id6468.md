---
topic_id: 6468
title: "How To Write Stl From Dicom Slices"
date: 2019-04-11
url: https://discourse.slicer.org/t/6468
---

# How to write STL from dicom slices

**Topic ID**: 6468
**Date**: 2019-04-11
**URL**: https://discourse.slicer.org/t/how-to-write-stl-from-dicom-slices/6468

---

## Post #1 by @selvakarna (2019-04-11 13:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> how to write STL from dicom slides[ its like 1000 slides], ?<br>
How to write STL from X Y Z coordinates , this coordinates are extracted from 1000 dicom slides,?</p>

---

## Post #2 by @lassoan (2019-04-11 14:01 UTC)

<p>To get a surface mesh from images, you need to segment them. Segment Editor module in Slicer has many tools for this. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>.</p>
<aside class="quote no-group" data-username="selvakarna" data-post="1" data-topic="6468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/71c47a/48.png" class="avatar"> selvakarna:</div>
<blockquote>
<p>How to write STL from X Y Z coordinates</p>
</blockquote>
</aside>
<p>STL file already contains XYZ coordinates. If you need coordinates in a different file format then you can load the STL, get point positions as a numpy array, and write to file using a short Python script.</p>

---
