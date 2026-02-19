---
topic_id: 15129
title: "Slice Order In Dicom Loader"
date: 2020-12-18
url: https://discourse.slicer.org/t/15129
---

# Slice order in dicom loader

**Topic ID**: 15129
**Date**: 2020-12-18
**URL**: https://discourse.slicer.org/t/slice-order-in-dicom-loader/15129

---

## Post #1 by @sogo (2020-12-18 04:07 UTC)

<p>Hi,<br>
I wanted to confirm the mechanism with which Slicer orders dicom slices. I need the slice order (basically z-coordinate value) with filenames to write to csv for my application use and I found that the examineFiles function in DICOMScalarVolumePlugin.py  uses getSortedImageFiles function DICOMUtils.py to order them.<br>
I wanted to know whether is this the Slicer’s backend for showing ordered slices in Slicer viewer so I can call this examineFiles function to get array of sorted files and index them accordingly to write to csv. Also I wanted to know the epsilon and where does this function gets epsilon from.  Thanks</p>

---

## Post #2 by @pieper (2020-12-18 14:50 UTC)

<p>Yes, that is the right method that determines the order of the dicom instances.  If you load the data and need to know the mapping from volume slices to dicom instances, you can use the <code>DICOM.instanceUIDs</code> attribute of the node.</p>
<p>As for epsilon, it’s set to 0.01mm by default as a practical compromise based on medical imaging technologies where slice spacing may vary a bit due to rounding error or limitations of the device while still forming usable volumes.</p>

---

## Post #3 by @sogo (2020-12-18 23:21 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thanks for confirming it, I will proceed to using this for my application.</p>
<p>Regards</p>

---
