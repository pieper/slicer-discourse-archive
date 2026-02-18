# import directory of Grayscale Word image slice files

**Topic ID**: 2873
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/import-directory-of-grayscale-word-image-slice-files/2873

---

## Post #1 by @john_micrima (2018-05-22 11:50 UTC)

<p>Operating system: Window 10<br>
Slicer version: 4.8.1<br>
Expected behavior: I expect to see an 3D image in the 3D pane<br>
Actual behavior: I see an empty cube and grayscale images in the other three panes</p>
<p>My first question is, “Does slicer DO 16bit word gray scale images? Would it load them if I got all the voodoo correct?”</p>
<p>If the answer to that question is, “No” then let me know and ignore the rest of this post.</p>
<p>I am new to Dicom and have inherited a C# app that reads a MatLab file that contains meta-data and an array of floats containing intensity data for a single 3D image. I am using the C# fo-dicom library to export this data as Grayscale images. I can save the slices as a multi-frame dcm file. That file is valid according to DVTK and I can load it into the leadtools dicom viewer and it plays as a “video” of slices.</p>
<p>I tried loading it into Slicer and that didn’t have anything visible displayed in the four Slicer panes. Can I assume that Slicer doesn’t load multi-frame files or have I got the voodoo wrong?</p>
<p>Anyway, I can also export my data as a series of images, one for each slice of my 3D volume. Each of those files is valid according to DVTK and can be viewed as a single slice in various Dicom viewers. But none of them will stitch the files into a, reconstructed, 3D volume. So I assume that I am doing it wrong, that I am not providing the information needed to reconstruct the 3D images from my slices.</p>
<p>I have Googled and will continue to Google for answers but I haven’t yet seen a simple list of requisites or instructions for creating a series of image slices that can be reconstructed into a 3D volume.</p>
<p>Does anyone know where I could find such a list or could you post the info I need?</p>
<p>As an aside:  I am pretty much stuck with C# based solutions as I will be called from a C# app and I’d rather not have to spawn a process to run a Python script or install Matlab on hospital machines. My reluctance might crumble as I get closer to my deadline <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"> I am also going to look at using VTK - I know I can load and view my data in VTK so VTK or ITK might be a good option for me to generate slices and I will investigate it.</p>
<p>For today, I am hoping that I am just missing a few Dicom elements that can be used to stitch my files together. I just don’t know what they are yet.</p>
<p>I tried to upload 2 text files that describe the Dicom elements in the first two files of my series so you could see what I’m setting. But that isn’t allowed so I will append them as replies to this post.</p>
<p>Now I’m thinking that this should be posted to the developer’s forum but I don’t want to cross post.</p>

---

## Post #2 by @lassoan (2018-05-22 11:53 UTC)

<p>What you describe should be easy to do. Can you confirm that you can browse through the volume by moving the sliders at the top of slice viewers? What imaging modality you use? What would you like to visualize in the 3D viewer? Have you tried Volume rendering module?</p>

---

## Post #3 by @john_micrima (2018-05-22 12:05 UTC)

<p>Hi Andras,</p>
<p>I can scroll through the image slices in all the 2D panes. It looks as good as our low res images always look. So that part works.</p>
<p>The imaging modality is imaging via a multi-static microwave antenna array which isn’t, yet, an official Dicom modality. This could be one of the many reasons that the volume isn’t reconstructed in the 3D pane (I guess).</p>
<p>My modality is: OT (other)</p>
<p>I am going to paste the text headers (exported by DVTK) of the first two files in my series.</p>
<p>First file headers follow this line.</p>
<details>
<summary>
DICOM header</summary>
<p>(0x00020000,	UL,	212)	<span class="hashtag">#Group</span> 0002 Length<br>
(0x00020001,	OB,	C:\DVTk - The Healthcare Validation Toolkit )\DICOM Editor\5.0.2.0\Results\B08_0026.pix)	<span class="hashtag">#File</span> Meta Information Version<br>
(0x00020002,	UI,	1.2.840.10008.5.1.4.1.1.7)	<span class="hashtag">#Media</span> Storage SOP Class UID<br>
(0x00020003,	UI,	1.2.826.0.1.5616345.57279226668323982872100893960904823680)	<span class="hashtag">#Media</span> Storage SOP Instance UID<br>
(0x00020010,	UI,	1.2.840.10008.1.2.1)	<span class="hashtag">#Transfer</span> Syntax UID<br>
(0x00020012,	UI,	1.3.6.1.4.1.30071.8)	<span class="hashtag">#Implementation</span> Class UID<br>
(0x00020013,	SH,	fo-dicom 3.0.2)	<span class="hashtag">#Implementation</span> Version Name<br>
(0x00020016,	AE,	REDACTED)	<span class="hashtag">#Source</span> Application Entity Title<br>
(0x00080005,	CS,	ISO_IR 100)	<span class="hashtag">#Specific</span> Character Set<br>
(0x00080008,	CS,	DERIVED\PRIMARY)	<span class="hashtag">#Image</span> Type<br>
(0x00080016,	UI,	1.2.840.10008.5.1.4.1.1.7)	<span class="hashtag">#SOP</span> Class UID<br>
(0x00080018,	UI,	1.2.826.0.1.5616345.57279226668323982872100893960904823680)	<span class="hashtag">#SOP</span> Instance UID<br>
(0x00080020,	DA,	20170131)	<span class="hashtag">#Study</span> Date<br>
(0x00080021,	DA,	20180521)	<span class="hashtag">#Series</span> Date<br>
(0x00080022,	DA,	20170131)	<span class="hashtag">#Acquisition</span> Date<br>
(0x00080023,	DA,	20180521)	<span class="hashtag">#Content</span> Date<br>
(0x00080030,	TM,	095821)	<span class="hashtag">#Study</span> Time<br>
(0x00080031,	TM,	151710)	<span class="hashtag">#Series</span> Time<br>
(0x00080032,	TM,	095951)	<span class="hashtag">#Acquisition</span> Time<br>
(0x00080033,	TM,	151710)	<span class="hashtag">#Content</span> Time<br>
(0x00080050,	SH,	EMPTY)	<span class="hashtag">#Accession</span> Number<br>
(0x00080060,	CS,	OT)	<span class="hashtag">#Modality</span><br>
(0x00080064,	CS,	WSD)	<span class="hashtag">#Conversion</span> Type<br>
(0x00080090,	PN,	EMPTY)	<span class="hashtag">#Referring</span> Physician’s Name<br>
(0x00081030,	LO,	EMPTY)	<span class="hashtag">#Study</span> Description<br>
(0x00081070,	PN,	R^S)	<span class="hashtag">#Operators</span>’ Name<br>
(0x00100010,	PN,	L^G)	<span class="hashtag">#Patient</span>’s Name<br>
(0x00100020,	LO,	M5-1_P153)	<span class="hashtag">#Patient</span> ID<br>
(0x00100022,	CS,	TEXT)	<span class="hashtag">#Type</span> of Patient ID<br>
(0x00100030,	DA,	20170131)	<span class="hashtag">#Patient</span>’s Birth Date<br>
(0x00100040,	CS,	F)	<span class="hashtag">#Patient</span>’s Sex<br>
(0x00101010,	AS,	001Y)	<span class="hashtag">#Patient</span>’s Age<br>
(0x00180015,	CS,	BREAST)	<span class="hashtag">#Body</span> Part Examined<br>
(0x00180050,	DS,	1)	<span class="hashtag">#Slice</span> Thickness<br>
(0x00181010,	LO,	REDACTED-SN003)	<span class="hashtag">#Secondary</span> Capture Device ID<br>
(0x00181016,	LO,	REDACTED)	<span class="hashtag">#Secondary</span> Capture Device Manufacturer<br>
(0x00181018,	LO,	REDACTED Workstation)	<span class="hashtag">#Secondary</span> Capture Device Manufacturer’s Model Name<br>
(0x00185100,	CS,	HFP)	<span class="hashtag">#Patient</span> Position<br>
(0x0020000d,	UI,	1.2.826.0.1.5616345.503559762324855987616799250770876782749)	<span class="hashtag">#Study</span> Instance UID<br>
(0x0020000e,	UI,	1.2.826.0.1.5616345.5059240054954347331544666827536685729)	<span class="hashtag">#Series</span> Instance UID<br>
(0x00200010,	SH,	20170131095819)	<span class="hashtag">#Study</span> ID<br>
(0x00200011,	IS,		)	<span class="hashtag">#Series</span> Number<br>
(0x00200013,	IS,	1)	<span class="hashtag">#Instance</span> Number<br>
(0x00200020,	CS,	R\H)	<span class="hashtag">#Patient</span> Orientation<br>
(0x00200060,	CS,	R)	<span class="hashtag">#Laterality</span><br>
(0x00280002,	US,	1)	<span class="hashtag">#Samples</span> per Pixel<br>
(0x00280004,	CS,	MONOCHROME2)	<span class="hashtag">#Photometric</span> Interpretation<br>
(0x00280008,	IS,	1)	<span class="hashtag">#Number</span> of Frames<br>
(0x00280010,	US,	127)	<span class="hashtag">#Rows</span><br>
(0x00280011,	US,	127)	<span class="hashtag">#Columns</span><br>
(0x00280030,	DS,	1\1)	<span class="hashtag">#Pixel</span> Spacing<br>
(0x00280100,	US,	16)	<span class="hashtag">#Bits</span> Allocated<br>
(0x00280101,	US,	16)	<span class="hashtag">#Bits</span> Stored<br>
(0x00280102,	US,	15)	<span class="hashtag">#High</span> Bit<br>
(0x00280103,	US,	0)	<span class="hashtag">#Pixel</span> Representation<br>
(0x00281050,	DS,	32768)	<span class="hashtag">#Window</span> Center<br>
(0x00281051,	DS,	65535)	<span class="hashtag">#Window</span> Width<br>
(0x00400244,	DA,	20170131)	<span class="hashtag">#Performed</span> Procedure Step Start Date<br>
(0x00400245,	TM,	095821)	<span class="hashtag">#Performed</span> Procedure Step Start Time<br>
(0x00400254,	LO,	EMPTY)	<span class="hashtag">#Performed</span> Procedure Step Description<br>
(0x7fe00010,	OW,	C:\DVTk - The Healthcare Validation Toolkit ()\DICOM Editor\5.0.2.0\Results\W16L0027.pix)	<span class="hashtag">#Pixel</span> Data</p>
</details>
<p>Second file headers follow this line:</p>
<details>
<summary>
DICOM header</summary>
<p>(0x00020000,	UL,	212)	<span class="hashtag">#Group</span> 0002 Length<br>
(0x00020001,	OB,	C:\DVTk - The Healthcare Validation Toolkit (<a href="http://www.dvtk.org" rel="nofollow noopener">www.dvtk.org</a>)\DICOM Editor\5.0.2.0\Results\B08_0028.pix)	<span class="hashtag">#File</span> Meta Information Version<br>
(0x00020002,	UI,	1.2.840.10008.5.1.4.1.1.7)	<span class="hashtag">#Media</span> Storage SOP Class UID<br>
(0x00020003,	UI,	1.2.826.0.1.5616345.46390217425012691973470357670106283408)	<span class="hashtag">#Media</span> Storage SOP Instance UID<br>
(0x00020010,	UI,	1.2.840.10008.1.2.1)	<span class="hashtag">#Transfer</span> Syntax UID<br>
(0x00020012,	UI,	1.3.6.1.4.1.30071.8)	<span class="hashtag">#Implementation</span> Class UID<br>
(0x00020013,	SH,	fo-dicom 3.0.2)	<span class="hashtag">#Implementation</span> Version Name<br>
(0x00020016,	AE,	REDACTED)	<span class="hashtag">#Source</span> Application Entity Title<br>
(0x00080005,	CS,	ISO_IR 100)	<span class="hashtag">#Specific</span> Character Set<br>
(0x00080008,	CS,	DERIVED\PRIMARY)	<span class="hashtag">#Image</span> Type<br>
(0x00080016,	UI,	1.2.840.10008.5.1.4.1.1.7)	<span class="hashtag">#SOP</span> Class UID<br>
(0x00080018,	UI,	1.2.826.0.1.5616345.46390217425012691973470357670106283408)	<span class="hashtag">#SOP</span> Instance UID<br>
(0x00080020,	DA,	20170131)	<span class="hashtag">#Study</span> Date<br>
(0x00080021,	DA,	20180521)	<span class="hashtag">#Series</span> Date<br>
(0x00080022,	DA,	20170131)	<span class="hashtag">#Acquisition</span> Date<br>
(0x00080023,	DA,	20180521)	<span class="hashtag">#Content</span> Date<br>
(0x00080030,	TM,	095821)	<span class="hashtag">#Study</span> Time<br>
(0x00080031,	TM,	151710)	<span class="hashtag">#Series</span> Time<br>
(0x00080032,	TM,	095951)	<span class="hashtag">#Acquisition</span> Time<br>
(0x00080033,	TM,	151710)	<span class="hashtag">#Content</span> Time<br>
(0x00080050,	SH,	EMPTY)	<span class="hashtag">#Accession</span> Number<br>
(0x00080060,	CS,	OT)	<span class="hashtag">#Modality</span><br>
(0x00080064,	CS,	WSD)	<span class="hashtag">#Conversion</span> Type<br>
(0x00080090,	PN,	EMPTY)	<span class="hashtag">#Referring</span> Physician’s Name<br>
(0x00081030,	LO,	EMPTY)	<span class="hashtag">#Study</span> Description<br>
(0x00081070,	PN,	R^S)	<span class="hashtag">#Operators</span>’ Name<br>
(0x00100010,	PN,	L^G)	<span class="hashtag">#Patient</span>’s Name<br>
(0x00100020,	LO,	M5-1_P153)	<span class="hashtag">#Patient</span> ID<br>
(0x00100022,	CS,	TEXT)	<span class="hashtag">#Type</span> of Patient ID<br>
(0x00100030,	DA,	20170131)	<span class="hashtag">#Patient</span>’s Birth Date<br>
(0x00100040,	CS,	F)	<span class="hashtag">#Patient</span>’s Sex<br>
(0x00101010,	AS,	001Y)	<span class="hashtag">#Patient</span>’s Age<br>
(0x00180015,	CS,	BREAST)	<span class="hashtag">#Body</span> Part Examined<br>
(0x00180050,	DS,	1)	<span class="hashtag">#Slice</span> Thickness<br>
(0x00181010,	LO,	REDACTED-SN003)	<span class="hashtag">#Secondary</span> Capture Device ID<br>
(0x00181016,	LO,	REDACTED)	<span class="hashtag">#Secondary</span> Capture Device Manufacturer<br>
(0x00181018,	LO,	REDACTED Workstation)	<span class="hashtag">#Secondary</span> Capture Device Manufacturer’s Model Name<br>
(0x00185100,	CS,	HFP)	<span class="hashtag">#Patient</span> Position<br>
(0x0020000d,	UI,	1.2.826.0.1.5616345.503559762324855987616799250770876782749)	<span class="hashtag">#Study</span> Instance UID<br>
(0x0020000e,	UI,	1.2.826.0.1.5616345.5059240054954347331544666827536685729)	<span class="hashtag">#Series</span> Instance UID<br>
(0x00200010,	SH,	20170131095819)	<span class="hashtag">#Study</span> ID<br>
(0x00200011,	IS,		)	<span class="hashtag">#Series</span> Number<br>
(0x00200013,	IS,	1)	<span class="hashtag">#Instance</span> Number<br>
(0x00200020,	CS,	R\H)	<span class="hashtag">#Patient</span> Orientation<br>
(0x00200060,	CS,	R)	<span class="hashtag">#Laterality</span><br>
(0x00280002,	US,	1)	<span class="hashtag">#Samples</span> per Pixel<br>
(0x00280004,	CS,	MONOCHROME2)	<span class="hashtag">#Photometric</span> Interpretation<br>
(0x00280008,	IS,	1)	<span class="hashtag">#Number</span> of Frames<br>
(0x00280010,	US,	127)	<span class="hashtag">#Rows</span><br>
(0x00280011,	US,	127)	<span class="hashtag">#Columns</span><br>
(0x00280030,	DS,	1\1)	<span class="hashtag">#Pixel</span> Spacing<br>
(0x00280100,	US,	16)	<span class="hashtag">#Bits</span> Allocated<br>
(0x00280101,	US,	16)	<span class="hashtag">#Bits</span> Stored<br>
(0x00280102,	US,	15)	<span class="hashtag">#High</span> Bit<br>
(0x00280103,	US,	0)	<span class="hashtag">#Pixel</span> Representation<br>
(0x00281050,	DS,	32768)	<span class="hashtag">#Window</span> Center<br>
(0x00281051,	DS,	65535)	<span class="hashtag">#Window</span> Width<br>
(0x00400244,	DA,	20170131)	<span class="hashtag">#Performed</span> Procedure Step Start Date<br>
(0x00400245,	TM,	095821)	<span class="hashtag">#Performed</span> Procedure Step Start Time<br>
(0x00400254,	LO,	EMPTY)	<span class="hashtag">#Performed</span> Procedure Step Description<br>
(0x7fe00010,	OW,	C:\DVTk - The Healthcare Validation Toolkit (<a href="http://www.dvtk.org" rel="nofollow noopener">www.dvtk.org</a>)\DICOM Editor\5.0.2.0\Results\W16L0029.pix)	<span class="hashtag">#Pixel</span> Data</p>
</details>

---

## Post #4 by @lassoan (2018-05-22 13:35 UTC)

<aside class="quote no-group" data-username="john_micrima" data-post="3" data-topic="2873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/839c29/48.png" class="avatar"> john_micrima:</div>
<blockquote>
<p>I can scroll through the image slices in all the 2D panes. It looks as good as our low res images always look</p>
</blockquote>
</aside>
<p>Data import is correct then. You have a 3D volume in the scene.</p>
<p>If you are lucky (structures that you would like to visualize have a distinct intensity range) then direct volume rendering can nicely visualize your data in 3D. So, I would recommend to experiment with <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering">Volume rendering module</a>.</p>
<p>If your structures of interest are not easily separable by intensity range, then you have to segment the volume by using <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment editor module</a>. There are some manual and semi-automatic tools - see step-by-step tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">here</a>.</p>

---

## Post #5 by @john_micrima (2018-05-22 14:53 UTC)

<p>Thanks, I used the Grayscale Model maker and saw a 3D volume. I will try your suggestions and see what I get.</p>
<p>My problems were, probably, down to my unfamiliarity with Slicer but I thought they were due to my data exporting.</p>
<p>Still, if anyone knows some good links that might help me export better data then I would be grateful. maybe I could export data that could be viewed in a wide range of Dicom viewers.</p>
<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
