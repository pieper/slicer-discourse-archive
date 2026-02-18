# Editor module/segment editer

**Topic ID**: 4267
**Date**: 2018-10-03
**URL**: https://discourse.slicer.org/t/editor-module-segment-editer/4267

---

## Post #1 by @Melanie (2018-10-03 09:40 UTC)

<p>Hi ,<br>
How can I edit one frame of a sequence (multivolume ) and depict the changes in all the frames of the sequence. Is  it possible with slicer</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-10-03 13:59 UTC)

<p>You need to re-apply editing operation to each sequence item by a script. See for example how it is done in <a href="https://github.com/SlicerRt/Sequences/blob/b1b2eeb7f8b33c728d5aeb983a605027a588f2bc/CropVolumeSequence/CropVolumeSequence.py#L163-L243">Crop Volume Sequence</a> module.</p>

---

## Post #3 by @Melanie (2018-10-03 14:01 UTC)

<p>Thank you very much Prof Lasso</p>

---
