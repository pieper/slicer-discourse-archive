---
topic_id: 39831
title: "Error When Changing Segment Name From Python"
date: 2024-10-23
url: https://discourse.slicer.org/t/39831
---

# Error when changing segment name from Python

**Topic ID**: 39831
**Date**: 2024-10-23
**URL**: https://discourse.slicer.org/t/error-when-changing-segment-name-from-python/39831

---

## Post #1 by @idris_deniz (2024-10-23 20:18 UTC)

<p>Hello 3D Slicer community,</p>
<p>I want to change (rename) segment names while using 3D Slicer. However, whenever I try to do this, I keep encountering errors or the segment names are not changing successfully. This has become quite problematic for me, as using the correct segment names is very important in my projects.</p>
<p>Below, I am sharing the code I am using. I would greatly appreciate it if you could review my code and help me with any errors or issues I am facing.</p>
<p>Any advice will be appreciated! Thanks!</p>
<pre><code class="lang-auto">import os
import slicer
import vtk

script_dir = os.path.dirname(os.path.realpath(_file_))
txt_path = os.path.join(script_dir, "..", "level", "Level5.txt")

def update_segment_names(outputFolder, txt_file_path=txt_path):
    subfolders = [f for f in os.listdir(outputFolder) if os.path.isdir(os.path.join(outputFolder, f))]

    for subfolder in subfolders:
        subfolder_path = os.path.join(outputFolder, subfolder)
        for f in os.listdir(subfolder_path):
            if f.endswith('.nii') and "_280" in f:
                nii_file_path = os.path.join(subfolder_path, f)

                
                slicer.mrmlScene.Clear(0)

               
                segmentation_node = slicer.util.loadSegmentation(nii_file_path)
                if not segmentation_node:
                    print(f"Segmentasyon dosyası {nii_file_path} yüklenemedi.")
                    continue

                
                segment_names = []
                try:
                    with open(txt_file_path, 'r') as file:
                        for line in file:
                            columns = line.strip().split()
                            if len(columns) &gt;= 2:
                                segment_names.append(columns[1])
                except FileNotFoundError:
                    print(f"TXT dosyası {txt_file_path} bulunamadı.")
                    continue

                segmentation = segmentation_node.GetSegmentation()
                segment_ids = vtk.vtkStringArray()
                segmentation.GetSegmentIDs(segment_ids)

                
                for i in range(segment_ids.GetNumberOfValues()):
                    segment_id = segment_ids.GetValue(i)
                    segment = segmentation.GetSegment(segment_id)
                    old_name = segment.GetName()
                    if i &lt; len(segment_names):
                        segment.SetName(segment_names[i])
                    else:
                        segment.SetName(f"Segment_{i}")

                    print(f"Eski isim: {old_name}, Yeni isim: {segment.GetName()}")

                
                labelmap_volume_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
                slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentation_node, labelmap_volume_node)

               
                volumesLogic = slicer.modules.volumes.logic()
                scalar_volume_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")  
                scalar_volume_node.SetName(segmentation_node.GetName()) 
                volumesLogic.CreateScalarVolumeFromVolume(slicer.mrmlScene, labelmap_volume_node, scalar_volume_node)

               
                output_nifti_path = os.path.join(subfolder_path, f"{os.path.splitext(f)[0]}.nii")
                success = slicer.util.saveNode(labelmap_volume_node, output_nifti_path)

                if success:
                    print(f"Segmentasyon güncellendi ve kaydedildi: {output_nifti_path}")
                else:
                    print(f"Segmentasyon kaydedilemedi: {output_nifti_path}")

                
                slicer.mrmlScene.RemoveNode(segmentation_node)
                slicer.mrmlScene.RemoveNode(labelmap_volume_node)
                slicer.mrmlScene.RemoveNode(scalar_volume_node)
</code></pre>

---

## Post #2 by @cpinter (2024-10-28 09:19 UTC)

<p>Hi! I think it would facilitate things if you shared a minimal code example that does not work for you. All the people who help out here are quite busy, so I think posting multi-page code discourages some of them. Thanks!</p>

---
