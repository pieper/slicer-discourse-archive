---
topic_id: 27215
title: "Error Loading A File On Mac Related With Node"
date: 2023-01-12
url: https://discourse.slicer.org/t/27215
---

# ERROR loading a file on Mac related with Node

**Topic ID**: 27215
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/error-loading-a-file-on-mac-related-with-node/27215

---

## Post #1 by @Adriana_Rojas_Garcia (2023-01-12 17:32 UTC)

<p>Problem report for Slicer 5.2.1 macosx-amd64: I try to charge a mrml file and the following errors appear:</p>
<ul>
<li>ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLParser.cxx, line 139</li>
</ul>
<p>vtkMRMLParser (0x600003edc840): Failed to CreateNodeByClass: vtkMRMLChartViewNode</p>
<ul>
<li>ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 326</li>
</ul>
<p>vtkMRMLScalarVolumeNode (0x7f79a2dfb180): vtkMRMLStorableNode::UpdateScene failed: Failed to read node 00000000 (vtkMRMLScalarVolumeNode1) using storage node vtkMRMLVolumeArchetypeStorageNode4.</p>
<ul>
<li>ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 326</li>
</ul>
<p>vtkMRMLVolumePropertyNode (0x7f79d2775c50): vtkMRMLStorableNode::UpdateScene failed: Failed to read node VolumeProperty (vtkMRMLVolumePropertyNode1) using storage node vtkMRMLVolumePropertyStorageNode1.</p>
<ul>
<li>ERROR: In /Volumes/D/S/S-0/Libs/MRML/Core/vtkMRMLStorableNode.cxx, line 326</li>
</ul>
<p>vtkMRMLAnnotationROINode (0x7f79928fe140): vtkMRMLStorableNode::UpdateScene failed: Failed to read node AnnotationROI (vtkMRMLAnnotationROINode1) using storage node vtkMRMLAnnotationLinesStorageNode1.</p>
<p>I worked with this file last year in a windows operative system and I didn’t have any problems, now when I try to work on it on a Mac the errors shown above appears.</p>
<p>I would appreciate if someone could help me.</p>

---

## Post #2 by @pieper (2023-01-12 17:50 UTC)

<p>It’s hard to say for sure, but if you only copied the .mrml file then these messages mean that the referenced data files are not available on your mac.  Using the .mrb format is a good way to ensure you have all the data in one handy file.</p>

---

## Post #3 by @lassoan (2023-01-12 17:54 UTC)

<aside class="quote no-group" data-username="Adriana_Rojas_Garcia" data-post="1" data-topic="27215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adriana_rojas_garcia/48/17992_2.png" class="avatar"> Adriana_Rojas_Garcia:</div>
<blockquote>
<p>I worked with this file last year in a windows operative system and I didn’t have any problems, now when I try to work on it on a Mac the errors shown above appears.</p>
</blockquote>
</aside>
<p>We improved error reporting during scene loading in recent Slicer versions. Errors that were previously ignored are now displayed. To get rid of the errors, the simplest is to load the data files (.nrrd, .vtk, … files) into Slicer instead of the .mrml file.</p>

---
