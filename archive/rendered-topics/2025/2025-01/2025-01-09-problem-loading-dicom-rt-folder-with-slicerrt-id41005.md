---
topic_id: 41005
title: "Problem Loading Dicom Rt Folder With Slicerrt"
date: 2025-01-09
url: https://discourse.slicer.org/t/41005
---

# Problem loading DICOM RT folder with SlicerRT

**Topic ID**: 41005
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/problem-loading-dicom-rt-folder-with-slicerrt/41005

---

## Post #1 by @Kenneth_Sutherland (2025-01-09 00:43 UTC)

<p>Problem report for Slicer 5.6.2 win-amd64: [please describe expected and actual behavior]</p>
<p>I have installed SlicerRT.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c782fd4bcdc874a2e232c54eb3e5635e82a0cc05.png" data-download-href="/uploads/short-url/ssXEVN8YXCgTC7cM4wk5pnqIhvv.png?dl=1" title="SlicerExtensionsManager" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c782fd4bcdc874a2e232c54eb3e5635e82a0cc05_2_690x211.png" alt="SlicerExtensionsManager" data-base62-sha1="ssXEVN8YXCgTC7cM4wk5pnqIhvv" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c782fd4bcdc874a2e232c54eb3e5635e82a0cc05_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c782fd4bcdc874a2e232c54eb3e5635e82a0cc05_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c782fd4bcdc874a2e232c54eb3e5635e82a0cc05.png 2x" data-dominant-color="424242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerExtensionsManager</span><span class="informations">1039×319 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have downloaded a sample DICOM RT folder from:<br>
<a href="https://github.com/SlicerRt/SlicerRtData/tree/master/eclipse-8.1.20-phantom-ent" rel="noopener nofollow ugc">eclipse-8.1.20-phantom-ent</a></p>
<p>I add data to the scene and select the folder and try to load the data, but it doesn’t seem to be able to load the DICOM RT plan data. Maybe SlicerRT isn’t installed correctly?</p>
<blockquote>
<p>Blockquote<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20250109_092652<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 19045, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 32715 MB physical, 37579 MB virtual<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: enabled<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin<br>
[DEBUG][Qt] 09.01.2025 09:26:52 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: D:/Work/Ishikawa/SlicerPIT/Plan2PIT, <a href="http://slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules</a><br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘unittest’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘logging’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘vtk’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘qt’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘ctk’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘slicer’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘DICOMScalarVolumePlugin’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘numpy’ is imported as ‘np’<br>
[INFO][Stream] 09.01.2025 09:26:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘copy’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘pandas’ is imported as ‘pd’<br>
[INFO][Stream] 09.01.2025 09:26:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘math’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘csv’ is imported<br>
[INFO][Stream] 09.01.2025 09:26:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - module ‘Rotation’ from ‘scipy.spatial.transform’ is imported as ‘R’<br>
[DEBUG][Python] 09.01.2025 09:26:54 [Python] (D:\Users\Tracy\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 09.01.2025 09:26:54 [Python] (D:\Users\Tracy\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 09.01.2025 09:26:55 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 09.01.2025 09:27:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[WARNING][Python] 09.01.2025 09:28:03 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:332) - Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects<br>
[WARNING][Python] 09.01.2025 09:28:05 [Python] (D:\Users\Tracy\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\DICOMBrowser.py:571) - Warning in DICOM plugin Scalar Volume when examining loadable 4: Unnamed Series: Reference image in series does not contain geometry information. Please use caution.<br>
[WARNING][Python] 09.01.2025 09:28:05 [Python] (D:\Users\Tracy\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\DICOMBrowser.py:571) - Warning in DICOM plugin Scalar Volume when examining loadable 5: Unnamed Series: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.<br>
[WARNING][Python] 09.01.2025 09:28:05 [Python] (D:\Users\Tracy\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\DICOMBrowser.py:571) - Warning in DICOM plugin Scalar Volume when examining loadable 8: Unnamed Series: Reference image in series does not contain geometry information. Please use caution.<br>
[INFO][Python] 09.01.2025 09:28:05 [Python] (D:\Users\Tracy\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
[INFO][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM<br>
[INFO][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 2: ENT IMRT<br>
[DEBUG][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:901) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 6.4e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 09.01.2025 09:28:08 [vtkITKArchetypeImageSeriesVectorReaderFile (000002E89F1605D0)] (vtkITKArchetypeImageSeriesReader.cxx:525) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/Tracy/Documents/SlicerDICOMDatabase/dicom/35b6dee7/9ab5477d/3e60bf55cf214f271f0016aa96e2a527.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/Tracy/Documents/SlicerDICOMDatabase/dicom/35b6dee7/9ab5477d/3e60bf55cf214f271f0016aa96e2a527.dcm<br>
Tried to create one of the following:<br>
BMPImageIO<br>
BioRadImageIO<br>
DCMTKImageIO<br>
GDCMImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
LSMImageIO<br>
MGHImageIO<br>
MINCImageIO<br>
MRCImageIO<br>
MetaImageIO<br>
NiftiImageIO<br>
NrrdImageIO<br>
PNGImageIO<br>
ScancoImageIO<br>
StimulateImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
MRMLIDImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 09.01.2025 09:28:08 [vtkCompositeDataPipeline (000002E8EE677720)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (000002E89F1605D0) returned failure for request: vtkInformation (000002E8A41767C0)<br>
Debug: Off<br>
Modified Time: 245317<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[ERROR][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:452) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 09.01.2025 09:28:08 [vtkITKArchetypeImageSeriesVectorReaderFile (000002E89F15D5D0)] (vtkITKArchetypeImageSeriesReader.cxx:525) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/Tracy/Documents/SlicerDICOMDatabase/dicom/35b6dee7/9ab5477d/3e60bf55cf214f271f0016aa96e2a527.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/Tracy/Documents/SlicerDICOMDatabase/dicom/35b6dee7/9ab5477d/3e60bf55cf214f271f0016aa96e2a527.dcm<br>
Tried to create one of the following:<br>
BMPImageIO<br>
BioRadImageIO<br>
DCMTKImageIO<br>
GDCMImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
LSMImageIO<br>
MGHImageIO<br>
MINCImageIO<br>
MRCImageIO<br>
MetaImageIO<br>
NiftiImageIO<br>
NrrdImageIO<br>
PNGImageIO<br>
ScancoImageIO<br>
StimulateImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
MRMLIDImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 09.01.2025 09:28:08 [vtkCompositeDataPipeline (000002E8EE6762E0)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (000002E89F15D5D0) returned failure for request: vtkInformation (000002E8A41752C0)<br>
Debug: Off<br>
Modified Time: 245412<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[ERROR][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:452) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM<br>
[WARNING][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 5: Unnamed Series<br>
[INFO][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM<br>
[INFO][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=15000.0, width=30000.0) has been applied to volume 8: Unnamed Series<br>
[WARNING][Python] 09.01.2025 09:28:08 [Python] (D:/Users/Tracy/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:827) - No geometry information available for DICOM data, skipping corner calculations<br>
[WARNING][Python] 09.01.2025 09:28:08 [Python] (D:\Users\Tracy\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Could not load: 4: Unnamed Series as a Scalar Volume<br>
[CRITICAL][FD] 09.01.2025 09:33:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[CRITICAL][FD] 09.01.2025 09:33:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - DevTools listening on ws://127.0.0.1:1337/devtools/browser/c4aeece0-34a6-4923-87a7-9410476e12da<br>
[WARNING][Qt] 09.01.2025 09:33:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Remote debugging server started successfully. Try pointing a Chromium-based browser to <a href="http://127.0.0.1:1337" rel="noopener nofollow ugc">http://127.0.0.1:1337</a><br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png" rel="noopener nofollow ugc">http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png" rel="noopener nofollow ugc">http://www.example.com/Slicer/Extensions/SlicerSurfaceLearner.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png</a>’. This content should also be served over HTTPS.”<br>
[WARNING][Qt] 09.01.2025 09:33:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png" rel="noopener nofollow ugc">http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png</a>’. This content should also be served over HTTPS.<br>
[WARNING][Qt] 09.01.2025 09:33:49 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>” 0 “A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SameSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" rel="noopener nofollow ugc">https://www.chromestatus.com/feature/5088147346030592</a> and <a href="https://www.chromestatus.com/feature/5633521622188032." rel="noopener nofollow ugc">https://www.chromestatus.com/feature/5633521622188032.</a>”<br>
[WARNING][Qt] 09.01.2025 09:33:49 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SameSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" rel="noopener nofollow ugc">https://www.chromestatus.com/feature/5088147346030592</a> and <a href="https://www.chromestatus.com/feature/5633521622188032" rel="noopener nofollow ugc">https://www.chromestatus.com/feature/5633521622188032</a>.<br>
Blockquote</p>
</blockquote>

---

## Post #2 by @cpinter (2025-01-09 12:58 UTC)

<p>If you open the module selector, is there a Radiotherapy category? If so, what modules are in there?</p>

---

## Post #3 by @Kenneth_Sutherland (2025-01-09 23:17 UTC)

<p>Thank you for your reply.<br>
I don’t see Radiotherapy.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afac817d50e4644a6afe03f7e51b591aa4d14f58.png" data-download-href="/uploads/short-url/p459g3U9Lq08wq9WkO1BhTbCM52.png?dl=1" title="ModuleSelector" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afac817d50e4644a6afe03f7e51b591aa4d14f58.png" alt="ModuleSelector" data-base62-sha1="p459g3U9Lq08wq9WkO1BhTbCM52" width="171" height="500" data-dominant-color="2B2B2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ModuleSelector</span><span class="informations">226×659 13.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I thought that maybe I downloaded SlicerRT but forgot to install it, but it seems to be installed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7e61f59914c914dac4ca429cf46d8a72abccd92.jpeg" data-download-href="/uploads/short-url/zn0Y9PjyH6HMHGd78zeWDSqC8kG.jpeg?dl=1" title="ExtentionsManager" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7e61f59914c914dac4ca429cf46d8a72abccd92_2_690x369.jpeg" alt="ExtentionsManager" data-base62-sha1="zn0Y9PjyH6HMHGd78zeWDSqC8kG" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7e61f59914c914dac4ca429cf46d8a72abccd92_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7e61f59914c914dac4ca429cf46d8a72abccd92_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7e61f59914c914dac4ca429cf46d8a72abccd92_2_1380x738.jpeg 2x" data-dominant-color="4F5152"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ExtentionsManager</span><span class="informations">1920×1027 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Kenneth_Sutherland (2025-01-09 23:31 UTC)

<p>I uninstalled SlicerRT and reinstalled it and it worked!<br>
I now see the Radiotherapy module and can open the sample data set.<br>
Thanks!</p>

---

## Post #5 by @jamesobutler (2025-01-09 23:37 UTC)

<aside class="quote no-group" data-username="Kenneth_Sutherland" data-post="1" data-topic="41005">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kenneth_sutherland/48/78200_2.png" class="avatar"> Kenneth_Sutherland:</div>
<blockquote>
<p>[DEBUG][Qt] 09.01.2025 09:26:52 (unknown:0) - Additional module paths …: D:/Work/Ishikawa/SlicerPIT/Plan2PIT, <a href="http://slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/SlicerElastix/lib/Slicer-5.6/qt-scripted-modules</a></p>
</blockquote>
</aside>
<p>Reviewing here there was no mention of the additional module paths to SlicerRT which is why the Radiotherapy category was not showing because the modules were not specified to load. Maybe <a class="mention" href="/u/kenneth_sutherland">@Kenneth_Sutherland</a>, you accidentally removed the SlicerRT entry when you went to add your own Photoimmunotherapy module to the additional module paths? Or you didn’t complete the installation of SlicerRT with a restart of the Slicer application?</p>

---

## Post #6 by @Kenneth_Sutherland (2025-01-09 23:46 UTC)

<p>I definitely restarted (many, many times) after installing SlicerRT.<br>
It seems I somehow removed SlicerRT when I installed Photoimmunotherapy. I will consult with the developer of the Photoimmunotherapy module here at Hokkaido University.<br>
Thanks again for your help!</p>

---

## Post #7 by @cpinter (2025-01-10 10:00 UTC)

<aside class="quote no-group" data-username="Kenneth_Sutherland" data-post="6" data-topic="41005">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kenneth_sutherland/48/78200_2.png" class="avatar"> Kenneth_Sutherland:</div>
<blockquote>
<p>It seems I somehow removed SlicerRT when I installed Photoimmunotherapy. I will consult with the developer of the Photoimmunotherapy module here at Hokkaido University.</p>
</blockquote>
</aside>
<p>I find this unlikely. It is possible that simply the first installation attempt failed. Unfortunately I’m not familiar with the Extensions Manager enough to know what are the events that trigger errors/warnings.</p>

---

## Post #8 by @Kenneth_Sutherland (2025-01-10 21:18 UTC)

<p>I agree. In fact, I think I installed SlicerRT <em>after</em> Pharmacotherapy.<br>
Anyway, it’s working now, so all is good! <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @cpinter (2025-01-14 12:27 UTC)

<p>So you just needed to uninstall and reinstall? Just to confirm <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Thanks</p>

---

## Post #10 by @Kenneth_Sutherland (2025-01-14 22:39 UTC)

<p>Yes, I just reinstalled SlicerRT and it worked. I don’t think it had anything to do with SlicerPIT.</p>

---

## Post #11 by @Kenneth_Sutherland (2025-01-14 22:40 UTC)

<p>Not  “Pharmacotherapy”, I meant “Photoimmunotherapy”.</p>

---
