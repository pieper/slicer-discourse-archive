---
topic_id: 32213
title: "Get Current Mouse Coordinates In A Slice View"
date: 2023-10-13
url: https://discourse.slicer.org/t/32213
---

# Get current mouse coordinates in a slice view

**Topic ID**: 32213
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/get-current-mouse-coordinates-in-a-slice-view/32213

---

## Post #1 by @susk (2023-10-13 14:22 UTC)

<p>I’ve been using the following example in the code repository to get the mouse position when the user moves the mouse: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-current-mouse-coordinates-in-a-slice-view" rel="noopener nofollow ugc">get-current-mouse-coordinates-in-a-slice-view</a>. In Slicer 5.2.2, this prints the cursor position when the mouse is moved in the 3D view only when the Shift key is pressed simultaneously. However, in Slicer 5.4.0 , the cursor position is printed whenever the user moves the mouse in the 3D view.</p>
<p>I’ve used this in my own code to let the user position a ROIBox along a centerline by moving the mouse and pressing the shift-key. This worked well in Slicer 5.2.2 but now with Slicer 5.4.0 the ROIBox repositions while the user moves the cursor out of the 3D view. Is there a way to get the old behaviour back?</p>

---
