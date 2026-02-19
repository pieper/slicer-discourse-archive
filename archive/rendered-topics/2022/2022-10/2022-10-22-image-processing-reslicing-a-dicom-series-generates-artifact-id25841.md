---
topic_id: 25841
title: "Image Processing Reslicing A Dicom Series Generates Artifact"
date: 2022-10-22
url: https://discourse.slicer.org/t/25841
---

# Image Processing: reslicing a DICOM series generates artifacts

**Topic ID**: 25841
**Date**: 2022-10-22
**URL**: https://discourse.slicer.org/t/image-processing-reslicing-a-dicom-series-generates-artifacts/25841

---

## Post #1 by @El_merendero (2022-10-22 12:39 UTC)

<p>I am creating a web application to manage 3D biomedical images. From each of these 3D images I would like to extract a slice that is not perpendicular to the principal axes (axial, saggital or coronal). However, the resulting 2D image has diagonal artifacts that depend on the inclination of the image with respect to the axial plane of the original 3D image (see image below). Is it possible to apply some filter or particular interpolation to moderate this effect?</p>
<p>I tried to do something similar in 3D Slicer and I see that this software allows you to enable / disable pixel interpolation in order to filter or not this type of artifact. But I don’t understand what kind of interpolation is performed.</p>
<p><img src="https://i.ibb.co/QK4MnWL/Cattura.png" alt="image info" width="526" height="500"></p>

---

## Post #2 by @lassoan (2022-10-22 12:46 UTC)

<p>You need to do at least linear interpolation. You can get a bit better results using cubic interpolation, but the difference is rarely visible (e.g., when you zoom in a lot).</p>

---
