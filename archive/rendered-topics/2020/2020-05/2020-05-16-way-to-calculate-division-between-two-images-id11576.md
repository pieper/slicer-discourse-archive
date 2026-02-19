---
topic_id: 11576
title: "Way To Calculate Division Between Two Images"
date: 2020-05-16
url: https://discourse.slicer.org/t/11576
---

# Way to calculate division between two images

**Topic ID**: 11576
**Date**: 2020-05-16
**URL**: https://discourse.slicer.org/t/way-to-calculate-division-between-two-images/11576

---

## Post #1 by @GMA (2020-05-16 15:10 UTC)

<p>it is possible in Slicer to calculate a division between two images? what is the best way? I’d like to divide two parametric maps one by another</p>

---

## Post #2 by @pieper (2020-05-16 15:26 UTC)

<p>Probably the easiest is to access the volumes as numpy arrays and divide them.  Be sure the two volumes are resampled to the same grid.</p>

---

## Post #3 by @lassoan (2020-05-16 18:11 UTC)

<p>For reference, here is a complete example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Combine_multiple_volumes_into_one">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Combine_multiple_volumes_into_one</a></p>

---
