---
topic_id: 27072
title: "Editing The Deformation Matrix"
date: 2023-01-06
url: https://discourse.slicer.org/t/27072
---

# Editing the Deformation matrix

**Topic ID**: 27072
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/editing-the-deformation-matrix/27072

---

## Post #1 by @ayman.kh (2023-01-06 02:40 UTC)

<p>Hi, there is a way to change the values of the Deformation matrix and save the new Deformation in DICOM Format?</p>

---

## Post #2 by @lassoan (2023-01-06 02:50 UTC)

<p>You can edit the transformation matrix in Transforms module. You can export transformations to DICOM if you install SlicerRT extension.</p>
<p>If you imported the registration from DICOM then the necessary references between the transform and the images should be already there. BRAINS and some other registration tools also set the references. However, if you create the transform from scratch manually or using Elastix or other modules then you may need to set the <a href="https://github.com/SlicerRt/SlicerRT/blob/d31f29dad69c83816c63eefe12ff752ad7f3e87c/DicomSroImportExport/DicomSroImportExportPlugin.py#L81-L82">references</a> manually.</p>
<p>We added experimental DICOM SRO support many years ago but have not heard back much from users, so we haven’t invested a lot in making it easy to use or very robust. If we get specific feedback from you then we may improve things to make your workflow more convenient to perform.</p>

---
