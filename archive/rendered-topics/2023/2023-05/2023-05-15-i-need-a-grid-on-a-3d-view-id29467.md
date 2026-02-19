---
topic_id: 29467
title: "I Need A Grid On A 3D View"
date: 2023-05-15
url: https://discourse.slicer.org/t/29467
---

# I need a grid on a 3D view

**Topic ID**: 29467
**Date**: 2023-05-15
**URL**: https://discourse.slicer.org/t/i-need-a-grid-on-a-3d-view/29467

---

## Post #1 by @q2577040659 (2023-05-15 01:48 UTC)

<p>Can I put a translucent picture on my camera?<br>
I need a grid to help me adjust the position of the model in 3D view. The grid doesn’t need to be zoomed in or out. It stays on the front of the camera. No matter what you do, the grid doesn’t change at all unless you turn it off.<br>
Who can tell me how to do it? Thank you for all.</p>

---

## Post #2 by @pieper (2023-05-15 14:28 UTC)

<p>Probably the cleanest would be to write <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#the-displayable-manager">a displayable manager</a>.  There’s <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/DisplayableManager/Python/mrmlDisplayableManager/vtkScriptedExampleDisplayableManager.py">an example</a> if you want to try writing one in python.</p>

---

## Post #3 by @q2577040659 (2023-05-16 05:13 UTC)

<p>Thank you. Is there another way?</p>

---
