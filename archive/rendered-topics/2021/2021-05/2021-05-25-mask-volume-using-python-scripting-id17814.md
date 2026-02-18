# Mask volume using Python scripting

**Topic ID**: 17814
**Date**: 2021-05-25
**URL**: https://discourse.slicer.org/t/mask-volume-using-python-scripting/17814

---

## Post #1 by @omnikron (2021-05-25 16:58 UTC)

<p>I also would like to perform 3D cropping on volume rendering. Are there any current examples using Python scripted modules that I can study to accomplish this? Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-05-26 17:01 UTC)

<p>You can find examples of using Segment Editor effects from Python in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a> and here is an <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSplitVolume/SegmentEditorSplitVolumeLib/SegmentEditorEffect.py#L129-L192">example of using Mask volume effect from a Python script</a>.</p>

---
