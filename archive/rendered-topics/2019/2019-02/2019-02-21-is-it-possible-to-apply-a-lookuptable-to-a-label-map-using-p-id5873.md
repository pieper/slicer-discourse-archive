---
topic_id: 5873
title: "Is It Possible To Apply A Lookuptable To A Label Map Using P"
date: 2019-02-21
url: https://discourse.slicer.org/t/5873
---

# Is it possible to apply a lookuptable to a label map using python?

**Topic ID**: 5873
**Date**: 2019-02-21
**URL**: https://discourse.slicer.org/t/is-it-possible-to-apply-a-lookuptable-to-a-label-map-using-python/5873

---

## Post #1 by @Kevin.Kn (2019-02-21 17:48 UTC)

<p>I have two separate files, one being a lookup table , and the other being a .nii labelvolume.</p>
<p>I know that you can use slicer.util.loadColorTable() , as well as slicer.util.loadLabelVolume() to load the files into slicer, but I haven’t found a way to apply the lookuptable to the volume as a python command/script.</p>
<p>By hand i can easily do this, but I have 5000+ image/table pairs that need to be combined before  processing into segmentations</p>

---

## Post #2 by @Kevin.Kn (2019-02-21 22:02 UTC)

<p>FOUND SOLUTION AFTER SOME MORE DIGGING</p>
<p>you can use slicer.util.getNode() to find the volume node.</p>
<p>Then with that volume node, you can use GetDisplayNode() to create a sub-node that contains all the display data (which includes where the Look up Table reference is).</p>
<p>with the displayNode , you can call SetAndObserveColorNodeID([ColorTable]) , where [ColorTable] is the lookup table that you loaded initially. [ColorTable] has to be a string that corresponds to whatever the label of the Lookup Table is.</p>
<p>In my case, since I only loaded a single ColorTable , it was labeled as ‘vtkMRMLColorTableNode1’ . You can check what the current ColorTableNode is by printing out the node, as well as you can check what the loaded colorTable node name is.</p>
<p>After the lookup table was applied, I created another node that references the original volume, and then used slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’) to create a new segmentation node.</p>
<p>slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segNode) was used to create the segmentation.</p>
<p>slicer.util.saveNode(slicer.mrmlScene.GetNodeByID(“vtkMRMLSegmentationNode1”), “/tmp/foo.seg.nrrd”) was then used to save the labeled segmentations to a directory as a .seg.nrrd file.</p>
<p>replace the directory name with wherever you want the output segment file to be written.</p>
<p>When reloading the output segment file, all Label and Color information is saved properly, and is read back properly into slicer</p>
<p>EDIT: there are probably ways to label the node references as they are being created/loaded, instead of having them be labeled ‘ColorNode1 / SegmentationNode1’ , but I am new to Slicer, and haven’t looked up how to do it yet.</p>

---
