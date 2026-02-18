# Saving creates multiple copies of files

**Topic ID**: 5971
**Date**: 2019-02-28
**URL**: https://discourse.slicer.org/t/saving-creates-multiple-copies-of-files/5971

---

## Post #1 by @meduser (2019-02-28 21:07 UTC)

<p>As I am segmenting, I save my work. I accept all the defaults offered in the save dialogs. When I look in the directory I see that it has saved everything but it creates additional copies of the items saved, more with each save operation: for instance:</p>
<p>Segmentation preview-label_ColorTable_1_3.ctbl<br>
Segmentation preview-label_ColorTable_1_2_1.ctbl<br>
Segmentation preview-label_ColorTable_1_1_2.ctbl<br>
Segmentation preview-label_ColorTable_1_1_1_1.ctbl</p>
<p>The original radiology volumes (*.nrrd) are only saved once thankfully, but if I close Slicer, and load the directory data, multiple copies of everything are loaded. I have to spend a lot of time pruning the extras to arrive at the situation I was when I saved.</p>
<p>Also it appears that Slicer saves things that have been long deleted, and in duplicate. Then when I load, there they are again. For example:</p>
<p>VolumeProperty_1_1.vp<br>
VolumeProperty_2_1.vp<br>
VolumeProperty_3_1.vp<br>
… etc</p>
<p>When I go to the data module, and look at my data after I have pruned it and I am happy, it looks good under the “subject Hierarchy tab”, I only have one item of each thing. But when I look under “All Nodes”, there is a long list of items with the same kind of repetitive duplicates that are saved to the directory.</p>
<p>What am I doing wrong ?   How should I be saving and loading so this doesn’t happen ?</p>
<p>Thank you for your help and care.</p>
<p>Andres</p>

---

## Post #2 by @lassoan (2019-02-28 21:44 UTC)

<p>It seems that you used an effect that has preview function (Grow from seeds, Fill between slices, etc) and forgot to click Apply when you are done.</p>
<p>If you are still getting new segmentation previews and then please send us the application log (menu: Help/Report a bug).</p>

---

## Post #4 by @Emanuel_Tschopp (2021-03-15 08:50 UTC)

<p>Hi there,<br>
we have the same problem as Andres with the multiple copies after saving, but we always hit apply when doing fill between slices. Now the file has become so large to load that it makes working unreasonable.<br>
Any other suggestions?<br>
Can we delete these useless additional copies permanently somehow?<br>
And is there a way we can save without adding more copies?<br>
Thanks a lot!</p>

---

## Post #5 by @lassoan (2021-03-15 13:28 UTC)

<p>If you save the scene while “Fill between slices” is active then the preview segmentation is saved. When you click “Apply” then the preview segmentation is removed from the scene, but previously saved files are not removed. You can choose anytime to save all nodes into an empty folder and that folder will not contain any unused files.</p>
<p>If you think that something different is happening on your computer then send a few screenshot of the “Save data” window and files on your system.</p>

---

## Post #6 by @Ertugrul_Furkan_Sava (2024-11-29 12:03 UTC)

<p>I have the exact same problem. When ever i save a CBCT image, 3D slicer is also save a copy of the original image. What i realize is that the copy of the image have better brigntness then the original one. When i do segmentation it also save copy of the segmentation.</p>
<p>Here is my log file content:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Session start time .......: 20241129_144851

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Operating system .........: Windows / Personal / (Build 19045, Code Page 65001) - 64-bit

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Memory ...................: 8104 MB physical, 10280 MB virtual

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Internationalization .....: disabled, language=

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Developer mode ...........: enabled

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Application path .........: C:/Users/E.F.S/AppData/Local/slicer.org/Slicer 5.6.2/bin

[DEBUG][Qt] 29.11.2024 14:48:51 [] (unknown:0) - Additional module paths ..: C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorDrawTube, C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorEngrave, C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorFastMarching, C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorFloodFilling, C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorLocalThreshold, C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorSplitVolume, C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorSurfaceCut, C:/Users/E.F.S/Downloads/SlicerSegmentEditorExtraEffects-master\SegmentEditorWatershed, slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules

[DEBUG][Python] 29.11.2024 14:48:54 [Python] (C:\Users\E.F.S\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor

[DEBUG][Python] 29.11.2024 14:48:54 [Python] (C:\Users\E.F.S\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics

[DEBUG][Qt] 29.11.2024 14:48:54 [] (unknown:0) - Switch to module: "Welcome"

[DEBUG][Qt] 29.11.2024 14:49:08 [] (unknown:0) - "MRML Scene" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/yunus_eda/2024-11-27-Scene.mrml" "[0.58s]"

[DEBUG][Qt] 29.11.2024 14:49:09 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/yunus_eda/2024-11-27-Scene.png" "[0.08s]"

[DEBUG][Qt] 29.11.2024 14:49:09 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/yunus_eda/5093 Unnamed Series cropped.nrrd" "[0.11s]"

[DEBUG][Qt] 29.11.2024 14:49:09 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/yunus_eda/5093 Unnamed Series.nrrd" "[0.48s]"

[DEBUG][Qt] 29.11.2024 14:49:09 [] (unknown:0) - "Markups" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/yunus_eda/Crop Volume ROI.mrk.json" "[0.05s]"

[DEBUG][Qt] 29.11.2024 14:49:09 [] (unknown:0) - "Segmentation" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/yunus_eda/Segmentation.seg.nrrd" "[0.02s]"

[DEBUG][Qt] 29.11.2024 14:49:12 [] (unknown:0) - Switch to module: "SegmentEditor"

[WARNING][Qt] 29.11.2024 14:49:12 [] (unknown:0) - QLayout::addChildLayout: layout "" already has a parent

[WARNING][Qt] 29.11.2024 14:49:12 [] (unknown:0) - ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1

[DEBUG][Qt] 29.11.2024 14:49:14 [] (unknown:0) - Switch to module: "Data"

[DEBUG][Qt] 29.11.2024 14:56:53 [] (unknown:0) - Close main MRML scene

[DEBUG][Qt] 29.11.2024 14:56:55 [] (unknown:0) - Switch to module: "DICOM"

[WARNING][Python] 29.11.2024 14:56:59 [Python] (C:\Users\E.F.S\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\DICOMBrowser.py:571) - Warning in DICOM plugin Scalar Volume when examining loadable 5231: Unnamed Series: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.

Reference image in series does not contain geometry information. Please use caution.

[INFO][Python] 29.11.2024 14:56:59 [Python] (C:\Users\E.F.S\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Warnings detected during load. Examine data in Advanced mode for details. Load anyway?

[INFO][Python] 29.11.2024 14:57:00 [Python] (C:/Users/E.F.S/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM

[INFO][Python] 29.11.2024 14:57:01 [Python] (C:/Users/E.F.S/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=2047.0, width=4095.0) has been applied to volume 5231: Unnamed Series

[WARNING][Python] 29.11.2024 14:57:01 [Python] (C:/Users/E.F.S/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:818) - Cannot get DICOM slice positions for volume 5231: Unnamed Series

[DEBUG][Qt] 29.11.2024 14:57:43 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""

[DEBUG][Qt] 29.11.2024 14:57:44 [] (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save information: ""

[DEBUG][Qt] 29.11.2024 14:57:56 [] (unknown:0) - Close main MRML scene

[DEBUG][Qt] 29.11.2024 14:58:04 [] (unknown:0) - "MRML Scene" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/deneme/2024-11-29-Scene.mrml" "[0.48s]"

[DEBUG][Qt] 29.11.2024 14:58:04 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/deneme/2024-11-29-Scene.png" "[0.07s]"

[DEBUG][Qt] 29.11.2024 14:58:04 [] (unknown:0) - "Volume" Reader has successfully read the file "C:/Users/E.F.S/Desktop/Doktora çalışmaları/2024-2025 güz/CBCT_Segmentation/all_teeth/deneme/5231 Unnamed Series.nrrd" "[0.47s]"
</code></pre>

---

## Post #7 by @lassoan (2024-12-01 05:39 UTC)

<p>When you open a scene file (.mrml file), all data that was in the scene are loaded, with the visualization settings that were saved in the scene (they are initialized with the settings stored in the DICOM file). If you load both the scene file (.mrml) and the image files again (.nrrd, …) then you’ll end up with all data loaded twice. The solution is to only load the scene file.</p>

---

## Post #8 by @Ertugrul_Furkan_Sava (2024-12-06 12:17 UTC)

<p>Oh that’s why. Thank you so much sir.</p>

---
