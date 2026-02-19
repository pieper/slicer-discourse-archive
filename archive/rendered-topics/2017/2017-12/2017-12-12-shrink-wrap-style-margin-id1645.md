---
topic_id: 1645
title: "Shrink Wrap Style Margin"
date: 2017-12-12
url: https://discourse.slicer.org/t/1645
---

# Shrink-wrap style margin?

**Topic ID**: 1645
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/shrink-wrap-style-margin/1645

---

## Post #1 by @hherhold (2017-12-12 12:32 UTC)

<p>Greetings slicers,</p>
<p>I have a micro-CT scan of an insect. The exoskeleton and associated dense internal cuticular structures are in a segment. What I would like to do is use the margin tool to erode away just the external exoskeleton part of the segmentation, but not act on the internal structure segmentation - kind of like a “shrink wrap” followed by margin, if that makes sense, to remove just the exoskeleton but keep the internal structures segmentation intact. Is there a way to do this? (Automated or semi-automated, that is - I can always do it by hand, but I was looking for a way to speed up the process.)</p>
<p>Many thanks in advance for any ideas anyone has!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-12-12 13:52 UTC)

<p>For this, I would create an “air” segment by Thresholding (if there air inside then you can remove it by applying Smoothing &gt; Opening and Islands &gt; Keep largest) or Flood filling (in SegmentEditorExtraEffects extension). Then, expand this “air” segment using Margin &gt; Grow effect.</p>
<p>For more sophisticated stripping (variable shell thickness), you can try <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper">SwissSkullStripper extension</a> - it is developed for stripping the skull, but it can be used for other shells, too. You have to provide one example image (Atlas volume) and a mask (Atlas mask volume; a labelmap that only covers the region that you want to keep).</p>

---
