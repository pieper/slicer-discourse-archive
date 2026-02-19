---
topic_id: 24240
title: "Attempting Ct Skull Stripping In Python"
date: 2022-07-08
url: https://discourse.slicer.org/t/24240
---

# Attempting CT skull stripping in python

**Topic ID**: 24240
**Date**: 2022-07-08
**URL**: https://discourse.slicer.org/t/attempting-ct-skull-stripping-in-python/24240

---

## Post #1 by @KateDelb (2022-07-08 14:18 UTC)

<p>I’m following the recipe for CT skull stripping (<a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" class="inline-onebox" rel="noopener nofollow ugc">Overview | 3D Slicer segmentation recipes</a>) which works perfectly in the GUI. I am attempting to automate this with python as I have many samples. I am new to this so sorry if any of this is trivial</p>
<p>Pseudocode/code steps as far as I can understand are the following:</p>
<ul>
<li>Import ct image into masterVolume node</li>
</ul>
<pre><code class="lang-auto">masterVolumeNode = slicer.util.loadVolume(pathct)
</code></pre>
<ul>
<li>I have previously already thresholded out the skull (HU &gt;300) and removed all small islands and need to load this array it into a Segmentation node.</li>
</ul>
<pre><code class="lang-auto">#Create Labelmap Node
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
#set its voxels from a numpy array using slicer.util.updateVolumeFromArray
**Labelmap_Skull = slicer.util.updateVolumeFromArray(skull_seg_arr, labelmapVolumeNode)**
#Create segmentation node
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

#Convert to segmentation node
slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(Labelmap_Skull, segmentationNode, selectedSegmentIds)
</code></pre>
<p>Next, I need to implement the WrapSolidify effect with the following parameters:<br>
<span class="hashtag">#set</span> region to Largest cavity<br>
<span class="hashtag">#Enable</span> Split cavities and set cavity size slider to approximately 30mm</p>
<pre><code class="lang-auto"># import module
import SegmentEditorWrapSolidify

</code></pre>
<p>However, I’ve been looking around at the source code <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/master/SegmentEditorWrapSolidify/SegmentEditorWrapSolidify.py" class="inline-onebox" rel="noopener nofollow ugc">Slicer-SurfaceWrapSolidify/SegmentEditorWrapSolidify.py at master · sebastianandress/Slicer-SurfaceWrapSolidify · GitHub</a>  and am a little lost concerning how to actually implement this in Python. I don’t understand the difference between the 2 classes, SegmentEditorWrapSolidifyTest and SegmentEditorWrapSolidify. Nor how to invoke  an instance of these classes seeing as Wrapsolidify = SegmentEditorWrapSolidify() shows the error “TypeError: ‘module’ object is not callable”</p>
<p>Are there any examples I could follow or anything similar?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @Miri_Trope (2025-02-14 19:48 UTC)

<p>Dear all, I’m interested in achieving the same as described in this post. Could anyone provide an answer? Additionally, if there are any recent recommendations from the past two years on applying WrapSolidify in a Python script outside Slicer interface, please let me know.</p>

---
