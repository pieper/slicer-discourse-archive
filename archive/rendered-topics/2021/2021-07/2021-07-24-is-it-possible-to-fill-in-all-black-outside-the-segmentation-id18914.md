---
topic_id: 18914
title: "Is It Possible To Fill In All Black Outside The Segmentation"
date: 2021-07-24
url: https://discourse.slicer.org/t/18914
---

# Is it possible to fill in all black outside the segmentation?

**Topic ID**: 18914
**Date**: 2021-07-24
**URL**: https://discourse.slicer.org/t/is-it-possible-to-fill-in-all-black-outside-the-segmentation/18914

---

## Post #1 by @angelsosamd (2021-07-24 22:35 UTC)

<p>Hi!</p>
<p>Is it possible to fill in all black outside the segmentation? (background)</p>
<p>Regards,</p>
<p>Angel S.</p>

---

## Post #2 by @Juicy (2021-07-24 23:19 UTC)

<p>Yes, you need to make a second segment and make sure the newly created segment is selected. You can then use the thresholding tool, you need to select a value which highlights all the black region and change “Editable area” under “Masking” to “Outside all Segments” to ensure you do not overwrite you previous segment. You could also use the “Invert” tool under “Logical Operators” to invert you segmentation, i.e. highlight all the background while the area where the segment was is un-highlighted.</p>

---

## Post #3 by @lassoan (2021-07-25 12:26 UTC)

<p>If you want to change the voxels of the original volume then you can use the “Mask Volume” effect in Segment Editor. It is part of Slicer core in recent Slicer Preview Releases, it is not n SegmentEditorExtraEffects extension for earlier Slicer versions.</p>

---
