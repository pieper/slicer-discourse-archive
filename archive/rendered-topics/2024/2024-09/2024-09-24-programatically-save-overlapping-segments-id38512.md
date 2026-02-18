# Programatically save Overlapping Segments

**Topic ID**: 38512
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/programatically-save-overlapping-segments/38512

---

## Post #1 by @tito21 (2024-09-24 11:27 UTC)

<p>Hi, I am using Slicer as part of a workflow that includes segmentation of overlapping regions. The segmentation needs to be saved programmatically.</p>
<p>When I save as a <code>.nrrd</code> file with <code>    slicer.modules.segmentations.logic().ExportSegmentsBinaryLabelmapRepresentationToFiles(segmentationNode, labelmapVolumeNode, referenceVolumeNode)</code> the overlapping segments get flatten. However, when I save the whole scene by clicking on the save icon, the segmentation gets exported as a <code>.seg.nrrd</code> 4D non overlapping volumes. What is the command to save the segmentation as a 4D volume?</p>
<p>Thanks in advance</p>

---

## Post #2 by @cpinter (2024-09-24 11:35 UTC)

<p>What is the difference between the <code>.seg.nrrd</code> and the 4D volume you need? The <code>.seg.nrrd</code> file is basically a 4D nrrd with some extra metadata in the header.</p>

---

## Post #3 by @tito21 (2024-09-24 11:43 UTC)

<p>Thanks for your prompt reply.</p>
<p>The <code>seg.nrrd</code> file is what I need, but I need a way to generate it programmatically. When I save the segmentation with the command above, I get only a 3D array, but I need the 4D volume you get by saving the file manually.</p>

---

## Post #4 by @cpinter (2024-09-24 11:52 UTC)

<p>Ah, I see. Here’s how I’d do it:</p>
<pre><code class="lang-auto">s = getNode('vtkMRMLSegmentationNode1')
ss = s.GetStorageNode()
ss.SetFileName(r'd:/segmentation.seg.nrrd')
ss.WriteData(s)
</code></pre>
<p>(I found the corresponding example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-a-node-to-file">script repository</a>, it says the same thing)</p>

---

## Post #5 by @lassoan (2024-09-24 14:01 UTC)

<p>You can also use the <code>saveNode</code> convenience function (from the script repository, too):</p>
<pre data-code-wrap="python"><code class="lang-python">success = slicer.util.saveNode(node, filename)
</code></pre>

---

## Post #6 by @tito21 (2024-09-24 14:04 UTC)

<p>This solved my problem.</p>
<p>Thanks for the help</p>
<p>Here is the code I use</p>
<pre data-code-wrap="python"><code class="lang-python">def exportLabelmap():

    filepath = outputPath + "/label.seg.nrrd"
    segmentationNode = getNode('vtkMRMLSegmentationNode1')
    storageNode = segmentationNode.CreateDefaultStorageNode()
    storageNode.SetFileName(filepath)
    storageNode.WriteData(segmentationNode)

    slicer.util.delayDisplay("Segmentation saved to " + filepath)

shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence("Ctrl+Shift+s"))
shortcut.connect( "activated()", exportLabelmap)
</code></pre>

---

## Post #7 by @lassoan (2024-09-24 15:55 UTC)

<p>Thanks for sharing the code that worked for you.</p>
<aside class="quote no-group" data-username="tito21" data-post="6" data-topic="38512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tito21/48/78012_2.png" class="avatar"> tito21:</div>
<blockquote>
<p><code>segmentationNode  = getNode('vtkMRMLSegmentationNode1')</code></p>
</blockquote>
</aside>
<p>Hardcoding an automatically generated ID would be fragile (e.g., you may create a second segmentation and delete the first one; then you will not find any node by the ID <code>vtkMRMLSegmentationNode1</code>). Instead, you can get the first segmentation node from the scene like this (from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">script repository</a>):</p>
<pre data-code-wrap="python"><code class="lang-python">segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
</code></pre>

---
