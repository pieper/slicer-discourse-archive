---
topic_id: 29234
title: "Export Individual Segements From Segmentation As Obj Files"
date: 2023-05-01
url: https://discourse.slicer.org/t/29234
---

# Export individual segements from segmentation as obj files 

**Topic ID**: 29234
**Date**: 2023-05-01
**URL**: https://discourse.slicer.org/t/export-individual-segements-from-segmentation-as-obj-files/29234

---

## Post #1 by @Kalgodon (2023-05-01 21:42 UTC)

<p>I am trying to export all segments as their own obj so that I don’t end up with just a surface like stl files.</p>
<p>I have been successful in the ui by hiding all the segments except 1 at a time, and then exporting all visible segments to an obj file and repeating this process.</p>
<p>How would I do this in a python script?</p>

---

## Post #2 by @lassoan (2023-05-01 21:49 UTC)

<aside class="quote no-group" data-username="Kalgodon" data-post="1" data-topic="29234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/96bed5/48.png" class="avatar"> Kalgodon:</div>
<blockquote>
<p>I am trying to export all segments as their own obj so that I don’t end up with just a surface like stl files.</p>
</blockquote>
</aside>
<p>When you export to OBJ, a single file is sufficient, because each segment is exported with a different material, so you can select in your external viewer/editor software what to show and how (you are not limited to show the external surface).</p>
<p>That said, if you want, you can export a segmentation to multiple OBJ files (one OBJ file for each segment). For this you can use the exporter in <a href="https://github.com/PerkLab/SlicerOpenAnatomy">SlicerOpenAnatomy extension</a>. The exporter can also simplify the models, which is useful if you want to load the models into software that requires meshes with low polygon count (e.g., Unity, HoloLens).</p>

---
