---
topic_id: 6326
title: "Failure To Open Quadbuffer"
date: 2019-03-28
url: https://discourse.slicer.org/t/6326
---

# Failure to open QuadBuffer

**Topic ID**: 6326
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/failure-to-open-quadbuffer/6326

---

## Post #1 by @sunhao1296 (2019-03-28 13:47 UTC)

<p>I’m using the Slicer 4.10.0 and when i want to choose quadbuffer as the stereo mode.<br>
But I failed and there is a warning:<br>
vtkGenericOpenGLRenderWindow (000001DF559FE7F0): Adjusting stereo mode on a window that does not support stereo type CrystalEyes is not possible.</p>
<p>My devices are as follows:<br>
Graphic card : NVIDIA Quadro P5000<br>
Monitor: Asus PG278QR<br>
Glasses: 3d vision 2</p>
<p>What should I do to open the quadbuffer?<br>
Thank you all.</p>

---

## Post #2 by @lassoan (2019-03-28 14:57 UTC)

<p>You may need to change the <a href="https://doc.qt.io/qt-5/qsurfaceformat.html" rel="nofollow noopener">default surface format in Qt</a> before you create the 3D view (if you already have a 3D view then you can switch to a layout that has more 3D views).</p>
<p>Since consumer virtual reality is so inexpensive and widely available and it offers practically infinite field of view and rich 3D controls (2x6DOF controllers), there are only a few, very little application areas polarized/shutter glasses technology may still make sense. I would recommend to explore virtual reality instead - using <a href="https://github.com/KitwareMedical/SlicerVirtualReality" rel="nofollow noopener">SlicerVirtualReality extension</a>.</p>

---
