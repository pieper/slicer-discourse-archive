---
topic_id: 582
title: "Data Format For Pose Information"
date: 2017-06-27
url: https://discourse.slicer.org/t/582
---

# Data Format for Pose Information

**Topic ID**: 582
**Date**: 2017-06-27
**URL**: https://discourse.slicer.org/t/data-format-for-pose-information/582

---

## Post #1 by @Alex_Benjamin (2017-06-27 17:25 UTC)

<p>Hi, I am very new to using 3D Slicer. At the moment, I have a setup which acquires PNGs of ultrasound images. DICOM access is restricted on the machine for various logistic reasons. My question is what should the accompanying pose format be? The pose of the probe is being estimated using a custom algorithm which outputs the rotation and translation vectors as an numpy array. What kind of format should this be exported to? Should the images and pose be in a single file?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2017-06-27 20:22 UTC)

<p>I would recommend to use the Sequence metafile format. It is an extension of MetaIO image format with custom fields for tracked ultrasound storage. If you install Sequences and SlicerIGT extensions then you can drag-and-drop sequence metafiles into Slicer and replay them. If you use .seq.mha (or .seq.mhd) extension in the file name then Slicer will interpret the file as a Sequence Metafile by default (you don’t have to select the format manually in the Add data dialog).</p>
<p>Specification of the file format: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceMetafile.html">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceMetafile.html</a><br>
Example image: <a href="https://app.assembla.com/spaces/plus/subversion/source/HEAD/trunk/PlusLibData/TestImages/fCal_Test_Calibration_3NWires_fCal2.0.mha">https://app.assembla.com/spaces/plus/subversion/source/HEAD/trunk/PlusLibData/TestImages/fCal_Test_Calibration_3NWires_fCal2.0.mha</a></p>

---
