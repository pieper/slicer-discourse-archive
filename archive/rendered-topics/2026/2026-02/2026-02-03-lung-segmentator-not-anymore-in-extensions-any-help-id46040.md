---
topic_id: 46040
title: "Lung Segmentator Not Anymore In Extensions Any Help"
date: 2026-02-03
url: https://discourse.slicer.org/t/46040
---

# Lung segmentator not anymore in extensions. Any help?

**Topic ID**: 46040
**Date**: 2026-02-03
**URL**: https://discourse.slicer.org/t/lung-segmentator-not-anymore-in-extensions-any-help/46040

---

## Post #1 by @MartinMD89 (2026-02-03 04:04 UTC)

<p>Hi everyone, paediatric surgeon here.</p>
<p>We are planning to perform an operation on a with CPAM and I wanted to create s segmentation of the lungs and the lesion. Some time ago, i used this lung segmentator extension. Now after updaing the slicer, I cant find it anymore. Is it dead and gone?</p>
<p>Thank you for your time and answer.</p>
<p>Martin</p>

---

## Post #2 by @pieper (2026-02-03 10:30 UTC)

<p>The lung CT analyzer should be available for the stable and preview builds.  Segmentation tools like TotalSegmentator and MONAI Auto3DSeg also do a good job on lungs, but have mostly been trained on “normal” adult cases, so you may do just as well using manual techniques to visualize and measure or the nnInteractive tool.</p>

---
