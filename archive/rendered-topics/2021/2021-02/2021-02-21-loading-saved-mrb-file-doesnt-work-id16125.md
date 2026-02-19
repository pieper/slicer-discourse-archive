---
topic_id: 16125
title: "Loading Saved Mrb File Doesnt Work"
date: 2021-02-21
url: https://discourse.slicer.org/t/16125
---

# Loading saved mrb file doesn't work

**Topic ID**: 16125
**Date**: 2021-02-21
**URL**: https://discourse.slicer.org/t/loading-saved-mrb-file-doesnt-work/16125

---

## Post #1 by @mohammed_alshakhas (2021-02-21 22:32 UTC)

<p>I’m trying to .mrb file i made. however, that doesn’t do anything at all.</p>
<p>can’t figure out the issue, thnak you for help!</p>

---

## Post #2 by @lassoan (2021-02-21 22:35 UTC)

<p>Please copy-paste here the complete application log (menu: Help / Report a bug).</p>

---

## Post #3 by @mohammed_alshakhas (2021-02-24 09:47 UTC)

<p>[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Session start time …: 2021-02-24 09:32:31<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) macosx-amd64 - installed release<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Operating system …: macOS / 11.2 / 20D64 - 64-bit<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Memory …: 8192 MB physical, 9216 MB virtual<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - CPU …:  Apple M1, 8 cores, 8 logical processors<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 24.02.2021 09:32:31 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 24.02.2021 09:32:32 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 24.02.2021 09:32:33 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 24.02.2021 09:32:33 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 24.02.2021 09:32:33 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 24.02.2021 09:32:33 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 24.02.2021 09:33:00 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 24.02.2021 09:33:07 [] (unknown:0) - Switch to module:  “SceneViews”<br>
[DEBUG][Qt] 24.02.2021 09:33:11 [] (unknown:0) - Switch to module:  “VolumeRendering”<br>
[INFO][VTK] 24.02.2021 09:33:11 [vtkMRMLScene (0x7fbc3630fd80)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][VTK] 24.02.2021 09:33:11 [vtkMRMLScene (0x7fbc3630fd80)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx:762) - vtkMRMLScene::Import<br>
[DEBUG][Qt] 24.02.2021 09:33:20 [] (unknown:0) - Switch to module:  “Data”<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkITKArchetypeDiffusionTensorImageReaderFile (0x7fbc363522a0)] (/Volumes/D/S/S-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:705) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb. ITK exception info: error in unknown:  Could not create IO object for reading file /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb<br>
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
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkCompositeDataPipeline (0x600002aa23e0)] (/Volumes/D/S/S-0-build/VTK/Common/ExecutionModel/vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(0x7fbc363522a0) returned failure for request: vtkInformation (0x600000d20880)<br>
Debug: Off<br>
Modified Time: 295004<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkITKArchetypeImageSeriesVectorReaderSeries (0x7fbc3639ee50)] (/Volumes/D/S/S-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:705) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb. ITK exception info: error in unknown:  Could not create IO object for reading file /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb<br>
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
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkCompositeDataPipeline (0x600002aa2220)] (/Volumes/D/S/S-0-build/VTK/Common/ExecutionModel/vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(0x7fbc3639ee50) returned failure for request: vtkInformation (0x600000d21f00)<br>
Debug: Off<br>
Modified Time: 296513<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkITKArchetypeImageSeriesVectorReaderFile (0x7fbc363a00a0)] (/Volumes/D/S/S-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:705) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb. ITK exception info: error in unknown:  Could not create IO object for reading file /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb<br>
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
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkCompositeDataPipeline (0x600002aa2140)] (/Volumes/D/S/S-0-build/VTK/Common/ExecutionModel/vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesVectorReaderFile(0x7fbc363a00a0) returned failure for request: vtkInformation (0x600000d27040)<br>
Debug: Off<br>
Modified Time: 296608<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkITKArchetypeImageSeriesScalarReader (0x7fbc3639ca20)] (/Volumes/D/S/S-0/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx:705) - vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb. ITK exception info: error in unknown:  Could not create IO object for reading file /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb<br>
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
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkCompositeDataPipeline (0x600002aa17a0)] (/Volumes/D/S/S-0-build/VTK/Common/ExecutionModel/vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0x7fbc3639ca20) returned failure for request: vtkInformation (0x600000d25dc0)<br>
Debug: Off<br>
Modified Time: 297409<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkMRMLNRRDStorageNode (0x7fbc3639eca0)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLNRRDStorageNode.cxx:187) - ReadData: This is not a nrrd file<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkMRMLVolumeArchetypeStorageNode (0x7fbc363520a0)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:387) - ReadDataInternal: Cannot read file as a volume of type DiffusionTensorVolume[fullName = /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb [reader 0th file name = /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb]<br>
FileFormatError<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkMRMLNRRDStorageNode (0x7fbc3639ec50)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLNRRDStorageNode.cxx:187) - ReadData: This is not a nrrd file<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkMRMLVolumeArchetypeStorageNode (0x7fbc3639ec50)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:323) - ReadDataInternal: Failed to instantiate a file reader<br>
[ERROR][VTK] 24.02.2021 09:34:16 [vtkMRMLVolumeArchetypeStorageNode (0x7fbc3639c820)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:387) - ReadDataInternal: Cannot read file as a volume of type Volume[fullName = /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb [reader 0th file name = /Users/Mohammad/Documents/slicer work/2021-02-24-Scene.mrb]<br>
FileFormatError<br>
[INFO][VTK] 24.02.2021 09:34:16 [vtkMRMLScene (0x7fbc95c87bb0)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 24.02.2021 09:34:45 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 24.02.2021 09:34:48 [] (unknown:0) - Switch to module:  “Markups”<br>
[DEBUG][Qt] 24.02.2021 09:34:49 [] (unknown:0) - Switch to module:  “Transforms”<br>
[WARNING][Qt] 24.02.2021 09:34:49 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:49 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:49 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:49 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[DEBUG][Qt] 24.02.2021 09:34:50 [] (unknown:0) - Switch to module:  “Models”<br>
[DEBUG][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 24.02.2021 09:34:52 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /Volumes/D/S/S-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
[DEBUG][Qt] 24.02.2021 09:34:53 [] (unknown:0) - Switch to module:  “Data”<br>
[INFO][VTK] 24.02.2021 09:36:05 [vtkMRMLScene (0x7fbc95ce9cc0)] (/Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 24.02.2021 09:36:24 [] (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 24.02.2021 09:36:28 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 24.02.2021 09:36:39 [] (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 24.02.2021 09:36:40 [] (unknown:0) - Switch to module:  “Models”<br>
[DEBUG][Qt] 24.02.2021 09:36:40 [] (unknown:0) - Switch to module:  “Transforms”<br>
[DEBUG][Qt] 24.02.2021 09:36:42 [] (unknown:0) - Switch to module:  “Markups”<br>
[DEBUG][Qt] 24.02.2021 09:36:43 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 24.02.2021 09:36:44 [] (unknown:0) - Switch to module:  “VolumeRendering”<br>
[DEBUG][Qt] 24.02.2021 09:36:44 [] (unknown:0) - Switch to module:  “SceneViews”<br>
[DEBUG][Qt] 24.02.2021 09:36:45 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 24.02.2021 09:36:48 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 24.02.2021 12:46:49 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #4 by @lassoan (2021-02-26 04:25 UTC)

<p>It seems that you are trying to load the .mrb file as a volume. You should be able to load it if you leave the default “MRB Slicer Data Bundle” value in the description column in “Add data…” window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff5aa2143252f8a44f9d05cd744669d097c7b5e5.png" data-download-href="/uploads/short-url/AqXW0aZGbCfaMLHUHJuxeqHFwC9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff5aa2143252f8a44f9d05cd744669d097c7b5e5.png" alt="image" data-base62-sha1="AqXW0aZGbCfaMLHUHJuxeqHFwC9" width="690" height="253" data-dominant-color="404141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1110×408 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @mohammed_alshakhas (2021-02-26 06:21 UTC)

<p>it is the same, i tried changing it to volume out of desperation but still not working though</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70bc59d9e2add3798f0db529ca344ed71cc71bab.jpeg" data-download-href="/uploads/short-url/g5j12Biddtu0CoWcD1lL2WmlRur.jpeg?dl=1" title="Screen Shot 2021-02-26 at 09.19.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70bc59d9e2add3798f0db529ca344ed71cc71bab_2_690x431.jpeg" alt="Screen Shot 2021-02-26 at 09.19.55" data-base62-sha1="g5j12Biddtu0CoWcD1lL2WmlRur" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70bc59d9e2add3798f0db529ca344ed71cc71bab_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70bc59d9e2add3798f0db529ca344ed71cc71bab_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70bc59d9e2add3798f0db529ca344ed71cc71bab_2_1380x862.jpeg 2x" data-dominant-color="2E2E34"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-26 at 09.19.55</span><span class="informations">2880×1800 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @muratmaga (2021-02-26 06:41 UTC)

<p>Your screenshot for MRB shows something like “com~apple~CloudDocs”<br>
Is it by any chance a cloud synced/mapped folder?</p>
<p>I am not a Mac user, but have seen strange issues with cloud storage mapped locally on Windows.</p>
<p>Can you try copying the MRB to your desktop and retry?</p>

---

## Post #7 by @mohammed_alshakhas (2021-02-26 06:44 UTC)

<p>i did , this only one file im working on on multiple computers, i actually fail to load file i created on same laptop even</p>

---

## Post #8 by @lassoan (2021-02-26 13:55 UTC)

<p>This is on a new M1, so it may be related to operating system changes or porting over settings from another computer. The user also reported the problem in another topic - let’s continue the discussion there:</p>
<aside class="quote" data-post="3" data-topic="16228">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-4-11-on-m1-not-loading-mrb-file/16228/3">Slicer 4.11 on M1 not loading .mrb file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    it was ok till installed 4.11 . 
still able to do full work , like i started the work fine . the issue is only when i load saved file in .mrb
  </blockquote>
</aside>


---
