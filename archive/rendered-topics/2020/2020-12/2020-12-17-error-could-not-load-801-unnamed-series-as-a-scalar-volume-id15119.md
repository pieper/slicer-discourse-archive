---
topic_id: 15119
title: "Error Could Not Load 801 Unnamed Series As A Scalar Volume"
date: 2020-12-17
url: https://discourse.slicer.org/t/15119
---

# Error: Could not load: 801: Unnamed Series as a Scalar Volume

**Topic ID**: 15119
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/error-could-not-load-801-unnamed-series-as-a-scalar-volume/15119

---

## Post #1 by @Mgi (2020-12-17 20:45 UTC)

<p>Hi Forum, I’m tryin to load a DICOM file from PET series and DICOM RT from PET segmentation but an error message appear: “Could not load Unnamed Series as a Scalar Volume”. Help me! please! I’m using Windows 10 OS and 3D slicer version: 4.11.20200930<br>
I attached the bug report:<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Session start time …: 2020-12-17 17:36:52<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) win-amd64 - installed release<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Operating system …: Windows /  Personal / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Memory …: 6019 MB physical, 16771 MB virtual<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Application path …: C:/Users/MARCO/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin<br>
[DEBUG][Qt] 17.12.2020 17:36:52 [] (unknown:0) - Additional module paths …: C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/DCMQI/lib/Slicer-4.11/cli-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PET-IndiC/lib/Slicer-4.11/cli-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PET-IndiC/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/cli-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETTumorSegmentation/lib/Slicer-4.11/qt-loadable-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETTumorSegmentation/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/mpReview/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/cli-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-scripted-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/cli-modules, C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 17.12.2020 17:37:08 [Python] (C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[WARNING][Qt] 17.12.2020 17:37:18 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 17.12.2020 17:37:29 [Python] (C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 17.12.2020 17:37:37 [Python] (C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Python] 17.12.2020 17:37:37 [Python] (C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[INFO][Python] 17.12.2020 17:37:42 [Python] (C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Qt] 17.12.2020 17:37:39 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 17.12.2020 17:37:42 [] (unknown:0) - This plugin dir: C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Qt] 17.12.2020 17:37:49 [] (unknown:0) - Switch to module:  “DICOM”<br>
[ERROR][Python] 17.12.2020 17:38:08 [Python] (C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py:680) - DICOM Plugin failed: SUVFactorCalculator CLI did not complete cleanly<br>
[DEBUG][Qt] 17.12.2020 17:38:06 [] (unknown:0) - Found CommandLine Module, target is  C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/cli-modules/SUVFactorCalculator.exe<br>
[DEBUG][Qt] 17.12.2020 17:38:06 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 17.12.2020 17:38:06 [] (unknown:0) - SUV Factor Calculator command line:</p>
<p>C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/cli-modules/SUVFactorCalculator.exe --returnparameterfile C:/Users/MARCO/AppData/Local/Temp/Slicer/14456_J0RfKqWdbF.params --petDICOMPath C:\Users\MARCO\AppData\Local\Temp\tmpkvj6usmj --petSeriesInstanceUID 1.2.826.0.1.3680043.2.228.6.2054.1608231753508 --rwvmDICOMPath C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RawVolume/12_PET EANM STD 10.10 PET/CT MAMA PRONO --seriesDescription PET SUV Factors --seriesNumber 1000 --instanceNumber “1”<br>
[DEBUG][Qt] 17.12.2020 17:38:08 [] (unknown:0) - SUV Factor Calculator standard output:</p>
<p>saving numbers to C:/Users/MARCO/AppData/Local/Temp/Slicer/14456_J0RfKqWdbF.params<br>
[ERROR][VTK] 17.12.2020 17:38:08 [vtkSlicerCLIModuleLogic (00000179590C7190): SUV Factor Calculator standard error:</p>
<p>WARNING: In D:\D\S\Slicer-0-build\ITK\Modules\IO\GDCM\src\itkGDCMSeriesFileNames.cxx, line 102<br>
GDCMSeriesFileNames (000001E2FD4C9850)] (D:\D\S\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2017) - No Series were found</p>
<p>Selected series instance UID not found in PET dicom path!<br>
ERROR: Failed to compute SUV<br>
[ERROR][VTK] 17.12.2020 17:38:08 [vtkSlicerCLIModuleLogic (00000179590C7190)] (D:\D\S\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2048) - SUV Factor Calculator completed with errors<br>
[INFO][VTK] 17.12.2020 17:38:08 [vtkMRMLScene (000001795CCB0D00)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) -   File “C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 675, in getLoadablesFromFileLists<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) -     loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) -   File “C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py”, line 127, in examine<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) -     rwvmFile = self.generateRWVMforFileList(fileList)<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) -   File “C:/Users/MARCO/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules/DICOMPETSUVPlugin.py”, line 169, in generateRWVMforFileList<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) -     raise RuntimeError(“SUVFactorCalculator CLI did not complete cleanly”)<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) - RuntimeError: SUVFactorCalculator CLI did not complete cleanly<br>
[CRITICAL][Stream] 17.12.2020 17:38:08 [] (unknown:0) - DICOM Plugin failed: SUVFactorCalculator CLI did not complete cleanly<br>
[ERROR][Python] 17.12.2020 17:38:09 [Python] (C:/Users/MARCO/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:273) - Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: ReferencedSOPClassUID (0008,1150) empty in ReferencedPatientSequence (type 1)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: ReferencedSOPInstanceUID (0008,1155) empty in ReferencedPatientSequence (type 1)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: StructureSetLabel (3006,0002) absent in StructureSetModule (type 1)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: StructureSetDate (3006,0008) absent in StructureSetModule (type 2)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: StructureSetTime (3006,0009) absent in StructureSetModule (type 2)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: ReferencedSOPClassUID (0008,1150) absent in RTReferencedStudySequence (type 1)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: ROIInterpreter (3006,00a6) absent in RTROIObservationsSequence (type 2)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: RTROIInterpretedType (3006,00a4) violates VR definition in RTROIObservationsSequence<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: ROIInterpreter (3006,00a6) absent in RTROIObservationsSequence (type 2)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: ROIInterpreter (3006,00a6) absent in RTROIObservationsSequence (type 2)<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: RTROIInterpretedType (3006,00a4) violates VR definition in RTROIObservationsSequence<br>
[CRITICAL][Stream] 17.12.2020 17:38:09 [] (unknown:0) - W: ROIInterpreter (3006,00a6) absent in RTROIObservationsSequence (type 2)<br>
[WARNING][Python] 17.12.2020 17:38:18 [Python] (C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py:602) - Warning in DICOM plugin Scalar Volume when examining loadable 801: Unnamed Series: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.<br>
Reference image in series does not contain geometry information. Please use caution.<br>
[CRITICAL][Stream] 17.12.2020 17:38:18 [] (unknown:0) - Warning in DICOM plugin Scalar Volume when examining loadable 801: Unnamed Series: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.<br>
[CRITICAL][Stream] 17.12.2020 17:38:18 [] (unknown:0) - Reference image in series does not contain geometry information. Please use caution.<br>
[CRITICAL][Stream] 17.12.2020 17:38:18 [] (unknown:0) -<br>
[INFO][Python] 17.12.2020 17:38:25 [Python] (C:/Users/MARCO/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[ERROR][Python] 17.12.2020 17:38:26 [Python] (C:/Users/MARCO/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:389) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Python] 17.12.2020 17:38:26 [Python] (C:/Users/MARCO/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: DCMTK<br>
[ERROR][Python] 17.12.2020 17:38:26 [Python] (C:/Users/MARCO/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:389) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[INFO][Stream] 17.12.2020 17:38:25 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkITKArchetypeImageSeriesScalarReader (0000017956B10830)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:514) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RawVolume/12_PET EANM STD 10.10 PET/CT MAMA PRONO/patientIDNoPatientID_studyID4866_seriesNumber12_seriesUnitSUVbw_SOPInstance1.2.840.113619.2.290.1460327308.1559660000.401563.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RawVolume/12_PET EANM STD 10.10 PET/CT MAMA PRONO/patientIDNoPatientID_studyID4866_seriesNumber12_seriesUnitSUVbw_SOPInstance1.2.840.113619.2.290.1460327308.1559660000.401563.dcm<br>
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
[ERROR][VTK] 17.12.2020 17:38:26 [vtkCompositeDataPipeline (000001795CDE07C0)] (D:\D\S\Slicer-0-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000017956B10830) returned failure for request: vtkInformation (000001795CD2DFD0)<br>
Debug: Off<br>
Modified Time: 256902<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 17.12.2020 17:38:26 [] (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[INFO][Stream] 17.12.2020 17:38:26 [] (unknown:0) - Loading with imageIOName: DCMTK<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkITKArchetypeImageSeriesScalarReader (0000017956B100F0)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:514) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RawVolume/12_PET EANM STD 10.10 PET/CT MAMA PRONO/patientIDNoPatientID_studyID4866_seriesNumber12_seriesUnitSUVbw_SOPInstance1.2.840.113619.2.290.1460327308.1559660000.401563.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RawVolume/12_PET EANM STD 10.10 PET/CT MAMA PRONO/patientIDNoPatientID_studyID4866_seriesNumber12_seriesUnitSUVbw_SOPInstance1.2.840.113619.2.290.1460327308.1559660000.401563.dcm<br>
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
[ERROR][VTK] 17.12.2020 17:38:26 [vtkCompositeDataPipeline (000001795CDDE6F0)] (D:\D\S\Slicer-0-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000017956B100F0) returned failure for request: vtkInformation (000001795CD2CEF0)<br>
Debug: Off<br>
Modified Time: 256985<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[CRITICAL][Stream] 17.12.2020 17:38:26 [] (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[WARNING][Python] 17.12.2020 17:38:27 [Python] (C:\Users\MARCO\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py:1951) - Could not load: 801: Unnamed Series as a Scalar Volume<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtReader (000001795C52BD00)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtReader.cxx:2045) - LoadContour: Contour sequence for ROI named ‘C1’ with number 1 is empty<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtReader (000001795C52BD00)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtReader.cxx:2045) - LoadContour: Contour sequence for ROI named ‘C1_nestle’ with number 2 is empty<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtReader (000001795C52BD00)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtReader.cxx:2045) - LoadContour: Contour sequence for ROI named ‘C2’ with number 4 is empty<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtReader (000001795C52BD00)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtReader.cxx:2045) - LoadContour: Contour sequence for ROI named ‘C2_nestle’ with number 8 is empty<br>
[WARNING][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtImportExportModuleLogic (0000017943BDC870)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:1480) - LoadRtStructureSet: Invalid structure ROI data for ROI named ‘C1’ in file ‘C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RoiVolume/patientIDNoPatientID_studyID4866_seriesNumber12_all_RTSTRUCT.dcm’ (internal ROI index: 0)<br>
[WARNING][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtImportExportModuleLogic (0000017943BDC870)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:1480) - LoadRtStructureSet: Invalid structure ROI data for ROI named ‘C1_nestle’ in file ‘C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RoiVolume/patientIDNoPatientID_studyID4866_seriesNumber12_all_RTSTRUCT.dcm’ (internal ROI index: 1)<br>
[WARNING][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtImportExportModuleLogic (0000017943BDC870)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:1480) - LoadRtStructureSet: Invalid structure ROI data for ROI named ‘C2’ in file ‘C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RoiVolume/patientIDNoPatientID_studyID4866_seriesNumber12_all_RTSTRUCT.dcm’ (internal ROI index: 2)<br>
[WARNING][VTK] 17.12.2020 17:38:26 [vtkSlicerDicomRtImportExportModuleLogic (0000017943BDC870)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:1480) - LoadRtStructureSet: Invalid structure ROI data for ROI named ‘C2_nestle’ in file ‘C:/Users/MARCO/data/FCDN_NEOADJ_BREAST_001_NoPatientID_4866_12/RoiVolume/patientIDNoPatientID_studyID4866_seriesNumber12_all_RTSTRUCT.dcm’ (internal ROI index: 3)<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkMRMLSubjectHierarchyNode (0000017957246A40)] (D:\D\S\Slicer-0\Modules\Loadable\SubjectHierarchy\Logic\vtkSlicerSubjectHierarchyModuleLogic.cxx:123) - vtkSlicerSubjectHierarchyModuleLogic::InsertDicomSeriesInHierarchy: Subject hierarchy item with DICOM UID ‘1.2.826.0.1.3680043.2.228.6.2054.1608232401761’ cannot be found<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkMRMLScene (000001793DA76570)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:2944) - vtkSlicerDicomRtImportExportModuleLogic::InsertSeriesInSubjectHierarchy: Patient item has not been created for series with Instance UID 1.2.826.0.1.3680043.2.228.6.2054.1608232401761<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkMRMLScene (000001793DA76570)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:2985) - vtkSlicerDicomRtImportExportModuleLogic::InsertSeriesInSubjectHierarchy: Study item has not been created for series with Instance UID 1.2.826.0.1.3680043.2.228.6.2054.1608232401761<br>
[ERROR][VTK] 17.12.2020 17:38:26 [vtkMRMLScene (000001793DA76570)] (D:\D\S\S-0-E-b\SlicerRT\DicomRtImportExport\Logic\vtkSlicerDicomRtImportExportModuleLogic.cxx:3004) - vtkSlicerDicomRtImportExportModuleLogic::InsertSeriesInSubjectHierarchy: Failed to insert series with Instance UID 1.2.826.0.1.3680043.2.228.6.2054.1608232401761<br>
[CRITICAL][Stream] 17.12.2020 17:38:27 [] (unknown:0) - Could not load: 801: Unnamed Series as a Scalar Volume</p>

---

## Post #2 by @pieper (2020-12-17 22:14 UTC)

<p>Did you try the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">dicom troubleshooting</a> steps?</p>

---
