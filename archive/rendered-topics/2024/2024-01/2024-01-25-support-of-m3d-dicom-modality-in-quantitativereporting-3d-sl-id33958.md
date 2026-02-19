---
topic_id: 33958
title: "Support Of M3D Dicom Modality In Quantitativereporting 3D Sl"
date: 2024-01-25
url: https://discourse.slicer.org/t/33958
---

# Support of M3D DICOM modality in QuantitativeReporting 3D Slicer extension

**Topic ID**: 33958
**Date**: 2024-01-25
**URL**: https://discourse.slicer.org/t/support-of-m3d-dicom-modality-in-quantitativereporting-3d-slicer-extension/33958

---

## Post #1 by @Cosmin_Ciausu (2024-01-25 01:15 UTC)

<p>Hi everyone,</p>
<p>We are excited to announce the addition of M3D DICOM modality into the 3D Slicer <a href="https://github.com/QIICR/QuantitativeReporting" rel="noopener nofollow ugc">QuantitativeReporting</a> extension.</p>
<p>DICOM M3D is a somewhat unusual modality, which corresponds to <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.85.html#table_A.85.1-1" rel="noopener nofollow ugc">DICOM Encapsulated STL</a>. <a href="https://en.wikipedia.org/wiki/STL_(file_format)" rel="noopener nofollow ugc">STL</a> is a commonly used format for representing surface meshes. With DICOM M3D these commonly used surfaces can be included as DICOM series alongside image and segmentation series. The advantage of using DICOM M3D is that it includes metadata needed to associate your STL with the patient and DICOM study, will have unique identifiers, include references to the image it corresponds to, among other features.</p>
<p>With this new DICOM plugin users can import the DICOM M3D object into the database and load the DICOM object into the scene as a Slicer segmentation.</p>
<p>You can find samples of DICOM M3D in this new analysis results collection in NCI Imaging Data Commons: <a href="https://portal.imaging.datacommons.cancer.gov/explore/filters/?analysis_results_id=Prostate-MRI-US-Biopsy-DICOM-Annotations" rel="noopener nofollow ugc">https://portal.imaging.datacommons.cancer.gov/explore/filters/?analysis_results_id=Prostate-MRI-US-Biopsy-DICOM-Annotations</a>.<br>
You can conveniently access the content of that collection using the SlicerIDCBrowser extension, as shown in the <a href="https://youtu.be/y1VPzsEGJYg?si=uZWr3tZdTDxmjQU7" rel="noopener nofollow ugc">video</a> below:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="y1VPzsEGJYg" data-video-title="How to open DICOM Encapsulated STL files (M3D) in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=y1VPzsEGJYg" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/y1VPzsEGJYg/maxresdefault.jpg" title="How to open DICOM Encapsulated STL files (M3D) in 3D Slicer" width="" height="">
  </a>
</div>

<p>If you would like to learn how we converted STL into DICOM M3D, please check out this notebook: <a href="https://github.com/ImagingDataCommons/prostate_mri_us_biopsy_dcm_conversion/blob/main/demo_conversion_stl_to_dicom.ipynb" rel="noopener nofollow ugc">demo_conversion_stl_to_dicom.ipynb</a></p>
<p>Many thanks to <span class="mention">@dclunie</span> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/fedorov">@fedorov</a> for their valuable advice and contributions to this module.</p>
<p>Feedback is always appreciated, please let us know what could be improved or modified about this module!</p>

---

## Post #2 by @Cosmin_Ciausu (2024-01-25 14:14 UTC)

<p>Also many thanks to <a class="mention" href="/u/david_clunie">@David_Clunie</a> for his help with this module!</p>

---
