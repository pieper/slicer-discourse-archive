# Could not access function from qMRMLSortFilterProxyModel

**Topic ID**: 11346
**Date**: 2020-04-29
**URL**: https://discourse.slicer.org/t/could-not-access-function-from-qmrmlsortfilterproxymodel/11346

---

## Post #1 by @giovform (2020-04-29 12:37 UTC)

<p>Hi! I am not being able to access the function <a href="https://apidocs.slicer.org/master/classqMRMLSortFilterProxyModel.html#a65d2c0a4108b992de0fdd9d7e511e2a7" rel="nofollow noopener">setHiddenNodeIDs</a> from inside my Slicer. Using 4.11.0-2020-01-20 r28737.</p>

---

## Post #2 by @lassoan (2020-04-29 13:17 UTC)

<p>hiddenNodeIDs is a property, so you can write it as <code>something.hiddenNodeIDs=["vtkMRMLMarkupsCurveNode", "vtkMRMLMarkupsLineNode"]</code></p>

---
