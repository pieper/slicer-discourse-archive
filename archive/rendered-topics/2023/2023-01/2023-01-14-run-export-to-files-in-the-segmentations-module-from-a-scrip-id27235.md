---
topic_id: 27235
title: "Run Export To Files In The Segmentations Module From A Scrip"
date: 2023-01-14
url: https://discourse.slicer.org/t/27235
---

# Run Export To Files in the Segmentations Module from a script

**Topic ID**: 27235
**Date**: 2023-01-14
**URL**: https://discourse.slicer.org/t/run-export-to-files-in-the-segmentations-module-from-a-script/27235

---

## Post #1 by @Alistair_McCutcheon (2023-01-14 01:12 UTC)

<p>I’d like to run the Export To Files functionality in the Segmentations Module from a slicer module I am developing. When running this, I need to be able to pass in the destination folder and the file format (nii.gz).</p>
<p>Does anyone know how to do this please?</p>

---

## Post #2 by @Alistair_McCutcheon (2023-01-14 04:53 UTC)

<p>This works (found here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>):</p>
<pre><code class="lang-auto">outputPath = "c:/tmp"

def exportLabelmap():
  segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
  referenceVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
  labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
  slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)
  filepath = outputPath + "/" + referenceVolumeNode.GetName() + "-label.nrrd"
  slicer.util.saveNode(labelmapVolumeNode, filepath)
  slicer.mrmlScene.RemoveNode(labelmapVolumeNode.GetDisplayNode().GetColorNode())
  slicer.mrmlScene.RemoveNode(labelmapVolumeNode)
  slicer.util.delayDisplay("Segmentation saved to " + filepath)

shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence("Ctrl+Shift+s"))
shortcut.connect( "activated()", exportLabelmap)

</code></pre>

---

## Post #3 by @rbumm (2023-01-14 16:27 UTC)

<p>For saving a scalar volume this should work, assuming you have a <code>yourScalarVolumeNode</code>:</p>
<pre><code class="lang-auto">tempDir = slicer.app.temporaryPath + "/Test/"
myStorageNode=yourScalarVolume.CreateDefaultStorageNode()
myStorageNode.SetFileName(tempDir+"test.nii.gz")
myStorageNode.WriteData(yourScalarVolume)
</code></pre>

---
