---
topic_id: 11608
title: "Workaround For Errors When Showing Annotationruler Label Tex"
date: 2020-05-18
url: https://discourse.slicer.org/t/11608
---

# Workaround for errors when showing AnnotationRuler Label text in 2D slice view

**Topic ID**: 11608
**Date**: 2020-05-18
**URL**: https://discourse.slicer.org/t/workaround-for-errors-when-showing-annotationruler-label-text-in-2d-slice-view/11608

---

## Post #1 by @jamesobutler (2020-05-18 23:01 UTC)

<p>I’m hoping there is a workaround to solve an issue I’m getting with showing the label text of an AnnotationRuler label in the 2D slice views.  I’m still needing to use this AnnotationRuler object instead of transitioning to a line node at the moment.</p>
<p>First place a ruler down on a volume and turn on the visibility for the 2D slice views.</p>
<pre data-code-wrap="python"><code class="lang-python">ruler_node = slicer.mrmlScene.GetNodeByID("vtkMRMLAnnotationRulerNode1")
ruler_node.GetAnnotationTextDisplayNode().SetVisibility2D(True)
</code></pre>
<p>This will then produces lots of these errors if the slice intersection offset crosses the display such as the yellow slice intersection shown below.  Turning off slice intersections has no change on these errors.</p>
<p><code>Tuple 1 out of range for provided array. Requested tuple: 0 Tuples: 0</code> from <a href="https://github.com/Slicer/VTK/blob/dd7e051af68cfbf3675e411494af7169fc7d5618/Common/Core/vtkDataArray.cxx#L878-L880" rel="noopener nofollow ugc">this place in the code</a><br>
and <code>Point array ctrlPtsSelected with 1 components, only has 0 tuples but there are 1 points</code> from <a href="https://github.com/Slicer/VTK/blob/dd7e051af68cfbf3675e411494af7169fc7d5618/Common/DataModel/vtkDataSet.cxx#L432-L435" rel="noopener nofollow ugc">this place in the code</a>.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc1546178fcb062857e1bf98099119c240ff426.png" alt="image" data-base62-sha1="t4v8glBtAWUSGxkYcgovmlMWr0G" width="359" height="381"></p>

---

## Post #2 by @pieper (2020-05-19 00:09 UTC)

<p>Usually if you can get a stack trace you can see what conditiions lead to those messages and find a way to handle them.  I know the Annotation code is kind of complex and slated for replacement, but if the only issue is avoiding the error message it should be manageable.</p>

---
