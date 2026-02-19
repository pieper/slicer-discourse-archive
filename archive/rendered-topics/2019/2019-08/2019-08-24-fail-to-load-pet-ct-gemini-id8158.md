---
topic_id: 8158
title: "Fail To Load Pet Ct Gemini"
date: 2019-08-24
url: https://discourse.slicer.org/t/8158
---

# Fail to load pet/ct Gemini

**Topic ID**: 8158
**Date**: 2019-08-24
**URL**: https://discourse.slicer.org/t/fail-to-load-pet-ct-gemini/8158

---

## Post #1 by @hu_shuang (2019-08-24 09:36 UTC)

<p>Operating system: Mac OS X<br>
Slicer version:4.10.2<br>
Expected behavior: load pet/ct acquired by Phillips Gemini<br>
Actual behavior: It returns to “Could not load: 7: bone as a Scalar Volume”, the metadata is as following. None of the files for one patient can be opened, pet or CTs. Do you know what’s the problem? Data in <a href="https://www.dropbox.com/sh/m0e7t4rahk2ykns/AABLbj8nlGAWtGdNowv1BTNwa?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/m0e7t4rahk2ykns/AABLbj8nlGAWtGdNowv1BTNwa?dl=0</a></p>
<p>Thanks<br>
Shuang</p>
<p>[0008,0005]	SpecificCharacterSet	ISO_IR 100	CS	10<br>
[0008,0008]	ImageType	[3] ORIGINAL, PRIMARY, AXIAL	CS	22<br>
[0008,0012]	InstanceCreationDate	20190628	DA	8<br>
[0008,0013]	InstanceCreationTime	101200	TM	6<br>
[0008,0016]	SOPClassUID	1.2.840.10008.5.1.4.1.1.2	UI	26<br>
[0008,0018]	SOPInstanceUID	1.2.840.113704.1.111.8320.1561687920.11509	UI	42<br>
[0008,0020]	StudyDate	20190628	DA	8<br>
[0008,0022]	AcquisitionDate	20190628	DA	8<br>
[0008,0023]	ContentDate	20190628	DA	8<br>
[0008,0030]	StudyTime	095513	TM	6<br>
[0008,0032]	AcquisitionTime	101052	TM	6<br>
[0008,0033]	ContentTime	101108.701	TM	10<br>
[0008,0050]	AccessionNumber	1906289110	SH	10<br>
[0008,0060]	Modality	CT	CS	2<br>
[0008,0070]	Manufacturer	Philips	LO	8<br>
[0008,0080]	InstitutionName	PMSTL	LO	6<br>
[0008,0081]	InstitutionAddress	Haifa, MATAM	ST	12<br>
[0008,0090]	ReferringPhysicianName	PET-11909-2	PN	12<br>
[0008,1010]	StationName	PHILIPS-0CE7C19	SH	16<br>
[0008,1030]	StudyDescription	Body	LO	4<br>
[0008,103e]	SeriesDescription	bone	LO	4<br>
[0008,1040]	InstitutionalDepartmentName	Radiology	LO	10<br>
[0008,1070]	OperatorsName		PN	0<br>
[0008,1090]	ManufacturerModelName	GEMINI TF TOF 16	LO	16<br>
[0008,1110]	ReferencedStudySequence		SQ	66<br>
[fffe,e000]	Item		na	50<br>
[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.3.1.2.3.1	UI	24<br>
[0008,1155]	ReferencedSOPInstanceUID	1906289110	UI	10<br>
[0008,1111]	ReferencedPerformedProcedureStepSequence		SQ	96<br>
[fffe,e000]	Item		na	80<br>
[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.3.1.2.3.3	UI	24<br>
[0008,1155]	ReferencedSOPInstanceUID	1.2.840.113704.1.111.2768.1561686900.44	UI	40<br>
[0008,1120]	ReferencedPatientSequence		SQ	32<br>
[fffe,e000]	Item		na	16<br>
[0008,1150]	ReferencedSOPClassUID		UI	0<br>
[0008,1155]	ReferencedSOPInstanceUID		UI	0<br>
[0008,1140]	ReferencedImageSequence		SQ	100<br>
[fffe,e000]	Item		na	84<br>
[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.5.1.4.1.1.2	UI	26<br>
[0008,1155]	ReferencedSOPInstanceUID	1.2.840.113704.1.111.8320.1561686995.11013	UI	42<br>
[0010,0010]	PatientName	DIAO SHU ZHEN	PN	14<br>
[0010,0020]	PatientID	PET-11909-2	LO	12<br>
[0010,0030]	PatientBirthDate	19430628	DA	8<br>
[0010,0040]	PatientSex	F	CS	2<br>
[0010,1000]	RETIRED_OtherPatientIDs		LO	0<br>
[0010,1010]	PatientAge	076Y	AS	4<br>
[0010,1020]	PatientSize	1.53	DS	4<br>
[0010,1030]	PatientWeight	58	DS	2<br>
[0010,2000]	MedicalAlerts		LO	0<br>
[0010,2110]	Allergies		LO	0<br>
[0010,2160]	EthnicGroup		SH	0<br>
[0010,21b0]	AdditionalPatientHistory		LT	0<br>
[0010,21c0]	PregnancyStatus		US	0<br>
[0010,4000]	PatientComments		LT	0<br>
[0018,0022]	ScanOptions	AXIAL	CS	6<br>
[0018,0050]	SliceThickness	3	DS	2<br>
[0018,0060]	KVP	120	DS	4<br>
[0018,0090]	DataCollectionDiameter	500	DS	4<br>
[0018,1020]	SoftwareVersions	2.3.0	LO	6<br>
[0018,1030]	ProtocolName	Brain C-/Head	LO	14<br>
[0018,1100]	ReconstructionDiameter	250	DS	4<br>
[0018,1120]	GantryDetectorTilt	0	DS	2<br>
[0018,1130]	TableHeight	185	DS	4<br>
[0018,1140]	RotationDirection	CW	CS	2<br>
[0018,1143]	ScanArc	360	DS	4<br>
[0018,1150]	ExposureTime	1500	IS	4<br>
[0018,1151]	XRayTubeCurrent	333	IS	4<br>
[0018,1152]	Exposure	500	IS	4<br>
[0018,1160]	FilterType	D	SH	2<br>
[0018,1210]	ConvolutionKernel	D	SH	2<br>
[0018,5100]	PatientPosition	HFS	CS	4<br>
[0018,9321]	CTExposureSequence		SQ	96<br>
[fffe,e000]	Item		na	80<br>
[0018,9324]	EstimatedDoseSaving	0	FD	8<br>
[0018,9328]	ExposureTimeInms	1.5015015015015014	FD	8<br>
[0018,9330]	XRayTubeCurrentInmA	333	FD	8<br>
[0018,9332]	ExposureInmAs	500	FD	8<br>
[0018,9345]	CTDIvol	69.200000000000003	FD	8<br>
[0018,9323]	ExposureModulationType		CS	0<br>
[0018,9345]	CTDIvol	69.200000000000003	FD	8<br>
[0020,000d]	StudyInstanceUID	1906289110	UI	10<br>
[0020,000e]	SeriesInstanceUID	1.2.840.113704.1.111.2744.1561687837.23	UI	40<br>
[0020,0010]	StudyID	50431	SH	6<br>
[0020,0011]	SeriesNumber	7	IS	2<br>
[0020,0012]	AcquisitionNumber		IS	0<br>
[0020,0013]	InstanceNumber	41	IS	2<br>
[0020,0032]	ImagePositionPatient	[3] -141, -55, 1781.5	DS	16<br>
[0020,0037]	ImageOrientationPatient	[6] 1, 0, 0, 0, 1, 0	DS	12<br>
[0020,0052]	FrameOfReferenceUID	1.2.840.113704.1.111.2744.1561686959.5	UI	38<br>
[0020,0060]	Laterality		CS	0<br>
[0020,1040]	PositionReferenceIndicator		LO	0<br>
[0020,1041]	SliceLocation	1781.5	DS	6<br>
[0020,4000]	ImageComments	bone	LT	4<br>
[0028,0002]	SamplesPerPixel	1	US	2<br>
[0028,0004]	PhotometricInterpretation	MONOCHROME2	CS	12<br>
[0028,0010]	Rows	512	US	2<br>
[0028,0011]	Columns	512	US	2<br>
[0028,0030]	PixelSpacing	[2] 0.48828125, 0.48828125	DS	22<br>
[0028,0100]	BitsAllocated	16	US	2<br>
[0028,0101]	BitsStored	12	US	2<br>
[0028,0102]	HighBit	11	US	2<br>
[0028,0103]	PixelRepresentation	0	US	2<br>
[0028,1050]	WindowCenter	[2] 600, 600	DS	8<br>
[0028,1051]	WindowWidth	[2] 1600, 1600	DS	10<br>
[0028,1052]	RescaleIntercept	-1024	DS	6<br>
[0028,1053]	RescaleSlope	1	DS	2<br>
[0032,1032]	RequestingPhysician	PET-11909-2	PN	12<br>
[0032,1033]	RequestingService		LO	0<br>
[0032,1060]	RequestedProcedureDescription	PET-11909-2	LO	12<br>
[0032,1070]	RequestedContrastAgent		LO	0<br>
[0038,0010]	AdmissionID	PET-11909-2	LO	12<br>
[0038,0050]	SpecialNeeds		LO	0<br>
[0038,0500]	PatientState		LO	0<br>
[0040,0012]	PreMedication		LO	0<br>
[0040,0253]	PerformedProcedureStepID	5043144	SH	8<br>
[0040,0275]	RequestAttributesSequence		SQ	120<br>
[fffe,e000]	Item		na	104<br>
[0040,0007]	ScheduledProcedureStepDescription		LO	0<br>
[0040,0008]	ScheduledProtocolCodeSequence		SQ	40<br>
[fffe,e000]	Item		na	24<br>
[0008,0100]	CodeValue		SH	0<br>
[0008,0102]	CodingSchemeDesignator		SH	0<br>
[0008,0104]	CodeMeaning		LO	0<br>
[0040,0009]	ScheduledProcedureStepID	PET-11909-2	SH	12<br>
[0040,1001]	RequestedProcedureID	PET-11909-2	SH	12<br>
[00e1,0010]	PrivateCreator	ELSCINT1	LO	8<br>
[00e1,1001]	DataDictionaryVersion	1	US	2<br>
[00e1,1022]	Unknown	[2] 0, 0	DS	4<br>
[00e1,1023]	Unknown	[2] 1, 1	DS	4<br>
[00e1,103f]	Unknown Tag &amp; Data	PETCT	CS	6<br>
[00e1,1040]	OffsetFromCTMRImages	bone	SH	4<br>
[00e1,1042]	Unknown Tag &amp; Data		LO	0<br>
[00e1,1061]	Unknown Tag &amp; Data	LYPET_Multi_1002_usr.proc	LO	26<br>
[00e1,1063]	Unknown Tag &amp; Data	CHINESE	SH	8<br>
[00e1,10c2]	Unknown Tag &amp; Data	1.2.840.113704.1.111.2728.1561687754.64	UI	40<br>
[01f1,0010]	PrivateCreator	ELSCINT1	LO	8<br>
[01f1,1001]	Unknown Tag &amp; Data	SLICES	CS	6<br>
[01f1,1002]	Unknown Tag &amp; Data	STANDARD	CS	8<br>
[01f1,1003]	Unknown Tag &amp; Data	FUSED	CS	6<br>
[01f1,1004]	Unknown Tag &amp; Data	HIGH	CS	4<br>
[01f1,1008]	Unknown Tag &amp; Data	168	DS	4<br>
[01f1,100a]	Unknown Tag &amp; Data	0	US	2<br>
[01f1,100c]	Unknown Tag &amp; Data	[2] 0, 0.064000003	DS	14<br>
[01f1,100d]	Unknown Tag &amp; Data	0	DS	2<br>
[01f1,100e]	Unknown Tag &amp; Data	0	FL	4<br>
[01f1,1027]	Unknown Tag &amp; Data	1.5	DS	4<br>
[01f1,1028]	Unknown Tag &amp; Data	24	DS	2<br>
[01f1,1030]	Unknown Tag &amp; Data	8	US	2<br>
[01f1,1032]	Unknown Tag &amp; Data	RIGHT_ON_LEFT	CS	14<br>
[01f1,1033]	Unknown Tag &amp; Data	3.3	DS	4<br>
[01f1,1042]	Unknown Tag &amp; Data	No	SH	2<br>
[01f1,1044]	Unknown Tag &amp; Data	aaaa	OW	644<br>
[01f1,1046]	Unknown Tag &amp; Data	1.5	FL	4<br>
[01f1,1047]	Unknown Tag &amp; Data	2D	SH	2<br>
[01f1,1049]	Unknown Tag &amp; Data	500	DS	4<br>
[01f1,104a]	Unknown Tag &amp; Data	NONE	SH	4<br>
[01f1,104b]	Unknown Tag &amp; Data	16x1.5	SH	6<br>
[01f1,104c]	Unknown Tag &amp; Data	NO	SH	2<br>
[01f1,104d]	Unknown Tag &amp; Data	NO	SH	2<br>
[01f1,104e]	Unknown Tag &amp; Data	Brain	LO	6<br>
[01f7,0010]	PrivateCreator	ELSCINT1	LO	8<br>
[01f7,1010]	Unknown Tag &amp; Data	00	OB	2<br>
[01f7,1011]	Unknown Tag &amp; Data	7c93	OW	488<br>
[01f7,1013]	Unknown Tag &amp; Data	3a43	OW	136<br>
[01f7,1014]	Unknown Tag &amp; Data	0000	OW	108<br>
[01f7,1015]	Unknown Tag &amp; Data	02a0	OW	188<br>
[01f7,1016]	Unknown Tag &amp; Data	772c	OW	40<br>
[01f7,1017]	Unknown Tag &amp; Data	0000	OW	8<br>
[01f7,1018]	Unknown Tag &amp; Data	0000	OW	228<br>
[01f7,1019]	Unknown Tag &amp; Data	0000	OW	2160<br>
[01f7,101a]	Unknown Tag &amp; Data	0000	OW	28<br>
[01f7,101b]	Unknown Tag &amp; Data	02a0	OW	1272<br>
[01f7,101c]	Unknown Tag &amp; Data	0001	OW	116<br>
[01f7,101e]	Unknown Tag &amp; Data	0000	OW	364<br>
[01f7,101f]	Unknown Tag &amp; Data	0000	OW	148<br>
[01f7,1022]	Unknown Tag &amp; Data	1.2.840.113704.1.111.2744.1561687837.19.1111.111111111111111	UI	60<br>
[01f7,1023]	Unknown Tag &amp; Data	0016	OW	4<br>
[01f7,1025]	Unknown Tag &amp; Data	0005	OW	12<br>
[01f7,1026]	Unknown Tag &amp; Data	f22d	OW	13076<br>
[01f7,1027]	Unknown Tag &amp; Data	c000	OW	36<br>
[01f7,1029]	Unknown Tag &amp; Data	4000	OW	440<br>
[01f7,102b]	Unknown Tag &amp; Data	0008	OW	36<br>
[01f7,102c]	Unknown Tag &amp; Data	0000	OW	656<br>
[01f7,102d]	Unknown Tag &amp; Data	0000	OW	8<br>
[01f7,102e]	Unknown Tag &amp; Data	0100	OW	128<br>
[01f7,1030]	Unknown Tag &amp; Data	0000	OW	16<br>
[01f7,1070]	Unknown Tag &amp; Data	0001	OW	584<br>
[01f7,1074]	Unknown Tag &amp; Data	0000	OW	288<br>
[01f7,1075]	Unknown Tag &amp; Data	0001	OW	136<br>
[07a1,0010]	PrivateCreator	ELSCINT1	LO	8<br>
[07a1,100a]	Unknown Tag &amp; Data	1e	OB	282228<br>
[07a1,1010]	Unknown Tag &amp; Data	3.5	LO	4<br>
[07a1,1011]	Unknown Tag &amp; Data	PMSCT_RLE1	CS	10<br>
[7fdf,0010]	PrivateCreator	ELSCINT1	LO	8<br>
[fffc,fffc]	DataSetTrailingPadding	00	OB	392</p>

---

## Post #2 by @hu_shuang (2019-08-24 14:37 UTC)

<p>Operating system: Mac Os<br>
Slicer version:4.10.2<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77246725be59c2e46910a2489e93c90d963c18f2.png" alt="37%20PM" data-base62-sha1="gZYOkRwRldmDF5EZVBW9vqzJisq" width="404" height="164"><br>
Expected behavior: load pet/ct data<br>
Actual behavior: return as  “Could not load: 2: Body-Low Dose CT as a Scalar Volume”<br>
The pet/ct data is from Philips Gemini</p>

---

## Post #3 by @issakomi (2019-08-26 09:49 UTC)

<p>The series are in private <em>Elscint</em> format with private transfer syntax <em>CT-private-ELE</em>, pixel data is in private data element, also compression in private <em>PMSCT_RLE1</em>. AFAIK, they shouldn’t leave Philips infrastructure, workstations can export files in standard DICOM for interchange, but from time to time they appear here and there. You can download converted files <a href="https://drive.google.com/file/d/18Io4AYoI-4TIRgmeJCIQUE5qMbyXnpKT/view?usp=sharing" rel="nofollow noopener">here</a>. Please let me know if you have downloaded the files, they seems to be not anonymized and i’ll delete them after.<br>
Best regards</p>

---

## Post #4 by @hu_shuang (2019-08-27 01:51 UTC)

<p>thanks, issakomi. that’s very helpful, I am new to image processing and not familiar with format. I will ask the tech about how to get standard DICOM. Is there any easy method to convert all my data to DICOM as you did? I have a bunch of data. Although the files have the patient name, they can not be located with only names here. However, it’s better to make the data full anonymized. Thanks for your reminder.</p>

---

## Post #5 by @hu_shuang (2019-08-27 01:58 UTC)

<p>one more question, why SUV is missing after I load the converted data to 3d slicer? thank you.</p>

---

## Post #6 by @issakomi (2019-08-27 09:27 UTC)

<blockquote>
<p>Is there any easy method to convert all my data to DICOM as you did?</p>
</blockquote>
<p>There is <a href="https://github.com/malaterre/GDCM/blob/master/Examples/Cxx/rle2img.cxx" rel="noopener nofollow ugc">rle2img.cxx</a> example in GDCM’s Examples folder, i took it as starting point some time ago, but IMHO it seems to be broken after last commit at 19 May.</p>
<blockquote>
<p>However, it’s better to make the data full anonymized.</p>
</blockquote>
<p>One tip - if you will anonymize files - better don’t modify dates/time for PET series, if possible. If possible also preserving UIDs were good, but it is your decision, of course.<br>
It is very easy to break PET series.</p>
<blockquote>
<p>one more question, why SUV is missing after I load the converted data to 3d slicer? thank you.</p>
</blockquote>
<p>The units in PET series are BQML (s. tag 0x0054, 0x1001), AFAIK SUV have to be calculated first. S. pdf files <a href="https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)" rel="noopener nofollow ugc">here</a>. That conversion extracted pixel data from private data element and put it into standard data element (0x7fe0,0x0010) and set transfer syntax appropriately, all the rest incl. private tags is not modified, should be OK, but i can not guarantee, this is reverse-engineered stuff. BTW, i was able to create SUV from that PET series.</p>
<blockquote>
<p>I have a bunch of data.</p>
</blockquote>
<p>I could convert more series, if you like, it is anyway already done.<br>
BTW, i am looking for example of Elscint files with <em>PMSCT_RGB1</em> compression.</p>
<p>Best regards</p>

---

## Post #7 by @lassoan (2019-08-27 13:45 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> It would be nice if you could implement a DICOM reader plugin for this image type. You can use either Python or C++. If you are interested in this then let us know and we can give pointers to where to start.</p>

---

## Post #8 by @Chris_Rorden (2019-08-27 16:10 UTC)

<p>This compression scheme is handled by the upcoming dcm2niix. Therefore, one can convert these with the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerDcm2nii" rel="nofollow noopener">SlicerDcm2nii extension</a>. You can test this out already by using the <a href="https://github.com/rordenlab/dcm2niix/tree/development" rel="nofollow noopener">developmental branch</a> of dcm2niix.</p>

---

## Post #9 by @issakomi (2019-08-27 17:27 UTC)

<blockquote>
<p>However, it’s better to make the data full anonymized.</p>
</blockquote>
<p>Again about de-identify and <strong>PET</strong>. I would recommend to use following options<br>
from <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#table_E.1-1" rel="noopener nofollow ugc">PS3.15 Table E.1-1. Application Level Confidentiality Profile Attributes</a></p>
<p><em>Rtn. Safe Priv. Opt.</em> (PET related attributes are often private)<br>
<em>Rtn. Pat. Chars. Opt.</em> (Patient Weight is important)<br>
<em>Rtn. Long. Full Dates Opt.</em> or <em>Rtn. Long. Modif. Dates Opt</em> (better 1st, retain full, even smallest error will break things)<br>
<em>Rtn. UIDs Opt.</em> (Frame of Reference UID may be important for fusion later)</p>
<p>or just hide name, birth date, institution, etc., if possible</p>

---

## Post #10 by @Chris_Rorden (2019-08-27 19:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> this is a very simple but not very effective compression format. The <a href="https://github.com/malaterre/GDCM/blob/a923f206060e85e8d81add565ae1b9dd7b210481/Examples/Cxx/rle2img.cxx" rel="nofollow noopener">GDCM C++ code is here</a>, or if you prefer the <a href="https://github.com/rordenlab/dcm2niix/blob/master/console/nii_dicom.cpp" rel="nofollow noopener">dcm2niix C function nii_loadImgPMSCT_RLE1() is here</a>. Both are based on the BSD License.</p>

---

## Post #11 by @hu_shuang (2019-08-28 03:05 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> thanks for your reply,  the information very helpful.<br>
There are around 350 datasets to be converted, so it’s better for me to do it offline, I am very fresh to coding,  AKA. layman, I don’t know how to employ pure coding yet. Could the convert to be done by click some kind of button or special software?  all my data are in the same format as I uploaded before.<br>
For SUV part, I will study the files you direct. Honestly, it is a lot for me to digest, but I’d like to try.  So glad to learn new things.<br>
PS. I am a radiologist lack of engineering background.</p>

---
