---
topic_id: 1066
title: "Dicom Volume Rendering Max 3D Texture Size Error"
date: 2017-09-16
url: https://discourse.slicer.org/t/1066
---

# DICOM volume rendering : MAX_3D_TEXTURE_SIZE error

**Topic ID**: 1066
**Date**: 2017-09-16
**URL**: https://discourse.slicer.org/t/dicom-volume-rendering-max-3d-texture-size-error/1066

---

## Post #1 by @chir.set (2017-09-16 12:49 UTC)

<p>I get this error with Volume Rendering with some DICOM CT series :</p>
<p>ERROR: OpenGL MAX_3D_TEXTURE_SIZE is 2048<br>
Invalid texture dimensions [512, 512, 2187]</p>
<p>No 3D model is computed. If I crop down the volume, Volume Rendering doesn’t complain.</p>
<p>Does this mean a hard  limit of the video card is reached ? Would adding a second adapter resolve the issue (which would use AMD Crossfire here)?</p>
<p>I’m using the QT5/VTK8 build.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2017-09-16 13:39 UTC)

<p>For now, it seems that you have to crop or resample your volume if it’s very large. You can do both using Crop volume module.</p>
<p>We are going to move to a new rendering backend in a couple of weeks that might not have this limitation.</p>

---
