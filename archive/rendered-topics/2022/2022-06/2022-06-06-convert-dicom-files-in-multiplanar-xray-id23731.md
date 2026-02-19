---
topic_id: 23731
title: "Convert Dicom Files In Multiplanar Xray"
date: 2022-06-06
url: https://discourse.slicer.org/t/23731
---

# Convert Dicom Files in multiplanar Xray

**Topic ID**: 23731
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/convert-dicom-files-in-multiplanar-xray/23731

---

## Post #1 by @Anton_Rockenstein (2022-06-06 12:30 UTC)

<p>Hi, I am planing to create a plugin and i am looking for a solution to convert a dicom file to a multiplanar 2d xray image. My approach would have been to convert the dicom file into a stack of 2d images and use volumeric shaders and colorshaders to simulate the xray.  Is this approach implementable? What data type should be chosen for the 2d images? Is 3DSlicer the right platform for this approach? Any help is welcome.</p>

---

## Post #2 by @pieper (2022-06-06 16:41 UTC)

<p>You can load the dicom data in slicer and experiment.  The volume rendering is not exactly a simulated x ray image but maybe you can adjust the parameters.  If not you can access the raw data and implement whatever ray summation algorithm you need.  Typically dicom will be 16 bit ints, but you may change to float for calculations.</p>

---
