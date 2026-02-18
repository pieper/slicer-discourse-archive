# PatientName and rus language - trouble

**Topic ID**: 28870
**Date**: 2023-04-12
**URL**: https://discourse.slicer.org/t/patientname-and-rus-language-trouble/28870

---

## Post #1 by @corsag21 (2023-04-12 18:02 UTC)

<p>Hello. I have a problem. Many CT of russian patients have problem with PatientName.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8185da14a4b3d5f23140f7c16f37a2c4d3b44c9.png" data-download-href="/uploads/short-url/nZ2pWjShTVJMle9qPhz9hQgmbt7.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8185da14a4b3d5f23140f7c16f37a2c4d3b44c9_2_554x500.png" alt="Screenshot" data-base62-sha1="nZ2pWjShTVJMle9qPhz9hQgmbt7" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8185da14a4b3d5f23140f7c16f37a2c4d3b44c9_2_554x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8185da14a4b3d5f23140f7c16f37a2c4d3b44c9_2_831x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8185da14a4b3d5f23140f7c16f37a2c4d3b44c9_2_1108x1000.png 2x" data-dominant-color="303336"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1148×1036 66.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried to use Dicompatcher, but it didn’t help.<br>
I could find only one topic where one had problem with ??? in the patientname.</p>
<p><em>(link removed until it is confirmed that the files do not contain patient information)</em></p>
<p>Please help. What i am doing wrong? Thank you</p>

---

## Post #2 by @lassoan (2023-04-12 18:04 UTC)

<p>Thanks for reporting, we’ll investigate and let you know what we find.</p>

---

## Post #3 by @issakomi (2023-04-12 21:28 UTC)

<p>There is no 0x0008, 0x0005 attribute … but even worse, encoding is WINDOWS-1251. I have already seen such data set, with silent WINDOWS-1251 encoding.</p>

---

## Post #4 by @lassoan (2023-04-12 21:28 UTC)

<p>The DICOM files have multiple sever DICOM non-conformities. The most serious are:</p>
<ul>
<li>
<code>CharacterSet</code> is not saved in the file. It seems that the file uses Windows-1251 code page, which is not even a valid DICOM character set.</li>
<li>
<code>XRayTubeCurrent</code> field is stored incorrectly (it must be an integer value, the value is <code>4.1</code> - see <a href="http://dclunie.blogspot.com/2008/11/dicom-exposure-attribute-fiasco.html" class="inline-onebox">David Clunie's Blog: The DICOM Exposure attribute fiasco</a>)</li>
</ul>
<p>There are also some incorrectly generated UIDs.</p>
<p>I would recommend to contact your device manufacturer and report these errors.</p>
<p>That said, <a href="https://github.com/Slicer/Slicer/pull/6940">I’ve added two rules to the DICOM patcher that can fix the two serious issues</a>. It will be available in Slicer Preview Release that you download tomorrow or later. Enable <code>Fix invalid exposure tags</code> and <code>Specify character set</code> with <code>cp1251</code> parameter.</p>

---

## Post #5 by @corsag21 (2023-04-17 08:17 UTC)

<p>I installed and try to patchdicom. I had no effect. I can’t find " <code>Fix invalid exposure tags</code> and <code>Specify character set</code></p>
<details>
<summary>
screens</summary>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b4962018e9868a556575d2de7719b44e000b2d.png" data-download-href="/uploads/short-url/xls9CMzWCM0OzVxJD4O4VeS3YD3.png?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b4962018e9868a556575d2de7719b44e000b2d_2_571x500.png" alt="Screenshot_3" data-base62-sha1="xls9CMzWCM0OzVxJD4O4VeS3YD3" width="571" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b4962018e9868a556575d2de7719b44e000b2d_2_571x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b4962018e9868a556575d2de7719b44e000b2d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b4962018e9868a556575d2de7719b44e000b2d.png 2x" data-dominant-color="9E9D9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">832×728 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad1fd2edc2382d87046e040802f7dbe977a5aee5.png" data-download-href="/uploads/short-url/oHwMF1rdlDGhlqf0oyQfzLqYEK1.png?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1fd2edc2382d87046e040802f7dbe977a5aee5_2_690x387.png" alt="Screenshot_2" data-base62-sha1="oHwMF1rdlDGhlqf0oyQfzLqYEK1" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1fd2edc2382d87046e040802f7dbe977a5aee5_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1fd2edc2382d87046e040802f7dbe977a5aee5_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad1fd2edc2382d87046e040802f7dbe977a5aee5_2_1380x774.png 2x" data-dominant-color="E6E8EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1919×1079 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</details>
<details>
<summary>
meta data</summary>
<p>[0008,0005]	SpecificCharacterSet	ISO_IR 100	CS	10<br>
[0008,0008]	ImageType	[3] DERIVED, PRIMARY, AXIAL	CS	22<br>
[0008,0016]	SOPClassUID	1.2.840.10008.5.1.4.1.1.2	UI	26<br>
[0008,0018]	SOPInstanceUID	1.2.410.200034.0.70090325.2.67805.398636784.101129341053.1100001	UI	64<br>
[0008,0020]	StudyDate	20230325	DA	8<br>
[0008,0021]	SeriesDate	20230325	DA	8<br>
[0008,0022]	AcquisitionDate	20230325	DA	8<br>
[0008,0023]	ContentDate	20230325	DA	8<br>
[0008,0030]	StudyTime	111841	TM	6<br>
[0008,0031]	SeriesTime	112933	TM	6<br>
[0008,0032]	AcquisitionTime	111841	TM	6<br>
[0008,0033]	ContentTime	112933	TM	6<br>
[0008,0050]	AccessionNumber		SH	0<br>
[0008,0060]	Modality	CT	CS	2<br>
[0008,0064]	ConversionType	WSD	CS	4<br>
[0008,0070]	Manufacturer	INSTRUMENTARIUM DENTAL	LO	22<br>
[0008,0080]	InstitutionName		LO	0<br>
[0008,0090]	ReferringPhysicianName		PN	0<br>
[0008,1010]	StationName		SH	0<br>
[0008,1030]	StudyDescription		LO	0<br>
[0008,103e]	SeriesDescription		LO	0<br>
[0008,1090]	ManufacturerModelName	OP300	LO	6<br>
[0008,2111]	DerivationDescription	Lossy compression with JPEG baseline, IJG quality factor 90, compression ratio 8.2084	ST	86<br>
[0008,9215]	DerivationCodeSequence		SQ	82<br>
[fffe,e000]	Item		na	66<br>
[0008,0000]	GenericGroupLength	54	UL	4<br>
[0008,0100]	CodeValue	121327	SH	6<br>
[0008,0102]	CodingSchemeDesignator	DCM	SH	4<br>
[0008,0104]	CodeMeaning	Full fidelity image	LO	20<br>
[000d,0010]	PrivateCreator	INSTRU_PRIVATE_IDENT_CODE	LO	26<br>
[000d,1000]	Unknown Tag &amp; Data	3c	OB	3546<br>
[0010,0010]	PatientName	Ðîäèîíöåâ Òèõîí Ñåðãååâè÷	PN	26<br>
[0010,0020]	PatientID	20230325111505113	LO	18<br>
[0010,0030]	PatientBirthDate		DA	0<br>
[0010,0040]	PatientSex	M	CS	2<br>
[0010,1000]	RETIRED_OtherPatientIDs	[2] 20230325111505113, dcddfff7-130e-43c8-957f-50da556280be	LO	54<br>
[0010,1010]	PatientAge		AS	0<br>
[0010,1030]	PatientWeight		DS	0<br>
[0010,4000]	PatientComments		LT	0<br>
[0018,0010]	ContrastBolusAgent		LO	0<br>
[0018,0015]	BodyPartExamined	SKULL	CS	6<br>
[0018,0024]	SequenceName		SH	0<br>
[0018,0050]	SliceThickness	0.2	DS	4<br>
[0018,0060]	KVP	89.8	DS	4<br>
[0018,0080]	RepetitionTime		DS	0<br>
[0018,0081]	EchoTime		DS	0<br>
[0018,0082]	InversionTime		DS	0<br>
[0018,0086]	EchoNumbers		IS	0<br>
[0018,0087]	MagneticFieldStrength		DS	0<br>
[0018,0091]	EchoTrainLength		IS	0<br>
[0018,1000]	DeviceSerialNumber	IE1502974	LO	10<br>
[0018,1012]	DateOfSecondaryCapture	20230325	DA	8<br>
[0018,1014]	TimeOfSecondaryCapture	112933	TM	6<br>
[0018,1016]	SecondaryCaptureDeviceManufacturer	Cybermed	LO	8<br>
[0018,1018]	SecondaryCaptureDeviceManufacturerModelName	OnDemand3DDental	LO	16<br>
[0018,1019]	SecondaryCaptureDeviceSoftwareVersions	OnDemand3DDental 1.0.10.7462	LO	28<br>
[0018,1020]	SoftwareVersions	CLINIVIEW 10.2.6.3	LO	18<br>
[0018,1060]	TriggerTime		DS	0<br>
[0018,1072]	RadiopharmaceuticalStartTime		TM	0<br>
[0018,1074]	RadionuclideTotalDose		DS	0<br>
[0018,1075]	RadionuclideHalfLife		DS	0<br>
[0018,1150]	ExposureTime	6090	IS	4<br>
[0018,1151]	XRayTubeCurrent	10	IS	2<br>
[0018,5100]	PatientPosition	HFS	CS	4<br>
[0020,000d]	StudyInstanceUID	1.2.840.113999.1000.2661001714.1314593456.1804752983149512882	UI	62<br>
[0020,000e]	SeriesInstanceUID	2.25.164214306710492919561096765912768039318	UI	44<br>
[0020,0010]	StudyID		SH	0<br>
[0020,0011]	SeriesNumber	1053	IS	4<br>
[0020,0012]	AcquisitionNumber		IS	0<br>
[0020,0013]	InstanceNumber	1	IS	2<br>
[0020,0032]	ImagePositionPatient	[3] 0, 0, 0	DS	6<br>
[0020,0037]	ImageOrientationPatient		DS	0<br>
[0020,0052]	FrameOfReferenceUID	1.2.840.113999.2001.3925856420.1200917467.7140941661092038557	UI	62<br>
[0020,0060]	Laterality		CS	0<br>
[0020,1002]	ImagesInAcquisition	390	IS	4<br>
[0020,1040]	PositionReferenceIndicator		LO	0<br>
[0020,4000]	ImageComments		LT	0<br>
[0028,0002]	SamplesPerPixel	3	US	2<br>
[0028,0004]	PhotometricInterpretation	YBR_FULL	CS	8<br>
[0028,0006]	PlanarConfiguration	0	US	2<br>
[0028,0008]	NumberOfFrames	1	IS	2<br>
[0028,0010]	Rows	256	US	2<br>
[0028,0011]	Columns	256	US	2<br>
[0028,0030]	PixelSpacing	[2] 0, 0	DS	4<br>
[0028,0034]	PixelAspectRatio	[2] 1, 1	IS	4<br>
[0028,0100]	BitsAllocated	8	US	2<br>
[0028,0101]	BitsStored	8	US	2<br>
[0028,0102]	HighBit	7	US	2<br>
[0028,0103]	PixelRepresentation	0	US	2<br>
[0028,0301]	BurnedInAnnotation	NO	CS	2<br>
[0028,1050]	WindowCenter	128	DS	4<br>
[0028,1051]	WindowWidth	255	DS	4<br>
[0028,1052]	RescaleIntercept	0.000000	DS	8<br>
[0028,1053]	RescaleSlope	1.000000	DS	8<br>
[0028,1054]	RescaleType	US	LO	2<br>
[0028,2110]	LossyImageCompression	01	CS	2<br>
[0028,2112]	LossyImageCompressionRatio	8.2084	DS	6<br>
[0028,2114]	LossyImageCompressionMethod	ISO_10918_1	CS	12<br>
[0054,1102]	DecayCorrection		CS	0<br>
[2050,0020]	PresentationLUTShape	IDENTITY	CS	8<br>
[3006,0024]	ReferencedFrameOfReferenceUID		UI	0<br>
[7573,0010]	PrivateCreator	CYBERMED	LO	8<br>
[7573,1000]	Unknown Tag &amp; Data	CYBERMED_OnDemand3D_PrivateTag_Identifier	LO	42<br>
[7573,1001]	Unknown Tag &amp; Data	OnDemand3DApp 1.0.10.7462	LO	26<br>
[7573,1003]	Unknown Tag &amp; Data	4f	OB	65588<br>
[7573,1004]	Unknown Tag &amp; Data	50	OB	59104<br>
[7fe0,0010]	PixelData		OB	0</p>
</details>

---

## Post #6 by @issakomi (2023-04-18 17:39 UTC)

<p>S. preview 2023-04-18.</p>

---

## Post #7 by @lassoan (2023-04-20 11:52 UTC)

<aside class="quote no-group" data-username="corsag21" data-post="5" data-topic="28870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/corsag21/48/77508_2.png" class="avatar"> corsag21:</div>
<blockquote>
<p>I installed and try to patchdicom. I had no effect. I can’t find " <code>Fix invalid exposure tags</code> and <code>Specify character set</code></p>
</blockquote>
</aside>
<p>Please use the very latest Slicer Preview Release (that you have downloaded today).</p>

---

## Post #8 by @corsag21 (2024-04-07 05:44 UTC)

<p>Hello. I tried to make friends with 3dslicer again. Cyrillic symbols dont works in many ct’s. And i found that filepath don’t works with cyrillic symbols. <a href="https://drive.google.com/drive/folders/1aK5m1o6_GOllwe457JL7k-THraxpIKHO?usp=drive_link" rel="noopener nofollow ugc">video describing errors and files</a></p>

---

## Post #9 by @lassoan (2024-04-07 19:24 UTC)

<p>The files that you attached suffer from the same issue (incorrect <code>SpecificCharacterSet</code> value) as those that you provided earlier. Please contact the manufacturer of the device/software that produced these files, as they are incorrect.</p>
<p>DICOM patcher’s <code>Specify character set</code> rule fixed most of these files, except those where the <code>SpecificCharacterSet</code> field was not just missing, but it contained incorrect value. I’ve submitted a <a href="https://github.com/Slicer/Slicer/pull/7683">pull request</a> that makes the patcher rule even stronger - if that is integrated then the <code>Force character set</code> rule will become available in DICOM Patcher module and you can fix all these flawed files and load them into Slicer with correct patient names.</p>
<p>Loading files that are stored in path that contained special characters: I’ve already submitted a <a href="https://github.com/commontk/AppLauncher/pull/127">fix</a>, but it has not been integrated yet. <a class="mention" href="/u/jcfr">@jcfr</a> please have a look.</p>

---
