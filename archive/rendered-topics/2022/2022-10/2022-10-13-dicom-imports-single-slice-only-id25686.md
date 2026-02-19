---
topic_id: 25686
title: "Dicom Imports Single Slice Only"
date: 2022-10-13
url: https://discourse.slicer.org/t/25686
---

# DICOM imports single slice only

**Topic ID**: 25686
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/dicom-imports-single-slice-only/25686

---

## Post #1 by @Markb (2022-10-13 16:39 UTC)

<p>Hi all. I’ve very recently started using 3D Slicer, and I’m using version 4.11.20210226 on a virtual machine hosting “VGate” (using Ubuntu 18.4).</p>
<p>I am trying to create some fake CT DICOM files using python and pydicom. Originally, I tried to create the meta information from scratch using instructions provided on a stackoverflow, which worked fine in ImageJ but wouldn’t open at all in 3D Slicer.</p>
<p>So instead, I imported an existing CT dicom file using pydicom and dcmread and then adjusted some attributes as required (PatientName, PatientID, ImagesInAcquisition, RescaleSlope and RescaleIntercept, PixelSpacing, SliceThickness, PhotometricInterpretation, PixelRepresentation, StudyDescription and SeriesDescription). The original CT data opens fine in 3D Slicer and is anonymised from a Siemens CT scanner.</p>
<p>This works opens fine in ImageJ but when I import it as DICOM in 3D slicer and open it, it is only showing a single slice from approximately the center of the dataset. It looks a little like there might be three slices to select from, based on moving the scroll bar in the transaxial image, but the two outermost images are black (and at positions -726mm and -724mm c.f. the single slice at -725mm). There are no errors in the log though.</p>
<p>If I import the data in as Add Data instead of DICOM, it works almost perfectly, but the z-direction is squished. If I view the properties of the data, it has 1.000mm as the spacing. This made me consider whether adding another attribute of SpacingBetweenSlices as 4.84 would work, but this made no difference to any of the above. The original CT data doesn’t have this attribute either yet opens fine.</p>
<p>I’m at a loss as to what my next steps might be, can anyone suggest an avenue for me to explore (if not a solution).</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2022-10-13 18:24 UTC)

<p>You could have a look at how the <a href="https://github.com/Slicer/Slicer/tree/main/Modules/CLI/CreateDICOMSeries">Create DICOM Series</a> module works for ideas.</p>

---

## Post #3 by @lassoan (2022-10-21 12:40 UTC)

<p>According to the DICOM standard, a 3D volume must be reconstructed from slices based on these 3 attributes:</p>
<ul>
<li>Image Position Patient</li>
<li>Image Orientation Patient</li>
<li>Pixel Spacing</li>
</ul>
<p>All other parameters, which might seem to be related (slice thickness, etc.) must be ignored.</p>
<p>It looks like you have not set the first two of these three parameters.</p>
<p>See example of how to add the missing parameters using pydicom (this particular example is for enhanced multiframe images; it is simpler to do it for classic single-slice-per-file series) in <a href="https://github.com/Slicer/Slicer/blob/969121214f74d1d73784582542bddae565993a27/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L362-L421">DICOM Patcher module</a>.</p>

---
