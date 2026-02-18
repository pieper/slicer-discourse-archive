# Creating volumeNode with scalars as RGB

**Topic ID**: 4359
**Date**: 2018-10-11
**URL**: https://discourse.slicer.org/t/creating-volumenode-with-scalars-as-rgb/4359

---

## Post #1 by @Niels (2018-10-11 12:30 UTC)

<p>Apart from the colormaps (that I use allot) would it be possible to create a volume which specifies an RGB color? Currently my volume has only one scalar, but maybe I can use 3 scalars to describe and display RGB?</p>

---

## Post #2 by @lassoan (2018-10-11 12:38 UTC)

<p>You can have RGB volume (vtkMRMLVectorVolumeNode), but you cannot do much with it other than viewing, saving, and loading. Most processing operations require single-component scalar volume.</p>

---

## Post #3 by @Niels (2018-10-11 17:46 UTC)

<p>Hi lassoan, Ok! I will take a look at that node. Do you know of any codeexamples?</p>

---

## Post #4 by @pieper (2018-10-11 18:09 UTC)

<p>If you load a series of png or jpeg files they will be vector volumes.</p>

---
