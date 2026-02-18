# Setting slice visibility per segment

**Topic ID**: 11974
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/setting-slice-visibility-per-segment/11974

---

## Post #1 by @muratmaga (2020-06-10 04:13 UTC)

<p>I have two segments in a segmentation. A segment_1 is the thresholded volume, and segment_2 is same structure after WrapSolidify. I want to show segment_1 only in the red slice and segment_2 in the yellow slice. While Segmentations module advanced section of Display tab seemingly to let me adjust it per segment, selection still applies to both of segments. Is this not possible (i.e., visibilities are set per segmentation, not per segment), or is this a bug?</p>

---

## Post #2 by @pieper (2020-06-10 17:08 UTC)

<p>I’m pretty sure all the segmentation display properties apply to all segments (other than per-segment visibility)</p>
<p>You can use the Copy/Move Segments panel to put your segment_2 in a new segmentation and then you can control the per-view visibility.</p>

---

## Post #3 by @muratmaga (2020-06-10 17:09 UTC)

<p>It is what I thought, but it actually display all the segments within the segmentation, and you can go back and forth with them thinking you can adjust them individually. That’s what confused me.</p>

---

## Post #4 by @pieper (2020-06-10 18:50 UTC)

<p>I think only the part in the box below the line “Selected segment” is the per-segment part.  The controls above that in Advanced are for the full Segmentation.</p>

---

## Post #5 by @lassoan (2020-06-10 19:07 UTC)

<p>Segmentation behaves the same way as all other displayable nodes: if you want to show different content in different views then you need to create additional display nodes, and in each display node <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a62cff2549fe8c0c4fbff5b363031e242">indicate which view(s) it should be used in</a>.</p>
<p>Slicer core GUI only shows the first display node, but you can easily add and configure additional display nodes using Python scripting (or add a scripted module for it, if this is something that you want to do regularly).</p>

---
