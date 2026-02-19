---
topic_id: 41060
title: "Dicom Voi Lut Vs Volume Rendering"
date: 2025-01-13
url: https://discourse.slicer.org/t/41060
---

# DICOM "VOI LUT" vs. Volume Rendering

**Topic ID**: 41060
**Date**: 2025-01-13
**URL**: https://discourse.slicer.org/t/dicom-voi-lut-vs-volume-rendering/41060

---

## Post #1 by @shai-ikko (2025-01-13 14:34 UTC)

<p>Hi Slicerers,</p>
<p>The DICOM standard defines fields which can be used to map source pixel (or voxel) values to presented pixel values; this is, essentially, the “scalar opacity mapping” of the volume rendering module. The DICOM fields are called “VOI LUT” (Values Of Interest Look Up Table); the relevant DICOM tags are 0028|3002 and 0028|3006, see <a href="https://dicom.nema.org/dicom/2013/output/chtml/part03/sect_C.11.html#sect_C.11.4" rel="noopener nofollow ugc">here</a> for more details.</p>
<p>AFAICT from looking at sources, when exporting a DICOM series, these tags are not used, and volume rendering is not consulted; I see them mentioned in neither Slicer sources nor the relevant ITK modules.</p>
<p>Has there been any attempt to use this DICOM facility from Slicer?</p>
<p>FWIW, this seems related to <a href="https://discourse.slicer.org/t/volume-rendering-preset-to-dicom-or-nifti/18605">this old question</a>.</p>

---

## Post #2 by @pieper (2025-01-13 15:45 UTC)

<p>VOI LUT interoperability has never been a high priority for us, but there’s no reason someone couldn’t add support for it.  Like a lot of things in DICOM, it can be hard to know if you’ve created a valid object and whether some other system will be able to read it.  Also, Slicer supports a lot of things that aren’t standardized in DICOM so there are always limitations.  If you have a specific use case and target system you want to exchange data with then yes, probably it can be done.</p>

---
