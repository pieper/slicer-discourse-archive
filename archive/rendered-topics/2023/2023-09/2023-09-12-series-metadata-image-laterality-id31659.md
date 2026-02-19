---
topic_id: 31659
title: "Series Metadata Image Laterality"
date: 2023-09-12
url: https://discourse.slicer.org/t/31659
---

# Series metadata image laterality

**Topic ID**: 31659
**Date**: 2023-09-12
**URL**: https://discourse.slicer.org/t/series-metadata-image-laterality/31659

---

## Post #1 by @SOFIA_R (2023-09-12 16:15 UTC)

<p>Hello, I am currently making segmentations in a Tomosynthesis series of images and I would like to know which series is the left breast or the right breast. That’s when I looked for the series metadata. Then I found “PatientOrientation” which says for example “[2] P, FL”. Is that related to left and right? Or which one of the metadata is the one that provides me the laterality of the image? Thank you.</p>

---

## Post #2 by @pieper (2023-09-12 16:50 UTC)

<p>It may vary depending on how the vendor implemented the standard, but PatientOrientation should describe only the relationship of the patient to the scanner (<a href="https://dicom.innolitics.com/ciods/cr-image/general-series/00185100" class="inline-onebox">Patient Position Attribute – DICOM Standard Browser</a>), while Laterality (<a href="https://dicom.innolitics.com/ciods/cr-image/general-series/00200060" class="inline-onebox">Laterality Attribute – DICOM Standard Browser</a>) should be used to describe which side of the body is being imaged.</p>

---

## Post #3 by @David_Clunie (2023-09-14 16:06 UTC)

<p>The laterality information (which breast) is distinct from the orientation information (which direction the rows and columns of the image point relative to the patient).</p>
<p>For the <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.55.html" rel="noopener nofollow ugc">Breast Tomosynthesis IOD</a>, which is of the enhanced multi-frame family, such anatomical information is in the <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.16.2.html#sect_C.7.6.16.2.8" rel="noopener nofollow ugc">Frame Anatomy Sequence in Frame Laterality</a>, which is usually in the Shared <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.55.4.html" rel="noopener nofollow ugc">Functional Group Sequence</a>, since all frames in a single instance are (usually) of the same breast.</p>
<p>I.e., it is not in the top level dataset, and not in Laterality or <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.11.2.html" rel="noopener nofollow ugc">Image Laterality</a> (the later being used for ordinary, non-tomographic <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.27.html" rel="noopener nofollow ugc">mammography images</a>).</p>
<p>There are examples in IDC such as <a href="https://viewer.imaging.datacommons.cancer.gov/viewer/1.2.826.0.1.3680043.8.498.11387662677066579919319049302075478647" rel="noopener nofollow ugc">this one</a>, and you can use the Tag Browser in OHIF to see the Frame Laterality.</p>

---
