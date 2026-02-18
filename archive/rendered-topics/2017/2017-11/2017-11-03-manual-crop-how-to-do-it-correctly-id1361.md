# Manual Crop how to do it correctly

**Topic ID**: 1361
**Date**: 2017-11-03
**URL**: https://discourse.slicer.org/t/manual-crop-how-to-do-it-correctly/1361

---

## Post #1 by @AndFor (2017-11-03 15:36 UTC)

<p>Operating system: win<br>
Slicer version: 4.9</p>
<p>Hello<br>
I’ve follow all instruction found here <a href="https://discourse.slicer.org/t/3d-cropping-volume-rendering/394/9">3D Cropping Volume Rendering</a><br>
If i’ve correctly understood, there is not a live crop direct on the main volume.</p>
<p>Then, i’ve make a segmentation - &gt; exported to labelmap</p>
<p>then Open Mask scalar volume<br>
Input MrBrainTumor (original volume)<br>
Mask Volume: Segmentation label 1</p>
<p>Apply, the is ok</p>
<p>Now I go to volume rendering, I can display the main volume or the masked volume ,  but I see only a solid colored form (the mask selection) but not the tissue volume whit the volume rendering setting</p>
<p>Help please<br>
Thanks</p>

---

## Post #2 by @lassoan (2017-11-03 15:47 UTC)

<p>Note that in recent version of Slicer, the workflow is much simpler than described in the old post, as <code>Mask Volume</code> effect allows masking directly from a segment, without leaving the Segment Editor module. <code>Mask Volume</code> will show up in the Segment Editor module after installing <code>SegmentEditorExtraEffects</code> extension.</p>
<p>See a short demo video here:</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @AndFor (2017-11-03 16:15 UTC)

<p>Fantastic thanks<br>
It work good</p>
<p>And… does is possible to use simoultaneusly 2 separated mask for the same volume?</p>

---

## Post #4 by @lassoan (2017-11-03 16:33 UTC)

<p>I don’t really understand what you mean by using separated masks. You can use all the tools in Segment Editor to draw shapes - they don’t have to be connected. You can also combine or separate a segments using <code>Logical operators</code> effect; or mask sequentially by using the same volume as <code>Input volume</code> and <code>Output volume</code> in <code>Mask volume</code> effect.</p>

---

## Post #5 by @AndFor (2017-11-03 18:07 UTC)

<p>mmmm I cannot find how to make it<br>
I’ve tried but dont work</p>
<p>I want try to use threshold AND Scissor, to isolate a little anatomic part and remove all little pixel outside…</p>

---

## Post #6 by @lassoan (2017-11-03 19:00 UTC)

<p>Use Threshold effect first, then Scissors effect (erase outside), finally Islands effect (remove small islands).</p>

---

## Post #7 by @AndFor (2017-11-03 21:42 UTC)

<p>perfect, tested and work well many thanks</p>

---

## Post #8 by @AndFor (2017-11-03 22:08 UTC)

<p>Other little question, how to center the rotation center of 3D view on a specific point of 3D Volume: if I zoom very much, during rotation the volume go out of the window space</p>

---

## Post #9 by @lassoan (2017-11-03 22:27 UTC)

<p>Click on the small box button (reset field of view) in the title bar of the 3D view to reset the center of rotation for the current content. I think Shift+LeftMouseDrag also shifts the center of rotation.</p>

---

## Post #10 by @lassoan (2019-05-24 13:37 UTC)

<p>A post was split to a new topic: <a href="/t/edit-existing-segmentation/6917">Edit existing segmentation</a></p>

---
