# Exporting multiple seg.nrrd files to obj all at once

**Topic ID**: 7747
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/exporting-multiple-seg-nrrd-files-to-obj-all-at-once/7747

---

## Post #1 by @NoobForSlicer (2019-07-25 05:53 UTC)

<p>I have finally segmented some files I was planing now I want to &gt;&gt; export them all to obj.</p>
<p>They are all in different seg.nrrd files. Is there some way to export them all at once instead of clicking on each seg.nrrd file and then exporting them separately.</p>
<p>It tried in data module to move the segmentations from one nrrd to another one and indeed it worked but it then puts everything under segmentation 1. I guess it would fuse the 3d models then.</p>
<p>Sure i can export them all manually one by one it would take me a couple of hours but I just wonder and would like to learn, so if anyone knows ?</p>

---

## Post #2 by @NoobForSlicer (2019-07-25 06:02 UTC)

<p>ups actually no, it calls it segment_1 all of them but still considers them as separate segmentations. Sorry, my bad.</p>
<p>Hmm but I had to go and move them one by one all to that one segmentation nrrd file. Is there some way where I can just fuse all nrrd files right away without manually taking segmentation out of it and putting them all in one.</p>

---

## Post #3 by @lassoan (2019-07-25 19:52 UTC)

<p>I’m not completely sure what your problem is, but you have a couple of options. If it was a one-time error that you created a separate segmentation for each segment then probably the fastest is to fix it using the GUI (drag-and-drop in Data module). If you have hundreds of segments to merge and so a manual fix-up would take more than a few ten minutes then you can write a few-line Python script to automate it. There are many examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" rel="nofollow noopener">script repository</a>.</p>
<p>If you use the “Export to file” feature then all segments are exported into a single .obj file but each with a different material, so you can process them separately, if needed.</p>
<p>If you need each segment in a separate file, choose STL format in Export to file and disable and uncheck “Merge into single file”. Or, export the segmentation to models and save them to file in two steps (go to Data module, right-click on segmentation, Export visible segments to models; then menu: File / Save).</p>

---
