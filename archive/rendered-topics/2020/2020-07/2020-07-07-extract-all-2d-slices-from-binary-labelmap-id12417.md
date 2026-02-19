---
topic_id: 12417
title: "Extract All 2D Slices From Binary Labelmap"
date: 2020-07-07
url: https://discourse.slicer.org/t/12417
---

# Extract all 2D slices from Binary labelMap

**Topic ID**: 12417
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/extract-all-2d-slices-from-binary-labelmap/12417

---

## Post #1 by @loubna (2020-07-07 14:46 UTC)

<p>Hi,</p>
<p>I have 3D vtkImageData (binarylabelMap) from which, I want extract all 2D slices. How can I do that</p>
<p>thank’s in advance</p>

---

## Post #2 by @lassoan (2020-07-08 12:19 UTC)

<p>Probably the simplest is to get the voxels as numpy array using <code>a=slicer.util.arrayFromVolume(volumeNode)</code>. Then you can extract a slice using numpy array indexing, for example the 6th slice is <code>a[:,:,5]</code>.</p>

---

## Post #3 by @loubna (2020-07-09 18:46 UTC)

<p>Thank you very much Mr for reply</p>

---
