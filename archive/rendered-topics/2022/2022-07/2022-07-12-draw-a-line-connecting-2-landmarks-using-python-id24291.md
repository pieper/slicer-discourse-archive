# Draw a line connecting 2 landmarks using Python

**Topic ID**: 24291
**Date**: 2022-07-12
**URL**: https://discourse.slicer.org/t/draw-a-line-connecting-2-landmarks-using-python/24291

---

## Post #1 by @l2022 (2022-07-12 18:56 UTC)

<p>Hi,</p>
<p>Could you please tell me how I can add a line in the 3D view connecting 2 specific landmarks using  Python in Slicer?</p>
<p>Thank you</p>

---

## Post #2 by @ungi (2022-07-12 20:10 UTC)

<p>Hi, there is a line markup in Slicer that may just be what you need. You can find example code on how to program markup nodes here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a><br>
The object type is vtkMRMLMarkupsLineNode.</p>

---

## Post #3 by @l2022 (2022-07-25 12:43 UTC)

<p>Hi, thank you for your reply.</p>
<p>I tried to find an example that does the same I want to do but I couldn’t find it.<br>
Can you please tell me what I should write in Python in order to define and show a 3D line connecting 2 specific vtkMRMKMarkupsFiducialNode?</p>
<p>Thank you</p>

---
