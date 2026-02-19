---
topic_id: 3294
title: "How To Import A Mvl File Format 3D Ultrasound Image"
date: 2018-06-25
url: https://discourse.slicer.org/t/3294
---

# How to import a .mvl file format (3D Ultrasound image)

**Topic ID**: 3294
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/how-to-import-a-mvl-file-format-3d-ultrasound-image/3294

---

## Post #1 by @Sherif_Galal1 (2018-06-25 23:55 UTC)

<p>Operating system: windows 10 64 bit<br>
Slicer version: 4.9 nightly<br>
Expected behavior: import .mvl file<br>
Actual behavior: doesn’t import</p>

---

## Post #2 by @jcfr (2018-06-26 00:02 UTC)

<p>File formats supported by default in Slicer are listed on this page: <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/SupportedDataFormat">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/SupportedDataFormat</a></p>
<p>Other formats can be supported after installing extensions.</p>
<p>To understand the status of MVL support and why there is no reader/writer for it, consider reading this discussion: <a href="https://community.ultimaker.com/topic/3506-converting-3d-ultrasound-images-to-stlobj/?page=2">https://community.ultimaker.com/topic/3506-converting-3d-ultrasound-images-to-stlobj/?page=2</a></p>

---

## Post #3 by @Leon_Eduard (2018-11-26 13:03 UTC)

<p>Hi hi!</p>
<p>Is there any news whether it would be already possible to import .mvl formats? A company is using it as only format and I’d like to 3D print, but the only format remains .mvl.</p>
<p>Thank you for all the good work so far!</p>

---

## Post #4 by @lassoan (2018-11-26 14:28 UTC)

<p>Medison remains a small player, so there is very little chance that somebody would take the time to analyze their file format and develop an open-source reader for it. See some more information in this post: <a href="https://discourse.slicer.org/t/could-not-load-ultrasound-from-mvl-medison-volume-format/3928">Could not load ultrasound from .mvl (Medison Volume) format</a></p>
<p>You may buy an option for your Medison software that allows export to standard file formats (this option may or may not exist, if it does not exist then let the vendor know that you would need it), buy software that can convert the data (I think TomoVision can do it), offer funding for developing an open-source reader, or use an ultrasound system that can readily export in open file formats.</p>

---
