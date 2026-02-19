---
topic_id: 31392
title: "Vtkmrmlmodeldisplaynode 00000267D9D32A80 Setsliceintersectio"
date: 2023-08-28
url: https://discourse.slicer.org/t/31392
---

# vtkMRMLModelDisplayNode (00000267D9D32A80): SetSliceIntersectionVisibility method is deprecated, please use SetVisibility2D instead

**Topic ID**: 31392
**Date**: 2023-08-28
**URL**: https://discourse.slicer.org/t/vtkmrmlmodeldisplaynode-00000267d9d32a80-setsliceintersectionvisibility-method-is-deprecated-please-use-setvisibility2d-instead/31392

---

## Post #1 by @Dex2046 (2023-08-28 01:06 UTC)

<p>Call for help</p>
<p>I use must-segmentator to create a VOI segmentation in liver, I got the warning message like this</p>
<pre><code class="lang-auto">[VTK] Warning: In vtkMRMLDisplayNode.cxx, line 996

[VTK] vtkMRMLModelDisplayNode (00000267D9D32A80): SetSliceIntersectionVisibility method is deprecated, please use SetVisibility2D instead

[Qt] int __cdecl qSlicerSubjectHierarchySegmentsPlugin::getDisplayVisibility(__int64) const : No display node for segmentation

[Qt] int __cdecl qSlicerSubjectHierarchySegmentsPlugin::getDisplayVisibility(__int64) const : No display node for segmentation

[Qt] int __cdecl qSlicerSubjectHierarchySegmentsPlugin::getDisplayVisibility(__int64) const : No display node for segmentation

[Qt] int __cdecl qSlicerSubjectHierarchySegmentsPlugin::getDisplayVisibility(__int64) const : No display node for segmentation

[VTK] Warning: In vtkMRMLSegmentationNode.h, line 228

[VTK] vtkMRMLSegmentationNode (00000267D0BEA100): vtkSegmentation::SetMasterRepresentationToClosedSurface() method is deprecated, please use SetSourceRepresentationToClosedSurface method instead
</code></pre>
<p>however, I got a sphere segmentation, but it can not be found in further calculation</p>
<p>How could I solve this problem? thank you all.</p>

---

## Post #2 by @cpinter (2023-08-28 09:46 UTC)

<p>The first warning is probably the one that has been fixed very recently: <a href="https://github.com/SlicerIGT/SlicerMarkupsToModel/pull/36" class="inline-onebox">BUG: Fix deprecated function calls by cpinter · Pull Request #36 · SlicerIGT/SlicerMarkupsToModel · GitHub</a></p>
<p>The ones to follow are from the segments plugin, maybe getting the visibility by the SH model is premature, but these are just warnings and have no effect on anything, so I haven’t considered it a priority.</p>
<p>The last error may come from your side as various functions have been deprecated (the word “master” was replaced with “source” in function names to make it more inclusive), but most of the usages have been updated as well. Again, no chance of indicating actual error.</p>

---

## Post #3 by @Dex2046 (2023-08-29 01:54 UTC)

<p>thank you~</p>
<p>just as you said, it is a different problem, this warning has nothing to do with the result.</p>

---
