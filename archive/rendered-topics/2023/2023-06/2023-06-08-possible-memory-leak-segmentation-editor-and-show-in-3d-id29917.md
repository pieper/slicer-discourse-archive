---
topic_id: 29917
title: "Possible Memory Leak Segmentation Editor And Show In 3D"
date: 2023-06-08
url: https://discourse.slicer.org/t/29917
---

# Possible Memory Leak - Segmentation Editor and Show in 3D

**Topic ID**: 29917
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/possible-memory-leak-segmentation-editor-and-show-in-3d/29917

---

## Post #1 by @BobAho (2023-06-08 11:03 UTC)

<p>Working on CT microscan volumes segmenting the specimen from the noise.  Start Slicer, it occupies about 500 MB memory.  Load volume and it’s about 2.2GB.  So far so good. Render the volume and Slicer jumps to 4.4 GB, still OK.  Activate Segmentation Editor, jumps to 6.25 GB, still no problem.  Start segmenting specimen memory use slowly crawls up to 12 GB (got 32 GB RAM so good for now).  Using a up and down and all around procedure I segment the specimen - up and down on the red slice, all around with the green and yellow slices.  One segment every 25 or so slices, use the fill between to get rough shape.  Again memory, goes up and down but stabilizes at about 15GB.  All good until I select <strong>Show in 3D</strong>.  At this point, the memory use goes up on each and every edit afterward.  Use any tool to clean up a slice, memory use goes up and does not go down.  Eventually the memory pegs, and swap disk ensues and the latency makes the product unusable.  Close the scene and the memory drops a bit, but does not fully release.  The latency will decrease if <strong>Show In 3D</strong> is deselected.</p>
<p>Slicer: 5.2.2 r31382 / fb46bd1</p>
<p>Computer: Apple M1 Pro, Ventura 13.4, 32GB RAM</p>

---

## Post #2 by @hherhold (2023-06-08 11:25 UTC)

<p>This is probably because of saving the undo state in segmentEditor, which can use a fair amount of memory with large segmentations. The default is 10 levels of undo, but you can reduce it in the python console:</p>
<p><code>slicer.modules.SegmentEditorWidget.editor.setMaximumNumberOfUndoStates(0)</code></p>
<p>Also, because volume rendering uses video memory (which is shared on that type of Mac and not dedicated to the GPU, so you’re using system memory), you can turn that off if not needed.</p>
<p>If segmenting is slow and you need to show it in 3D while segmenting, turn off Surface Smoothing (click the arrow in the Show 3D button). This will speed things up quite a bit.</p>

---

## Post #3 by @hherhold (2023-06-08 11:28 UTC)

<p>Also, the general rule of thumb is your memory should be 10x the size of volume you’re working on. For a 2.2GB volume, that’s 22GB, but the shared memory setup of the new Macs is somewhat new territory, I think, especially if you’re using volume rendering and Show 3D simultaneously.</p>

---

## Post #4 by @BobAho (2023-06-08 17:09 UTC)

<p>Thank you very much.  Ahh, I suspected the undo was responsible but was not sure where to look to modify it.<br>
I can work without 3D visualization, indeed it’s unneeded until final work needs visualization. It was when I left that feature on that I stumbled across it.<br>
I forgot how fast the files occupy memory.  My other machine has 64 GB and and better graphics card, so it’s likely I would not have found it if not on the road.  Fortunately, when I teach this I can use 300MB specimens.</p>

---
