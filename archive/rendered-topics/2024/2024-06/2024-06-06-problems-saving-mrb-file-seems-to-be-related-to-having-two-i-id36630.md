---
topic_id: 36630
title: "Problems Saving Mrb File Seems To Be Related To Having Two I"
date: 2024-06-06
url: https://discourse.slicer.org/t/36630
---

# Problems saving MRB file, seems to be related to having two image sets at different time points

**Topic ID**: 36630
**Date**: 2024-06-06
**URL**: https://discourse.slicer.org/t/problems-saving-mrb-file-seems-to-be-related-to-having-two-image-sets-at-different-time-points/36630

---

## Post #1 by @kkwst2 (2024-06-06 18:18 UTC)

<p>Problem report for Slicer 5.7.0-2024-06-05 win-amd64: [Imported two different MRA sequences with same volume but gated to two different time points in the cardiac cycle. It seemed to automatically bundes them into a time series. I can’t get it to save the mrb because it won’t save that combined sequence properly.  Not sure how to work around this.  I can get it to save unbundled by unchecking the offending sequence.]</p>
<p>Here is the error log:<br>
[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - itk::ExceptionObject (000000AA098F3DA8)</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Location: “unknown”</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File: C:\D\P\S-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Line: 1145</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Description: ITK ERROR: NrrdImageIO(000002248A881870): Write: Error writing C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0.nrrd:</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0.nrrd”,“wb”): No such file or directory</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -</p>
<p>[ERROR][VTK] 06.06.2024 12:59:36 [vtkMRMLVolumeArchetypeStorageNode (00000224412A3530)] (vtkMRMLVolumeArchetypeStorageNode.cxx:934) - vtkMRMLVolumeArchetypeStorageNode::UpdateFileList: Failed to write ‘C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0.nrrd’</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - itk::ExceptionObject (000000AA098F3DA8)</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Location: “unknown”</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File: C:\D\P\S-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Line: 1145</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Description: ITK ERROR: NrrdImageIO(000002248A884EB0): Write: Error writing C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped.nrrd:</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped.nrrd”,“wb”): No such file or directory</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -</p>
<p>[CRITICAL][Stream] 06.06.2024 12:59:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -</p>
<p>[ERROR][VTK] 06.06.2024 12:59:36 [vtkMRMLVolumeArchetypeStorageNode (000002244129B9F0)] (vtkMRMLVolumeArchetypeStorageNode.cxx:934) - vtkMRMLVolumeArchetypeStorageNode::UpdateFileList: Failed to write ‘C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped.nrrd’</p>
<p>[ERROR][VTK] 06.06.2024 12:59:37 [vtkMRMLScene (0000022475CCE010)] (vtkMRMLScene.cxx:3921) - vtkMRMLScene::WriteToMRB: Failed to save C:/Users/whiteheadk/OneDrive - Children’s Hospital of Philadelphia/Models/**/Systole Wrapped with Valves/2024-06-05-Scene.mrb: Failed to save scene to data bundle directory</p>
<p>[CRITICAL][Qt] 06.06.2024 12:59:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - bool __cdecl qSlicerCoreIOManager::saveNodes(class QString,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLMessageCollection *,class vtkMRMLScene *) error: Saving failed with all writers found for file “C:/Users/whiteheadk/OneDrive - Children’s Hospital of Philadelphia/Models/**/Systole Wrapped with Valves/2024-06-05-Scene.mrb” of type “SceneFile”</p>
<p>[CRITICAL][Qt] 06.06.2024 12:59:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save error: “- Error: 57: MR MR HEART VELOCITY &amp; MRA CHEST W&amp;W O IV CON - 2 frames Volume Sequence by SeriesTime [0] (vtkMRMLScalarVolumeNode6): Failed to write ‘C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0.nrrd’\n- Error: 57: MR MR HEART VELOCITY &amp; MRA CHEST W&amp;W O IV CON - 2 frames Volume Sequence by SeriesTime [0] cropped (vtkMRMLScalarVolumeNode7): Failed to write ‘C:/Users/whiteheadk/AppData/Local/slicer.org/Slicer/cache/SlicerIO/__BundleSaveTemp-2024-06-06_125935_250/2024-06-05-Scene/Data/TempWrite57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped/57 MR MR HEART VELOCITY MRA CHEST WW O IV CON - 2 frames Volume Sequence by SeriesTime 0 cropped.nrrd’\n- Error: Failed to save C:/Users/whiteheadk/OneDrive - Children’s Hospital of Philadelphia/Models/<strong>/Systole Wrapped with Valves/2024-06-05-Scene.mrb: Failed to save scene to data bundle directory\n- Error: Failed to save scene as C:/Users/whiteheadk/OneDrive - Children’s Hospital of Philadelphia/Models/</strong>/Systole Wrapped with Valves/2024-06-05-Scene.mrb\n- Error: Saving failed with all writers found for file ‘C:/Users/whiteheadk/OneDrive - Children’s Hospital of Philadelphia/Models/**/Systole Wrapped with Valves/2024-06-05-Scene.mrb’ of type ‘SceneFile’.\n”</p>

---

## Post #2 by @lassoan (2024-06-06 18:25 UTC)

<p>It seems that you’ve hit the file system maximum path length limit.<br>
Renaming the node from <code>57: MR MR HEART VELOCITY &amp; MRA CHEST W&amp;W O IV CON - 2 frames Volume Sequence by SeriesTime [0] cropped</code> to something like <code>57: MR VELOCITY W&amp;W O IV CON [0] cropped</code> should fix the problem. If this happens frequently then we could look into how to make node names shorter or how to shorten temporary file path lengths.</p>

---

## Post #3 by @kkwst2 (2024-06-07 15:15 UTC)

<p>That was easy enough!  It wasn’t clear to me from the error what was happening.  Thanks so much!</p>

---

## Post #4 by @kkwst2 (2024-06-07 15:31 UTC)

<p>It does seem like this is going to be an issue going forward because of the long length of the shared folder name.  For now I’ll try to save them in a different directory without that long filename.</p>

---
