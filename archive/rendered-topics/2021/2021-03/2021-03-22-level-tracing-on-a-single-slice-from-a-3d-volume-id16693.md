---
topic_id: 16693
title: "Level Tracing On A Single Slice From A 3D Volume"
date: 2021-03-22
url: https://discourse.slicer.org/t/16693
---

# Level tracing on a single slice from a 3D volume

**Topic ID**: 16693
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/level-tracing-on-a-single-slice-from-a-3d-volume/16693

---

## Post #1 by @Marc0 (2021-03-22 15:02 UTC)

<p>I would like to load a single slice out of a DICOM volume on 3DSlicer and to segment it via the Level Tracing tool. The level tracing works on the full volume but it does not work if I load a single slice out of this volume. Is there a way to perform this task?</p>
<p>Thank you very much</p>

---

## Post #2 by @lassoan (2021-03-24 17:34 UTC)

<p>Level tracing effect cannot operate at the slice boundary and there is a somewhat too simplistic <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L166-L170">check</a> that ensures that the current position is not at the boundary. Since it checks all 3 axes (and not just within the slice axes), this check also prevents using it on the first and last slice of the volume. You can simply comment out the check, but it would be even better if you updated the check so that it is done only in the current image plane (see how the current image plane is detected <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L181-L186">here</a>) and send a pull request with the fix. Thank you!</p>

---

## Post #3 by @alireza (2021-07-06 14:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> if the level tracing in 3D slicer is 2d, does it make sense to comment out the simplistic check in the upstream? I don’t understand why a 2D algorithm cannot be run on first and last slice.</p>

---

## Post #4 by @pieper (2021-07-06 19:38 UTC)

<p>Yes, it’s just some faulty logic that needs to be sorted out.  I don’t think it’s a huge task but someone would need to dig in a bit on both the C++ and python code.</p>

---

## Post #5 by @alireza (2021-07-07 16:14 UTC)

<p>I created a PR here <a href="https://github.com/Slicer/Slicer/pull/5728" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix the check for 3D while tool logic is 2D in levelTracing tool by sedghi · Pull Request #5728 · Slicer/Slicer · GitHub</a></p>

---
