---
topic_id: 48974
title: "Not identifying uterus or large ovarian fibroma on CT scan"
date: 2026-11-19
url: https://discourse.slicer.org/t/48974
last_bumped: 2026-11-21T17:04:52.770Z
---

# Not identifying uterus or large ovarian fibroma on CT scan

**Topic ID**: 48974
**Date**: 2026-11-19
**URL**: https://discourse.slicer.org/t/not-identifying-uterus-or-large-ovarian-fibroma-on-ct-scan/48974

---

## Post #1 by @framistat (2026-11-19 14:29 UTC)

<p>Thank you for this amazing tool.  Have you trained it to recognize the uterus separate from the bladder?  What about fibroids and ovarian fibromas?</p>
<p>I ask because it did not identify these automatically on my scan.  It gives the uterus a different color but labels it as “urinary bladder” as if I have two.  The large fibroma is grey and unidentified.</p>

---

## Post #2 by @framistat (2026-11-20 01:19 UTC)

<p>This is using TotalSegmentor.</p>
<p>I’ve tried manual segmentation of the fibroma using the Draw tool then Fill Between Slices, but in 3D view it is shown as a series of slices, not a solid mass.</p>

---

## Post #3 by @pieper (2026-11-21 16:57 UTC)

<p>TotalSegmentator won’t make segmentations of pathologies, just the “normal” tissues.  You may want to try nnInteractive, but fill between slicers should also work.  Maybe you need to confirm you are using it correctly.</p>

---

## Post #4 by @framistat (2026-11-21 17:04 UTC)

<p>Actually it segmented a large kidney cyst perfectly, and identifies it as “cyst”.  The problem as I stated is that it segmented the uterus only partly, and labeled it as “urinary bladder” as if there were two bladders; and it did not segment a 12 cm ovarian fibroma at all.  Maybe it needs to be trained better on basic female anatomy as well as pathologies.</p>
<p>I suspect the training issue even more because a Chinese researcher contacted me through this post, commented on the lack of public data for females, and asked if I would be willing to contribute so that he could develop his tool.</p>
<p>UPDATE:  Total Segmentator’s README links to a list of structures it recognizes.  No female organs appear in the list.  Shameful.  I contacted the developer.</p>

---
