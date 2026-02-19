---
topic_id: 12781
title: "Slicer Crashes When Loading Segmentation Editor"
date: 2020-07-29
url: https://discourse.slicer.org/t/12781
---

# Slicer crashes when loading segmentation editor

**Topic ID**: 12781
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-loading-segmentation-editor/12781

---

## Post #1 by @Bo_Lan (2020-07-29 22:52 UTC)

<p>Hi all! So I am segmenting using 3D slicer and finished almost all of my project and saved it last night, but then today when I open up my segmentations saved from yesterday and attempt to open up segmentation editor, the program simply crashes and exits me out of slicer. I also cannot move on any of the three views and can only move in the 3D picture. I thought it was a disk space issue, but then I checked and still have more than 50 GB of disk left and restarting the computer produces the same problem. However, opening up an earlier version of my segmentations from a month ago opens segmentation editor nicely but I need the latest saved version of my segmentations. I am using the latest version of slicer as well so I do not know what is wrong. Thank You!</p>

---

## Post #2 by @muratmaga (2020-07-29 23:13 UTC)

<p>Can you try to load the individual files (the seg.nrrd and volume) individually as oppose to through a scene, and see if you can recover.<br>
It will also be useful to reopen the slicer after the crash, go to help-&gt;Report a bug, and copy and paste the contents of the log one down the list (the top one would be the session you are in, so you need the one before that).</p>

---
