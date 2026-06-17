---
topic_id: 47184
title: "Unable to import GE Vivid E95 4D echocardiography data into 3D Slicer"
date: 2026-05-31
url: https://discourse.slicer.org/t/47184
last_bumped: 2026-06-16T10:19:17.720Z
---

# Unable to import GE Vivid E95 4D echocardiography data into 3D Slicer

**Topic ID**: 47184
**Date**: 2026-05-31
**URL**: https://discourse.slicer.org/t/unable-to-import-ge-vivid-e95-4d-echocardiography-data-into-3d-slicer/47184

---

## Post #1 by @taki011 (2026-05-31 23:48 UTC)

<p>Hello,</p>
<p>I am trying to import 4D cardiac ultrasound data from a <strong>GE Vivid E95</strong> into 3D Slicer (using the SlicerHeart extension) but I have not been able to load the volumetric data successfully.</p>
<p><strong>What I have tried:</strong></p>
<p>1.  Exported data from EchoPAC in three different formats:</p>
<p><strong>•  Raw DICOM</strong> → 3D Slicer gives an error: “Error occurred while loading the selected files”</p>
<p><strong>•  Vol DICOM</strong> → Same error</p>
<p><strong>•  Standard DICOM</strong> → Loads only as 2D images (cine-loop), no 3D/4D volume</p>
<p>2.  In 3D Slicer, I tried the following import methods:</p>
<p><strong>•  GE Kretz 4D US</strong> → Does not recognize the files</p>
<p><strong>•  Philips 4D US</strong> → Does not recognize the files as Philips format</p>
<p><strong>•  MultiVolume Importer</strong> → Works, but only loads 2D frames (no volumetric reconstruction)</p>
<p>3.  A GE engineer suggested switching to a 4D layout in EchoPAC before exporting, but this did not change the result.</p>
<p><strong>Error message (with Raw DICOM):</strong></p>
<p>Error: Loading C:/Users/[username]/Downloads/rawdicom/rawdicom/GEMS<em>IMG/2026</em>MAY/18/W1204650/Q51KNCGA - load failed.</p>
<p><strong>My question:</strong></p>
<p>Is there any way to import GE Vivid E95 4D echo data into 3D Slicer? Is there a specific export format from EchoPAC that would work, or is support for GE Vivid 4D data planned in SlicerHeart?</p>
<p>I would be happy to share anonymized sample files or DICOM metadata (via pydicom) if that would help.</p>
<p>Thank you very much for your help.</p>

---

## Post #2 by @michaly (2026-06-16 10:19 UTC)

<p>Hi,</p>
<p>Can you please share if you were able to get the 3D dll from GE compile with the 3D API library as was previously suggested and upload your 3D data to the 3D slicer app? I sent a request to GE through Edison program, last week, and was invited to the Github project.</p>

---
