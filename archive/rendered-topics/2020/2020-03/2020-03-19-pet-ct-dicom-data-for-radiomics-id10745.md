---
topic_id: 10745
title: "Pet Ct Dicom Data For Radiomics"
date: 2020-03-19
url: https://discourse.slicer.org/t/10745
---

# PET/CT DICOM data for radiomics

**Topic ID**: 10745
**Date**: 2020-03-19
**URL**: https://discourse.slicer.org/t/pet-ct-dicom-data-for-radiomics/10745

---

## Post #1 by @Nora (2020-03-19 14:36 UTC)

<p>Hi all,</p>
<p>When I pull the PET/CT DICOM data from the PACS.<br>
I’m getting 5 different groups of series files.<br>
3 for PET data, namely, PT HD AC, PT NC and PTQC400.<br>
2 for CT: WB slandered and CTAC 3.75 Thick.</p>
<p>Which ones should I use to extract SUVs and Radiomics? and what are the differences between them please.</p>
<p>Thank you,</p>
<p>Nora</p>

---

## Post #2 by @gcsharp (2020-03-19 15:19 UTC)

<p>I suppose AC = attenuation corrected, NC = not corrected, and QC = quality control.  Therefore I’d go with the first one.</p>

---

## Post #3 by @gcsharp (2020-03-19 15:21 UTC)

<p>But I’ll add, you should really ask your technologist.  We can only make an educated guess.</p>

---
