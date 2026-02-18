# Error Loading MRI Files

**Topic ID**: 1473
**Date**: 2017-11-16
**URL**: https://discourse.slicer.org/t/error-loading-mri-files/1473

---

## Post #1 by @Jake_Simon (2017-11-16 18:59 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8/4.9<br>
Expected behavior: Be able to 3d model mri scan<br>
Actual behavior: Cant see the scans at all when loading</p>
<p>So I have tried using my own mri scans and a friend’s mri scans from 2 different imaging centers and the same error occurs. I am unable to load the series to make it a full image and then make into a 3d model as well. Other viewers work but I cant 3d render with those. What should I do? It says there is no pixel attributions every time i try to examine.</p>

---

## Post #2 by @Jake_Simon (2017-11-16 19:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/103899c4c66f65e74b7ec7bfe31cb8f3e2cb6f64.png" data-download-href="/uploads/short-url/2juUacqf6stevlmjvhr6kVjuGHO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/103899c4c66f65e74b7ec7bfe31cb8f3e2cb6f64_2_690x367.png" alt="image" data-base62-sha1="2juUacqf6stevlmjvhr6kVjuGHO" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/103899c4c66f65e74b7ec7bfe31cb8f3e2cb6f64_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/103899c4c66f65e74b7ec7bfe31cb8f3e2cb6f64_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/103899c4c66f65e74b7ec7bfe31cb8f3e2cb6f64_2_1380x734.png 2x" data-dominant-color="E9E9E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2048×1092 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How do I over come these errors?</p>

---

## Post #3 by @Jake_Simon (2017-11-16 19:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5e0834d36df376fd49e87806b8b8a933703c5b4.png" data-download-href="/uploads/short-url/wNAm9Pv7zcgzn2ktNedTUGDEJY8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5e0834d36df376fd49e87806b8b8a933703c5b4_2_690x367.png" alt="image" data-base62-sha1="wNAm9Pv7zcgzn2ktNedTUGDEJY8" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5e0834d36df376fd49e87806b8b8a933703c5b4_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5e0834d36df376fd49e87806b8b8a933703c5b4_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e5e0834d36df376fd49e87806b8b8a933703c5b4_2_1380x734.png 2x" data-dominant-color="9696AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2048×1092 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And when I try loading, this pops up.</p>

---

## Post #4 by @lassoan (2017-11-16 19:38 UTC)

<p>Does it load correctly if you select a single series (e.g., SeriesNumber 3, 4, 5, 6, 7, or 8 only) and click Load?</p>
<p>If you select a single series and click <code>Metadata</code> button, can you see a slider in the window that pops up? if yes, what is the range of the slider? (1 / …? displayed on the right side of the slider)<br>
Could you click on <code>Copy metadata</code> button and past the result here? Make sure to remove all patient identifiable information - name, birth date, patient ID, etc.</p>

---

## Post #5 by @Jake_Simon (2017-11-16 19:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdd2ee5fadf84f3cdfe8f149de714fae028016e8.png" data-download-href="/uploads/short-url/tmNNyFoWDbiD4SFnUDfg8pYaBoQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cdd2ee5fadf84f3cdfe8f149de714fae028016e8_2_690x367.png" alt="image" data-base62-sha1="tmNNyFoWDbiD4SFnUDfg8pYaBoQ" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cdd2ee5fadf84f3cdfe8f149de714fae028016e8_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cdd2ee5fadf84f3cdfe8f149de714fae028016e8_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cdd2ee5fadf84f3cdfe8f149de714fae028016e8_2_1380x734.png 2x" data-dominant-color="9E9EB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2048×1092 450 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>this is if i load 1 series. The pictures are blurry and when i scroll through it looks like rains is falling while only displaying a single picture.</p>

---

## Post #6 by @Jake_Simon (2017-11-16 19:54 UTC)

<p>[0008,0000]	GenericGroupLength	1406	UL	4<br>
[0008,0005]	SpecificCharacterSet	ISO_IR 100	CS	10<br>
[0008,0008]	ImageType	[5] DERIVED, PRIMARY, M, DIS2D, JP2K LOSSY 6:1	CS	38<br>
[0008,0012]	InstanceCreationDate	20170804	DA	8<br>
[0008,0013]	InstanceCreationTime	153202.562	TM	10<br>
[0008,0016]	SOPClassUID	1.2.840.10008.5.1.4.1.1.4	UI	26<br>
[0008,0018]	SOPInstanceUID	1.2.840.113837.225093149.20170804154425.3	UI	42<br>
[0008,0020]	StudyDate	20170804	DA	8<br>
[0008,0021]	SeriesDate	20170804	DA	8<br>
[0008,0022]	AcquisitionDate	20170804	DA	8<br>
[0008,0023]	ContentDate	20170804	DA	8<br>
[0008,0030]	StudyTime	152601.562	TM	10<br>
[0008,0031]	SeriesTime	153202.531	TM	10<br>
[0008,0032]	AcquisitionTime	152813.5875	TM	12<br>
[0008,0033]	ContentTime	153202.562	TM	10<br>
[0008,0050]	AccessionNumber	03303523	SH	8<br>
[0008,0060]	Modality	MR	CS	2<br>
[0008,0070]	Manufacturer		LO	0<br>
[0008,0080]	InstitutionName		LO	12<br>
[0008,0081]	InstitutionAddress		52<br>
[0008,0090]	ReferringPhysicianName		PN	18<br>
[0008,1010]	StationName	MRC31439	SH	8<br>
[0008,1030]	StudyDescription	MR SHOULDER WO DYE RIGHT	LO	24<br>
[0008,1032]	ProcedureCodeSequence		SQ	84<br>
[fffe,e000]	Item		na	68<br>
[0008,0100]	CodeValue	73221 SH R	SH	10<br>
[0008,0102]	CodingSchemeDesignator	73221 SH R	SH	10<br>
[0008,0104]	CodeMeaning	MR SHOULDER WO DYE RIGHT	LO	24<br>
[0008,103e]	SeriesDescription	pd_blade_FS_AX _320	LO	20<br>
[0008,1040]	InstitutionalDepartmentName	Clinic	LO	6<br>
[0008,1048]	PhysiciansOfRecord		PN	18<br>
[0008,1050]	PerformingPhysicianName		PN	0<br>
[0008,1070]	OperatorsName	RP	PN	2<br>
[0008,1090]	ManufacturerModelName	Espree	LO	6<br>
[0008,1110]	ReferencedStudySequence		SQ	94<br>
[fffe,e000]	Item		na	78<br>
[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.3.1.2.3.1	UI	24<br>
[0008,1155]	ReferencedSOPInstanceUID	1.2.840.113837.1592560075.1501881959.3	UI	38<br>
[0008,1120]	ReferencedPatientSequence		SQ	32<br>
[fffe,e000]	Item		na	16<br>
[0008,1150]	ReferencedSOPClassUID		UI	0<br>
[0008,1155]	ReferencedSOPInstanceUID		UI	0<br>
[0008,1140]	ReferencedImageSequence		SQ	330<br>
[fffe,e000]	Item		na	94<br>
[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.5.1.4.1.1.4	UI	26<br>
[0008,1155]	ReferencedSOPInstanceUID	1.3.12.2.1107.5.2.31.31439.2017080415271043912449763	UI	52<br>
[fffe,e000]	Item		na	94<br>
[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.5.1.4.1.1.4	UI	26<br>
[0008,1155]	ReferencedSOPInstanceUID	1.3.12.2.1107.5.2.31.31439.2017080415265594998349731	UI	52<br>
[fffe,e000]	Item		na	94<br>
[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.5.1.4.1.1.4	UI	26<br>
[0008,1155]	ReferencedSOPInstanceUID	1.3.12.2.1107.5.2.31.31439.2017080415263090299549720	UI	52<br>
[0008,2111]	DerivationDescription	LOSSY JPEG 2000 COMPRESSION 6:1 (AMICAS)	ST	40<br>
[0008,2112]	SourceImageSequence		SQ	110<br>
[fffe,e000]	Item		na	94<br>
[0008,0016]	SOPClassUID	1.2.840.10008.5.1.4.1.1.4	UI	26<br>
[0008,0018]	SOPInstanceUID	1.3.12.2.1107.5.2.31.31439.2017080415320196130550085	UI	52<br>
[0010,0000]	GenericGroupLength	210	UL	4<br>
[0010,0010]	PatientName		PN	14<br>
[0010,0020]	PatientID		LO	6<br>
[0010,0021]	IssuerOfPatientID		LO	4<br>
[0010,0030]	PatientBirthDate		DA	8<br>
[0010,0040]	PatientSex	F	CS	2<br>
[0010,1000]	RETIRED_OtherPatientIDs		LO	12<br>
[0010,1010]	PatientAge		AS	4<br>
[0010,1030]	PatientWeight		DS	14<br>
[0010,1040]	PatientAddress		36<br>
[0010,2154]	PatientTelephoneNumbers		SH	14<br>
[0010,21b0]	AdditionalPatientHistory		LT	0<br>
[0010,4000]	PatientComments		LT	0<br>
[0018,0000]	GenericGroupLength	426	UL	4<br>
[0018,0015]	BodyPartExamined	SHOULDER	CS	8<br>
[0018,0020]	ScanningSequence	SE	CS	2<br>
[0018,0021]	SequenceVariant	[3] SK, SP, OSP	CS	10<br>
[0018,0022]	ScanOptions	FS	CS	2<br>
[0018,0023]	MRAcquisitionType	2D	CS	2<br>
[0018,0024]	SequenceName	<em>tseB2d1_11	SH	12<br>
[0018,0025]	AngioFlag	N	CS	2<br>
[0018,0050]	SliceThickness	3	DS	2<br>
[0018,0080]	RepetitionTime	3000	DS	4<br>
[0018,0081]	EchoTime	48	DS	2<br>
[0018,0083]	NumberOfAverages	1	DS	2<br>
[0018,0084]	ImagingFrequency	63.653639	DS	10<br>
[0018,0085]	ImagedNucleus	1H	SH	2<br>
[0018,0086]	EchoNumbers	1	IS	2<br>
[0018,0087]	MagneticFieldStrength	1.5	DS	4<br>
[0018,0088]	SpacingBetweenSlices	3.75	DS	4<br>
[0018,0089]	NumberOfPhaseEncodingSteps	320	IS	4<br>
[0018,0091]	EchoTrainLength	11	IS	2<br>
[0018,0093]	PercentSampling	100	DS	4<br>
[0018,0094]	PercentPhaseFieldOfView	100	DS	4<br>
[0018,0095]	PixelBandwidth	260	DS	4<br>
[0018,1000]	DeviceSerialNumber	31439	LO	6<br>
[0018,1020]	SoftwareVersions	syngo MR B19	LO	12<br>
[0018,1030]	ProtocolName	pd_blade_FS_AX _320	LO	20<br>
[0018,1251]	TransmitCoilName	Body	SH	4<br>
[0018,1310]	AcquisitionMatrix	[4] 320, 0, 0, 320	US	8<br>
[0018,1312]	InPlanePhaseEncodingDirection	COL	CS	4<br>
[0018,1314]	FlipAngle	150	DS	4<br>
[0018,1315]	VariableFlipAngleFlag	N	CS	2<br>
[0018,1316]	SAR	1.1928163770324	DS	16<br>
[0018,1318]	dBdt	0	DS	2<br>
[0018,5100]	PatientPosition	HFS	CS	4<br>
[0019,0000]	PrivateGroupLength	216	UL	4<br>
[0019,0010]	PrivateCreator	SIEMENS MR HEADER	LO	18<br>
[0019,1008]	Unknown Tag &amp; Data	IMAGE NUM 4	CS	12<br>
[0019,1009]	Unknown Tag &amp; Data	1.0	LO	4<br>
[0019,100b]	Unknown Tag &amp; Data	225985	DS	6<br>
[0019,100f]	Unknown Tag &amp; Data	Fast	SH	4<br>
[0019,1011]	Unknown Tag &amp; Data	No	SH	2<br>
[0019,1012]	Unknown Tag &amp; Data	[3] 0, 0, -1231	SL	12<br>
[0019,1013]	Unknown Tag &amp; Data	[3] 0, 0, -1221	SL	12<br>
[0019,1014]	Unknown Tag &amp; Data	[3] 0, 0, 10	IS	6<br>
[0019,1015]	Unknown Tag &amp; Data	[3] -217.26391602000001, -64.745762830000004, -35.913135529999998	FD	24<br>
[0019,1016]	Unknown Tag &amp; Data	1.505	DS	6<br>
[0019,1017]	Unknown Tag &amp; Data	1	DS	2<br>
[0019,1018]	Unknown Tag &amp; Data	6000	IS	4<br>
[0020,0000]	GenericGroupLength	330	UL	4<br>
[0020,000d]	StudyInstanceUID	1.2.840.113837.3779700918.1501881959.2	UI	38<br>
[0020,000e]	SeriesInstanceUID	1.3.12.2.1107.5.2.31.31439.2017080415320180937050053.0.0.0	UI	58<br>
[0020,0010]	StudyID	yw0w6kooz	SH	10<br>
[0020,0011]	SeriesNumber	3	IS	2<br>
[0020,0012]	AcquisitionNumber	1	IS	2<br>
[0020,0013]	InstanceNumber	20	IS	2<br>
[0020,0032]	ImagePositionPatient	[3] -217.26391601563, -64.745762825012, -25.913135528564	DS	50<br>
[0020,0037]	ImageOrientationPatient	[6] 1, 0, 0, 0, 1, 0	DS	12<br>
[0020,0052]	FrameOfReferenceUID	1.3.12.2.1107.5.2.31.31439.2.20170804152601718.0.0.0	UI	52<br>
[0020,1040]	PositionReferenceIndicator		LO	0<br>
[0020,1041]	SliceLocation	-25.913135528564	DS	16<br>
[0023,0000]	PrivateGroupLength	198	UL	4<br>
[0023,0010]	PrivateCreator	AMICAS0	LO	8<br>
[0023,1001]	Unknown Tag &amp; Data	1.3.12.2.1107.5.2.31.31439.2017080415320196130550085	UI	52<br>
[0023,1008]	Unknown Tag &amp; Data	0	US	2<br>
[0023,1010]	Unknown Tag &amp; Data	1967	US	2<br>
[0023,1016]	Unknown Tag &amp; Data	0	SL	4<br>
[0023,1021]	Unknown Tag &amp; Data	1	US	2<br>
[0023,1022]	Unknown Tag &amp; Data	2902	UL	4<br>
[0023,1045]	Unknown Tag &amp; Data	3	US	2<br>
[0023,1054]	Unknown Tag &amp; Data	MRC31439\MGPACS2	ST	16<br>
[0023,1055]	Unknown Tag &amp; Data	RP	LO	2<br>
[0023,1065]	Unknown Tag &amp; Data	MergeHealthCare	LO	16<br>
[0028,0000]	GenericGroupLength	184	UL	4<br>
[0028,0002]	SamplesPerPixel	1	US	2<br>
[0028,0004]	PhotometricInterpretation	MONOCHROME2	CS	12<br>
[0028,0010]	Rows	320	US	2<br>
[0028,0011]	Columns	320	US	2<br>
[0028,0030]	PixelSpacing	[2] 0.5, 0.5	DS	8<br>
[0028,0100]	BitsAllocated	16	US	2<br>
[0028,0101]	BitsStored	12	US	2<br>
[0028,0102]	HighBit	11	US	2<br>
[0028,0103]	PixelRepresentation	0	US	2<br>
[0028,1050]	WindowCenter	442	DS	4<br>
[0028,1051]	WindowWidth	1087	DS	4<br>
[0028,1055]	WindowCenterWidthExplanation	Algo1	LO	6<br>
[0028,2110]	LossyImageCompression	01	CS	2<br>
[0028,2112]	LossyImageCompressionRatio	6	DS	2<br>
[0028,2114]	LossyImageCompressionMethod	ISO_15444_1	CS	12<br>
[0029,0000]	PrivateGroupLength	69898	UL	4<br>
[0029,0010]	PrivateCreator	SIEMENS CSA HEADER	LO	18<br>
[0029,0011]	PrivateCreator	SIEMENS MEDCOM HEADER2	LO	22<br>
[0029,1008]	CSAImageHeaderType	IMAGE NUM 4	CS	12<br>
[0029,1009]	CSAImageHeaderVersion	20170804	LO	8<br>
[0029,1010]	CSAImageHeaderInfo	53	OB	9468<br>
[0029,1018]	CSASeriesHeaderType	MR	CS	2<br>
[0029,1019]	CSASeriesHeaderVersion	20170804	LO	8<br>
[0029,1020]	CSASeriesHeaderInfo	53	OB	60276<br>
[0029,1160]	SeriesWorkflowStatus	com	LO	4<br>
[0032,0000]	GenericGroupLength	162	UL	4<br>
[0032,1032]	RequestingPhysician		PN	18<br>
[0032,1060]	RequestedProcedureDescription	MR SHOULDER WO DYE RIGHT	LO	24<br>
[0032,1064]	RequestedProcedureCodeSequence		SQ	84<br>
[fffe,e000]	Item		na	68<br>
[0008,0100]	CodeValue	73221 SH R	SH	10<br>
[0008,0102]	CodingSchemeDesignator	73221 SH R	SH	10<br>
[0008,0104]	CodeMeaning	MR SHOULDER WO DYE RIGHT	LO	24<br>
[0040,0000]	GenericGroupLength	292	UL	4<br>
[0040,0244]	PerformedProcedureStepStartDate	20170804	DA	8<br>
[0040,0245]	PerformedProcedureStepStartTime	152601.656	TM	10<br>
[0040,0253]	PerformedProcedureStepID	yw0w6kop0	SH	10<br>
[0040,0254]	PerformedProcedureStepDescription	MR SHOULDER WO DYE RIGHT	LO	24<br>
[0040,0275]	RequestAttributesSequence		SQ	184<br>
[fffe,e000]	Item		na	168<br>
[0040,0007]	ScheduledProcedureStepDescription	MR SHOULDER WO DYE RIGHT	LO	24<br>
[0040,0008]	ScheduledProtocolCodeSequence		SQ	84<br>
[fffe,e000]	Item		na	68<br>
[0008,0100]	CodeValue	73221 SH R	SH	10<br>
[0008,0102]	CodingSchemeDesignator	73221 SH R	SH	10<br>
[0008,0104]	CodeMeaning	MR SHOULDER WO DYE RIGHT	LO	24<br>
[0040,0009]	ScheduledProcedureStepID	yw0w6kop0	SH	10<br>
[0040,1001]	RequestedProcedureID	yw0w6kooz	SH	10<br>
[0051,0000]	PrivateGroupLength	220	UL	4<br>
[0051,0010]	PrivateCreator	SIEMENS MR HEADER	LO	18<br>
[0051,1008]	Unknown Tag &amp; Data	IMAGE NUM 4	CS	12<br>
[0051,1009]	Unknown Tag &amp; Data	1.0	LO	4<br>
[0051,100a]	Unknown Tag &amp; Data	TA 03:45	LO	8<br>
[0051,100b]	Unknown Tag &amp; Data	320</em>320	LO	8<br>
[0051,100c]	Unknown Tag &amp; Data	FoV 160*160	LO	12<br>
[0051,100d]	Unknown Tag &amp; Data	SP F25.9	SH	8<br>
[0051,100e]	Unknown Tag &amp; Data	Tra	LO	4<br>
[0051,100f]	Unknown Tag &amp; Data	C:SH	LO	4<br>
[0051,1012]	Unknown Tag &amp; Data	TP H10	SH	6<br>
[0051,1013]	Unknown Tag &amp; Data	+LPH	SH	4<br>
[0051,1016]	Unknown Tag &amp; Data	M/DIS2D	LO	8<br>
[0051,1017]	Unknown Tag &amp; Data	SL 3.0	SH	6<br>
[0051,1019]	Unknown Tag &amp; Data	A1/FS	LO	6<br>
[7fe0,0000]	GenericGroupLength	34126	UL	4<br>
[7fe0,0010]	PixelData		OB	0</p>

---

## Post #7 by @Jake_Simon (2017-11-16 19:55 UTC)

<p>1/20 sliders is the range of the sliders for a single series metadata</p>

---

## Post #8 by @lassoan (2017-11-16 20:07 UTC)

<aside class="quote no-group" data-username="Jake_Simon" data-post="6" data-topic="1473">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/2acd7d/48.png" class="avatar"> Jake_Simon:</div>
<blockquote>
<p>LOSSY JPEG 2000 COMPRESSION</p>
</blockquote>
</aside>
<p>Probably the issue is that the image is compressed.</p>
<p>Potential solutions:</p>
<ol>
<li>
<p>Set DICOM reader to GDCM and try to load again (menu: Edit/Application settings/DICOM/DICOM reader approach)</p>
</li>
<li>
<p>Download DCMTK toolkit and use <a href="http://support.dcmtk.org/docs/dcmdjpeg.html">dcmdjpeg</a> utility to decompress each file</p>
</li>
</ol>

---
