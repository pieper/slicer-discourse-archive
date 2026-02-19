---
topic_id: 22023
title: "Does 3D Slicer Allow Annotation Metadata"
date: 2022-02-17
url: https://discourse.slicer.org/t/22023
---

# Does 3D slicer allow annotation metadata?

**Topic ID**: 22023
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/does-3d-slicer-allow-annotation-metadata/22023

---

## Post #1 by @alex_ndre (2022-02-17 15:39 UTC)

<p>hello, and first of all thanks to those who will take the time to answer.</p>
<p>In our current workflow, it is possible for several people to annotate the same 3D data. In order to have a better traceability, is it possible to retrieve the metadata/attributes of our annotations?(e.g annotator id) If so, do you know how to do this?  Unfortunately I can’t find the answer, only for the metadata already present in the dicom images.</p>
<p><em>Operating system: Ubuntu 21.04</em><br>
<em>Slicer version: 4.11.20210226</em></p>

---

## Post #2 by @lassoan (2022-02-17 19:39 UTC)

<p>User information can be specified in application settings (menu: Edit / Application settings / User) and that information is available for data exporters to include in files.</p>
<p>Currently, the only exporter that I know that writes user information to the output is the <a href="https://github.com/QIICR/QuantitativeReporting">QuantitativeReporting extension</a>, which writes to <a href="https://dicom.innolitics.com/ciods/segmentation">DICOM Segmentation Object</a> and <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part21/sect_A.7.2.html">DICOM Structured Report with TID1500 template</a>. I’ve tested this with the latest Slicer Preview Release and found a few small regressions. I’ve submitted fixes, so if you want to use this in the latest Slicer Preview Release then you need to wait 1-2 days (you can monitor the status of these fixes here: <a href="https://github.com/QIICR/QuantitativeReporting/pull/262">QuantitativeReporting#262</a>, <a href="https://github.com/QIICR/SlicerDevelopmentToolbox/pull/42">DevelopmentToolbox#42</a>).</p>
<p>It would not be hard to add user information to other exported data sets, too. By “annotation” do you mean markups (points, lines, curves, etc.) or segmentation (labeled image)? What format you would like to use for saving?</p>

---
