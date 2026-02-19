---
topic_id: 31483
title: "Click On Segment In 3D View"
date: 2023-08-31
url: https://discourse.slicer.org/t/31483
---

# Click on Segment in 3D View

**Topic ID**: 31483
**Date**: 2023-08-31
**URL**: https://discourse.slicer.org/t/click-on-segment-in-3d-view/31483

---

## Post #1 by @JASON (2023-08-31 20:29 UTC)

<p>Hello, I am looking to make a script that will allow me to click within the 3D view on to a segmentation node and get the specific segment under the mouse cursor.  Before I start trying to do this the hard way, I wanted to ask if there are any known modules / extensions that have this capability.  Drawing segmentations in the 3D view will raycast onto the segmentation surface from the 3D camera projection.  Is there existing API to raycast and return the segment within the segmentation node?</p>
<p>My goal here is we have many misclassified segments that need corrections for boundaries with adjacent segments.  These are easily corrected in a single stroke by using the paint tool with the ‘editable area’ set to INSIDE the misclassified segment.  It’s easy to identify misclassified boundaries in the 3D view, but more time consuming to find the same structure in the orthographic view, hover the mouse in the orthographic view to get the name in the DataProbe, then find &amp; select the name within the segmentation editor.  With 100+ segments, I’m looking to speed this up by making a script to select the segment in the editor and set the target ‘editable area’ by ray-casting in the 3D view.</p>

---

## Post #2 by @pieper (2023-08-31 20:49 UTC)

<p>Hi Jason -  thanks for the explanation, I agree with you that’s an important scenario.  My experience is that you can do this with the feature where holding shift while moving the mouse in the 3D view updates the slice views to that location (sometimes it helps to select the “Jump Slices - centered” option in the crosshair toolbar menu).</p>
<p>Then the easy way to set the paint color us by enabling “Color smudge” mode, where the segment is set based segment you are on when when the mouse button is depressed (something like finger painting).  This way you can easily go back and forth to adjust the edge between adjacent segments.  Using shift also works in the Slice views to scroll the other slices so you can inspect the interface.</p>
<p>Try those out and see what you think.  It is on my wishlist to be able to right-click on a segment in 3D and invoke some Segment Editor features (e.g. like save-island or set visibility) but we don’t have that yet.</p>

---
