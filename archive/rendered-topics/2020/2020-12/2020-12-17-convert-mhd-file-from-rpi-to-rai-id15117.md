---
topic_id: 15117
title: "Convert Mhd File From Rpi To Rai"
date: 2020-12-17
url: https://discourse.slicer.org/t/15117
---

# Convert mhd file from RPI to RAI

**Topic ID**: 15117
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/convert-mhd-file-from-rpi-to-rai/15117

---

## Post #1 by @suranga (2020-12-17 16:45 UTC)

<p>I have load a CT volume to the 3D slicer and centred it and saved it as a mhd file. The header file is shown below and it is in RPI orientation. Now I want to convert this into RAI orientation.</p>
<p>How can I do that using the Slicer ?</p>
<p>In order to change from RPI to RAI, is that Ok if I change the Transformation Matrix as 1 0 0 0 1 0 0 0 1 instead of 1 0 0 0 -1 0 0 0 1 and the offset as -196.615234375 -196.615234375 -250 ?</p>
<pre><code>ObjectType = Image
NDims = 3
BinaryData = True
BinaryDataByteOrderMSB = False
CompressedData = False
TransformMatrix = 1 0 0 0 -1 0 0 0 1
Offset = -196.615234375 196.615234375 -250
CenterOfRotation = 0 0 0
AnatomicalOrientation = RPI
ElementSpacing = 0.76953125 0.76953125 1
DimSize = 512 512 501
ElementType = MET_FLOAT
ElementDataFile = volume-10.raw</code></pre>

---

## Post #2 by @lassoan (2020-12-17 17:23 UTC)

<p>Original intent of AnatomicalOrientation field in metafiles (mha, mhd) is unclear, but the current directive to all application developers is to ignore the field and interpret images to be in LPS coordinate system. See more information here: <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1017#issuecomment-568544897">https://github.com/InsightSoftwareConsortium/ITK/issues/1017#issuecomment-568544897</a></p>

---
