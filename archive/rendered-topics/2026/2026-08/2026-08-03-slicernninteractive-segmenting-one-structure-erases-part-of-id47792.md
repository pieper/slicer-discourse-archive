---
topic_id: 47792
title: "SlicerNNInteractive: segmenting one structure erases part of an adjacent, already-completed segment"
date: 2026-08-03
url: https://discourse.slicer.org/t/47792
last_bumped: 2026-08-03T16:36:34.126Z
---

# SlicerNNInteractive: segmenting one structure erases part of an adjacent, already-completed segment

**Topic ID**: 47792
**Date**: 2026-08-03
**URL**: https://discourse.slicer.org/t/slicernninteractive-segmenting-one-structure-erases-part-of-an-adjacent-already-completed-segment/47792

---

## Post #1 by @Jean_Pinson (2026-08-03 07:32 UTC)

<p>Hi everyone,</p>
<p>The new version of nninteractive in 3D slicer is huge !!! I’m using it on local on my desktop PC but I’ve now an issue that I hadn’t before where several structures are directly adjacent (e.g., bladder and rectum).</p>
<p><strong>Issue:</strong> When I finish segmenting structure A, then start prompting on adjacent structure B, any voxels where B’s segmentation slightly overlaps A get erased from A — with no way to recover them via Ctrl+Z (which only undoes the last nnInteractive prompt, not the erasure of the other segment).</p>
<p>my Segment Editor masking settings are “Modify other segments” → “Allow overlap”</p>
<p>Neither prevented the overlap-erase behavior. This suggests nnInteractive writes directly to the shared labelmap layer rather than going through Slicer’s standard masking pipeline ? The only solution I’ve find for the moment is to create a new segmentation to segment the other structure…</p>
<p>But sometimes, I succeed to get an overlap, and I doesn’t know why !</p>
<p>Is this expected behavior, or a bug? Is there a recommended workflow for segmenting adjacent structures without risking overwriting completed work ? Can I freeze one segment so it dosent change ?</p>
<p>my setup Slicer 5.12.2, Windows, RTX 5080</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2026-08-03 10:10 UTC)

<p>I am not familiar with the implementation of this effect, but this sounds like a bug that it does not respect the masking settings (I suppose it outputs a normal labelmap without overlaps and inserts it to the layer in the segmentation).</p>
<p>Until this is fixed I’d probably do the following: clone the segmentation just before starting using NNInteractive, create the new segment, then drag&amp;drop that segment into your original segmentation, finally delete the clone.</p>

---

## Post #3 by @lassoan (2026-08-03 16:36 UTC)

<p>I agree that this is a subtle bug (that should not be too difficult to fix). Please let the developers know by submitting an issue to <a href="https://github.com/coendevente/SlicerNNInteractive/issues" class="inline-onebox">Issues · coendevente/SlicerNNInteractive · GitHub</a></p>
<p>To get latest updates, you need to use the latest Slicer Stable Release (currently Slicer-5.12.3).</p>

---
