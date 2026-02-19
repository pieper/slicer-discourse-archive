---
topic_id: 4095
title: "Deformable Registration Grid Dicom Import"
date: 2018-09-13
url: https://discourse.slicer.org/t/4095
---

# Deformable Registration Grid DICOM import

**Topic ID**: 4095
**Date**: 2018-09-13
**URL**: https://discourse.slicer.org/t/deformable-registration-grid-dicom-import/4095

---

## Post #1 by @Lowey (2018-09-13 02:48 UTC)

<p>Hi there,</p>
<p>I am trying to get my head around how Slicer reads TPS exported Displacement fields and calculates its <strong>Grid Orientation</strong> values.</p>
<p>For example, I have exported an arbitrary displacement field from my TPS and have the following values for <strong>Grid orientation</strong>,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea968d775fe02af53b88e2d89acace7a9353a1a7.png" alt="image" data-base62-sha1="xtghHEi6nTpyMevtnHfkaBA0fCn" width="437" height="235"></p>
<p>However, when I look at the DICOM metadata regarding the same displacement field I get the following,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ac33ad4448ab3679afe8763fd862b728f3919d5.png" data-download-href="/uploads/short-url/aFnBREXc5F9m8kFlOhNAuht9eQt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ac33ad4448ab3679afe8763fd862b728f3919d5.png" alt="image" data-base62-sha1="aFnBREXc5F9m8kFlOhNAuht9eQt" width="689" height="94" data-dominant-color="F2F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1194×164 8.07 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I assume the <strong>FrameOfReferenceTransformationMatrix</strong> DICOM tag has something to do with the previously mentioned <strong>Grid orientation</strong> but they seem to be inverted compared to one another.</p>
<p>All of this is important because I want to accumulate dose by applying the inverse displacement field to a dose distribution. I am wondering if I need to rotate/tilt my dose distribution before applying the inverse displacement field.</p>
<p>Any help would be greatly appreciated!</p>

---

## Post #2 by @lassoan (2018-09-13 04:57 UTC)

<p>DICOM uses LPS coordinate system, while Slicer internally uses RAS. When the displacement field is imported from DICOM, the position and orientation is converted accordingly. See details <a href="https://github.com/SlicerRt/SlicerRT/blob/988f0746d0a5e9fef8d1872585ad78656bf90cca/DicomSroImport/Logic/vtkSlicerDicomSroReader.cxx#L158-L251">here</a>.</p>

---
