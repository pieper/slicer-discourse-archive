---
topic_id: 44761
title: "Ct Or Cbct Databases Of Edentulous Patients"
date: 2025-10-14
url: https://discourse.slicer.org/t/44761
---

# CT or CBCT databases of edentulous patients

**Topic ID**: 44761
**Date**: 2025-10-14
**URL**: https://discourse.slicer.org/t/ct-or-cbct-databases-of-edentulous-patients/44761

---

## Post #1 by @Fluvio_Lobo (2025-10-14 16:35 UTC)

<p>Hi all!</p>
<p>It has been a minute. Does anyone know of a good open-source library of HEAD/NECK CT or CBCT showing very severe edentulism? This may be too specific, but I thought I would give it a shot!</p>

---

## Post #2 by @lassoan (2025-10-14 23:24 UTC)

<p>You can get large data sets from TCIA or IDC and then you have several options to identify the relevant images:</p>
<ul>
<li>a few slices from each 3D image and use a powerful general-purpose LLM to ask questions about it</li>
<li>run a specialized AI segmentation model (DentalSegmentator, TotalSegmentator, etc.) on the 3D volumes and use simple rules to decide if the image is likely usable</li>
<li>write a short Python script that volume renders the images and extracts a few slices and save them into PNGs or animated GIFs so that you can quickly review hundreds of them (this can be combined with the previous two options, i.e., render all the candidates that AI models identified)</li>
</ul>

---
