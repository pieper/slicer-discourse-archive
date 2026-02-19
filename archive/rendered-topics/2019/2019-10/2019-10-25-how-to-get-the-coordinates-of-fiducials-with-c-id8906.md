---
topic_id: 8906
title: "How To Get The Coordinates Of Fiducials With C"
date: 2019-10-25
url: https://discourse.slicer.org/t/8906
---

# How to get the coordinates of fiducials with C++

**Topic ID**: 8906
**Date**: 2019-10-25
**URL**: https://discourse.slicer.org/t/how-to-get-the-coordinates-of-fiducials-with-c/8906

---

## Post #1 by @Haoyin_Zhou (2019-10-25 19:19 UTC)

<p>Hi, if there already exist two sets of fiducials, for example “fixed” and “moving”, which are placed manually. Then how to get the list of coordinates of the two sets of fiducials?</p>
<p>I found the class vtkMRMLMarkupsFiducialNode, but I don’t know how to initialize it.</p>
<p>Thanks for any help!</p>

---

## Post #2 by @lassoan (2019-10-27 17:23 UTC)

<p>You can get the node pointer from a MRML node selector from the GUI (or by node ID from the MRML scene) and then call <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#a5f20da6f3cd4904e0d1a335062ea15de"> GetNthControlPointPosition()</a>.</p>
<p>In general, try to find a module that does something similar to what you would like to do and copy and modify that.</p>

---
