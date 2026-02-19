---
topic_id: 27467
title: "Editing Segmentations After Loading"
date: 2023-01-25
url: https://discourse.slicer.org/t/27467
---

# Editing segmentations after loading

**Topic ID**: 27467
**Date**: 2023-01-25
**URL**: https://discourse.slicer.org/t/editing-segmentations-after-loading/27467

---

## Post #1 by @Alex_Benjamin (2023-01-25 19:31 UTC)

<p>Hello, I have been able to segment a few images (both in Slicer3D and externally using an algorithm).</p>
<p>Is there a way to load in these segmentation masks and edit or fine tune the segmentation masks without deleting or erasing (think spline based shape editing).</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-01-25 19:33 UTC)

<p>If you mean that you just want to make small adjustments to segments, that should be no problem at all. This is how Segment Editor works. You can make adjustments to segments anytime, you don’t need to delete and recreate the segment to modify it.</p>
<p>If you mean that you want to edit an alternative representation of a segment, such as a spline, that’s doable, too. You can have a look at how spline-based curve segmentation works in the <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py">Draw Tube effect</a>. The main idea is that we save the control point positions in the segment as custom tags, therefore the user can switch to edit mode anytime, make adjustments, and apply the changes.</p>

---

## Post #3 by @Alex_Benjamin (2023-01-26 15:22 UTC)

<p>Thanks Andras! Much appreciated. I was able to make fine adjustments to the segmentations by redrawing or erasing tiny parts of the original segmentation.</p>
<p>I am wondering if the entire segmentation (label map) is editable through control points? i.e. once a segmentation is done, can it later be edited by simply moving around control points on the contour?</p>

---

## Post #4 by @lassoan (2023-01-26 23:10 UTC)

<p>Segmentations in Slicer can have several representations (binary labelmap, planar contours, ribbons, closed surface, fractional labaelmap), but by far the most commonly used is binary labelmap. In this representation, each segment is defined by a 3D array of binary values. In general, you cannot efficiently and accurately edit this representation in a slice view as smooth contours, as you may have thousands of small blobs with potentially very intricate details. For special cases, such as editing one large simple shape,  I can imagine that we could use a smooth curve. However, you would not save much time if you edited a single slice at a time. Alternative methods, such as circular or spherical detrctor/attractor tool might work much better, or you may find that grow-cut based tools (such as the existing Grow from seeds effect) or some AI based interactive tools provide much more accurate results much faster.</p>
<p>What would you like to segment on what kind of images?<br>
What are the main challenges with your current segmentation workflow?</p>

---

## Post #5 by @Alex_Benjamin (2023-01-27 21:44 UTC)

<p>Thanks Andras!</p>
<p>The workflow is retinal layer segmentation. I have an algorithm that can produce layer maps and we want to review and edit these outputs.</p>
<p>As binary label maps, the segmentations are 1/0s but there are no editable points or surfaces when imported into Slicer. As a result, the only option is to erase sections and re-draw. Would be nice to dynamically edit without having to do so.</p>

---

## Post #6 by @lassoan (2023-01-28 17:28 UTC)

<p>You can use the “color smudge“ mode of the Paint effect. It allows you to expand the current label (where you click on) to neighbor region (by dragging while holding down the mouse button). You can change the brush size using Ctrl-mousewheel, or by zooming the image in/out.</p>
<p>If these general-purpose tools are not sufficient convenient then you may write custom Python scripts to implement features that are specialized to work optimally on your data. For example, if you are sure that you can adjust segments much faster by editing curves then you can implement curve fitting and editing. Or maybe all you need is automatic adjustment of brush size (e.g., the closer you click when you start click-and-drag the smaller the brush size is). You may also find that you get much higher quality results much faster if you make corrections in 3D.</p>

---

## Post #7 by @Alex_Benjamin (2023-01-30 14:33 UTC)

<p>Thanks Andras. Much appreciated.</p>

---
