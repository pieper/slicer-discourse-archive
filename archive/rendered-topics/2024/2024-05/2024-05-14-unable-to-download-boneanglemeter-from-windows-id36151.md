# Unable to download BoneAngleMeter from Windows

**Topic ID**: 36151
**Date**: 2024-05-14
**URL**: https://discourse.slicer.org/t/unable-to-download-boneanglemeter-from-windows/36151

---

## Post #1 by @Rosamv (2024-05-14 17:43 UTC)

<p>Hello,<br>
I am trying to download BoneAngleMeter to Slicer on a Windows PC. The ZIP files provided do not appear to be working. Could someone please check this out for me? Here are the error logs. Thanks! Rod</p>
<p>[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20240514_133309<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 22621, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 7924 MB physical, 11026 MB virtual<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/vet/AppData/Local/slicer.org/Slicer 5.6.2/bin<br>
[DEBUG][Qt] 14.05.2024 13:33:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32448/OsteotomyPlanner/lib/Slicer-5.6/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/OsteotomyPlanner/lib/Slicer-5.6/cli-modules</a>, <a href="http://slicer.org/Extensions-32448/OsteotomyPlanner/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/OsteotomyPlanner/lib/Slicer-5.6/qt-scripted-modules</a>, C:/Users/vet/Downloads/BoneAngleMeter_public-1.0.1 (1)/BoneAngleMeter_public-1.0.1<br>
[DEBUG][Python] 14.05.2024 13:33:12 [Python] (C:\Users\vet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 14.05.2024 13:33:12 [Python] (C:\Users\vet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 14.05.2024 13:33:12 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 14.05.2024 13:33:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Local filepath received via command-line:  “C:\Users\vet\AppData\Local\Temp\2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a\README.md”<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkITKArchetypeDiffusionTensorImageReaderFile (0000014C5B0DB400)] (vtkITKArchetypeImageSeriesReader.cxx:525) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md<br>
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
[ERROR][VTK] 14.05.2024 13:33:13 [vtkCompositeDataPipeline (0000014C12D415E0)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile (0000014C5B0DB400) returned failure for request: vtkInformation (0000014C13422A30)<br>
Debug: Off<br>
Modified Time: 192389<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkITKArchetypeImageSeriesVectorReaderSeries (0000014C5B0DB400)] (vtkITKArchetypeImageSeriesReader.cxx:525) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md<br>
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
[ERROR][VTK] 14.05.2024 13:33:13 [vtkCompositeDataPipeline (0000014C12D40BC0)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries (0000014C5B0DB400) returned failure for request: vtkInformation (0000014C13429870)<br>
Debug: Off<br>
Modified Time: 193902<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkITKArchetypeImageSeriesScalarReader (0000014C5B0DDC00)] (vtkITKArchetypeImageSeriesReader.cxx:525) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md<br>
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
[ERROR][VTK] 14.05.2024 13:33:13 [vtkCompositeDataPipeline (0000014C12D3FE40)] (vtkExecutive.cxx:742) - Algorithm vtkITKArchetypeImageSeriesScalarReader (0000014C5B0DDC00) returned failure for request: vtkInformation (0000014C134197A0)<br>
Debug: Off<br>
Modified Time: 194709<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLMultiVolumeStorageNode (0000014C132FADB0)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node README (vtkMRMLMultiVolumeNode1) from filename=‘C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md’<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLNRRDStorageNode (0000014C132FFE20)] (vtkMRMLNRRDStorageNode.cxx:187) - ReadData: This is not a nrrd file<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLNRRDStorageNode (0000014C132FFE20)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node README (vtkMRMLDiffusionWeightedVolumeNode1) from filename=‘C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md’<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLVolumeArchetypeStorageNode (0000014C11D81180)] (vtkMRMLVolumeArchetypeStorageNode.cxx:412) - vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type DiffusionTensorVolume [fullName = C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 0 files. File reader used the archetype file name of C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md <span class="chcklst-box fa fa-square-o fa-fw"></span>.<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLVolumeArchetypeStorageNode (0000014C11D81180)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node README (vtkMRMLDiffusionTensorVolumeNode1) from filename=‘C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md’<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLNRRDStorageNode (0000014C13302340)] (vtkMRMLNRRDStorageNode.cxx:187) - ReadData: This is not a nrrd file<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLNRRDStorageNode (0000014C13302340)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node README (vtkMRMLVectorVolumeNode1) from filename=‘C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md’<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLVolumeArchetypeStorageNode (0000014C11D80900)] (vtkMRMLVolumeArchetypeStorageNode.cxx:352) - vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Failed to instantiate a file reader<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLVolumeArchetypeStorageNode (0000014C11D80900)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node README (vtkMRMLVectorVolumeNode2) from filename=‘C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md’<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLVolumeArchetypeStorageNode (0000014C11D846A0)] (vtkMRMLVolumeArchetypeStorageNode.cxx:412) - vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type Volume [fullName = C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 0 files. File reader used the archetype file name of C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md <span class="chcklst-box fa fa-square-o fa-fw"></span>.<br>
[ERROR][VTK] 14.05.2024 13:33:13 [vtkMRMLVolumeArchetypeStorageNode (0000014C11D846A0)] (vtkMRMLStorageNode.cxx:1294) - vtkMRMLStorageNode::ReadData: Failed to read node README (vtkMRMLScalarVolumeNode1) from filename=‘C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md’<br>
[WARNING][Qt] 14.05.2024 13:33:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - void __cdecl qSlicerIOManager::showLoadNodesResultDialog(bool,class vtkMRMLMessageCollection *) Errors occurred while loading nodes: “Error: Loading C:/Users/vet/AppData/Local/Temp/2f0518dc-60fd-4c56-8626-7f79b1b0fc8a_slicer3d.zip.c8a/README.md -  load failed.\n”</p>

---
