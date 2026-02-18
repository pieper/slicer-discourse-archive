# Import DICOM after format change from NETCDF using pydicom

**Topic ID**: 18312
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/import-dicom-after-format-change-from-netcdf-using-pydicom/18312

---

## Post #1 by @asims (2021-06-24 02:10 UTC)

<p>OS: Windows 10 64bit<br>
Slicer Version:4.10.0</p>
<p>Hi</p>
<p>I have a lab CT scan of an item stored in NETCDF (*.nc) format in multiple blocks. I would like to open this in Slicer. I have converted to dicom slices (1 file per slice) using the pydicom package in Python.</p>
<p>I understand that I have included all the required metadata. The dicom files can be successfully opened as a stack in a 2D program (ImageJ). The metadata is able to be queried in ImageJ.</p>
<p>When importing into Slicer, either by the DICOM import directory, or adding data using individual files, or even using the Patch DICOM function, errors were returned and the volume would not load.</p>
<p>From the error messages, it appears to be some problem in the meta data. One of the functions reports that the required field “PatientName” is not present, however it is present as is evident from the ImageJ metadata query.</p>
<p>Thanks for any assistance you can provide to debug this and allow this volume to be imported.</p>
<p>Below are the error messages and metadata from the import function, patch dicom and ImageJ.</p>
<p>-------- <strong>Import DICOM</strong> --------------<br>
W: DcmMetaInfo: No Group Length available in Meta Information Header<br>
W: DcmItem: Non-standard VR ’  ’ (08\00) encountered while parsing element (0008,0020), assuming 2 byte length field<br>
W: DcmItem: Non-standard VR ‘06’ (30\36) encountered while parsing element (3032,3132), assuming 2 byte length field<br>
W: DcmItem: Non-standard VR ’  ’ (00\00) encountered while parsing element (0000,0000), assuming 2 byte length field<br>
W: DcmItem: Dataset not in ascending tag order, at element (0000,0000)<br>
W: DcmItem: Non-standard VR ’  ’ (00\00) encountered while parsing element (0000,0000), assuming 2 byte length field<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Non-standard VR ’  ’ (00\00) encountered while parsing element (0000,0000), assuming 2 byte length field<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Non-standard VR ’  ’ (00\00) encountered while parsing element (0000,0000), assuming 2 byte length field<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry<br>
W: DcmItem: Non-standard VR ’  ’ (00\00) encountered while parsing element (0000,0000), assuming 2 byte length field<br>
W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry</p>
<p>Could not load  “&lt;path_to_&gt;/tomo00004.dcm”<br>
DCMTK says:  I/O suspension or premature end of stream</p>
<p>-------- <strong>Patch DICOM</strong>  --------------<br>
Traceback (most recent call last):<br>
File “C:/Data/Utilities/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMPatcher.py”, line 154, in onPatchButton<br>
self.logic.patchDicomDir(self.inputDirSelector.currentPath, self.outputDirSelector.currentPath)<br>
File “C:/Data/Utilities/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMPatcher.py”, line 563, in patchDicomDir<br>
rule.processDataSet(ds)<br>
File “C:/Data/Utilities/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMPatcher.py”, line 223, in processDataSet<br>
if ds.PatientName == ‘’:<br>
File “C:\Data\Utilities\Slicer 4.10.0\lib\Python\Lib\site-packages\dicom\dataset.py”, line 256, in <strong>getattr</strong><br>
“‘{0:s}’.”.format(name))<br>
AttributeError: Dataset does not have attribute ‘PatientName’.</p>
<h2><a name="p-61897-imagej-metadata-00020002-media-storage-sop-class-uid-1284010008514112-00020003-media-storage-sop-inst-uid-123-00020010-transfer-syntax-uid-1284010008121-00020012-implementation-class-uid-1234-00080020-study-date-20210609-00080030-study-time-110000000000-00080050-accession-number-19078400556130-00080090-referring-physicians-name-00100010-patients-name-something-00100020-patient-id-556130-00100030-patients-birth-date-19870113-00100040-patients-sex-m-00180050-slice-thickness-001874854601919651-00200010-study-id-19078400556130-00200011-series-number-1-00200020-patient-orientation-00200032-image-position-patient-00007499418407678604-00201041-slice-location-007499418407678604-00280002-samples-per-pixel-1-00280004-photometric-interpretation-monochrome2-00280010-rows-2520-00280011-columns-2520-00280030-pixel-spacing-00187485460018748546-00280100-bits-allocated-16-00280103-pixel-representation-0-7fe00010-pixel-data-600-1" class="anchor" href="#p-61897-imagej-metadata-00020002-media-storage-sop-class-uid-1284010008514112-00020003-media-storage-sop-inst-uid-123-00020010-transfer-syntax-uid-1284010008121-00020012-implementation-class-uid-1234-00080020-study-date-20210609-00080030-study-time-110000000000-00080050-accession-number-19078400556130-00080090-referring-physicians-name-00100010-patients-name-something-00100020-patient-id-556130-00100030-patients-birth-date-19870113-00100040-patients-sex-m-00180050-slice-thickness-001874854601919651-00200010-study-id-19078400556130-00200011-series-number-1-00200020-patient-orientation-00200032-image-position-patient-00007499418407678604-00201041-slice-location-007499418407678604-00280002-samples-per-pixel-1-00280004-photometric-interpretation-monochrome2-00280010-rows-2520-00280011-columns-2520-00280030-pixel-spacing-00187485460018748546-00280100-bits-allocated-16-00280103-pixel-representation-0-7fe00010-pixel-data-600-1" aria-label="Heading link"></a>-------- <strong>ImageJ MetaData</strong> -----------<br>
0002,0002  Media Storage SOP Class UID: 1.2.840.10008.5.1.4.1.1.2<br>
0002,0003  Media Storage SOP Inst UID: 1.2.3<br>
0002,0010  Transfer Syntax UID: 1.2.840.10008.1.2.1<br>
0002,0012  Implementation Class UID: 1.2.3.4<br>
0008,0020  Study Date: 20210609<br>
0008,0030  Study Time: 110000.000000<br>
0008,0050  Accession Number: 19078400556130<br>
0008,0090  Referring Physician’s Name:<br>
0010,0010  Patient’s Name: Something<br>
0010,0020  Patient ID: 556130<br>
0010,0030  Patient’s Birth Date: 19870113<br>
0010,0040  Patient’s Sex: M<br>
0018,0050  Slice Thickness: 0.01874854601919651<br>
0020,0010  Study ID: 19078400556130<br>
0020,0011  Series Number: 1<br>
0020,0020  Patient Orientation:<br>
0020,0032  Image Position (Patient): 0\0\0.07499418407678604<br>
0020,1041  Slice Location: 0.07499418407678604<br>
0028,0002  Samples per Pixel: 1<br>
0028,0004  Photometric Interpretation: MONOCHROME2<br>
0028,0010  Rows: 2520<br>
0028,0011  Columns: 2520<br>
0028,0030  Pixel Spacing: 0.018748546\0.018748546<br>
0028,0100  Bits Allocated: 16<br>
0028,0103  Pixel Representation: 0<br>
7FE0,0010  Pixel Data: 600</h2>
<p>(Fiji Is Just) ImageJ 2.1.0/1.53c; Java 1.8.0_172 [64-bit]; Windows 10 10.0; 403MB of 48953MB (&lt;1%)</p>
<p>Title: tomo00004.dcm<br>
Width:  47.2463 mm (2520)<br>
Height:  47.2463 mm (2520)<br>
Size:  12MB<br>
Resolution:  53.3375 pixels per mm<br>
Pixel size: 0.0187x0.0187 mm^2<br>
ID: -49<br>
Bits per pixel: 16 (unsigned)<br>
Display range: 0 - 21181<br>
No threshold<br>
Magnification: 0.33<br>
ScaleToFit: false<br>
Uncalibrated<br>
Path: &lt;path_to_&gt;\tomo00004.dcm<br>
Screen location: 152,52 (1920x1080)<br>
No properties<br>
No overlay<br>
No selection</p>

---

## Post #2 by @lassoan (2021-06-25 17:35 UTC)

<p>Creating valid DICOM files is very difficult. You would need to invest at least several days into learning about the DICOM standard and specific details about the information object that you want to create.</p>
<p>Instead of going into all this trouble, I would recommend to convert your data set into nrrd. For example, convert the volume to a numpy array and then save it using pynrrd.</p>

---

## Post #3 by @asims (2021-07-01 01:52 UTC)

<p>Thank you Andras.</p>
<p>I have experience with DICOM but it has been quite a while, so rusty and will take the time that you mention to get across everything.</p>
<p>Thank you for the recommendation of using pynrrd to save a numpy array. That did the trick and I have the volume saved and successfully imported into Slicer now.</p>
<p>While the original question is still open - that will require some research and playing around on my part, your suggestion provided the desired outcome much more simply and quickly. Thank you.</p>
<p>Task complete.</p>

---
