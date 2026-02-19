---
topic_id: 7244
title: "Film Dosimetry Deprecated Function"
date: 2019-06-19
url: https://discourse.slicer.org/t/7244
---

# Film Dosimetry - deprecated function

**Topic ID**: 7244
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/film-dosimetry-deprecated-function/7244

---

## Post #1 by @kmalexander (2019-06-19 14:57 UTC)

<p>Seems that there is a bit of deprecated code in the line profile aspect of the Film Dosimetry slicelet.  After generating the first couple profiles, the line profile viewer stops displaying the film dose profile, and only displays the treatment planning profile.</p>
<p>For now - it can be displayed by unchecking, then rechecking the ‘double array’ in the dropbox for the plot, but would be good to clean it up.</p>
<p>Error report:</p>
<p>Warning: In D:\D\S\Slicer-4102\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 1442</p>
<p>vtkMRMLLinearTransformNode (0000000026728180): vtkMRMLTransformNode::GetMatrixTransformToParent() method is deprecated. Use vtkMRMLTransformNode::GetMatrixTransformToParent(vtkMatrix4x4*) instead</p>

---
