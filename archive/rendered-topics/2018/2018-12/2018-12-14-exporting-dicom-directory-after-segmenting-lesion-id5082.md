---
topic_id: 5082
title: "Exporting Dicom Directory After Segmenting Lesion"
date: 2018-12-14
url: https://discourse.slicer.org/t/5082
---

# Exporting DICOM directory after segmenting lesion

**Topic ID**: 5082
**Date**: 2018-12-14
**URL**: https://discourse.slicer.org/t/exporting-dicom-directory-after-segmenting-lesion/5082

---

## Post #1 by @avarghes23 (2018-12-14 22:17 UTC)

<p>Hi everybody,</p>
<p>Forgive me if this has already been mentioned but I wasn’t able to find a procedure that works with the version of Slicer I’m using (Nightly 4.11.0, 2018-11-25)  Does anyone know of a way to export a DICOM directory after segmentation? I am working with a hepatic lesion CT and have segmented the lesion, liver, and ribs. I know that I can easily export all three files as a 3D model in .OBJ or .STL format and then print it. However, I was wondering if there was a way that I can export the cropped and segmented DICOM dataset from Slicer so that another person can simply view my segmentation of the lesion slice by slice via a simple DICOM viewer.</p>
<p>I tried right-clicking on the parent DICOM directory (in my case a cropped DICOM dataset) and selecting “Export to DICOM” but when I click “Export” I receive the error message “Error occurred in exporter”</p>
<p>And another random question: Is there a way to view the 3D workspace and one of the three slices (for example: Red slice and 3D side-by-side)</p>

---

## Post #2 by @lassoan (2018-12-15 14:59 UTC)

<p>You can export segmentation as DICOM RTSTRUCT if you Install SlicerRT extension. If you install Reporting extension then you may export to DICOM Segmentation object.</p>
<p>There was an error in the image export in nightly version that I’ve fixed today, so the export should work correctly in nightly builds that you download tomorrow or later. Latest stable Slicer-4.10.0 should work as is.</p>

---

## Post #3 by @avarghes23 (2018-12-17 15:48 UTC)

<p>Thank you Andras! I will try what you recommended and update the thread if I have any issues.</p>

---

## Post #4 by @avarghes23 (2018-12-17 16:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745a17f93e300eebfca696cc4197fe876d1e8cf1.png" data-download-href="/uploads/short-url/gBipv79A9Bc0onUt7H9JzWCmeRP.png?dl=1" title="50%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745a17f93e300eebfca696cc4197fe876d1e8cf1_2_690x289.png" alt="50%20AM" data-base62-sha1="gBipv79A9Bc0onUt7H9JzWCmeRP" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745a17f93e300eebfca696cc4197fe876d1e8cf1_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745a17f93e300eebfca696cc4197fe876d1e8cf1_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745a17f93e300eebfca696cc4197fe876d1e8cf1_2_1380x578.png 2x" data-dominant-color="9E9E9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">50%20AM</span><span class="informations">2330×978 480 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I downloaded the most recent nightly build of Slicer as well as the SlicerRT extension and am still getting the same error after clicking “Export”. Is there a step in the workflow that I am missing?</p>
<p>I am running MacOS High Sierra 10.13.6</p>

---

## Post #5 by @lassoan (2018-12-17 17:24 UTC)

<p>Could you please upload the application log (menu: Help / Report a bug) to somewhere and post the link here?</p>

---

## Post #6 by @avarghes23 (2018-12-17 17:32 UTC)

<p>I apologize in advance if this makes this post (and the thread) unnecessarily long but here is the application log</p>
<details>
<summary>
Logs</summary>
<p>[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - Session start time …: 2018-12-17 12:22:27<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - Slicer version …: 4.11.0-2018-12-16 (revision 27662) macosx-amd64 - installed release<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - Operating system …: Mac OS X / 10.13.6 / 17G65 - 64-bit<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - Memory …: 8192 MB physical, 4096 MB virtual<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-7500 CPU @ 3.40GHz, 4 cores, 4 logical processors<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 17.12.2018 12:22:27 [] (unknown:0) - Additional module paths …: /Applications/Slicer Nightly.app/Contents/Extensions-27662/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/PETDICOMExtension/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/DCMQI/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/AnglePlanesExtension/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/EasyClip/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MatlabBridge/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MatlabBridge/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerOpenIGTLink/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerOpenIGTLink/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MeshToLabelMap/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/ModelToModelDistance/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/PedicleScrewSimulator/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SegmentRegistration/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MeshStatisticsExtension/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerProstate/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerProstate/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerFab/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/Sequences/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/Sequences/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/TCIABrowser/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/VolumeClip/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerHeart/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerRT/lib/Slicer-4.11/cli-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerRT/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer Nightly.app/Contents/Extensions-27662/MatlabModules<br>
[DEBUG][Python] 17.12.2018 12:22:36 [Python] (/Applications/Slicer Nightly.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Qt] 17.12.2018 12:22:41 [] (unknown:0) - MatlabExecutablePath not found, default path used: /Applications/MATLAB_XXXXX.app/bin/matlab<br>
[DEBUG][Python] 17.12.2018 12:22:43 [Python] (/Applications/Slicer Nightly.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 17.12.2018 12:22:43 [Python] (/Applications/Slicer Nightly.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 17.12.2018 12:22:44 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 17.12.2018 12:22:46 [vtkMRMLVolumeArchetypeStorageNode (0x7fd95f50ee50)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Applications/Slicer Nightly.app/Contents/Extensions-27662/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[WARNING][VTK] 17.12.2018 12:22:54 [vtkMRMLModelDisplayNode (0x7fd95f556a50)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLDisplayNode.cxx:529) - Invalid activeAttributeLocation:<br>
[WARNING][VTK] 17.12.2018 12:22:54 [vtkMRMLModelDisplayNode (0x7fd95f559620)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLDisplayNode.cxx:529) - Invalid activeAttributeLocation:<br>
[INFO][VTK] 17.12.2018 12:22:55 [vtkMRMLVolumeArchetypeStorageNode (0x7fd95f555110)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Users/AVarghese11/Documents/LIVER_DeleteAfter/601 ABD COR 3X3.nrrd. Dimensions: 512x512x100. Number of components: 1. Pixel type: int.<br>
[INFO][VTK] 17.12.2018 12:22:55 [vtkMRMLVolumeArchetypeStorageNode (0x7fd95f554f20)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Users/AVarghese11/Documents/LIVER_DeleteAfter/601 ABD COR 3X3 cropped.nrrd. Dimensions: 168x64x132. Number of components: 1. Pixel type: int.<br>
[ERROR][VTK] 17.12.2018 12:22:56 [vtkMRMLSegmentationStorageNode (0x7fd95f55df70)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx:251) - ReadDataInternal: segmentation file ‘/Users/AVarghese11/Documents/LIVER_DeleteAfter/601 ABD COR 3X3 cropped_Segmentation.seg.nrrd’ not found.<br>
[ERROR][VTK] 17.12.2018 12:22:56 [vtkTransformPolyDataFilter (0x60c000318930)] (/Volumes/Dashboards/Preview/Slicer-0-build/VTK/Filters/General/vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[ERROR][VTK] 17.12.2018 12:22:56 [vtkTransformPolyDataFilter (0x604000501830)] (/Volumes/Dashboards/Preview/Slicer-0-build/VTK/Filters/General/vtkTransformPolyDataFilter.cxx:85) - No input data<br>
[DEBUG][Qt] 17.12.2018 12:23:04 [] (unknown:0) - Switch to module:  “Data”<br>
[CRITICAL][Stream] 17.12.2018 12:24:05 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 17.12.2018 12:24:05 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 17.12.2018 12:24:05 [] (unknown:0) - KeyError: ‘DicomRtImportExportPlugin’</p>
</details>

---

## Post #7 by @lassoan (2018-12-17 17:36 UTC)

<aside class="quote no-group" data-username="avarghes23" data-post="6" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>[ERROR][VTK] 17.12.2018 12:22:56 [vtkMRMLSegmentationStorageNode (0x7fd95f55df70)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx:251) - ReadDataInternal: segmentation file ‘/Users/AVarghese11/Documents/LIVER_DeleteAfter/601 ABD COR 3X3 cropped_Segmentation.seg.nrrd’ not found.</p>
</blockquote>
</aside>
<p>It seems that the segmentation has failed to load (segmentation file was not found). Make sure you load or create a valid segmentation and try to export that.</p>

---

## Post #8 by @avarghes23 (2018-12-17 18:47 UTC)

<p>I believe the segmentation loaded correctly. But for some reason, while performing the export it says the segmentation is not found. But when I look at the data tree, the segmentation is there. Attached is a screenshot illustrating this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca6faa38e1ad35861a2fff6784e9bcde514426c3.png" data-download-href="/uploads/short-url/sSPGMw2XeXqRZCyZhMpDGze2C79.png?dl=1" title="05%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6faa38e1ad35861a2fff6784e9bcde514426c3_2_690x356.png" alt="05%20PM" data-base62-sha1="sSPGMw2XeXqRZCyZhMpDGze2C79" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6faa38e1ad35861a2fff6784e9bcde514426c3_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6faa38e1ad35861a2fff6784e9bcde514426c3_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6faa38e1ad35861a2fff6784e9bcde514426c3_2_1380x712.png 2x" data-dominant-color="B9BABA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">05%20PM</span><span class="informations">2812×1452 807 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @fedorov (2018-12-17 19:37 UTC)

<aside class="quote no-group" data-username="avarghes23" data-post="1" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>I was wondering if there was a way that I can export the cropped and segmented DICOM dataset from Slicer so that another person can simply view my segmentation of the lesion slice by slice via a simple DICOM viewer</p>
</blockquote>
</aside>
<p>If your goal is to “view my segmentation of the lesion slice by slice via a simple DICOM viewer”, you should probably export your segmentation as a DICOM image, and not as a DICOM Segmentation or DICOM RT object. You might want to look into the “Create DICOM Series” module. Do you have more details about the specific DICOM viewer another person is going to use?</p>

---

## Post #10 by @avarghes23 (2018-12-17 19:50 UTC)

<p>Thank you for the suggestion. Unfortunately, when I do this, I end up with a DICOM image stack of the cropped image stack I was previously working with (prior to segmentation). Is there a setting within the “Create a DICOM Series” module where I can specify my segmentations to be included in the exported DICOM image stack.</p>
<p>To answer your second question, I do not have more information about the DICOM viewer the other user would use. However, my understanding is that DICOM is a universal medical imaging format so in theory any program with the ability to upload a DICOM directory into it should be able to read this exported DICOM image stack.</p>

---

## Post #11 by @lassoan (2018-12-17 19:56 UTC)

<p>I agree that simple 3D image volumes can be loaded by most viewers. However, I am not sure if many viewers can show the original volume with the segmentation volume overlaid.</p>
<aside class="quote no-group" data-username="avarghes23" data-post="10" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>However, my understanding is that DICOM is a universal medical imaging format so in theory any program with the ability to upload a DICOM directory into it should be able to read this exported DICOM image stack</p>
</blockquote>
</aside>
<p>DICOM standard is fairly universal, but it is also huge and therefore each software application implements only a tiny fraction of it. You must know in advance what are the capabilities of the program that will need to read the data and export in an appropriate format (RTSTRUCT, segmentation object, or image volume).</p>

---

## Post #12 by @avarghes23 (2018-12-17 19:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>DICOM standard is fairly universal, but it is also huge and therefore each software application implements only a tiny fraction of it. You must know in advance what are the capabilities of the program that will need to read the data and export in an appropriate format (RTSTRUCT, segmentation object, or image volume).</p>
</blockquote>
</aside>
<p>Ah ok I see. So even if I was able to export the DICOM image stack from my segmentation, I would still need to make sure that the program the other user is using is capable of reading it as an RTSTRUCT, segmentation object, or image volume?</p>

---

## Post #13 by @lassoan (2018-12-17 20:14 UTC)

<p>Yes. Most DICOM viewers can display slices of CT and MRI images, but you cannot assume anything beyond that.</p>

---

## Post #14 by @fedorov (2018-12-17 20:19 UTC)

<p><a class="mention" href="/u/avarghes23">@avarghes23</a> why don’t you just point that another person to 3D Slicer?</p>
<p>I understand it may not meet your constraint of having “a simple DICOM viewer”.</p>

---

## Post #15 by @lassoan (2018-12-20 18:02 UTC)

<p>7 posts were merged into an existing topic: <a href="/t/make-slicer-simpler-to-use-for-new-users/5059/20">Make Slicer simpler to use for new users</a></p>

---

## Post #16 by @lassoan (2018-12-29 05:26 UTC)

<p>A post was split to a new topic: <a href="/t/export-volume-with-burnt-in-segmentation/5216">Export volume with burnt-in segmentation</a></p>

---
