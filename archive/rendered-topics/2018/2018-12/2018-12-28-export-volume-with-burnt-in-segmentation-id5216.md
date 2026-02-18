# Export volume with burnt-in segmentation

**Topic ID**: 5216
**Date**: 2018-12-28
**URL**: https://discourse.slicer.org/t/export-volume-with-burnt-in-segmentation/5216

---

## Post #1 by @avarghes23 (2018-12-28 15:46 UTC)

<p>Returning to the original topic of this post, I have been trying to export the segmentations made in Slicer as a DICOM dataset. What I would like to do is burn in my segmentation as an outline over the original CT dataset and then export that as a new uneditable DICOM dataset.</p>
<p>Orignal CT ------&gt; Segmentation ------&gt; New CT with Segmentation burned in</p>
<p>From the above discussion, it seems that based on the program that the end user will be viewing the file in, I need to export my segmentation as a DICOM RTSTRUCT file. I tried to replicate this tutorial (<a href="https://www.youtube.com/watch?v=nzWf4xHy1BM" class="inline-onebox" rel="noopener nofollow ugc">Create DICOM files from CT volume and segmentation - YouTube</a>) but I keep receiving an error on the export.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aeb9ed1972d91d44223907c2993ca0497368fcae.jpeg" data-download-href="/uploads/short-url/oVHql55XW6rkKawbGdfeqxtSFr0.jpeg?dl=1" title="25%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aeb9ed1972d91d44223907c2993ca0497368fcae_2_690x451.jpeg" alt="25%20AM" data-base62-sha1="oVHql55XW6rkKawbGdfeqxtSFr0" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aeb9ed1972d91d44223907c2993ca0497368fcae_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aeb9ed1972d91d44223907c2993ca0497368fcae_2_1035x676.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aeb9ed1972d91d44223907c2993ca0497368fcae_2_1380x902.jpeg 2x" data-dominant-color="A7A7AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">25%20AM</span><span class="informations">3432×2246 1.32 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Below is the error log corresponding to the screenshot:</p>
<details>
<summary>
Application log</summary>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2018-12-28 10:40:01</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.0-2018-12-16 (revision 27662) macosx-amd64 - installed release</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Mac OS X / 10.13.6 / 17G65 - 64-bit</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 8192 MB physical, 3072 MB virtual</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i5-7500 CPU @ 3.40GHz, 4 cores, 4 logical processors</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: /Applications/Slicer Nightly.app/Contents/Extensions-27662/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/PETDICOMExtension/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/DCMQI/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/AnglePlanesExtension/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/EasyClip/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MatlabBridge/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MatlabBridge/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerOpenIGTLink/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerOpenIGTLink/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MeshToLabelMap/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/ModelToModelDistance/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/PedicleScrewSimulator/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SegmentRegistration/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MeshStatisticsExtension/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerProstate/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerProstate/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerFab/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/Sequences/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/Sequences/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/TCIABrowser/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/VolumeClip/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerHeart/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerRT/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerRT/lib/Slicer-4.11/qt-scripted-modules</p>
<p>[DEBUG][Python] 28.12.2018 10:40:09 [Python] (/Applications/Slicer Nightly.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - MatlabExecutablePath not found, default path used: /Applications/MATLAB_XXXXX.app/bin/matlab</p>
<p>[DEBUG][Python] 28.12.2018 10:40:16 [Python] (/Applications/Slicer Nightly.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 28.12.2018 10:40:16 [Python] (/Applications/Slicer Nightly.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module: “Welcome”</p>
<p>[INFO][VTK] 28.12.2018 10:40:19 [vtkMRMLVolumeArchetypeStorageNode (0x7fed52b43f10)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.</p>
<p>[INFO][Stream] 28.12.2018 10:40:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [/Users/AVarghese11/.slicerrc.py]</p>
<p>[INFO][VTK] 28.12.2018 10:40:31 [vtkMRMLVolumeArchetypeStorageNode (0x7fed529ad4a0)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Users/AVarghese11/Documents/3D Slicer Segmentation Practice/AAA2/Panoramix-cropped.nrrd. Dimensions: 441x321x215. Number of components: 1. Pixel type: short.</p>
<p>[INFO][VTK] 28.12.2018 10:40:32 [vtkMRMLVolumeArchetypeStorageNode (0x7fed529aa490)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Users/AVarghese11/Documents/3D Slicer Segmentation Practice/AAA2/Segmentation-label.nrrd. Dimensions: 441x321x215. Number of components: 1. Pixel type: short.</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:32 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “MRML Scene” Reader has successfully read the file “/Users/AVarghese11/Documents/3D Slicer Segmentation Practice/AAA2/2018-12-26-Scene.mrml” “[1.76s]”</p>
<p>[DEBUG][Qt] 28.12.2018 10:40:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module: “Data”</p>
<p>[CRITICAL][Stream] 28.12.2018 10:41:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):</p>
<p>[CRITICAL][Stream] 28.12.2018 10:41:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File “&lt;string&gt;”, line 1, in &lt;module&gt;</p>
<p>[CRITICAL][Stream] 28.12.2018 10:41:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - KeyError: ‘DicomRtImportExportPlugin’</p>
</details>
<p>Please let me know if you have any suggestions</p>

---

## Post #2 by @lassoan (2018-12-29 15:57 UTC)

<p>You can only export segmentation as a DICOM RT Structure Set or Segmentation Object. You need to put segmentation node in the subject hierarchy directly under the study (the screenshot shows that you have the segmentation node under the image volume). To visualize this data, you need a DICOM viewer that can display RT Structure Set or Segmentation Object.</p>
<p>You can burn in contours in the volume using Segment Editor:</p>
<ul>
<li>Use Hollow effect to create thin contours from solid segments</li>
<li>Use Mask volume effect (in SegmentEditorExtraEffects extension) with Fill inside, Fill value = 3000, Output volume = same as master volume, to burn in the contour in the image.</li>
<li>Repeat the above steps for each segment.</li>
<li>Export the CT volume (you can choose “Scalar Volume” export type in the DICOM Export window)</li>
</ul>

---

## Post #3 by @cpinter (2018-12-30 22:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Reported this <a href="https://github.com/SlicerRt/SlicerRT/issues/98" rel="nofollow noopener">issue in SlicerRT</a>. I fixed it now, so <a class="mention" href="/u/avarghes23">@avarghes23</a> when you try again then please use the nightly on the 31st or later.</p>

---

## Post #4 by @avarghes23 (2019-01-02 17:11 UTC)

<p>Thank you both for your input. I was able to follow <a class="mention" href="/u/lassoan">@lassoan</a>’s steps, but when I execute the LabelOverlayImageFilter, I get a weird looking result (see screenshot)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e02120e8128c55c3c2412fff3076043ab4f808f.jpeg" data-download-href="/uploads/short-url/dpDjJCG8FEvt0jzyWGT7lSKD3Zl.jpeg?dl=1" title="40%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e02120e8128c55c3c2412fff3076043ab4f808f_2_566x500.jpeg" alt="40%20AM" data-base62-sha1="dpDjJCG8FEvt0jzyWGT7lSKD3Zl" width="566" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e02120e8128c55c3c2412fff3076043ab4f808f_2_566x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e02120e8128c55c3c2412fff3076043ab4f808f_2_849x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e02120e8128c55c3c2412fff3076043ab4f808f_2_1132x1000.jpeg 2x" data-dominant-color="6E6D71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">40%20AM</span><span class="informations">2970×2622 1.21 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2019-01-02 17:25 UTC)

<p>Sorry, that was a typo, if you use Hollow and Mask volume effects then there is no need to use LabelOverlayImageFilter.</p>

---
