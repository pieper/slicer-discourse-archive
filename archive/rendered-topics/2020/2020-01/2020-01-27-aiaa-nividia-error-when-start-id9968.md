# AIAA NIVIDIA error when start

**Topic ID**: 9968
**Date**: 2020-01-27
**URL**: https://discourse.slicer.org/t/aiaa-nividia-error-when-start/9968

---

## Post #1 by @ahmed.elsakka (2020-01-27 14:43 UTC)

<p>hello i have a problem using AIAA NIVIDIA TOOL FOR SEGMENTATION. when i click start to begin segmentation, an error cause slicer to expectantly close</p>
<p>[DEBUG][Python] 27.01.2020 15:08:03 [Python] (C:/Users/Split/AppData/Roaming/NA-MIC/Extensions-28746/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py:732) - Node Id: vtkMRMLScalarVolumeNode2 =&gt; C:\Users\Split\AppData\Local\Temp\Slicer\slicer-aiaa2020-01-27_15+02+46.625\tmp7kbhpzha.nii.gz</p>
<p>[DEBUG][Python] 27.01.2020 15:08:03 [Python] (C:/Users/Split/AppData/Roaming/NA-MIC/Extensions-28746/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py:744) - Using Saved Node from: C:\Users\Split\AppData\Local\Temp\Slicer\slicer-aiaa2020-01-27_15+02+46.625\tmp7kbhpzha.nii.gz</p>
<p>[DEBUG][Python] 27.01.2020 15:08:03 [Python] (C:\Users\Split\AppData\Roaming\NA-MIC\Extensions-28746\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py:169) - Preparing for Annotation/Dextr3D Action</p>
<p>[DEBUG][Python] 27.01.2020 15:08:03 [Python] (C:\Users\Split\AppData\Roaming\NA-MIC\Extensions-28746\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py:305) - Reading Image from: C:\Users\Split\AppData\Local\Temp\Slicer\slicer-aiaa2020-01-27_15+02+46.625\tmp7kbhpzha.nii.gz</p>
<p>[ERROR][Python] 27.01.2020 15:08:03 [Python] (C:\Users\Split\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-24\bin\Python\slicer\util.py:1548) - Run Annotation for model: annotation_mri_brain_tumors_t1ce_tc for segment: Segment_1 - unexpected error.</p>
<p>[CRITICAL][Stream] 27.01.2020 15:08:03 [] (unknown:0) - Run Annotation for model: annotation_mri_brain_tumors_t1ce_tc for segment: Segment_1 - unexpected error.</p>

---

## Post #2 by @lassoan (2020-01-27 20:07 UTC)

<p>Does it all work well if you use example data sets shown in <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#tutorials-and-examples">this tutorial</a>?</p>
<p>Does the <code>C:\Users\Split\AppData\Local\Temp\Slicer\slicer-aiaa2020-01-27_15+02+46.625\tmp7kbhpzha.nii.gz</code> file exist? Is it valid? Can you load it into Slicer by drag-and-dropping? (the file may be deleted automatically when you click OK, so try to make a copy of the file before clicking OK in the error popup).</p>

---
