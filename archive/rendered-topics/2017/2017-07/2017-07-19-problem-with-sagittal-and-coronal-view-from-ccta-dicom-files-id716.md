# Problem with sagittal and coronal view from CCTA DICOM files

**Topic ID**: 716
**Date**: 2017-07-19
**URL**: https://discourse.slicer.org/t/problem-with-sagittal-and-coronal-view-from-ccta-dicom-files/716

---

## Post #1 by @Young_Jin_Youn (2017-07-19 12:23 UTC)

<p>Hi?<br>
I’ve loaded DICOM images acquired from CCTA.<br>
As you can see below images, sagittal and coronal views look like compressed (not real thickness) when using 3D slicing. But those views are normal when using InVesalius.<br>
Please let me know how to solve this problem.<br>
Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/095f618b76fe385f29549438521d8e00d984a34c.JPG" data-download-href="/uploads/short-url/1kUEjcL3WFGfMR0cgT4JYox2YbO.JPG?dl=1" title="슬라이드2.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/095f618b76fe385f29549438521d8e00d984a34c_2_690x388.JPG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/095f618b76fe385f29549438521d8e00d984a34c_2_690x388.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/095f618b76fe385f29549438521d8e00d984a34c_2_1035x582.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/095f618b76fe385f29549438521d8e00d984a34c.jpeg 2x" data-dominant-color="3F453F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">슬라이드2.JPG</span><span class="informations">1280×720 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/307e176e1ca00ed14b650ec6b7edbd0fb90ea1ba.JPG" data-download-href="/uploads/short-url/6UZ4f1Kh2wopVyeK4eLnfDFYEFs.JPG?dl=1" title="슬라이드1.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/307e176e1ca00ed14b650ec6b7edbd0fb90ea1ba_2_690x388.JPG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/307e176e1ca00ed14b650ec6b7edbd0fb90ea1ba_2_690x388.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/307e176e1ca00ed14b650ec6b7edbd0fb90ea1ba_2_1035x582.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/307e176e1ca00ed14b650ec6b7edbd0fb90ea1ba.jpeg 2x" data-dominant-color="7B7E7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">슬라이드1.JPG</span><span class="informations">1280×720 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-07-19 12:58 UTC)

<p>Thanks for reporting this.</p>
<p>Could you please try if the image is loaded correctly in the latest <strong>nightly</strong> version of Slicer?</p>
<p>If it does not work, could you give additional information:</p>
<ul>
<li>How did you load the image: by importing it into the DICOM database and load it from the DICOM browser / using the Data dialog?</li>
<li>What scanner acquired the image?</li>
</ul>

---

## Post #3 by @pieper (2017-07-19 13:07 UTC)

<p>Also refer to the techniques listed here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #4 by @Young_Jin_Youn (2017-07-20 02:02 UTC)

<p>Thanks for replying.<br>
I’ve tried this with the latest nightly version of 3D Slicer. But it showed same phenomena.<br>
I’ve loaded DICOM images using the Botton shaped [DCM] (Raise the DICOM module…) and then import button.  I tried this by ‘copy’ and by ‘add link’.<br>
I don’t understand your last question ‘What scanner…’. Do you mean product name of CT scanner?<br>
I wish you can solve this problem.<br>
Thanks.</p>

---

## Post #5 by @Young_Jin_Youn (2017-07-20 02:02 UTC)

<p>Thank you. I’ll check this.</p>

---

## Post #6 by @lassoan (2017-07-20 02:11 UTC)

<aside class="quote no-group" data-username="Young_Jin_Youn" data-post="4" data-topic="716">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/977dab/48.png" class="avatar"> Young_Jin_Youn:</div>
<blockquote>
<p>Do you mean product name of CT scanner?</p>
</blockquote>
</aside>
<p>Yes, what brand and model? Some scanner models known to have DICOM conformance problems and older other scanners often used varying slice spacing.</p>
<p>Do you get any warning about potential geometry issues when you load the image?</p>
<p>If you click on the Advanced option in the DICOM browser and click Examine, what is in the DICOM data column in the first line (that has a checked checkbox)?</p>

---

## Post #7 by @Young_Jin_Youn (2017-07-20 04:10 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="716" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="Young_Jin_Youn" data-post="4" data-topic="716">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/977dab/48.png" class="avatar"> Young_Jin_Youn:</div>
<blockquote>
<p>Do you mean product name of CT scanner?</p>
</blockquote>
</aside>
<p>Yes, what brand and model? Some scanner models known to have DICOM conformance problems and older other scanners often used varying slice spacing.</p>
<p>Do you get any warning about potential geometry issues when you load the image?</p>
<p>If you click on the Advanced option in the DICOM browser and click Examine, what is in the DICOM data column in the first line (that has a checked checkbox)?</p>
</blockquote>
</aside>
<p>Thank you, Mr. Andras Lasso.</p>
<p>I don’t know the exact brand and model. But probably from GE.<br>
During loading, I did not receive any warning sign.<br>
On the advanced option, the first column shows like this<br>
DICOM data: [v] 80656: AXI 75% 62-56-62<br>
Reader: Scalar Volume<br>
Warnings: none</p>

---

## Post #8 by @pieper (2017-07-20 12:58 UTC)

<p>Also you can use the “Metadata” button to look at the dicom headers.  There you can see the manufacturer and other useful information.</p>

---

## Post #9 by @lassoan (2017-07-20 13:19 UTC)

<p>To make it easier to share the metadata with us for analysis, I’ve added the option to copy the metadata to clipboard. Could you please download the latest nightly version of Slicer now (if you downloaded Slicer yesterday or before then it is too old, it does not contain this feature yet), and then:</p>
<ul>
<li>Open DICOM browser</li>
<li>Select the image that you want to load</li>
<li>Check Advanced checkbox</li>
<li>Click Examine button</li>
<li>Click Metadata button</li>
<li>Click Copy Metadata button</li>
<li>Paste the copied text to any text editor</li>
<li><strong>Remove patient name, birthdate, ID, and all other patient identifiable information</strong></li>
<li>Copy-paste the metadata here so that we can have a look</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/6a13a1c9c1838a8353e8ad4dc2381e087d0e08b9.png" data-download-href="/uploads/short-url/f8oFJMEVaDpf7bCacJOTwDNILUt.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6a13a1c9c1838a8353e8ad4dc2381e087d0e08b9_2_690x444.png" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6a13a1c9c1838a8353e8ad4dc2381e087d0e08b9_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6a13a1c9c1838a8353e8ad4dc2381e087d0e08b9_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6a13a1c9c1838a8353e8ad4dc2381e087d0e08b9_2_1380x888.png 2x" data-dominant-color="F3EFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">2982×1920 360 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @Young_Jin_Youn (2017-07-21 07:31 UTC)

<p>Thnaks, Mr. Iassoan.<br>
I paste the metadata.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/56750df3caf69caa86c40d59af98b54475ebf0f4.png" data-download-href="/uploads/short-url/ckPQJAReVj5SymWWDBwF5gSNh0o.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/56750df3caf69caa86c40d59af98b54475ebf0f4_2_568x500.png" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/56750df3caf69caa86c40d59af98b54475ebf0f4_2_568x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/56750df3caf69caa86c40d59af98b54475ebf0f4_2_852x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/56750df3caf69caa86c40d59af98b54475ebf0f4_2_1136x1000.png 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1628×1431 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>[0008,0005]	SpecificCharacterSet	ISO_IR 100	CS	10		<br>
[0008,0008]	ImageType	[3] DERIVED, SECONDARY, AQNETSC	CS	26		<br>
[0008,0012]	InstanceCreationDate	20170717	DA	8		<br>
[0008,0013]	InstanceCreationTime	143957	TM	6		<br>
[0008,0016]	SOPClassUID	1.2.840.10008.5.1.4.1.1.7	UI	26		<br>
[0008,0018]	SOPInstanceUID	2.16.840.1.113669.632.21.4079790272.20170717.364973997.0.97414.1	UI	64		<br>
[0008,0020]	StudyDate	20170717	DA	8		<br>
[0008,0021]	SeriesDate	20170717	DA	8		<br>
[0008,0022]	AcquisitionDate	20170717	DA	8		<br>
[0008,0030]	StudyTime	141020	TM	6		<br>
[0008,0031]	SeriesTime	143957	TM	6		<br>
[0008,0032]	AcquisitionTime	141827	TM	6		<br>
[0008,0050]	AccessionNumber	E20170086239	SH	12		<br>
[0008,0060]	Modality	CT	CS	2		<br>
[0008,0064]	ConversionType	WSD	CS	4		<br>
[0008,0070]	Manufacturer	Philips	LO	8		<br>
[0008,0080]	InstitutionName	*****************************	LO	20		<br>
[0008,0090]	ReferringPhysicianName	*****************************	PN	12		<br>
[0008,1010]	StationName	CT-95305	SH	8		<br>
[0008,1030]	StudyDescription	CT Cardiac Angiography[3D]	LO	26		<br>
[0008,1032]	ProcedureCodeSequence		SQ	82		<br>
[fffe,e000]	Item		na	66	<br>
[0008,0100]	CodeValue	2CGC05CAD	SH	10<br>
[0008,0102]	CodingSchemeDesignator	BROKER	SH	6<br>
[0008,0104]	CodeMeaning	CT Cardiac Angiography[3D]	LO	26<br>
[0008,103e]	SeriesDescription	HEART 75%	LO	10		<br>
[0008,1110]	ReferencedStudySequence		SQ	0		<br>
[0009,0000]	PrivateGroupLength	14	UL	4		<br>
[0009,0010]	PrivateCreator	GEIIS	LO	6		<br>
[0010,0010]	PatientName	*****************************	PN	12		<br>
[0010,0020]	PatientID	*****************************	LO	8		<br>
[0010,0021]	IssuerOfPatientID	*****************************	LO	24		<br>
[0010,0030]	PatientBirthDate	*****************************	DA	8		<br>
[0010,0040]	PatientSex	*****************************	CS	2		<br>
[0010,1040]	PatientAddress	ì ìë¡14 2	LO	14		<br>
[0018,1012]	DateOfSecondaryCapture	20170717	DA	8		<br>
[0018,1014]	TimeOfSecondaryCapture	143957	TM	6		<br>
[0018,1016]	SecondaryCaptureDeviceManufacturer	TERARECON	LO	10		<br>
[0018,1018]	SecondaryCaptureDeviceManufacturerModelName	AQNET	LO	6		<br>
[0018,1019]	SecondaryCaptureDeviceSoftwareVersions	V4.4.7.851	LO	10		<br>
[0018,1030]	ProtocolName	CARDIAC ANGIO/Cardiac	LO	22		<br>
[0018,5100]	PatientPosition	FFS	CS	4		<br>
[0020,000d]	StudyInstanceUID	1.2.840.113704.1.111.5572.1500268220.1	UI	38		<br>
[0020,000e]	SeriesInstanceUID	2.16.840.1.113669.2.1.1.47404864.54.20170717.636359002560781250	UI	64		<br>
[0020,0010]	StudyID	132221	SH	6		<br>
[0020,0011]	SeriesNumber	1031	IS	4		<br>
[0020,0013]	InstanceNumber	1	IS	2		<br>
[0020,0020]	PatientOrientation		CS	0		<br>
[0020,0060]	Laterality		CS	0		<br>
[0028,0002]	SamplesPerPixel	3	US	2		<br>
[0028,0004]	PhotometricInterpretation	RGB	CS	4		<br>
[0028,0006]	PlanarConfiguration	0	US	2		<br>
[0028,0008]	NumberOfFrames	1	IS	2		<br>
[0028,0010]	Rows	1024	US	2		<br>
[0028,0011]	Columns	1024	US	2		<br>
[0028,0030]	PixelSpacing	[2] 0.2588700056076, 0.2588700056076	DS	32		<br>
[0028,0100]	BitsAllocated	8	US	2		<br>
[0028,0101]	BitsStored	8	US	2		<br>
[0028,0102]	HighBit	7	US	2		<br>
[0028,0103]	PixelRepresentation	0	US	2		<br>
[0032,1033]	RequestingService	CAR	LO	4		<br>
[0040,0275]	RequestAttributesSequence		SQ	36		<br>
[fffe,e000]	Item		na	20	<br>
[0040,1001]	RequestedProcedureID	E20170086239	SH	12<br>
[0040,2017]	FillerOrderNumberImagingServiceRequest	RAD23	LO	6</p>

---

## Post #11 by @lassoan (2017-07-22 00:28 UTC)

<p>This image seems to be just a screenshot. Do you have multiple series in the series list (the list that has “SeriesNumber” as the first column)? Can you send the content (copied as text) for the other series as well? (don’t forget to remove patient information)</p>

---

## Post #12 by @Young_Jin_Youn (2017-07-27 12:13 UTC)

<p>Sorry for late response.<br>
I attach metadata of another patient underwent CCTA.<br>
I’ve checked this data set is consisted of multiple series.<br>
Thank your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e104b7528bcb95e7f7778e9cbd9b9945769ee3.png" data-download-href="/uploads/short-url/57oOiixuXfHYYuJNs7eFYlnVYe7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23e104b7528bcb95e7f7778e9cbd9b9945769ee3_2_189x500.png" alt="image" data-base62-sha1="57oOiixuXfHYYuJNs7eFYlnVYe7" width="189" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23e104b7528bcb95e7f7778e9cbd9b9945769ee3_2_189x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23e104b7528bcb95e7f7778e9cbd9b9945769ee3_2_283x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23e104b7528bcb95e7f7778e9cbd9b9945769ee3_2_378x1000.png 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1075×2839 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>[0008,0005]			SpecificCharacterSet	ISO_IR 100	CS	10<br>
[0008,0008]			ImageType	[3] DERIVED, SECONDARY, MIP	CS	22<br>
[0008,0012]			InstanceCreationDate	20161212	DA	8<br>
[0008,0013]			InstanceCreationTime	152552	TM	6<br>
[0008,0016]			SOPClassUID	1.2.840.10008.5.1.4.1.1.7	UI	26<br>
[0008,0018]			SOPInstanceUID	1.2.840.113704.7.1.1.8088.1481523952.312	UI	40<br>
[0008,0020]			StudyDate	20161212	DA	8<br>
[0008,0022]			AcquisitionDate	20161212	DA	8<br>
[0008,0023]			ContentDate	20161212	DA	8<br>
[0008,0030]			StudyTime	141200	TM	6<br>
[0008,0032]			AcquisitionTime	141628	TM	6<br>
[0008,0033]			ContentTime	141200	TM	6<br>
[0008,0050]			AccessionNumber	I20160141126	SH	12<br>
[0008,0060]			Modality	CT	CS	2<br>
[0008,0064]			ConversionType	WSD	CS	4<br>
[0008,0070]			Manufacturer	Philips	LO	8<br>
[0008,0080]			InstitutionName	InstitutionName	LO	20<br>
[0008,0081]			InstitutionAddress	InstitutionAddress	ST	6<br>
[0008,0090]			ReferringPhysicianName	ReferringPhysicianName	PN	14<br>
[0008,1010]			StationName	PHILIPS-705	SH	12<br>
[0008,1030]			StudyDescription	CT Cardiac Angiography[3D]	LO	26<br>
[0008,1032]			ProcedureCodeSequence		SQ	92<br>
[fffe,e000]		Item		na	76<br>
[0008,0100]	CodeValue	2CGC05CAD	SH	10<br>
[0008,0102]	CodingSchemeDesignator	GEIIS	SH	6<br>
[0008,0103]	CodingSchemeVersion	0	SH	2<br>
[0008,0104]	CodeMeaning	CT Cardiac Angiography[3D]	LO	26<br>
[0008,103e]			SeriesDescription	AXI  75%  74-66-68	LO	18<br>
[0008,1040]			InstitutionalDepartmentName	Radiology	LO	10<br>
[0008,1070]			OperatorsName	HHH	PN	4<br>
[0008,1090]			ManufacturerModelName	Brilliance 64	LO	14<br>
[0009,0000]			PrivateGroupLength	14	UL	4<br>
[0009,0010]			PrivateCreator	GEIIS	LO	6<br>
[0010,0010]			PatientName	PatientName	PN	12<br>
[0010,0020]			PatientID	PatientID	LO	8<br>
[0010,0021]			IssuerOfPatientID	WONJU CHRISTIAN HOSPITAL	LO	24<br>
[0010,0030]			PatientBirthDate	19620218	DA	8<br>
[0010,0040]			PatientSex	PatientSex	CS	2<br>
[0010,1010]			PatientAge	PatientAge	AS	4<br>
[0010,1040]			PatientAddress	ìía101-	LO	12<br>
[0018,0010]			ContrastBolusAgent	CONTRAST	LO	8<br>
[0018,0022]			ScanOptions	HELIX	CS	6<br>
[0018,0050]			SliceThickness	0.550000017	DS	12<br>
[0018,0060]			KVP	120	DS	4<br>
[0018,0090]			DataCollectionDiameter	500	DS	4<br>
[0018,1016]			SecondaryCaptureDeviceManufacturer	Philips	LO	8<br>
[0018,1018]			SecondaryCaptureDeviceManufacturerModelName	Brilliance64	LO	12<br>
[0018,1019]			SecondaryCaptureDeviceSoftwareVersions	3.5	LO	4<br>
[0018,1020]			SoftwareVersions	2.6.2	LO	6<br>
[0018,1030]			ProtocolName	CARDIAC ANGIO/Cardiac	LO	22<br>
[0018,1100]			ReconstructionDiameter	192	DS	4<br>
[0018,1120]			GantryDetectorTilt	0	DS	2<br>
[0018,1130]			TableHeight	85	DS	10<br>
[0018,1140]			RotationDirection	CW	CS	2<br>
[0018,1150]			ExposureTime	2100	IS	4<br>
[0018,1151]			XRayTubeCurrent	405	IS	4<br>
[0018,1152]			Exposure	850	IS	4<br>
[0018,1160]			FilterType	XCC	SH	4<br>
[0018,1210]			ConvolutionKernel	XCC	SH	4<br>
[0018,5100]			PatientPosition	FFS	CS	4<br>
[0020,000d]			StudyInstanceUID	1.2.840.113704.1.111.4756.1481519520.1	UI	38<br>
[0020,000e]			SeriesInstanceUID	1.2.840.113704.7.1.1.8088.1481523951.1	UI	38<br>
[0020,0010]			StudyID	125987	SH	6<br>
[0020,0011]			SeriesNumber	80688	IS	6<br>
[0020,0012]			AcquisitionNumber		IS	0<br>
[0020,0013]			InstanceNumber	1	IS	2<br>
[0020,0020]			PatientOrientation		CS	0<br>
[0020,0032]			ImagePositionPatient	[3] -75, 30, 440.654903	DS	18<br>
[0020,0037]			ImageOrientationPatient	[6] 1, 0, 0, 0, 1, 0	DS	12<br>
[0020,1041]			SliceLocation	0	DS	2<br>
[0020,4000]			ImageComments	AXI  75%  74-66-68	LT	18<br>
[0028,0002]			SamplesPerPixel	1	US	2<br>
[0028,0004]			PhotometricInterpretation	MONOCHROME2	CS	12<br>
[0028,0010]			Rows	512	US	2<br>
[0028,0011]			Columns	512	US	2<br>
[0028,0030]			PixelSpacing	[2] 0.375, 0.375	DS	12<br>
[0028,0100]			BitsAllocated	16	US	2<br>
[0028,0101]			BitsStored	12	US	2<br>
[0028,0102]			HighBit	11	US	2<br>
[0028,0103]			PixelRepresentation	0	US	2<br>
[0028,1050]			WindowCenter	[2] 150, 150	DS	8<br>
[0028,1051]			WindowWidth	[2] 900, 900	DS	8<br>
[0028,1052]			RescaleIntercept	-1024	DS	6<br>
[0028,1053]			RescaleSlope	1	DS	2<br>
[0032,1033]			RequestingService	CAR	LO	4<br>
[0040,0012]			PreMedication		LO	0<br>
[0040,0253]			PerformedProcedureStepID	12598756	SH	8<br>
[0040,0254]			PerformedProcedureStepDescription	CT Cardiac Angiography[3D]	LO	26<br>
[0040,0275]			RequestAttributesSequence		SQ	36<br>
[fffe,e000]	Item		na	20<br>
[0040,1001]	RequestedProcedureID	I20160141126	SH	12<br>
[0040,2017]			FillerOrderNumberImagingServiceRequest	RAD24	LO	6<br>
[0040,3001]			ConfidentialityConstraintOnPatientDataDescription		LO	0<br>
[0088,0200]			IconImageSequence		SQ	16498<br>
[fffe,e000]	Item		na	16482<br>
[0028,0002]	SamplesPerPixel	1	US	2<br>
[0028,0004]	PhotometricInterpretation	MONOCHROME2	CS	12<br>
[0028,0010]	Rows	128	US	2<br>
[0028,0011]	Columns	128	US	2<br>
[0028,0100]	BitsAllocated	8	US	2<br>
[0028,0101]	BitsStored	8	US	2<br>
[0028,0102]	HighBit	7	US	2<br>
[0028,0103]	PixelRepresentation	0	US	2<br>
[7fe0,0010]	PixelData	0	OW	16384<br>
[00e1,0010]			PrivateCreator	ELSCINT1	LO	8<br>
[00e1,1014]			Unknown	N	CS	2<br>
[00e1,1022]			Unknown	[2] 0, 0	DS	4<br>
[00e1,1023]			Unknown	[2] 1, 1	DS	4<br>
[00e1,1040]			OffsetFromCTMRImages	AXI  75%  74-66-68	SH	18<br>
[07a1,0010]			PrivateCreator	ELSCINT1	LO	8<br>
[07a1,1010]			Unknown Tag &amp; Data	3.5	LO	4<br>
[0903,0010]			PrivateCreator	GEIIS PACS	LO	10<br>
[0903,1010]			Unknown Tag &amp; Data	0	US	2<br>
[0903,1011]			Unknown Tag &amp; Data	0	US	2<br>
[0903,1012]			Unknown Tag &amp; Data	0	US	2<br>
[0905,0010]			PrivateCreator	GEIIS	LO	6<br>
[0905,1030]			Unknown Tag &amp; Data	WONJU CHRISTIAN HOSPITAL	LO	24<br>
[3109,0010]			PrivateCreator	Applicare/RadWorks/Version 5.0	LO	30<br>
[3109,0011]			PrivateCreator	Applicare/RadWorks/Version 6.0/Summary	LO	38<br>
[3109,1002]			Unknown Tag &amp; Data	NEW	SH	4<br>
[3109,1008]			Unknown Tag &amp; Data	192.168.1.176	LO	14<br>
[3109,100a]			Unknown Tag &amp; Data	20170727	DA	8<br>
[3109,100b]			Unknown Tag &amp; Data	203911	TM	6<br>
[3109,1112]			Unknown Tag &amp; Data	GEPACS	ST	6<br>
[7fd1,0000]			PrivateGroupLength	26	UL	4<br>
[7fd1,0010]			PrivateCreator	GEIIS	LO	6<br>
[7fd1,1010]			Unknown Tag &amp; Data	0	UL	4<br>
[7fe0,0000]			GenericGroupLength	524300	UL	4<br>
[7fe0,0010]			PixelData	0	OW	524288</p>

---

## Post #13 by @lassoan (2017-07-27 17:16 UTC)

<p>Thank you for the information. I’ve added more metadata query capability to Slicer so that I can investigate your issue. Please install the latest nightly version of Slicer and follow these steps:</p>
<ul>
<li>Open DICOM browser</li>
<li>Click on the patient</li>
<li>Check <code>Advanced</code> checkbox</li>
<li>Click `Metadata button</li>
<li>Enter <code>Image</code> in the search box</li>
<li>Click <code>Copy all files metadata</code> button to copy image position information on the clipboard</li>
<li>Paste it to an empty Excel sheet</li>
<li>Upload the Excel sheet to OneDrive, Dropbox, or any other file sharing service, and paste the link in your response (taking a screenshot of the sheet and attaching it is not enough, as only a small fraction of the data would be visible)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f71cba9670a1fc9af08c728e0bd6ca2fd08fe897.png" data-download-href="/uploads/short-url/qGLkp04H6A2PWLM3I06UevTMjU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f71cba9670a1fc9af08c728e0bd6ca2fd08fe897.png" alt="image" data-base62-sha1="qGLkp04H6A2PWLM3I06UevTMjU" width="690" height="332" data-dominant-color="F7F5F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">846×408 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @Young_Jin_Youn (2017-08-02 23:01 UTC)

<p>Sorry for late response.<br>
Your latest nightly version 4.7.0 does not import any DICOM data.<br>
After completing SlicerApp-real process,<br>
DICOM Directory Import says<br>
Directory import complete<br>
0 new patients<br>
0 new studies<br>
0 new series<br>
0 new instances</p>
<p>I think this is another bug. Please check it. Thanks</p>

---

## Post #15 by @lassoan (2017-08-02 23:52 UTC)

<p>Please choose a writeable DICOM database directory (click on the double-arrow icon next to the Repair menu item at the top to see the directory selector) and then import the images again. If import fails then copy-paste the application log here (menu: File / Report a bug).</p>

---

## Post #16 by @Rasha (2017-08-03 00:57 UTC)

<p>It happens when you first instal the software. Try to restart your computer and try again. It should work.</p>
<p>Best Regards,<br>
Rasha</p>

---
