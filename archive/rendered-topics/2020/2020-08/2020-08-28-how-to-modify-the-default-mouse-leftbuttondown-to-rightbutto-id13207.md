---
topic_id: 13207
title: "How To Modify The Default Mouse Leftbuttondown To Rightbutto"
date: 2020-08-28
url: https://discourse.slicer.org/t/13207
---

# How to modify the default mouse leftbuttondown to rightbuttondown?

**Topic ID**: 13207
**Date**: 2020-08-28
**URL**: https://discourse.slicer.org/t/how-to-modify-the-default-mouse-leftbuttondown-to-rightbuttondown/13207

---

## Post #1 by @pingdan (2020-08-28 03:12 UTC)

<p>I use vtkImagePlaneWidget to display a image. the default operation is  leftbutton change window/level, now I need to rightbutton change window/level, how can I do?</p>

---

## Post #2 by @lassoan (2020-08-28 03:42 UTC)

<p>In current Slicer version, window/level has a separate mouse mode.</p>
<p>If you still want to change the <em>interaction event</em> (mouse move, clicks, etc.) to <em>widget event</em> (adjust window/level, reset window/level, etc.) mapping then it can be done <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLWindowLevelWidget.cxx#L79-L91">here</a> just by modifying a few lines. If necessary, we can expose these in Python, too. At some point, we’ll make this mapping editable from the user interface, too.</p>

---
