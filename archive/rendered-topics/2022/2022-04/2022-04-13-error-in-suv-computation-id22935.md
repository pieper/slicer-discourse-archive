---
topic_id: 22935
title: "Error In Suv Computation"
date: 2022-04-13
url: https://discourse.slicer.org/t/22935
---

# Error in SUV computation

**Topic ID**: 22935
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/error-in-suv-computation/22935

---

## Post #1 by @KateDelb (2022-04-13 12:23 UTC)

<p>I’m trying to compute SUV values for my FET-PET images, however it throws the following error:</p>
<pre><code class="lang-auto">Geometric issues were found with 1 of the series. Please use caution.

Traceback (most recent call last):
  File "C:\Users\kated\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 678, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examine(fileLists)
  File "C:/Users/kated/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py", line 127, in examine
    rwvmFile = self.generateRWVMforFileList(fileList)
  File "C:/Users/kated/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py", line 169, in generateRWVMforFileList
    raise RuntimeError("SUVFactorCalculator CLI did not complete cleanly")
RuntimeError: SUVFactorCalculator CLI did not complete cleanly
DICOM Plugin failed: SUVFactorCalculator CLI did not complete cleanly
Traceback (most recent call last):
  File "C:\Users\kated\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 678, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examine(fileLists)
  File "C:/Users/kated/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py", line 127, in examine
    rwvmFile = self.generateRWVMforFileList(fileList)
  File "C:/Users/kated/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py", line 169, in generateRWVMforFileList
    raise RuntimeError("SUVFactorCalculator CLI did not complete cleanly")
RuntimeError: SUVFactorCalculator CLI did not complete cleanly
DICOM Plugin failed: SUVFactorCalculator CLI did not complete cleanly
</code></pre>
<p>This issue seemed similar to <a href="https://discourse.slicer.org/t/unnamed-series-as-a-scalar-volume/22085/4" class="inline-onebox">Unnamed Series as a Scalar Volume - #4 by lassoan</a><br>
Here, the advice was to check that certain values in the metadata we’re not ruined by anonimization.<br>
However, I can’t find the following attributes in my metadata: injectedDose, patientWeight, , injectionTime, radionuclideHalfLife. I was wondering what I’m doing wrong here?</p>
<p>I obtain the metadata by right-clicking on the patient file → “View metadata”. The metadata looks as follows:</p>
<pre><code class="lang-auto">[0008,0005]	SpecificCharacterSet	ISO_IR 100	CS	10
[0008,0008]	ImageType	[2] ORIGINAL, PRIMARY	CS	16
[0008,0016]	SOPClassUID	1.2.840.10008.5.1.4.1.1.128	UI	28
[0008,0018]	SOPInstanceUID	1.2.19.99.170800	UI	16
[0008,0020]	StudyDate	20120327	DA	8
[0008,0021]	SeriesDate	20120327	DA	8
[0008,0022]	AcquisitionDate	20120327	DA	8
[0008,0023]	ContentDate	20120327	DA	8
[0008,0030]	StudyTime	125233.525000	TM	14
[0008,0031]	SeriesTime	131012.000000	TM	14
[0008,0032]	AcquisitionTime	133012.000000	TM	14
[0008,0033]	ContentTime	135930.000000	TM	14
[0008,0050]	AccessionNumber	A4766GLIMAS	SH	12
[0008,0060]	Modality	PT	CS	2
[0008,0070]	Manufacturer	Manu	LO	4
[0008,0080]	InstitutionName	Institute of Radiology	LO	22
[0008,0081]	InstitutionAddress	Dept of Radiology	ST	18
[0008,0090]	ReferringPhysicianName		PN	0
[0008,0092]	ReferringPhysicianAddress		ST	0
[0008,1010]	StationName	TOESTEL	SH	8
[0008,1030]	StudyDescription	TheStudy	LO	8
[0008,103e]	SeriesDescription	FET Brain Corr Sum 20-40 UHD	LO	28
[0008,1050]	PerformingPhysicianName		PN	0
[0008,1060]	NameOfPhysiciansReadingStudy		PN	0
[0008,1070]	OperatorsName		PN	0
[0008,1090]	ManufacturerModelName	model	LO	6
[0008,1110]	ReferencedStudySequence		SQ	98
	[fffe,e000]	Item		na	82
		[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.3.1.2.3.1	UI	24
		[0008,1155]	ReferencedSOPInstanceUID	1.3.51.0.1.1.140.140.21.70.2684395.2684374	UI	42
[0008,1120]	ReferencedPatientSequence		SQ	114
	[fffe,e000]	Item		na	98
		[0008,1150]	ReferencedSOPClassUID	1.2.840.10008.3.1.2.1.1	UI	24
		[0008,1155]	ReferencedSOPInstanceUID	1.2.124.113532.59449.13802.32934.20200805.164135.224473808	UI	58
[0008,1250]	RelatedSeriesSequence		SQ	392
	[fffe,e000]	Item		na	376
		[0020,000d]	StudyInstanceUID	1.3.51.0.1.1.140.140.21.70.2684395.2684374	UI	42
		[0020,000e]	SeriesInstanceUID	1.3.12.2.1107.5.1.4.31082.30000021051205564447000012755	UI	56
		[0040,a170]	PurposeOfReferenceCodeSequence		SQ	246
			[fffe,e000]	Item		na	100
				[0008,0100]	CodeValue	122401	SH	6
				[0008,0102]	CodingSchemeDesignator	DCM	SH	4
				[0008,0104]	CodeMeaning	Same Anatomy	LO	12
				[0008,0105]	MappingResource	DCMR	CS	4
				[0008,0106]	ContextGroupVersion	20030619000000.000000	DT	22
				[0008,010f]	ContextIdentifier	7210	CS	4
			[fffe,e000]	Item		na	114
				[0008,0100]	CodeValue	122403	SH	6
				[0008,0102]	CodingSchemeDesignator	DCM	SH	4
				[0008,0104]	CodeMeaning	For Attenuation Correction	LO	26
				[0008,0105]	MappingResource	DCMR	CS	4
				[0008,0106]	ContextGroupVersion	20030619000000.000000	DT	22
				[0008,010f]	ContextIdentifier	7210	CS	4
[0010,0010]	PatientName	PGLIMAS0001	PN	12
[0010,0020]	PatientID	PGLIMAS0001	LO	12
[0010,0021]	IssuerOfPatientID	UNKNOWN	LO	8
[0010,0030]	PatientBirthDate	19570119	DA	8
[0010,0032]	PatientBirthTime	000000.000000	TM	14
[0010,0040]	PatientSex	M	CS	2
[0010,1000]	RETIRED_OtherPatientIDs	""	LO	2
[0010,1001]	OtherPatientNames	""	PN	2
[0010,1080]	MilitaryRank	""	LO	2
[0010,21b0]	AdditionalPatientHistory	""	LT	2
[0018,0022]	ScanOptions	TEST	CS	4
[0018,0050]	SliceThickness	3	DS	2
[0018,1000]	DeviceSerialNumber	31082	LO	6
[0018,1020]	SoftwareVersions	TEST	LO	4
[0018,1181]	CollimatorType	NONE	CS	4
[0018,1200]	DateOfLastCalibration	[2] 20210512, 20210414	DA	18
[0018,1201]	TimeOfLastCalibration	[2] 063000.000000, 120434.000000	TM	28
[0018,1210]	ConvolutionKernel	XYZ Gauss2.00	SH	14
[0018,1242]	ActualFrameDuration	1200000	IS	8
[0018,1250]	ReceiveCoilName	Test	SH	4
[0018,5100]	PatientPosition	HFS	CS	4
[0020,000d]	StudyInstanceUID	1.3.51.0.1.1.140.140.21.70.2684395.2684374	UI	42
[0020,000e]	SeriesInstanceUID	1.3.12.2.1107.5.1.4.31082.30000021051207560011000006757	UI	56
[0020,0010]	StudyID	00000	SH	6
[0020,0011]	SeriesNumber	10	IS	2
[0020,0012]	AcquisitionNumber	2001	IS	4
[0020,0013]	InstanceNumber	1	IS	2
[0020,0032]	ImagePositionPatient	[3] -202.237, -400.857, -394.5	DS	24
[0020,0037]	ImageOrientationPatient	[6] 1, 0, 0, 0, 1, 0	DS	12
[0020,0052]	FrameOfReferenceUID	1.3.12.2.1107.5.1.4.31082.30000021051207031816500000026	UI	56
[0020,1040]	PositionReferenceIndicator		LO	0
[0020,1041]	SliceLocation	-394.5	DS	6
[0020,4000]	ImageComments	Frame 1 of 1^AC CT Brain  3.0  J30f	LT	36
[0028,0002]	SamplesPerPixel	1	US	2
[0028,0004]	PhotometricInterpretation	MONOCHROME2	CS	12
[0028,0010]	Rows	400	US	2
[0028,0011]	Columns	400	US	2
[0028,0030]	PixelSpacing	[2] 1.01821, 1.01821	DS	16
[0028,0051]	CorrectedImage	[6] NORM, DTIM, ATTN, SCAT, DECY, RAN	CS	28
[0028,0100]	BitsAllocated	16	US	2
[0028,0101]	BitsStored	16	US	2
[0028,0102]	HighBit	15	US	2
[0028,0103]	PixelRepresentation	0	US	2
[0028,0106]	SmallestImagePixelValue	0	US	2
[0028,0107]	LargestImagePixelValue	65535	US	2
[0028,1050]	WindowCenter	224	DS	4
[0028,1051]	WindowWidth	448	DS	4
[0028,1052]	RescaleIntercept	0	DS	2
[0028,1053]	RescaleSlope	0.00684244	DS	10
[0028,1054]	RescaleType	BQML	LO	4
[0032,000a]	RETIRED_StudyStatusID	COMPLETED	CS	10
[0032,000c]	RETIRED_StudyPriorityID	NORMAL	CS	6
[0032,1030]	RETIRED_ReasonForStudy	""	LO	2
[0032,1032]	RequestingPhysician		PN	0
[0032,1033]	RequestingService		LO	0
[0032,1060]	RequestedProcedureDescription	""	LO	2
[0032,4000]	RETIRED_StudyComments	""	LT	2
[0038,0300]	CurrentPatientLocation	Home	LO	4
[0040,0009]	ScheduledProcedureStepID	"         "	SH	12
[0040,0253]	PerformedProcedureStepID	""	SH	2
[0040,0254]	PerformedProcedureStepDescription	""	LO	2
[0040,1001]	RequestedProcedureID	"         "	SH	12
[0054,0013]	EnergyWindowRangeSequence		SQ	40
	[fffe,e000]	Item		na	24
		[0054,0014]	EnergyWindowLowerLimit	435	DS	4
		[0054,0015]	EnergyWindowUpperLimit	650	DS	4
[0054,0016]	RadiopharmaceuticalInformationSequence		SQ	420
	[fffe,e000]	Item		na	404
		[0018,0031]	Radiopharmaceutical	Fluorethyltyrosin	LO	18
		[0018,1072]	RadiopharmaceuticalStartTime	131001.000000	TM	14
		[0018,1074]	RadionuclideTotalDose	206000000	DS	10
		[0018,1075]	RadionuclideHalfLife	6586.2	DS	6
		[0018,1076]	RadionuclidePositronFraction	0.9673	DS	6
		[0018,1078]	RadiopharmaceuticalStartDateTime	20210512131001.000000	DT	22
		[0054,0300]	RadionuclideCodeSequence		SQ	118
			[fffe,e000]	Item		na	102
				[0008,0100]	CodeValue	C-111A1	SH	8
				[0008,0102]	CodingSchemeDesignator	SRT	SH	4
				[0008,0104]	CodeMeaning	^18^Fluorine	LO	12
				[0008,0105]	MappingResource	DCMR	CS	4
				[0008,0106]	ContextGroupVersion	20070625000000.000000	DT	22
				[0008,010f]	ContextIdentifier	4020	CS	4
		[0054,0304]	RadiopharmaceuticalCodeSequence		SQ	130
			[fffe,e000]	Item		na	114
				[0008,0100]	CodeValue	C-B07E0	SH	8
				[0008,0102]	CodingSchemeDesignator	SRT	SH	4
				[0008,0104]	CodeMeaning	Fluorethyltyrosin F^18^	LO	24
				[0008,0105]	MappingResource	DCMR	CS	4
				[0008,0106]	ContextGroupVersion	20070625000000.000000	DT	22
				[0008,010f]	ContextIdentifier	4021	CS	4
[0054,0081]	NumberOfSlices	74	US	2
[0054,0101]	NumberOfTimeSlices	1	US	2
[0054,0410]	PatientOrientationCodeSequence		SQ	244
	[fffe,e000]	Item		na	228
		[0008,0100]	CodeValue	F-10450	SH	8
		[0008,0102]	CodingSchemeDesignator	99SDM	SH	6
		[0008,0104]	CodeMeaning	recumbent	LO	10
		[0008,0105]	MappingResource	DCMR	CS	4
		[0008,0106]	ContextGroupVersion	20020904000000.000000	DT	22
		[0008,010f]	ContextIdentifier	19	CS	2
		[0054,0412]	PatientOrientationModifierCodeSequence		SQ	112
			[fffe,e000]	Item		na	96
				[0008,0100]	CodeValue	F-10340	SH	8
				[0008,0102]	CodingSchemeDesignator	99SDM	SH	6
				[0008,0104]	CodeMeaning	supine	LO	6
				[0008,0105]	MappingResource	DCMR	CS	4
				[0008,0106]	ContextGroupVersion	20020904000000.000000	DT	22
				[0008,010f]	ContextIdentifier	20	CS	2
[0054,0414]	PatientGantryRelationshipCodeSequence		SQ	116
	[fffe,e000]	Item		na	100
		[0008,0100]	CodeValue	F-10470	SH	8
		[0008,0102]	CodingSchemeDesignator	99SDM	SH	6
		[0008,0104]	CodeMeaning	headfirst	LO	10
		[0008,0105]	MappingResource	DCMR	CS	4
		[0008,0106]	ContextGroupVersion	20020904000000.000000	DT	22
		[0008,010f]	ContextIdentifier	21	CS	2
[0054,1000]	SeriesType	[2] DYNAMIC, IMAGE	CS	14
[0054,1001]	Units	BQML	CS	4
[0054,1002]	CountsSource	EMISSION	CS	8
[0054,1100]	RandomsCorrectionMethod	DLYD	CS	4
[0054,1101]	AttenuationCorrectionMethod	measured,AC CT Brain  3.0  J30f	LO	32
[0054,1102]	DecayCorrection	START	CS	6
[0054,1103]	ReconstructionMethod	PSF+TOF 5i21s	LO	14
[0054,1105]	ScatterCorrectionMethod	Model-based, relative scatter scaling	LO	38
[0054,1200]	AxialAcceptance	49	DS	2
[0054,1201]	AxialMash	[2] 5, 6	IS	4
[0054,1300]	FrameReferenceTime	1793686.2979257	DS	16
[0054,1321]	DecayFactor	1.20777	DS	8
[0054,1322]	DoseCalibrationFactor	33010000	DS	8
[0054,1323]	ScatterFractionFactor	0.257761	DS	8
[0054,1330]	ImageIndex	1	US	2
[7fe0,0010]	PixelData	0000	OW	320000
</code></pre>

---

## Post #2 by @lassoan (2022-04-13 21:16 UTC)

<aside class="quote no-group" data-username="KateDelb" data-post="1" data-topic="22935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katedelb/48/14981_2.png" class="avatar"> KateDelb:</div>
<blockquote>
<p>Geometric issues were found with 1 of the series. Please use caution.</p>
</blockquote>
</aside>
<p>This is just a warning. Details about it are found in the application log. It is probably not the reason for the SUV computation to fail.</p>
<p>Check out the application log if you find more information about why the SUV calculation fails.</p>

---

## Post #3 by @KateDelb (2022-07-16 16:48 UTC)

<p>Dear lassoan, the message showing up in the error log is the following:</p>
<pre><code class="lang-auto">Found CommandLine Module, target is  C:/Users/kated/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/cli-modules/SUVFactorCalculator.exe
ModuleType: CommandLineModule
SUV Factor Calculator command line: 

C:/Users/kated/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/cli-modules/SUVFactorCalculator.exe --returnparameterfile C:/Users/kated/AppData/Local/Temp/Slicer/15932_4vQba3y7PA.params --petDICOMPath C:/Users/kated/Jupyter/ThesisData/DCM_Files/PGLIMAS0009_20211214_111127221 --petSeriesInstanceUID 1.3.12.2.1107.5.1.4.31082.30000021051207560011000006757 --rwvmDICOMPath C:/Users/kated/Jupyter/ThesisData/DCM_Files/PGLIMAS0009_20211214_111127221 --seriesDescription PET SUV Factors --seriesNumber 1000 --instanceNumber "1" 

SUV Factor Calculator standard output:

saving numbers to C:/Users/kated/AppData/Local/Temp/Slicer/15932_4vQba3y7PA.params
</code></pre>
<p>But I can’t quite figure out what the error is from this?</p>

---
