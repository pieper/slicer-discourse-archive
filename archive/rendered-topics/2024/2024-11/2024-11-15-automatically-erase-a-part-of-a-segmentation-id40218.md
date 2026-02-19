---
topic_id: 40218
title: "Automatically Erase A Part Of A Segmentation"
date: 2024-11-15
url: https://discourse.slicer.org/t/40218
---

# Automatically erase a part of a segmentation

**Topic ID**: 40218
**Date**: 2024-11-15
**URL**: https://discourse.slicer.org/t/automatically-erase-a-part-of-a-segmentation/40218

---

## Post #1 by @Fleur_Gaudfernau (2024-11-15 16:11 UTC)

<p>Hello,<br>
I am fairly new to using python scripts in Slicer.<br>
I have rather simple brain segmentation (1 label) and I want to physically separate the brain hemispheres, i.e. remove the <strong>junction</strong> between the hemispheres and obtain two <strong>separate</strong> segments/islands (one for each hemisphere) instead of one. As my segmentations have been registered to a common space, I do <strong>know</strong> which areas of the segmentation map have to be erased.</p>
<p>I basically want to go from this (first row) to that (second row):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a177c5b6272593fd8a2122ffea15a31d82ff079.png" data-download-href="/uploads/short-url/1rh5KsXVIeknfDLDoukQURh0viN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a177c5b6272593fd8a2122ffea15a31d82ff079_2_300x250.png" alt="image" data-base62-sha1="1rh5KsXVIeknfDLDoukQURh0viN" width="300" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a177c5b6272593fd8a2122ffea15a31d82ff079_2_300x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a177c5b6272593fd8a2122ffea15a31d82ff079_2_450x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a177c5b6272593fd8a2122ffea15a31d82ff079_2_600x500.png 2x" data-dominant-color="555B55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">930×764 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The python code I am trying to transpose to Slicer is the following:</p>
<blockquote>
<p>image = nib.load(“path/to/segmentation.nii.gz”)<br>
data = image.get_fdata()<br>
data[72:77, 105:140, 75:98] = 0<br>
data[62:67, 105:140, 75:100] = 0</p>
</blockquote>
<p>Basically I have tried:</p>
<ol>
<li>
<p>using segmentEditor, using the “eraser” effect but I do not know how to automatically specify the area to erase</p>
</li>
<li>
<p>Create a new segment, and use the Paint tool to “write over” the existing segment.</p>
</li>
</ol>
<blockquote>
<p>segmentationNode = slicer.util.loadSegmentation(path_to_file)<br>
VolumeNode = slicer.util.loadVolume(path_to_volume)<br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode =slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(VolumeNode)<br>
theSegmentation = segmentationNode.GetSegmentation()<br>
theSegmentation.AddEmptySegment(“Middle”)<br>
segmentEditorNode.SetSelectedSegmentID(“Middle”)<br>
segmentEditorWidget.setActiveEffectByName(“Paint”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“BrushRelativeDiameter”, “1”)  # Brush size relative to the volume size<br>
effect.setParameter(“BrushSphere”, “1”)  # Use a spherical brush<br>
effect.paintApply((70,70,70))</p>
</blockquote>
<p>I get an error with the last line. Same issue here, I do not know how to specify the coordinates for the Paint tool.<br>
<strong>ValueError: Called paintApply(qMRMLWidget viewWidget) → void with wrong arguments: ((70, 70, 70),)</strong></p>
<ol start="3">
<li>Create a vtk polygon and use segmentationNode.AddSegmentFromClosedSurfaceRepresentation(Polygon, …) to create a new segment. I also get an error.</li>
</ol>
<p>Any help would be greatly appreciated!</p>

---
