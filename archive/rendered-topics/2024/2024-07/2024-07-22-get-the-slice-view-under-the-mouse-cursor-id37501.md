# Get the slice view under the mouse cursor

**Topic ID**: 37501
**Date**: 2024-07-22
**URL**: https://discourse.slicer.org/t/get-the-slice-view-under-the-mouse-cursor/37501

---

## Post #1 by @rohithck (2024-07-22 13:59 UTC)

<p>Hello slicer developers,<br>
How to get the slice view (Red, Green or Yellow) under the mouse cursor in Python, like what shown in Data Probe module (Eg: Green in the image)?</p>
<p>And also how to get the plane coordinates (or plane equation) of the current slice view, so that i can set the plane to that slice view later when a button is clicked.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88871b4d3b466dfe228b5b8d81d3eb473cc0299f.png" alt="Screenshot from 2024-07-21 11-39-51" data-base62-sha1="jtMoQ3bAtAQVCodrMoZ3eQcskAT" width="465" height="183"></p>

---

## Post #2 by @lassoan (2024-07-22 21:12 UTC)

<p>See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view">script repository</a>. You can get the slice normal from the <a href="https://apidocs.slicer.org/master/classvtkMRMLSliceNode.html#a888f4614c00f350f4440ac9bde8a3a6d">SliceToRAS</a> homogeneous transformation matrix (slice normal in the RAS coordinate system is the third column of the matrix).</p>

---
