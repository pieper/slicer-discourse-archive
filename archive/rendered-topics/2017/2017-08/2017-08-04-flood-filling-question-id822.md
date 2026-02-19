---
topic_id: 822
title: "Flood Filling Question"
date: 2017-08-04
url: https://discourse.slicer.org/t/822
---

# Flood filling question

**Topic ID**: 822
**Date**: 2017-08-04
**URL**: https://discourse.slicer.org/t/flood-filling-question/822

---

## Post #1 by @hherhold (2017-08-04 14:02 UTC)

<p>Does flood filling work on 16-bit data? For some of my datasets, the intensity tolerance maximum of 1000 might be a little small, and flood filling doesn’t seem to do anything. I’ve checked intensity values using the data probe and lowered the neighborhood size all the way down to 0.01, and mouse clicks do nothing.</p>
<p>This is with a relatively recent (7/18) nightly build on MacOS 10.12.5. Flood filling works fine on an example dataset (MR brain tumor 2).</p>
<p>I highly suspect the problem is between chair and keyboard, as they say.</p>
<p>Thanks,</p>
<p>-Hollister</p>

---

## Post #2 by @doc-xie (2017-08-04 14:30 UTC)

<p>The problem about “Flood filling” have been solved.I set the intensity tolerance maximum of 25 and the neighborhood size to 0.15 in hematoma reconstruction.<br>
Thanks to everyone!</p>

---

## Post #3 by @lassoan (2017-08-04 15:22 UTC)

<p>I’ve implemented initialization of slider range based on selected master volume, so you should be able to specify larger tolerance values for images with larger dynamic range. You can either <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorFloodFilling/SegmentEditorFloodFillingLib/SegmentEditorEffect.py">get the latest version of FloodFilling effect script here</a> and update the file manually; or download the nightly version of Slicer tomorrow or later.</p>

---

## Post #4 by @hherhold (2017-08-05 19:13 UTC)

<p>I’ll give this a try. Thank you!</p>

---
