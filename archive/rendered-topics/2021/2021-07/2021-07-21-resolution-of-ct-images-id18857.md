---
topic_id: 18857
title: "Resolution Of Ct Images"
date: 2021-07-21
url: https://discourse.slicer.org/t/18857
---

# Resolution of CT images

**Topic ID**: 18857
**Date**: 2021-07-21
**URL**: https://discourse.slicer.org/t/resolution-of-ct-images/18857

---

## Post #1 by @Mohammed110 (2021-07-21 12:58 UTC)

<p>Dear all,<br>
I have CT images obtained online and I want to know the resolution and slice thickness, is that possible, I would appreciate any help</p>
<p>Thanks<br>
Mo</p>

---

## Post #2 by @pieper (2021-07-21 13:09 UTC)

<p>You can look in the Volume Information section of the Volumes module.</p>

---

## Post #3 by @Mohammed110 (2021-07-21 13:14 UTC)

<p>Thanks, but is it ok to upload the nrrd instead of DICOM</p>
<p>Regrads,<br>
MO</p>

---

## Post #4 by @pieper (2021-07-21 13:23 UTC)

<p>If you work with nrrd the geometry is all in text at the top of the file.  Most text editors can open it and you can read it.  The meanings are defined <a href="http://teem.sourceforge.net/nrrd/descformat.html">in the nrrd spec</a>.</p>
<p>Or you can load in Slicer and look in the Volume Information.</p>

---
