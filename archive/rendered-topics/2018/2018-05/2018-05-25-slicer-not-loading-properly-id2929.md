# slicer not loading properly

**Topic ID**: 2929
**Date**: 2018-05-25
**URL**: https://discourse.slicer.org/t/slicer-not-loading-properly/2929

---

## Post #1 by @bharat (2018-05-25 06:30 UTC)

<p>Operating system:<br>
Slicer version: 4.8<br>
Expected behavior: running normal mode<br>
Actual behavior: running advanced mode<br>
The message detail is:</p>
<p>Exception thrown in event: d:\d\p\slicer-481-package\itkv4\modules\io\imagebase\include\itkImageFileReader.hxx:143:<br>
Could not create IO object for reading file C:/Users/HOME/Documents/SlicerDICOMDatabase/dicom/1.2.840.113619.2.278.3.2831191556.205.1459907380.468/1.2.840.113619.2.278.3.2831191556.205.1459907380.517/1.2.840.113619.2.278.3.2831191556.205.1459907380.518<br>
Tried to create one of the following:<br>
NiftiImageIO<br>
NrrdImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
GDCMImageIO<br>
BMPImageIO<br>
LSMImageIO<br>
PNGImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
StimulateImageIO<br>
BioRadImageIO<br>
MetaImageIO<br>
MRCImageIO<br>
MINCImageIO<br>
MGHImageIO<br>
MRMLIDImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-05-25 12:22 UTC)

<p>What is the file name extension of the data you are trying to load?</p>

---

## Post #3 by @cpinter (2018-05-25 13:14 UTC)

<p>You need to use the DICOM browser to load DICOM data. You can open it using the “DCM” button right next to add data button on the toolbar. First you have to import the whole DICOM folder, then you can browse patient/study/series and load the selected datasets.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>

---
