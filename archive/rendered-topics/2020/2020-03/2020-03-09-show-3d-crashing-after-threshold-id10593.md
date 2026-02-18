# Show 3D crashing after threshold

**Topic ID**: 10593
**Date**: 2020-03-09
**URL**: https://discourse.slicer.org/t/show-3d-crashing-after-threshold/10593

---

## Post #1 by @rfarman (2020-03-09 04:19 UTC)

<p>Hi,</p>
<p>Was wondering if anyone could help me! I am trying to segment a frog skeleton. Once I have used threshold and want to view the 3d image it crashes. I have everything closed except for slicer and I suspect it might be something to do with my laptops capabilities. My specs are Intel Core I7 - 9750H, 2.6ghz, 16gb ram, NVIDIA GeForce GTX 1660 Ti.</p>
<p>Is my hardware sufficient and is there anyway I can change something for it to work?</p>
<p>Any help would be very much appreciated!</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2020-03-09 04:24 UTC)

<p>How big is your dataset?</p>
<p>Can you post the log file from the Help-&gt;Report a bug and then choose the session log that crash occured (usually the one below the latest).</p>

---

## Post #3 by @rfarman (2020-03-09 05:28 UTC)

<p>Hi,</p>
<p>The file is 6.7gb and I copied everything except for the welcome.</p>
<p>Hopefully I have copied everything correctly.</p>
<p>Thank you!</p>
<p>[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - Session start time …: 2020-03-09 16:17:43<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - Memory …: 16196 MB physical, 32165 MB virtual<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 09.03.2020 16:17:43 [] (unknown:0) - Additional module paths …: C:/Users/short/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules<br>
[DEBUG][Python] 09.03.2020 16:17:45 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 09.03.2020 16:17:46 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 09.03.2020 16:17:46 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>

---

## Post #4 by @muratmaga (2020-03-09 06:23 UTC)

<p>I don’t see an error message in here. Few suggestions:</p>
<ol>
<li>You re using the stable, try a preview build and see if you still have problems.</li>
<li>We typically suggest 6-10X more memory than your dataset for segmentation tasks. Given the size of the dataset, you might be running out of memory. You can try downsampling your volume by <code>Crop Volume</code> module to see if working with lower resolution helps.</li>
<li>Make sure to check Nvidia control panel to see if the Slicer is actually set to run on the geforce 1650 GPU. <a href="https://discourse.slicer.org/t/can-i-choose-which-gpu-to-use/3149" class="inline-onebox">Can I choose which GPU to use?</a>
</li>
</ol>

---

## Post #5 by @lassoan (2020-03-09 12:53 UTC)

<p>Please send the log of the session where the crash occurred. In Help / Report a bug dialog, there is a list where you can select previous sessions.</p>

---

## Post #6 by @rfarman (2020-03-10 01:46 UTC)

<p>Thank you Murat! I changed the settings in Nvidia control panel and changed to the preview build. That seemed to fix the problem!!</p>

---

## Post #7 by @rfarman (2020-03-10 01:47 UTC)

<p>The suggestions given to me by Murat worked. Would you still like the report?</p>
<p>Cheers</p>

---

## Post #8 by @lassoan (2020-03-10 01:48 UTC)

<p>If it’s not too much trouble, then it would be interesting how the error shows up in the log (we might then identify the problem easier next time, only by looking at the logs).</p>

---

## Post #9 by @rfarman (2020-03-10 01:57 UTC)

<p>Not a problem! I believe this is the one from yesterday.</p>
<p>[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - Session start time …: 2020-03-09 16:00:22<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - Memory …: 16196 MB physical, 32165 MB virtual<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 09.03.2020 16:00:22 [] (unknown:0) - Additional module paths …: C:/Users/short/AppData/Roaming/NA-MIC/Extensions-28257/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules<br>
[DEBUG][Python] 09.03.2020 16:00:24 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 09.03.2020 16:00:25 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 09.03.2020 16:00:25 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 09.03.2020 16:00:25 [] (unknown:0) - Switch to module:  “Welcome”<br>
[ERROR][VTK] 09.03.2020 16:02:28 [vtkITKArchetypeDiffusionTensorImageReaderFile (000001E405BDF010)] (D:\D\S\Slicer-4102\Libs\vtkITK\vtkITKArchetypeDiffusionTensorImageReaderFile.cxx:175) - There is more than one file, use the vtkITKArchetypeImageSeriesReader instead<br>
[INFO][VTK] 09.03.2020 16:03:08 [vtkMRMLVolumeArchetypeStorageNode (000001E416629560)] (D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/short/Desktop/Heleioporus eyrei/Morphosource_mcz_herp_a-139552_M30020/mcz_herp_a-139552_M30020-57700_Heleioporus_eyrei_skeleton/MCZ-A139552_H_eyrei_Rec/MCZ-A139552_H_eyrei_rec0049.tif. Dimensions: 1876x872x2191. Number of components: 1. Pixel type: unsigned short.<br>
[DEBUG][Qt] 09.03.2020 16:03:08 [] (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/short/Desktop/Heleioporus eyrei/Morphosource_mcz_herp_a-139552_M30020/mcz_herp_a-139552_M30020-57700_Heleioporus_eyrei_skeleton/MCZ-A139552_H_eyrei_Rec/MCZ-A139552_H_eyrei_rec0049.tif” “[42.40s]”<br>
[DEBUG][Qt] 09.03.2020 16:13:16 [] (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 09.03.2020 16:13:17 [] (unknown:0) - ctkDoubleRangeSlider::setSingleStep( 100 ) is outside of valid bounds.<br>
[WARNING][Qt] 09.03.2020 16:13:17 [] (unknown:0) - ctkRangeWidget::setSingleStep( 100 ) is outside valid bounds<br>
[DEBUG][Qt] 09.03.2020 16:13:32 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 09.03.2020 16:13:47 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[CRITICAL][Qt] 09.03.2020 16:13:47 [] (unknown:0) - void __cdecl qSlicerSegmentationsModuleWidget::onEditSelectedSegment(void) : MRMLNodeComboBox_Segmentation is not found in Segment Editor module<br>
[DEBUG][Qt] 09.03.2020 16:14:43 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 09.03.2020 16:14:46 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[CRITICAL][Qt] 09.03.2020 16:14:46 [] (unknown:0) - void __cdecl qSlicerSegmentationsModuleWidget::onEditSelectedSegment(void) : MRMLNodeComboBox_Segmentation is not found in Segment Editor module<br>
[DEBUG][Qt] 09.03.2020 16:15:12 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[WARNING][VTK] 09.03.2020 16:15:12 [vtkMRMLSegmentationDisplayNode (000001E4083F58F0)] (D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLSegmentationDisplayNode.cxx:296) - vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=Segment_1, return default<br>
[CRITICAL][Qt] 09.03.2020 16:15:12 [] (unknown:0) - void __cdecl qMRMLSegmentationDisplayNodeWidget::updateSelectedSegmentSection(void) : No display properties found for segment ID  “Segment_1”<br>
[WARNING][VTK] 09.03.2020 16:15:12 [vtkMRMLSegmentationDisplayNode (000001E4083F58F0)] (D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLSegmentationDisplayNode.cxx:296) - vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=Segment_1, return default<br>
[CRITICAL][Qt] 09.03.2020 16:15:12 [] (unknown:0) - void __cdecl qMRMLSegmentationDisplayNodeWidget::updateSelectedSegmentSection(void) : No display properties found for segment ID  “Segment_1”<br>
[DEBUG][Qt] 09.03.2020 16:15:23 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[CRITICAL][Qt] 09.03.2020 16:15:23 [] (unknown:0) - void __cdecl qSlicerSegmentationsModuleWidget::onEditSelectedSegment(void) : MRMLNodeComboBox_Segmentation is not found in Segment Editor module</p>

---

## Post #10 by @lassoan (2020-03-10 04:53 UTC)

<p>Thank you. There does not seem to be any suspicious in this log. If you are sure that this was the session where you had problems then maybe our logs were just not detailed enough to capture more information about the issue.</p>

---

## Post #11 by @muratmaga (2020-03-10 06:02 UTC)

<p>If this was caused by opengl crash, I never managed to get any errors on windows during my tests with 4.10.2.</p>

---

## Post #12 by @lassoan (2020-03-10 13:17 UTC)

<p>By OpenGL crash, do you mean <a href="https://discourse.slicer.org/t/volume-rendering-causes-application-crash/3783/4">TDR related errors</a> or others? How did you know that it was OpenGL crash (from displayed error message, Windows logs, …)?</p>

---

## Post #13 by @muratmaga (2020-03-10 15:00 UTC)

<p>I might have misspoke, I don’t necessarily know that they are opengl issues. But always happened rendering. Preview builds are much better handling larger 3D volumes than 4.10.2.</p>

---

## Post #14 by @muratmaga (2020-03-10 15:39 UTC)

<p>Actually I do have a follow up question on this. What is the purpose of ‘adaptive’ setting in the <code>Volume Rendering</code> module? For small volumes (medical size) this has no appreciably performance difference between Normal and Adaptive. For large datasets (&gt;1 gigavoxel) Adaptive often performs poorly compared to Normal (stutters, crashes or results in lower FPS for the same volume property).</p>
<p>Can it be removed? Or at least make the Normal as the default  global setting?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #15 by @lassoan (2020-03-10 15:58 UTC)

<p>Adaptive settings is essential for lower-end graphics hardware and CPU-based volume rendering. It measures rendering time and degrades rendering settings to achieve the desired interactive refresh rate. It works very well for CPU-based rendering, but since GPU-based rendering performs a lot of processing in background threads and on the hardware, rendering time measurement is not a good estimation of how overloaded the rendering pipeline is.</p>
<p>Probably we could use “Normal” quality for GPU-based rendering by default, but unfortunately, quality mode is defined in the view node and not in the display node, so it would not be easy to change it cleanly.</p>

---

## Post #16 by @muratmaga (2020-03-10 17:46 UTC)

<p>I have seen quite a bit of the stuttering sort of 3D rendering issues for larger volumes fixed simply switching to Normal, even with integrated GPUs. Yes, I would encourage making the default setting Normal, but of course can’t comment on the feasibility.</p>

---
