# Creating dummy displayable and display nodes to show color legend

**Topic ID**: 22656
**Date**: 2022-03-23
**URL**: https://discourse.slicer.org/t/creating-dummy-displayable-and-display-nodes-to-show-color-legend/22656

---

## Post #1 by @Mik (2022-03-23 16:05 UTC)

<p>I’m trying to rework Isodose module, so that color legend was used instead of scalar bars.<br>
There is a <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Isodose/Logic/vtkMRMLIsodoseNode.h" rel="noopener nofollow ugc">IsodoseNode</a> that is used as parameters storing node.</p>
<p>I want convert that vtkMRMLNode to vtkMRMLDisplayableNode and also add vtkMRMLIsodoseDiplayNode to store isolevels color table node. In that case IsodoseNode will display color legend and nothing else.</p>
<p>Are there any drawbacks of such scheme?</p>

---
