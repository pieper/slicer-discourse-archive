---
topic_id: 35520
title: "Importing A Template With Empty Segmentation"
date: 2024-04-16
url: https://discourse.slicer.org/t/35520
---

# Importing a template with empty segmentation

**Topic ID**: 35520
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/importing-a-template-with-empty-segmentation/35520

---

## Post #1 by @coco (2024-04-16 08:54 UTC)

<p>Dear all,</p>
<p>I have a question that has come up before and my apologies if there the answers I am looking for elsewhere.<br>
My query is related to a previous post:<br>
<a href="https://discourse.slicer.org/t/segment-editor-color-name-template/10982/1">Segment Editor color/name template - Support - 3D Slicer Community</a></p>
<p>I can certainly spend some time decoding the script in the proposed solution to adapt my own template but since I already have .seg.nrrd files, is it not possible for me to simply import an empty .seg.nrrd file, apply the new volume’s geometry and start segmenting again ?</p>
<p>Again thanks to the developpers and community for such a great software. Thumbs up !</p>

---

## Post #2 by @lassoan (2024-04-16 15:42 UTC)

<p>The feature is already implemted in recent Slicer Preview Releases: you can create a segmentation, set up all the segments (use terminology selector to set name, color, standard codes that define segment content), and save the .seg.nrrd file. You can use this empty .seg.nrrd file as template for future segmentaitons.</p>

---

## Post #3 by @coco (2024-04-16 17:01 UTC)

<p>Yes, I eventually figured that one out.<br>
My .seg.nrrd files all have slightly different geometries so all I have to do is to keep an empty template and apply the new geometry when opening a new volume.<br>
Thanks again</p>

---
