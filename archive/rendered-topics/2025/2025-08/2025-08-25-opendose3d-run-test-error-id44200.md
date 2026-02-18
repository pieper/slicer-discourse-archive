# OpenDose3D Run Test error

**Topic ID**: 44200
**Date**: 2025-08-25
**URL**: https://discourse.slicer.org/t/opendose3d-run-test-error/44200

---

## Post #1 by @gaia_muti (2025-08-25 18:49 UTC)

<p>Problem report for Slicer 5.6.2 win-amd64: [please describe expected and actual behavior]</p>
<p>After installing Slicer 5.6.2 and the requested extension for OpenDose3D, after running the test to check the correct functioning the software stopped with this log:</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20250825_150909</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows / Professional / (Build 19044, Code Page 65001) - 64-bit</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16220 MB physical, 18652 MB virtual</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths ..: <a href="http://slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/cli-modules</a>, <a href="http://slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-scripted-modules</a></p>
<p>[DEBUG][Python] 25.08.2025 15:09:11 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\matplotlib\_<em>init</em>_.py:341) - matplotlib data path: C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\matplotlib\mpl-data</p>
<p>[DEBUG][Python] 25.08.2025 15:09:11 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\matplotlib\_<em>init</em>_.py:341) - CONFIGDIR=C:\Users\gmuti\.matplotlib</p>
<p>[DEBUG][Python] 25.08.2025 15:09:11 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\matplotlib\_<em>init</em>_.py:1512) - interactive is False</p>
<p>[DEBUG][Python] 25.08.2025 15:09:11 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\matplotlib\_<em>init</em>_.py:1513) - platform is win32</p>
<p>[DEBUG][Python] 25.08.2025 15:09:12 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\matplotlib\_<em>init</em>_.py:341) - CACHEDIR=C:\Users\gmuti\.matplotlib</p>
<p>[DEBUG][Python] 25.08.2025 15:09:12 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\matplotlib\font_manager.py:1580) - Using fontManager instance from C:\Users\gmuti\.matplotlib\fontlist-v390.json</p>
<p>[DEBUG][Python] 25.08.2025 15:09:32 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 25.08.2025 15:09:32 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:32 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module: “Welcome”</p>
<p>[DEBUG][Python] 25.08.2025 15:09:32 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: Elastix</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module: “OpenDose3D”</p>
<p>[ERROR][Python] 25.08.2025 15:09:44 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\testbuilder.py:158) - DICOM test data dir: C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Resources\DICOM\A_Cycle3-6848MBq-9h57</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Skipped 10 files that were already in the database: C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/CT/CT_1h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/CT/CT_24h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/CT/CT_48h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/CT/CT_4h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/CT/CT_96h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/SPECT_1h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/SPECT_24h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/SPECT_48h.dcm, C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/Resources/DICOM/A_Cycle3-6848MBq-9h57/SPECT_4h.dcm…</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “DICOM indexer has successfully processed 10 files [0.00s]”</p>
<p>[DEBUG][Qt] 25.08.2025 15:09:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “DICOM indexer has updated display fields for 0 files [0.00s]”</p>
<p>[ERROR][Python] 25.08.2025 15:09:44 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\testbuilder.py:169) - Successfully loaded patient 2 with StudyInstanceUID: 1.2.392.200036.9116.2.6.1.61487.1955899372.1653959898.845999 and SeriesInstanceUID: 2.16.840.1.113669.1919.1659510452</p>
<p>[INFO][Python] 25.08.2025 15:09:44 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:452) - Test FullTest_positive started!</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=1579.0, width=3158.0) has been applied to volume 1: CT SPECT-CT 1HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: CT SPECT-CT 1HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=2070.0, width=4140.0) has been applied to volume 1: CT SPECT-CT 24HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: CT SPECT-CT 24HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=4785.0, width=9571.0) has been applied to volume 1: CT SPECT-CT 48HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: CT SPECT-CT 48HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=2467.0, width=4935.0) has been applied to volume 1: CT SPECT-CT 4HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: CT SPECT-CT 4HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=1663.0, width=3327.0) has been applied to volume 1: CT SPECT-CT 96HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: CT SPECT-CT 96HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=32767.0, width=65534.0) has been applied to volume 1: ACSC SPECT-CT 1HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 1HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=32767.0, width=65534.0) has been applied to volume 1: ACSC SPECT-CT 24HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 24HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=32767.0, width=65534.0) has been applied to volume 1: ACSC SPECT-CT 48HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 48HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=32767.0, width=65534.0) has been applied to volume 1: ACSC SPECT-CT 4HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 4HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=32767.0, width=65534.0) has been applied to volume 1: ACSC SPECT-CT 96HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 1: ACSC SPECT-CT 96HR</p>
<p>[INFO][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:466) - Standardise started!</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:487) - Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:281) - Attribute ‘DICOM.Acquisition.Duration’ is empty</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:487) - Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:281) - Attribute ‘DICOM.Acquisition.Duration’ is empty</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:487) - Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:281) - Attribute ‘DICOM.Acquisition.Duration’ is empty</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:487) - Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:281) - Attribute ‘DICOM.Acquisition.Duration’ is empty</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:487) - Failed to read DICOM attribute ‘DICOM.AcquisitionFramesDuration’</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:281) - Attribute ‘DICOM.Acquisition.Duration’ is empty</p>
<p>[ERROR][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeMRB.py:197) - No injection time and no timestamp in name for node 1: ACSC SPECT-CT 1HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:535) - Failed to retrieve DICOM attribute: DICOM.Injection.Date</p>
<p>[ERROR][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeMRB.py:197) - No injection time and no timestamp in name for node 1: ACSC SPECT-CT 24HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:535) - Failed to retrieve DICOM attribute: DICOM.Injection.Date</p>
<p>[ERROR][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeMRB.py:197) - No injection time and no timestamp in name for node 1: ACSC SPECT-CT 48HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:45 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:535) - Failed to retrieve DICOM attribute: DICOM.Injection.Date</p>
<p>[ERROR][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeMRB.py:197) - No injection time and no timestamp in name for node 1: ACSC SPECT-CT 4HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:535) - Failed to retrieve DICOM attribute: DICOM.Injection.Date</p>
<p>[ERROR][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeMRB.py:197) - No injection time and no timestamp in name for node 1: ACSC SPECT-CT 96HR</p>
<p>[WARNING][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\NodeDICOM.py:535) - Failed to retrieve DICOM attribute: DICOM.Injection.Date</p>
<p>[INFO][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:478) - Standardise passed!</p>
<p>[INFO][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:482) - Setup isotope started!</p>
<p>[INFO][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:491) - Setup Isotope passed!</p>
<p>[INFO][Python] 25.08.2025 15:09:46 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:495) - Resample started!</p>
<p>[INFO][VTK] 25.08.2025 15:09:46 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe</p>
<p>[INFO][VTK] 25.08.2025 15:09:46 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule</p>
<p>[INFO][VTK] 25.08.2025 15:09:46 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Resample Image (BRAINS) command line:</p>
<p>C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe --inputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeB.nrrd --referenceVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeG.nrrd --outputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBB.nrrd --pixelType float --interpolationMode Lanczos --defaultValue -1000 --numberOfThreads -1</p>
<p>[INFO][VTK] 25.08.2025 15:09:49 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1917) - Resample Image (BRAINS) standard output:</p>
<p>WARNING: neither warpTransform nor deformationVolume are defined, so warpTransform is set as identity.</p>
<p>=====================================================</p>
<p>Input Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeB.nrrd</p>
<p>Reference Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeG.nrrd</p>
<p>Output Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBB.nrrd</p>
<p>Pixel Type: float</p>
<p>Interpolation: Lanczos</p>
<p>Background Value: -1000</p>
<p>Warp By Transform: Identity</p>
<p>=====================================================</p>
<p>[INFO][VTK] 25.08.2025 15:09:49 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1943) - Resample Image (BRAINS) completed without errors</p>
<p>[INFO][VTK] 25.08.2025 15:09:49 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe</p>
<p>[INFO][VTK] 25.08.2025 15:09:49 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule</p>
<p>[INFO][VTK] 25.08.2025 15:09:49 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Resample Image (BRAINS) command line:</p>
<p>C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe --inputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeE.nrrd --referenceVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeJ.nrrd --outputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBC.nrrd --pixelType float --interpolationMode Lanczos --defaultValue -1000 --numberOfThreads -1</p>
<p>[INFO][VTK] 25.08.2025 15:09:51 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1917) - Resample Image (BRAINS) standard output:</p>
<p>WARNING: neither warpTransform nor deformationVolume are defined, so warpTransform is set as identity.</p>
<p>=====================================================</p>
<p>Input Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeE.nrrd</p>
<p>Reference Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeJ.nrrd</p>
<p>Output Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBC.nrrd</p>
<p>Pixel Type: float</p>
<p>Interpolation: Lanczos</p>
<p>Background Value: -1000</p>
<p>Warp By Transform: Identity</p>
<p>=====================================================</p>
<p>[INFO][VTK] 25.08.2025 15:09:51 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1943) - Resample Image (BRAINS) completed without errors</p>
<p>[INFO][VTK] 25.08.2025 15:09:51 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe</p>
<p>[INFO][VTK] 25.08.2025 15:09:51 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule</p>
<p>[INFO][VTK] 25.08.2025 15:09:51 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Resample Image (BRAINS) command line:</p>
<p>C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe --inputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeC.nrrd --referenceVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeH.nrrd --outputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBD.nrrd --pixelType float --interpolationMode Lanczos --defaultValue -1000 --numberOfThreads -1</p>
<p>[INFO][VTK] 25.08.2025 15:09:54 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1917) - Resample Image (BRAINS) standard output:</p>
<p>WARNING: neither warpTransform nor deformationVolume are defined, so warpTransform is set as identity.</p>
<p>=====================================================</p>
<p>Input Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeC.nrrd</p>
<p>Reference Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeH.nrrd</p>
<p>Output Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBD.nrrd</p>
<p>Pixel Type: float</p>
<p>Interpolation: Lanczos</p>
<p>Background Value: -1000</p>
<p>Warp By Transform: Identity</p>
<p>=====================================================</p>
<p>[INFO][VTK] 25.08.2025 15:09:54 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1943) - Resample Image (BRAINS) completed without errors</p>
<p>[INFO][VTK] 25.08.2025 15:09:54 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe</p>
<p>[INFO][VTK] 25.08.2025 15:09:54 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule</p>
<p>[INFO][VTK] 25.08.2025 15:09:54 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Resample Image (BRAINS) command line:</p>
<p>C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe --inputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeD.nrrd --referenceVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeI.nrrd --outputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBE.nrrd --pixelType float --interpolationMode Lanczos --defaultValue -1000 --numberOfThreads -1</p>
<p>[INFO][VTK] 25.08.2025 15:09:56 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1917) - Resample Image (BRAINS) standard output:</p>
<p>WARNING: neither warpTransform nor deformationVolume are defined, so warpTransform is set as identity.</p>
<p>=====================================================</p>
<p>Input Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeD.nrrd</p>
<p>Reference Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeI.nrrd</p>
<p>Output Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBE.nrrd</p>
<p>Pixel Type: float</p>
<p>Interpolation: Lanczos</p>
<p>Background Value: -1000</p>
<p>Warp By Transform: Identity</p>
<p>=====================================================</p>
<p>[INFO][VTK] 25.08.2025 15:09:56 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1943) - Resample Image (BRAINS) completed without errors</p>
<p>[INFO][VTK] 25.08.2025 15:09:56 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe</p>
<p>[INFO][VTK] 25.08.2025 15:09:56 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule</p>
<p>[INFO][VTK] 25.08.2025 15:09:56 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Resample Image (BRAINS) command line:</p>
<p>C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/cli-modules/BRAINSResample.exe --inputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeF.nrrd --referenceVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBA.nrrd --outputVolume C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBF.nrrd --pixelType float --interpolationMode Lanczos --defaultValue -1000 --numberOfThreads -1</p>
<p>[INFO][VTK] 25.08.2025 15:09:59 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1917) - Resample Image (BRAINS) standard output:</p>
<p>WARNING: neither warpTransform nor deformationVolume are defined, so warpTransform is set as identity.</p>
<p>=====================================================</p>
<p>Input Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeF.nrrd</p>
<p>Reference Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBA.nrrd</p>
<p>Output Volume: C:/Users/gmuti/AppData/Local/Temp/Slicer/HEDG_vtkMRMLScalarVolumeNodeBF.nrrd</p>
<p>Pixel Type: float</p>
<p>Interpolation: Lanczos</p>
<p>Background Value: -1000</p>
<p>Warp By Transform: Identity</p>
<p>=====================================================</p>
<p>[INFO][VTK] 25.08.2025 15:09:59 [vtkSlicerCLIModuleLogic (0000023B5EB3DF70)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1943) - Resample Image (BRAINS) completed without errors</p>
<p>[INFO][Python] 25.08.2025 15:09:59 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:507) - Resample passed!</p>
<p>[INFO][Python] 25.08.2025 15:09:59 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:511) - Rescale started!</p>
<p>[INFO][Python] 25.08.2025 15:09:59 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:535) - Rescale passed!</p>
<p>[INFO][Python] 25.08.2025 15:09:59 [Python] (C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py:539) - Registration started!</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “C:/Users/gmuti/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/OpenDose3D.py”, line 1228, in onRunTestButton</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - self.test.FullTest_positive()</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DTest.py”, line 542, in FullTest_positive</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - self.logic.createTransforms(referenceNode.data)</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “C:\Users\gmuti\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\OpenDose3D\lib\Slicer-5.6\qt-scripted-modules\Logic\OpenDose3DLogic.py”, line 919, in createTransforms</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Elastix.RegistrationPresets_ParameterFilenames</p>
<p>[CRITICAL][Stream] 25.08.2025 15:09:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: module ‘Elastix’ has no attribute ‘RegistrationPresets_ParameterFilenames’</p>

---

## Post #2 by @lassoan (2025-08-25 18:50 UTC)

<p>Elastix extension has been greatly improved, but the refactoring also resulted in changing some of the APIs. You need to adjust how OpenDose3D uses Elastix to avoid errors.</p>

---
