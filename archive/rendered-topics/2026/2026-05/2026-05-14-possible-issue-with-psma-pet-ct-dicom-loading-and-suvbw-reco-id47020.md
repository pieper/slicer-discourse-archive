---
topic_id: 47020
title: "Possible Issue With Psma Pet Ct Dicom Loading And Suvbw Reco"
date: 2026-05-14
url: https://discourse.slicer.org/t/47020
---

# Possible issue with PSMA PET/CT DICOM loading and SUVbw recognition

**Topic ID**: 47020
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/possible-issue-with-psma-pet-ct-dicom-loading-and-suvbw-recognition/47020

---

## Post #1 by @ranahashemi (2026-05-14 06:25 UTC)

<p>Hello everyone,</p>
<p>I encountered a possible issue when loading PSMA PET/CT DICOM files in 3D Slicer.</p>
<p>When I select and load all DICOM files from DICOM database for one patient together, 3D Slicer does not seem to recognize the PET images as SUV. The PET volume is loaded/reported in <strong>Bq/mL</strong> instead.</p>
<p>However, when I first load the <strong>PET DICOM series from the DICOM database</strong>, and then load the <strong>CT series separately</strong>, the PET volume appears with <strong>(SUVbw)</strong> in the name.</p>
<p>So, it seems that the way the PET/CT DICOM files are selected or loaded may affect whether Slicer recognizes the PET data as SUVbw.</p>
<p>Could this be a bug, or is there a recommended way to load PSMA PET/CT DICOM files so that SUVbw is correctly recognized?</p>
<p>Thank you very much for your help.</p>

---

## Post #2 by @ThomasVanParys (2026-05-14 08:02 UTC)

<p>Have you tried Slicer’s PET DICOM Extension? This plugin should use specific metadata tags (e.g., Total Dose, Patient Weight, Half-life) and create a new volume with the suffix <code>(SUVbw)</code>.</p>

---

## Post #3 by @ranahashemi (2026-05-15 00:24 UTC)

<p>Yeah By using that extension, it still like the way I mentioned above</p>

---
