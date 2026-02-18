# Error when loading CT data

**Topic ID**: 11044
**Date**: 2020-04-08
**URL**: https://discourse.slicer.org/t/error-when-loading-ct-data/11044

---

## Post #1 by @sanlen (2020-04-08 15:14 UTC)

<p>Hi,</p>
<p>when I try to load a dual-energy CT virtual non contrast series, I get the error</p>
<p>‘Reference image in series does not contain geometry information’.</p>
<p>I know that these series do not contain the same geometry information as regular series (e.g. you cannot co-register them correctly with a regular CT series of the same scan in PACS), but they should load and allow ROI measurements as they are not just secondary captures. Is there any way to get them to load? DICOM patcher did not work.</p>
<p>Anonymized test series: <a href="https://drive.google.com/open?id=19aUvDyDyIhYexWw6M0KngGnCFy0Hy35T" class="inline-onebox" rel="noopener nofollow ugc">Test_VNC - Google Drive</a></p>
<p>Error log:</p>
<blockquote>
<p>Blockquote<br>
[INFO][Python] 08.04.2020 06:51:09 [Python] (C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:318) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 08.04.2020 06:51:09 [Python] (C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:324) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 08.04.2020 06:51:09 [Python] (C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:318) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 08.04.2020 06:51:09 [Python] (C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:324) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[ERROR][Python] 08.04.2020 06:51:09 [Python] (C:\Users\AG\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py:656) - DICOM plugin failed to load ’ - as a 85 frames MultiVolume by ImagePositionPatient+AcquisitionTime’ as a ‘MultiVolume’.<br>
Traceback (most recent call last):<br>
File “C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 620, in load<br>
if frame.GetImageData() == None:<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetImageData’</p>
</blockquote>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\AG\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 650, in loadLoadables<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 729, in load<br>
logging.error(“Failed to read a multivolume: {0}”.format(e.message))<br>
AttributeError: ‘AttributeError’ object has no attribute ‘message’<br>
[WARNING][Python] 08.04.2020 06:51:09 [Python] (C:\Users\AG\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\bin\Python\slicer\util.py:1567) - Could not load:  - as a 85 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume<br>
[INFO][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 08.04.2020 06:51:09 [vtkITKArchetypeImageSeriesScalarReader (000001E985EA26C0)] (D:\D\P\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:228) - UpdateFromFile: Unsupported number of components (only 1 allowed): 3<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 08.04.2020 06:51:09 [vtkITKArchetypeImageSeriesScalarReader (000001E985E9F400)] (D:\D\P\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:228) - UpdateFromFile: Unsupported number of components (only 1 allowed): 3<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - DICOM plugin failed to load ’ - as a 85 frames MultiVolume by ImagePositionPatient+AcquisitionTime’ as a ‘MultiVolume’.<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 620, in load<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     if frame.GetImageData() == None:<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘GetImageData’<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - During handling of the above exception, another exception occurred:<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\AG\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 650, in loadLoadables<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     loadSuccess = plugin.load(loadable)<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/AG/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 729, in load<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     logging.error(“Failed to read a multivolume: {0}”.format(e.message))<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: ‘AttributeError’ object has no attribute ‘message’<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][Stream] 08.04.2020 06:51:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not load:  - as a 85 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume</p>
<blockquote>
<p>Blockquote</p>
</blockquote>
<p>Thank you so much!</p>

---

## Post #2 by @lassoan (2020-04-08 15:59 UTC)

<p>The error message is accurate, there is no geometry information in the image. Required ImagePositionPatient, ImageOrientationPatient tags are missing, therefore you cannot load these frames as a 3D volume.</p>

---

## Post #3 by @sanlen (2020-04-08 16:57 UTC)

<p>Thank you very much for checking. Will get back to the vendor and ask if there might be a way to export the series with the corresponding tags.</p>

---
