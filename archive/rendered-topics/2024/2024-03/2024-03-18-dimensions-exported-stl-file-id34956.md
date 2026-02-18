# Dimensions exported stl file

**Topic ID**: 34956
**Date**: 2024-03-18
**URL**: https://discourse.slicer.org/t/dimensions-exported-stl-file/34956

---

## Post #1 by @Marthe (2024-03-18 14:05 UTC)

<p>Dear all</p>
<p>After segmenting a body part from a CT in 3D slicer and performing a ROI cut, I exported the segmented part as an STL to make a mold in Solid Edge. However, when I open the STL file in Solid Edge, the dimensions seem to be changed (much larger). Does anyone has an idea what went wrong? I already checked if the units used in 3D slicer and Solid Edge are the same in the settings.</p>
<p>Thank you in advance!</p>

---

## Post #2 by @pieper (2024-03-18 14:09 UTC)

<p>STL files don’t store units, so you need to do it manually.  By default Slicer will output mm, while many other systems might use meters.</p>

---
