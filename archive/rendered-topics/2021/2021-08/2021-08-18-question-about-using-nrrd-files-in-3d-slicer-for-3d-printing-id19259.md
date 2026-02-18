# Question about using NRRD files in 3D Slicer for 3D printing

**Topic ID**: 19259
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/question-about-using-nrrd-files-in-3d-slicer-for-3d-printing/19259

---

## Post #1 by @DylanR (2021-08-18 15:44 UTC)

<p>I am interested in using de-identified NRRD files to create STL files for 3D printing in 3D Slicer. I previously used DICOM data (CT) which works great, but want to use de-identified data. Is it correct that I can go directly from NRRD to STL in 3D Slicer? From everything I have found on the 3D Slicer website and from testing it looks like the NRRD to STL workflow is the same as DICOM to STL, but I found this <a href="https://medimodel.com/guide/how-to-convert-nrrd-file-to-dicom-for-3d-printing/" rel="noopener nofollow ugc">article</a> that says you need to first convert the NRRD to DICOM in 3D Slicer before segmenting. I don’t think this is correct, but want to confirm that I do not need to convert the NRRD to DICOM in 3D Slicer before segmenting. Thank you.</p>

---

## Post #2 by @muratmaga (2021-08-18 15:52 UTC)

<p>That’s completely misleading. DICOM and NRRD contain same type of data, voxels. You can segment and create an STL from a NRRD dataset in the same way and you can print.</p>
<p>It looks like they are not doing the segmentation in Slicer, but only to use convert NRRD to DICOM, which makes me think that the software they are printing from takes only DICOM format.</p>

---

## Post #3 by @DylanR (2021-08-18 17:59 UTC)

<p>Thank you for the confirmation. I agree, the article is misleading. You are right, they are using InVesalius and not Slicer to segment. Thank you again, much appreciated.</p>

---
