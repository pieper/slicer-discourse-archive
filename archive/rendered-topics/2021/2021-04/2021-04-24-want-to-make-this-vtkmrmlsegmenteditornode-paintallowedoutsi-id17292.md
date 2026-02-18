# Want to make this vtkMRMLSegmentEditorNode::PaintAllowedOutsideAllLockedSegments

**Topic ID**: 17292
**Date**: 2021-04-24
**URL**: https://discourse.slicer.org/t/want-to-make-this-vtkmrmlsegmenteditornode-paintallowedoutsidealllockedsegments/17292

---

## Post #1 by @Shazam_L (2021-04-24 03:21 UTC)

<p>Hello,</p>
<p>I want to pass individual segments that cannot be painted over.<br>
Where can I access the segmentation mask so I can specify which segments can be painted over?</p>
<p>Thanks,</p>
<p>Harsh</p>

---

## Post #2 by @lassoan (2021-04-25 13:35 UTC)

<p>There are many options for this. You can use masking settings or temporarily move protected segments to another segmentation node. Moving is immediate and lossless, so you can do it easily as many times as needed.</p>

---
