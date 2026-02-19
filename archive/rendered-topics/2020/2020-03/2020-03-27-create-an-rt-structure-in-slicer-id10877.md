---
topic_id: 10877
title: "Create An Rt Structure In Slicer"
date: 2020-03-27
url: https://discourse.slicer.org/t/10877
---

# Create an RT Structure in Slicer

**Topic ID**: 10877
**Date**: 2020-03-27
**URL**: https://discourse.slicer.org/t/create-an-rt-structure-in-slicer/10877

---

## Post #1 by @Mohammad (2020-03-27 18:30 UTC)

<p>Hi</p>
<p>Is it possible to create an RT Structure file from the binary mask in 3D Slicer?</p>

---

## Post #2 by @lassoan (2020-03-27 18:33 UTC)

<p>DICOM RT structure set is very poor representation of segmentation data, so only create them if you really don’t have any other option at all (e.g., you must export data that can be read into your RT treatment planning system).</p>
<p>You can export a segmentation as RT structure set using standard <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export_2">DICOM export</a> feature after you installed SlicerRT extension.</p>

---

## Post #3 by @Mohammad (2020-03-27 18:51 UTC)

<p>Exactly. I trained an auto segmentation model and model output is a binary mask, so as you mentioned TPS required RT Structure files.<br>
Thank you</p>

---

## Post #4 by @Mohammad (2020-03-28 20:22 UTC)

<p>Hello again</p>
<p>As you said I exported a segmentation as RT Structure in 3D Slicer, but how can I do this through a python code?<br>
Is there any Python library for this purpose?</p>
<p>Regards</p>

---

## Post #5 by @lassoan (2020-03-28 21:53 UTC)

<p>All Slicer features are accessible via Python scripting. You can find lots of examples in Slicer Script Repository. DICOM export: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_volume_to_DICOM_file_format">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_volume_to_DICOM_file_format</a></p>

---
