# I need help: Encountered "Could not load ... as a scalar volume" when loading MRI sequence

**Topic ID**: 32038
**Date**: 2023-10-04
**URL**: https://discourse.slicer.org/t/i-need-help-encountered-could-not-load-as-a-scalar-volume-when-loading-mri-sequence/32038

---

## Post #1 by @IrisFang (2023-10-04 17:50 UTC)

<p>Dear developer,<br>
Hello~<br>
When I loaded the MRI image sequence today, the software kept reporting errors, “Could not load: 23: t1_quick3d_tra_fs_bh_P_MPRTRA as a Scalar Volume”, but there was no problem when loading CT images. The specific log is as follows. I have searched but failed to solve the problem, I hope you can get help, thank you!</p>
<p>[INFO][Python] 04.10.2023 13:24:06 [Python] (F:/3D SLICER/Slicer 5.0.2/bin/…/lib/Slicer-5.0/qt-scripted-modules/DICOMScalarVolumePlugin.py:391) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 04.10.2023 13:24:06 [Python] (F:/3D SLICER/Slicer 5.0.2/bin/…/lib/Slicer-5.0/qt-scripted-modules/DICOMScalarVolumePlugin.py:397) - Could not read scalar volume using GDCM approach.   Error is: FileFormatError<br>
[INFO][Python] 04.10.2023 13:24:06 [Python] (F:/3D SLICER/Slicer 5.0.2/bin/…/lib/Slicer-5.0/qt-scripted-modules/DICOMScalarVolumePlugin.py:391) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 04.10.2023 13:24:06 [Python] (F:/3D SLICER/Slicer 5.0.2/bin/…/lib/Slicer-5.0/qt-scripted-modules/DICOMScalarVolumePlugin.py:397) - Could not read scalar volume using DCMTK approach.   Error is: FileFormatError<br>
[WARNING][Python] 04.10.2023 13:24:06 [Python] (F:\3D SLICER\Slicer 5.0.2\bin\Python\slicer\util.py:2610) - Could not load: 23: t1_quick3d_tra_fs_bh_P_MPRTRA as a Scalar Volume<br>
[INFO][Stream] 04.10.2023 13:24:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 04.10.2023 13:24:06 [vtkITKArchetypeImageSeriesScalarReader (0000024173E28540)] (D:\D\S\S-0\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:517) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/2023-6 影像收集/何宏硕20210119 间隔时间长/20200408腹部MRI/51DT35BB/UTBCMUPO/I4100000.  ITK exception info: error in unknown: ITK ERROR: Pixel type larger than output type<br>
[ERROR][VTK] 04.10.2023 13:24:06 [vtkCompositeDataPipeline (000002417DC7DA40)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:741) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000024173E28540) returned failure for request: vtkInformation (00000241166BD3F0)<br>
Debug: Off<br>
Modified Time: 71921732<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 04.10.2023 13:24:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not read scalar volume using GDCM approach.   Error is: FileFormatError<br>
[INFO][Stream] 04.10.2023 13:24:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 04.10.2023 13:24:06 [vtkITKArchetypeImageSeriesScalarReader (0000024173E29440)] (D:\D\S\S-0\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:517) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/2023-6 影像收集/何宏硕20210119 间隔时间长/20200408腹部MRI/51DT35BB/UTBCMUPO/I4100000.  ITK exception info: error in unknown: ITK ERROR: Pixel type larger than output type<br>
[ERROR][VTK] 04.10.2023 13:24:06 [vtkCompositeDataPipeline (000002417DC7DC40)] (D:\D\S\S-0-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:741) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000024173E29440) returned failure for request: vtkInformation (00000241166C0460)<br>
Debug: Off<br>
Modified Time: 71921838<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 04.10.2023 13:24:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not read scalar volume using DCMTK approach.   Error is: FileFormatError<br>
[CRITICAL][Stream] 04.10.2023 13:24:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not load: 23: t1_quick3d_tra_fs_bh_P_MPRTRA as a Scalar Volume</p>

---

## Post #2 by @lassoan (2023-10-04 17:54 UTC)

<p>It seems that the data set is invalid. The issue looks very similar to this one:</p>
<aside class="quote quote-modified" data-post="9" data-topic="30417">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/pixel-larger-than-the-output-type/30417/9">Pixel larger than the output type</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The data set is invalid. See the output of David Clunie’s dciodvfy tool: 
(0x0040,0x1008) LO Confidentiality Code  - Warning - Explicit value representation doesn't match data dictionary; Explicit &lt;ST&gt; Dictionary &lt;LO&gt;
(0x07a3,0x10ca)  ?  - Warning - Unrecognized tag - assuming explicit value representation OK
Warning - Value dubious for this VR - (0x0010,0x0010) PN Patient's Name  PN [1] = &lt;Anonymous&gt; - Retired Person Name form
MRImage
Error - Empty attribute (no value) Type 1 Required Element=&lt;R…
  </blockquote>
</aside>

<p>Probably the image has not come straight from the scanner but it was processed/anonymized, which corrupted its content.</p>

---

## Post #3 by @IrisFang (2023-10-05 02:26 UTC)

<p>Thank you very much !<br>
However, I am very sorry that I am still a rookie in using 3Dslicer. May I ask where I can find the repair tool “dcmodify.exe”? Do I run every file in the dicom folder?</p>

---

## Post #4 by @pearsonm (2023-10-05 21:55 UTC)

<p>dcmodify is part of the dcmtk set of DICOM tools <a href="https://dicom.offis.de/dcmtk.php.en" rel="noopener nofollow ugc">https://dicom.offis.de/dcmtk.php.en</a> and you will need to run it for all affected files.</p>
<p>You could also try using gdcmconv from the gdcm DICOM toolkit <a href="https://sourceforge.net/projects/gdcm/" rel="noopener nofollow ugc">https://sourceforge.net/projects/gdcm/</a> as it can automatically correct some issues during conversion. The Ubuntu man page has a section on usage <a href="https://manpages.ubuntu.com/manpages/jammy/man1/gdcmconv.1.html" class="inline-onebox" rel="noopener nofollow ugc">Ubuntu Manpage: gdcmconv - Tool to convert DICOM to DICOM.</a></p>

---

## Post #5 by @IrisFang (2023-10-06 07:43 UTC)

<p>Thank you! I will try it.</p>

---
