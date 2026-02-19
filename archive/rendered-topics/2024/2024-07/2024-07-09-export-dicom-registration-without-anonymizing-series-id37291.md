---
topic_id: 37291
title: "Export Dicom Registration Without Anonymizing Series"
date: 2024-07-09
url: https://discourse.slicer.org/t/37291
---

# Export DICOM registration without anonymizing series

**Topic ID**: 37291
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/export-dicom-registration-without-anonymizing-series/37291

---

## Post #1 by @dgriner (2024-07-09 18:44 UTC)

<p>Maybe this is a naive question, but I cannot figure out this problem.  I have two CT series that I have segmentations from totalsegmentator that I want to export as rtstructs using RTSlicer.  I also perform registration between the two CT volumes and want to export this registration as DICOM so that I can eventually pull everything into Eclipse (the two CT volumes with associated contours and the registration between them).  So I export the contours with slicerRT, and then I export the transform with the REG export type, but this creates an .sro and moving and fixed folders with anonymized images.  How can I get the .sro for the two non anonymized volumes?</p>

---

## Post #2 by @dgriner (2024-07-10 14:34 UTC)

<p>I guess I can be more detailed.  I have two different DICOM imaging series of the same patient that I eventually want to compare the dose distribution.  Each series has a segmentation (i.e. cord and vertebra T2)  loaded from .nii that I want to export as an RT struct.  I am looking at how couch tolerances affect the dose so I perform different registrations between the two series (focused around the treatment site T2).  What I would like is to export the series with the associated RT structs as well as the DICOM registration objects that connects the two series together that Eclipse uses for registration. An example of my workflow:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ae83a4b1a6b857c0e3f31a84b545d8db786f090.png" alt="image" data-base62-sha1="jOPr3SrozxTXhHvIzmYCIeiuwM0" width="628" height="181"></p>
<p>I am able to export the segmentations as RT structs just fine, however, I am really struggling with exporting the registration.  When I export the transforms as DICOM it creates a fixed and moving folders with the images and .sro, however, it seems like it anonymizes because when I load these back into slicer they have a different patient name and ID.  I am also not able to export the RTstructs to the fixed or moving images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/564a207687a91a0730fec57e8d8451e21880ec6d.png" data-download-href="/uploads/short-url/cjlSsCz7IXRUMyClyxiSUwC39Jr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/564a207687a91a0730fec57e8d8451e21880ec6d.png" alt="image" data-base62-sha1="cjlSsCz7IXRUMyClyxiSUwC39Jr" width="259" height="500" data-dominant-color="323839"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">269×519 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In short, I would just like to export contours and registration and have them connected correctly to the corresponding series.</p>

---

## Post #3 by @lassoan (2024-07-10 20:10 UTC)

<p>You are right, the current implementation of the DICOM RTSTRUCT and SRO exporters have this limitation that they always export a new reference image. Instead, we should update the exporters to use the existing images if they are loaded from DICOM.</p>
<p>We use Plastimatch for creating the SRO and it allows specifying an existing DICOM file, so we would just need to modify the code <a href="https://github.com/SlicerRt/SlicerRT/blob/3a1c14f91cfd5486cdbde395a39983fe3c343638/PlastimatchPy/Logic/vtkPlmpyDicomSroExport.cxx#L235">here</a> specify DICOM file path and the <a href="https://github.com/SlicerRt/SlicerRT/blob/3a1c14f91cfd5486cdbde395a39983fe3c343638/DicomSroImportExport/DicomSroImportExportPlugin.py#L126">exporter plugin</a> to provide a DICOM file path instead of a node ID.</p>
<p>Would you have the time and expertise to modify C++ and Python classes?</p>
<p>Alternatively, a workaround could be to use pydicom to modify the generated DICOM SRO file to match the patient name, ID, and UIDs of the original DICOM images.</p>

---

## Post #4 by @dgriner (2024-07-11 10:30 UTC)

<p>Thank you for the reply! I need a quick fix to meet a deadline so I will look into that workaround, but long term the functionality you mentioned will be great.  I will take a look at implementing those changes to the C++ and Python classes and share my progress (I will likely have follow-up questions).</p>

---
