---
topic_id: 847
title: "Vtk Failure And Segment Editor Failure"
date: 2017-08-09
url: https://discourse.slicer.org/t/847
---

# VTK failure and Segment Editor failure

**Topic ID**: 847
**Date**: 2017-08-09
**URL**: https://discourse.slicer.org/t/vtk-failure-and-segment-editor-failure/847

---

## Post #1 by @stevenagl12 (2017-08-09 17:42 UTC)

<p>For some reason when I go to apply my newly created segmentation using the segment editor (mainly using fastmarching) the segment disappears and is irretrievable.</p>
<p>In addition, I have gotten warnings about a VTK leak. I’ve attached my log file from when I go the leak below, not sure if this helps:</p>
<pre><code class="lang-auto">[WARNING][VTK] 09.08.2017 11:52:17 [] (unknown:0) - Generic Warning: In c:\d\n\e-0\markupstomodel\markupstomodel\logic\CreateClosedSurfaceUtil.h, line 466
Surface extrusion amount smaller than 0.01 : 0. Consider checking the points for singularity. Setting surface extrusion amount to default 0.01.
[WARNING][VTK] 09.08.2017 11:52:17 [] (unknown:0) - Generic Warning: In c:\d\n\e-0\markupstomodel\markupstomodel\logic\CreateClosedSurfaceUtil.h, line 466
Surface extrusion amount smaller than 0.01 : 0. Consider checking the points for singularity. Setting surface extrusion amount to default 0.01.
[WARNING][VTK] 09.08.2017 11:52:54 [] (unknown:0) - Generic Warning: In c:\d\n\e-0\markupstomodel\markupstomodel\logic\CreateClosedSurfaceUtil.h, line 368
Extent ranges not provided in order largest to smallest. Unexpected results may occur.
[WARNING][VTK] 09.08.2017 11:52:54 [] (unknown:0) - Generic Warning: In c:\d\n\e-0\markupstomodel\markupstomodel\logic\CreateClosedSurfaceUtil.h, line 368
Extent ranges not provided in order largest to smallest. Unexpected results may occur.

[ERROR][VTK] 09.08.2017 11:54:14 [vtkMRMLScene (00000253B4BD29D0)] (C:\D\N\Slicer-0\Modules\Loadable\Segmentations\Logic\vtkSlicerSegmentationsModuleLogic.cxx:674) - vtkSlicerSegmentationsModuleLogic::GetSegmentForSegmentSubjectHierarchyItem: Segmentation does not contain segment with given ID: Segment_2
[WARNING][VTK] 09.08.2017 11:54:15 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore
[WARNING][VTK] 09.08.2017 11:54:15 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore
[WARNING][VTK] 09.08.2017 11:54:15 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore
[WARNING][VTK] 09.08.2017 11:54:15 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore
[WARNING][VTK] 09.08.2017 11:54:15 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore
[WARNING][VTK] 09.08.2017 11:54:16 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore
[WARNING][VTK] 09.08.2017 11:54:16 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore
[...]
[WARNING][VTK] 09.08.2017 11:54:20 [vtkSegmentationHistory (00000253C1DCA980)] (C:\D\N\Slicer-0\Libs\vtkSegmentationCore\vtkSegmentationHistory.cxx:207) - vtkSegmentation::RestorePreviousState failed: There are no previous state available for restore

[CRITICAL][Qt] 09.08.2017 11:54:24 [] (unknown:0) - class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  "PercentMax"  cannot be found for effect  "Fast Marching"
[CRITICAL][Qt] 09.08.2017 11:54:24 [] (unknown:0) - double __cdecl qSlicerSegmentEditorAbstractEffect::doubleParameter(class QString) : Parameter named  "PercentMax"  cannot be converted to floating point number!
[...]
[CRITICAL][Qt] 09.08.2017 11:54:24 [] (unknown:0) - double __cdecl qSlicerSegmentEditorAbstractEffect::doubleParameter(class QString) : Parameter named  "PercentMax"  cannot be converted to floating point number!
[CRITICAL][Qt] 09.08.2017 11:54:24 [] (unknown:0) - class QString __cdecl qSlicerSegmentEditorAbstractEffect::parameter(class QString) : Parameter named  "PercentMax"  cannot be found for effect  "Fast Marching"
[CRITICAL][Qt] 09.08.2017 11:54:24 [] (unknown:0) - double __cdecl qSlicerSegmentEditorAbstractEffect::doubleParameter(class QString) : Parameter named  "PercentMax"  cannot be converted to floating point number!

[WARNING][Qt] 09.08.2017 11:54:25 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 09.08.2017 11:54:25 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
</code></pre>

---

## Post #2 by @cpinter (2017-08-09 18:16 UTC)

<p>Can you please describe what steps did you <em>exactly</em> took on what input?</p>
<p>Based on the log the problem doesn’t seem to be in VTK but in SegmentEditor, when interpreting the parameters. Can you please elaborate on what parameters you use? A screenshot about right before clicking Apply could also help.</p>
<p>Thanks!</p>

---

## Post #4 by @stevenagl12 (2017-08-14 13:09 UTC)

<p>I opened a volume of dicom images, through the dicom browser, switched to the segment editor, used the pain effect to label some pixel values, then switched to the fast marching effect and initialized it, and clicked apply and the segmentation disappeared. Then I switched and tried a fast grow cut after relabeling pixels with the paint effect, initialized it, and after it ran and I had a good segmentation, I clicked apply again and it did the same thing. So I shut the program down to restart it, and that’s when it gave me the VTK leak error. I restarted and tried several more Segment Editor effects but got the same results.</p>

---

## Post #5 by @lassoan (2017-08-14 13:24 UTC)

<p>Thanks for reporting this. Could you please send the application log? You can find the logs of the last 10 sessions in menu: Help / Report a bug. Make sure there is no patient information is includes in the text.</p>

---

## Post #6 by @stevenagl12 (2017-08-14 13:38 UTC)

<p>I reported the log file above with the errors and warnings from Slicer. I redownloaded the nightly build that you suggested in a different post today because of the extension issues, so I doubt I will be able to give you anything more. I am able to do all the segmentation effects on that build it seems though.</p>

---

## Post #7 by @lassoan (2017-08-14 13:41 UTC)

<p>I would need the complete logs but at least the log file header that shows exact version information etc.</p>

---
