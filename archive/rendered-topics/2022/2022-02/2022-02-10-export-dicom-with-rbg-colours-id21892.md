---
topic_id: 21892
title: "Export Dicom With Rbg Colours"
date: 2022-02-10
url: https://discourse.slicer.org/t/21892
---

# Export DICOM with RBG colours

**Topic ID**: 21892
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/export-dicom-with-rbg-colours/21892

---

## Post #1 by @lidia (2022-02-10 12:59 UTC)

<p>Hi,</p>
<p>I’m working with MRI brain images, and i have segmented a structure, with the Segment Editor module, (colour: green), how can i add this segmentation to the original image, without losing the green colour?</p>
<p>It’s that possible?</p>

---

## Post #2 by @pieper (2022-02-10 13:38 UTC)

<p>If you install the <code>Quantitative Reporting</code> extension you can export a DICOM Segmentation Object with the color recorded.  Be aware that not many other programs will be able to read and process DICOM with color.</p>

---

## Post #3 by @lidia (2022-02-11 12:38 UTC)

<p>Thanks,</p>
<p>I try, but i get this error when i push the button “Save Report” :</p>
<p>NameError: name ‘returnValue’ is not defined</p>
<p>And the same error for “Complete Report”</p>

---

## Post #4 by @lassoan (2022-02-11 15:39 UTC)

<p>After installing QuantitativeReporting extension, follow these instructions for exporting a segmentation to DICOM Segmentation Object: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database" class="inline-onebox">DICOM — 3D Slicer documentation</a>. Use the latest Slicer Preview Release for this, as there have been related fixes and improvements recently.</p>

---
