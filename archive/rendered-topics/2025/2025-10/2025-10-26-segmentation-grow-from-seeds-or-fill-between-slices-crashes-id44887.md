# Segmentation grow from seeds or fill between slices crashes

**Topic ID**: 44887
**Date**: 2025-10-26
**URL**: https://discourse.slicer.org/t/segmentation-grow-from-seeds-or-fill-between-slices-crashes/44887

---

## Post #1 by @FinnR (2025-10-26 22:09 UTC)

<p>When trying to segment by (1) painting selected slices and using ”fill in between slices” or (2) “grow from seeds” the program crashes and exits a few seconds after pressing “initialize”. The number of slices involved is not very high (about 100). Could the problem be insuffient hardware? My graphics card is Nvidea GeForce RTX 2060, CPU is Core i5-9400F, 2.90 GHz, 16 GB RAM installed.</p>

---

## Post #2 by @pieper (2025-10-27 14:27 UTC)

<p>16GB of ram is pretty small by today’s standards.  One way to check would be to use the Crop Volume option to operate on a subset of the data.  Or you can adjust your pagefile settings to get more swap space (for windows).  Or you can use a rental computer from a cloud provider or a use <a href="https://morphocloud.org/">MorphoCloud</a>.</p>

---
