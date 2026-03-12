---
topic_id: 46439
title: "Wrong Positionning Of Segments Exported To Files"
date: 2026-03-12
url: https://discourse.slicer.org/t/46439
---

# Wrong positionning of segments exported to files 

**Topic ID**: 46439
**Date**: 2026-03-12
**URL**: https://discourse.slicer.org/t/wrong-positionning-of-segments-exported-to-files/46439

---

## Post #1 by @rbg (2026-03-12 00:25 UTC)

<p>Hello,</p>
<p>I segmented lesions on DICOM using 3DSlicer 5.10.0. The segments were exported to files with the right reference volume, in NIFTI.</p>
<p>The problem is that the orientation of the segmentation is not the good one when using another software, but is still right with 3D Slicer.</p>
<p>I cannot use the segmentations for a deep learning model with this problem.</p>
<p>Is there a way to export the segmentation with the right orientation for every software ?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2026-03-12 00:38 UTC)

<p>Maybe your input volume axes defined a left-handed coordinate system? Could you provide some example files?</p>
<p>You can also try to save as NRRD file format, which has many advantages over NIFTI, one of them being that you can look at the image header with any text editor to see what is in it. You will see if the image geometry (origin, spacing, axis directions) of the segmentation is the same as the reference volume’s.</p>

---
