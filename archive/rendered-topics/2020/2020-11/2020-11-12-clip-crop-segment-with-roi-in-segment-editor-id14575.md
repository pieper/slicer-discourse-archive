# Clip/crop segment with ROI in segment editor?

**Topic ID**: 14575
**Date**: 2020-11-12
**URL**: https://discourse.slicer.org/t/clip-crop-segment-with-roi-in-segment-editor/14575

---

## Post #1 by @hherhold (2020-11-12 20:54 UTC)

<p>Often when I’m doing hand-segmentation of internal anatomy of various things, it’s useful to be able to cut the segmentation in half to double-check what it looks like “on the inside”. Is it possible to use an annotation ROI to “crop the view” of a segment? What I’ve been doing so far is to export it to a model and clip the model, but this is an extra step. Is it possible to use an annotation ROI inside Segment Editor?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2020-11-12 20:54 UTC)

<p>Oh yeah, this is in the 3D view. Sorry for not including that fairly important detail…</p>

---

## Post #3 by @lassoan (2020-11-13 06:17 UTC)

<p>Thanks for the suggestion. We planned to add plane cut of segments early on, but then it hasn’t really come up as a widely needed feature, maybe because you can see what is inside a segment in slice views or by making the 3D model semi-transparent.</p>
<p>Currently, for cases when we need to look inside the segmentation we do what you described - export to model and cut using Dynamic modeler module. This is certainly not ideal, especially if you want to do this during segmentation.</p>
<p>Could you add a feature request in the <a href="http://issues.slicer.org/">issue tracker</a>?</p>

---

## Post #4 by @hherhold (2020-11-13 12:46 UTC)

<p>Sure, will do.</p>
<p>If cropping/clipping using an ROI (rather than clip planes using slice positions) is possible, it would be really really nice. Especially with fossils (insect inclusions in amber), it is helpful to see internal morphology in 3D while segmenting.</p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2020-11-13 15:26 UTC)

<p>Another workaround came to my mind: you can split a segment into two segments using Scissors effect. You can then hide one side so that you can look inside. You can join them later using Logical operators effect.</p>

---

## Post #6 by @lassoan (2020-11-13 15:27 UTC)

<p>For reference, this feature request was added to track status of this: <a href="https://github.com/Slicer/Slicer/issues/5299">https://github.com/Slicer/Slicer/issues/5299</a></p>

---

## Post #7 by @manjula (2020-11-13 16:15 UTC)

<p>I just make use of the undo. Cut with scissor erasing then undo. (Ctrl Z) much faster.</p>

---

## Post #8 by @hherhold (2020-11-13 16:24 UTC)

<p>Thanks, Manjula. Yeah, I do that sometimes too, but sometimes I need to see “inside” while I’m segmenting, and using undo will then undo what I just added with a brush/scissors/etc.</p>
<p>And thanks, Andras - the splitting and joining is a great idea, I’ll try that.</p>

---
