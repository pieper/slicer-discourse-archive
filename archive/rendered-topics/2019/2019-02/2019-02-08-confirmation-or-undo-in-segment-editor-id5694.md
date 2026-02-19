---
topic_id: 5694
title: "Confirmation Or Undo In Segment Editor"
date: 2019-02-08
url: https://discourse.slicer.org/t/5694
---

# Confirmation or undo in Segment Editor?

**Topic ID**: 5694
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/confirmation-or-undo-in-segment-editor/5694

---

## Post #1 by @ungi (2019-02-08 16:44 UTC)

<p>I’ve just accidentally deleted an hour worth of segmentation by pressing the Remove (-) button instead of the Erase button. I got lost in monotonic segmentation and it just happened. Do you think it would be a good idea to add a pop-up dialog to confirm if the user actually wants to delete a segmentation? And/or extend the function of the Undo button in Segment Editor to be able to bring back the last deleted segmentation?</p>

---

## Post #2 by @pieper (2019-02-08 16:57 UTC)

<p>Ouch.  Yes, I think an undo at that level makes sense.</p>
<p>Also, in the past I’ve added an autosave feature to support specific workflows.</p>

---

## Post #3 by @lassoan (2019-02-08 17:01 UTC)

<p>Undo can restore deleted segments. Can you try again?</p>

---

## Post #4 by @ungi (2019-02-08 17:02 UTC)

<p>It doesn’t restore the deleted segment for me on 4.10.1, but I will download the nightly and try again.</p>

---

## Post #5 by @cpinter (2019-02-08 17:02 UTC)

<p>You mean you deleted a segment with in a segmentation wirh the Remove button in the top bar that has (Add/Remove/Show 3D/…)? Or you deleted the segmentation node somehow?</p>
<p>If just a segment, then yes, having undo cover that would be a must. Which should, but maybe there’s a bug? I don’t think a popup would be a good idea.<br>
Sorry for the time you lost because of this.</p>

---

## Post #6 by @cpinter (2019-02-08 17:03 UTC)

<p>I just tried it on 4.10.1 and it did restore the deleted segment. Can you check that specific log? It might contain something useful.</p>

---

## Post #7 by @ungi (2019-02-08 17:09 UTC)

<p>Yes, Undo does work in different scenes, but not in the one I’m working on. I will share it. Thanks for trying to reproduce.</p>

---

## Post #8 by @ungi (2019-02-08 17:15 UTC)

<p>Sorry for the large file. I don’t have a smaller one at hand to reproduce.<br>
Just delete the segment and press Undo. It doesn’t do anything, and I don’t see an error or warning message that would explain it. The special thing about this scene is that I didn’t use a master volume, just a ROI, because I’m creating a 3D segmentation from 2D+tracked ultrasound.<br>
<a href="https://1drv.ms/u/s!AhiABcbe1DBygrdCxt3piXBo9ZFrfA" class="onebox" target="_blank" rel="nofollow noopener">https://1drv.ms/u/s!AhiABcbe1DBygrdCxt3piXBo9ZFrfA</a><br>
Maybe this scene will help find a bug…</p>

---

## Post #9 by @cpinter (2019-02-08 17:17 UTC)

<p>I don’t believe scenes contain segment editor undo history, sorry. Is there any error in the log form the session when you accidentally deleted the segment?</p>

---

## Post #10 by @ungi (2019-02-08 17:23 UTC)

<p>The log can be regenerated any time. Just load the scene I linked, remove the segment in Segment Editor, and press Undo. The segment will not come back.</p>
<p>Here is the log:</p>
<p>[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - Session start time …: 2019-02-08 12:17:53<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - Slicer version …: 4.10.1 (revision 27931) win-amd64 - installed release<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - Memory …: 32706 MB physical, 53186 MB virtual<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 08.02.2019 12:17:53 [] (unknown:0) - Additional module paths …: C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27931/SlicerOpenIGTLink/lib/Slicer-4.10/qt-loadable-modules, C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27931/SlicerOpenIGTLink/lib/Slicer-4.10/qt-scripted-modules, C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27931/SlicerIGT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27931/SlicerIGT/lib/Slicer-4.10/qt-scripted-modules, C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27931/Sequences/lib/Slicer-4.10/qt-loadable-modules, C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27931/Sequences/lib/Slicer-4.10/qt-scripted-modules, C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27931/DebuggingTools/lib/Slicer-4.10/qt-scripted-modules, J:/UsAnnotationExport/LiveFeedbackExtension/LiveFeedbackModule<br>
[DEBUG][Python] 08.02.2019 12:17:57 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 08.02.2019 12:17:58 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 08.02.2019 12:17:58 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 08.02.2019 12:17:58 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 08.02.2019 12:20:59 [vtkMRMLVolumeArchetypeStorageNode (0000023D21C5A110)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: J:/Data/Bone_Segmentation/Image_Image.nrrd. Dimensions: 512x512x1. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][VTK] 08.02.2019 12:20:59 [vtkMRMLVolumeArchetypeStorageNode (0000023D21C59D50)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: J:/Data/Bone_TrainingImagesRecorded/Image_Reference.nrrd. Dimensions: 512x512x1. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][Stream] 08.02.2019 12:20:59 [] (unknown:0) - CreateVTKTransformFromITK - SetVTKLinearTransformFromITK conversionSuccess:1<br>
[INFO][VTK] 08.02.2019 12:20:59 [vtkMRMLVolumeArchetypeStorageNode (0000023D21C59B70)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: J:/Data/Bone_TrainingImagesRecorded/ScoutScan.nrrd. Dimensions: 27x23x29. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][VTK] 08.02.2019 12:20:59 [vtkMRMLVolumeArchetypeStorageNode (0000023D21C5A2F0)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: J:/Data/Bone_TrainingImagesRecorded/liveReconstruction.nrrd. Dimensions: 98x83x105. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][Stream] 08.02.2019 12:20:59 [] (unknown:0) - CreateVTKTransformFromITK - SetVTKLinearTransformFromITK conversionSuccess:1<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:21:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[DEBUG][Qt] 08.02.2019 12:21:16 [] (unknown:0) - “MRML Scene” Reader has successfully read the file “J:/Data/Bone_Segmentation/2019-01-31-Scene.mrml” “[17.00s]”<br>
[DEBUG][Qt] 08.02.2019 12:22:04 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[INFO][Stream] 08.02.2019 12:22:04 [] (unknown:0) - C:/Program Files/Slicer 4.10.1/bin/…/lib/Slicer-4.10/qt-scripted-modules\Resources\UI/SegmentEditor.ui<br>
[WARNING][Qt] 08.02.2019 12:22:07 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:22:07 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:22:07 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:22:07 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:22:07 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544<br>
[WARNING][Qt] 08.02.2019 12:22:07 [] (unknown:0) - ctkSliderWidget::setSingleStep()  1 is out of bounds. 173.504 173.583 173.544</p>

---

## Post #11 by @cpinter (2019-02-08 17:27 UTC)

<p><a class="mention" href="/u/ungi">@ungi</a> If you load the scene and then just press undo, nothing will happen. This log does not help us. Please find the log that Slicer wrote when you accidentally deleted the segment.</p>

---

## Post #12 by @cpinter (2019-02-08 17:28 UTC)

<p>It should basically be the last log file that is significantly larger than the others that you just generated.</p>

---

## Post #13 by @lassoan (2019-02-08 17:38 UTC)

<p>I could reproduce the issue, investigating.</p>

---

## Post #14 by @ungi (2019-02-08 17:44 UTC)

<p>You need to delete the segment before pressing Undo.</p>

---

## Post #15 by @lassoan (2019-02-08 17:51 UTC)

<p>I’ve found the root cause of the issue and <a href="https://github.com/Slicer/Slicer/commit/0b13a3256492547d029be8e2a5f4afb42d30a693" rel="nofollow noopener">fixed it</a>. Thanks for reporting it!</p>

---
