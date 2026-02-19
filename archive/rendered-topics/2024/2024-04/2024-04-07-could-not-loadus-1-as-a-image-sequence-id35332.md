---
topic_id: 35332
title: "Could Not Loadus 1 As A Image Sequence"
date: 2024-04-07
url: https://discourse.slicer.org/t/35332
---

# Could not load:1:US [1] as a image sequence

**Topic ID**: 35332
**Date**: 2024-04-07
**URL**: https://discourse.slicer.org/t/could-not-loadus-1-as-a-image-sequence/35332

---

## Post #1 by @Nancy (2024-04-07 10:55 UTC)

<p>I can’t open the ultrasound images in dicom format, what might be the problem?</p>

---

## Post #2 by @lassoan (2024-04-07 13:13 UTC)

<p>Most likely the image is corrupted. More details may be available in the application log.</p>

---

## Post #3 by @Nancy (2024-04-08 07:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ee696ab126be94667748f6b046fdd043893e68e.jpeg" data-download-href="/uploads/short-url/dxwUMKpiCugLD95pWtyFAaFMXhQ.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ee696ab126be94667748f6b046fdd043893e68e_2_690x115.jpeg" alt="error" data-base62-sha1="dxwUMKpiCugLD95pWtyFAaFMXhQ" width="690" height="115" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ee696ab126be94667748f6b046fdd043893e68e_2_690x115.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ee696ab126be94667748f6b046fdd043893e68e_2_1035x172.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ee696ab126be94667748f6b046fdd043893e68e_2_1380x230.jpeg 2x" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">2396×400 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2024-04-08 12:44 UTC)

<p>Look for the full log under Help-&gt;Report a bug.</p>

---

## Post #5 by @lassoan (2024-04-08 16:09 UTC)

<p>Please also test with the latest Slicer Preview Release and let us know if you still experience any issues.</p>

---

## Post #6 by @Nancy (2024-04-10 08:07 UTC)

<p>[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2024-04-10 16:03:48<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.4.0 (revision 31938 / 311cb26) win-amd64 - installed release<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 22000, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 14198 MB physical, 25819 MB virtual<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 7 5800H with Radeon Graphics         , 16 cores, 16 logical processors<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/86131/Desktop/Slicer 5.4.0/bin<br>
[DEBUG][Qt] 10.04.2024 16:03:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-31938/SlicerRadiomics/lib/Slicer-5.4/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-31938/SlicerRadiomics/lib/Slicer-5.4/cli-modules</a>, <a href="http://slicer.org/Extensions-31938/SlicerRadiomics/lib/Slicer-5.4/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-31938/SlicerRadiomics/lib/Slicer-5.4/qt-scripted-modules</a><br>
[DEBUG][Python] 10.04.2024 16:03:53 [Python] (C:\Users\86131\Desktop\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 10.04.2024 16:03:53 [Python] (C:\Users\86131\Desktop\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 10.04.2024 16:03:53 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 10.04.2024 16:05:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Qt] 10.04.2024 16:05:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “DICOM indexer has successfully inserted 14 files [0.04s]”<br>
[DEBUG][Qt] 10.04.2024 16:05:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “DICOM indexer has successfully processed 14 files [0.06s]”<br>
[DEBUG][Qt] 10.04.2024 16:05:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “DICOM indexer has updated display fields for 14 files [0.04s]”<br>
[INFO][Python] 10.04.2024 16:05:20 [Python] (C:\Users\86131\Desktop\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\DICOMLib\DICOMBrowser.py:261) - Imported a DICOM directory, checking for extensions<br>
[WARNING][Python] 10.04.2024 16:05:23 [Python] (C:\Users\86131\Desktop\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\DICOMLib\DICOMBrowser.py:568) - Warning in DICOM plugin Image sequence when examining loadable 1: US [6]: Image spacing may need to be calibrated for accurate size measurements.<br>
[INFO][Python] 10.04.2024 16:05:23 [Python] (C:\Users\86131\Desktop\Slicer 5.4.0\bin\Python\slicer\util.py:2909) - Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
[ERROR][VTK] 10.04.2024 16:05:24 [vtkITKArchetypeImageSeriesVectorReaderFile (000001E818FE2B10)] (vtkITKArchetypeImageSeriesReader.cxx:708) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/86131/Desktop/11/zhao gui lian_01_0006_0001.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/86131/Desktop/11/zhao gui lian_01_0006_0001.dcm<br>
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
Bruker2dseqImageIO<br>
GE4ImageIO<br>
GE5ImageIO<br>
HDF5ImageIO<br>
JPEG2000ImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 10.04.2024 16:05:24 [vtkCompositeDataPipeline (000001E856C37300)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderFile (000001E818FE2B10) returned failure for request: vtkInformation (000001E8670014B0)<br>
Debug: Off<br>
Modified Time: 192980<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[ERROR][Python] 10.04.2024 16:05:24 [Python] (C:\Users\86131\Desktop\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\DICOMLib\DICOMUtils.py:794) - DICOM plugin failed to load ‘1: US [6]’ as a ‘Image sequence’.<br>
Traceback (most recent call last):<br>
File “C:\Users\86131\Desktop\Slicer 5.4.0\lib\Slicer-5.4\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 790, in loadLoadables<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Users/86131/Desktop/Slicer 5.4.0/bin/…/lib/Slicer-5.4/qt-scripted-modules/DICOMImageSequencePlugin.py”, line 357, in load<br>
imageData, ijkToRas = self.loadImageData(filePath, loadable.grayscale, tempFrameVolume)<br>
File “C:/Users/86131/Desktop/Slicer 5.4.0/bin/…/lib/Slicer-5.4/qt-scripted-modules/DICOMImageSequencePlugin.py”, line 233, in loadImageData<br>
f"Could not read image {loadable.name} from file {filePath}. Error is: {errorString}")<br>
NameError: name ‘loadable’ is not defined<br>
[WARNING][Python] 10.04.2024 16:05:24 [Python] (C:\Users\86131\Desktop\Slicer 5.4.0\bin\Python\slicer\util.py:2909) - Could not load: 1: US [6] as a Image sequence</p>

---
