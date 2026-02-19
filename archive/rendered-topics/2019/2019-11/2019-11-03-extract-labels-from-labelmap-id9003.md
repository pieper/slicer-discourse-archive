---
topic_id: 9003
title: "Extract Labels From Labelmap"
date: 2019-11-03
url: https://discourse.slicer.org/t/9003
---

# Extract labels from labelmap

**Topic ID**: 9003
**Date**: 2019-11-03
**URL**: https://discourse.slicer.org/t/extract-labels-from-labelmap/9003

---

## Post #1 by @Vinny (2019-11-03 12:19 UTC)

<p>Hello 3d Slicer community,</p>
<p>I’d like to extract a specific label(s) from a segmentation labelmap that has multiple labels.  I’ve had to either:</p>
<ol>
<li>
<p>Use Model Maker module to generate a model of the specific label and then use Model to Label Map module to obtain the specific label that I could save in nrrd/nifti format or;</p>
</li>
<li>
<p>Use Label Map Smoothing module to extract the specific label but the result is a smoothed label.</p>
</li>
</ol>
<p>Is there a way to extract a label directly from a segmentation labelmap without having to either generate a model or smooth the label?</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2019-11-03 13:35 UTC)

<p>If you import a segmentation into a labelmap then each label is listed as a separate segment. You can delete all the segments that you don’t need.</p>

---

## Post #3 by @Vinny (2019-11-03 15:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>: thanks that worked!</p>

---
