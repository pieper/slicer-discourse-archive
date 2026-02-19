---
topic_id: 4101
title: "Error Running Dwiconvert Cli"
date: 2018-09-13
url: https://discourse.slicer.org/t/4101
---

# Error running DWIConvert (cli)

**Topic ID**: 4101
**Date**: 2018-09-13
**URL**: https://discourse.slicer.org/t/error-running-dwiconvert-cli/4101

---

## Post #1 by @devg (2018-09-13 16:42 UTC)

<p>Hi</p>
<p>I was trying to use DWIConvert to convert a dicom series to nifti (the series is from TCIA NSCLC_Radiogenomics collection, Patient R01-022, Series RECON 3: CT CHEST W/O). I get the error below when I run DWIConvert. Any help is appreciated.</p>
<p>Thanks</p>
<h2>Dev</h2>
<p>Slicer --launch DWIConvert --conversionMode DicomToFSL --inputDicomDirectory dicoms/ --outputDirectory out/ --outputVolume R01-022.nii<br>
W: DcmItem: Length of element (493c,616d) is odd<br>
E: DcmElement: Unknown Tag &amp; Data (493c,616d) larger (1849779559) than remaining bytes in file<br>
W: DcmItem: Dataset not in ascending tag order, at element (0000,0000)<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Length of element (0520,050a) is odd<br>
E: DcmElement: Unknown Tag &amp; Data (0520,050a) larger (88802609) than remaining bytes in file<br>
W: DcmItem: Dataset not in ascending tag order, at element (0000,0000)<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Length of element (0520,050a) is odd<br>
E: DcmElement: Unknown Tag &amp; Data (0520,050a) larger (88802609) than remaining bytes in file<br>
=================== this-&gt;m_SlicesPerVolume:235<br>
Dicom images are ordered in a volume interleaving way.<br>
ImageOrientationPatient (0020:0037): LPS Orientation Matrix<br>
1 0 0<br>
0 1 0<br>
0 0 1</p>
<p>this-&gt;m_SpacingMatrix<br>
0.859375 0 0<br>
0 0.859375 0<br>
0 0 1.25</p>
<p>NRRDSpaceDirection<br>
0.859375 0 0<br>
0 0.859375 0<br>
0 0 1.25</p>
<p>Slice 0: -233.5 -263.6 539<br>
Slice 1: -233.5 -263.6 538<br>
Slice order is SI<br>
Number of Slices: 235<br>
Number of Volume: 1<br>
Number of Slices in each volume: 235<br>
WARNING: Missing B Value<br>
Exception extracting gradient vectors<br>
itk::ExceptionObject (0x2e44380)<br>
Location: “unknown”<br>
File: /home/kitware/Dashboards/Package/Slicer-462-package/ITKv4/Modules/IO/DCMTK/src/itkDCMTKFileReader.cxx<br>
Line: 963<br>
Description: itk::ERROR: Cant find tag 19 10bb</p>

---

## Post #2 by @ihnorton (2018-09-13 16:46 UTC)

<p>It looks like you are opening a CT file… The main focus of DWIConvert is DWI, so it isn’t really tested with CT data. If you need to convert DICOM to Nifti on the command line, I would suggest</p>
<ul>
<li>writing a Python script to use Slicer’s loading logic</li>
<li>using dcm2niix.</li>
</ul>

---
