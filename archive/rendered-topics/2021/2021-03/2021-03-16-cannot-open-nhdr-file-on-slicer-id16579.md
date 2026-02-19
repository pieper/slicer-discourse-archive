---
topic_id: 16579
title: "Cannot Open Nhdr File On Slicer"
date: 2021-03-16
url: https://discourse.slicer.org/t/16579
---

# cannot open .nhdr file on Slicer

**Topic ID**: 16579
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/cannot-open-nhdr-file-on-slicer/16579

---

## Post #1 by @Tamires_Zanao (2021-03-16 15:50 UTC)

<p>Hi everyone! I am trying to proceed with dwi QC, but I cannot open my axis aligned .nhdr dwi image on Slicer. I checked with unu head and the information of the image itself looks fine. I can also open/visualize my previous .nrrd image (before axis and alignment) on Slice. Any idea about what is probably wrong?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-04-14 06:16 UTC)

<p>You could try loading a nrrd and save as nhdr and see if Slicer can load it. If it can, then you can compare the nhdr files to see what is the difference between them (nrrd file header is text file, so you can easily interpret and compare using any text editor).</p>

---
