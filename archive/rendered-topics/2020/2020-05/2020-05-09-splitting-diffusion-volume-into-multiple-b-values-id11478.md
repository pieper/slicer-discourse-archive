---
topic_id: 11478
title: "Splitting Diffusion Volume Into Multiple B Values"
date: 2020-05-09
url: https://discourse.slicer.org/t/11478
---

# Splitting Diffusion Volume into multiple b-values

**Topic ID**: 11478
**Date**: 2020-05-09
**URL**: https://discourse.slicer.org/t/splitting-diffusion-volume-into-multiple-b-values/11478

---

## Post #1 by @Margherita_Mottola (2020-05-09 07:42 UTC)

<p>Hi all, I have some troubles with an enhanced dicom files contaning 9-b-values diffusion volume. When loading the Dicom file, in Examine-&gt;Reader, it is written “Diffusion volume-please see DWI Convert module for advanced options and help”, but DWIConvert does not work on purpose. I would like to open the whole sequence, and also open only one b-value at a time. Thank you for any help</p>

---

## Post #2 by @pieper (2020-05-09 14:56 UTC)

<p>Did you try dcm2niix?  It’s available through <a href="http://dmri.slicer.org/">SlicerDMRI</a>.  Try the latest nightly.</p>
<p>If that doesn’t work, it would help if you could share an example scan.  When you say enhanced dicom files, so you mean <a href="https://www.dicomstandard.org/wp-content/uploads/2018/10/Day1_S9-Solomon-Multiframe.pdf">like this</a>?  Those are fairly new and not too common yet, but it would be great if we could support it.</p>

---
