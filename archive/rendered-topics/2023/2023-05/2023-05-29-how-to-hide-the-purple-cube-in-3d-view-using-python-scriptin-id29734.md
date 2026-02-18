# How to hide the purple cube in 3D view using Python scripting?

**Topic ID**: 29734
**Date**: 2023-05-29
**URL**: https://discourse.slicer.org/t/how-to-hide-the-purple-cube-in-3d-view-using-python-scripting/29734

---

## Post #1 by @seanchoi0519 (2023-05-29 10:24 UTC)

<p>Hello Prof Lasso,</p>
<p>Is there a way to implement hiding the magenta cube programmatically via python code?</p>
<p>Thanks a lot!<br>
Sean</p>

---

## Post #2 by @pearsonm (2023-05-30 01:08 UTC)

<p>One way to do it is to find the node in the Subject Hierarchy and set the visibility to 0. The script repository has an example of manipulating a hierarchy item <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#manipulate-subject-hierarchy-item" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#manipulate-subject-hierarchy-item</a></p>

---

## Post #3 by @seanchoi0519 (2023-05-30 04:27 UTC)

<p>Thank you - though I am not sure how to locate the magenta cube node in the subject hierarchy</p>

---

## Post #4 by @jamesobutler (2023-05-30 11:24 UTC)

<p>With some searching in the forum you can usually find existing solutions that can help directly or indirectly with finding what you need.</p>
<p>For example see this post that mentions about the box in the 3D view.</p>
<aside class="quote quote-modified" data-post="1" data-topic="24350">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/change-color-box-within-3d-view/24350">Change color box within 3D view</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi, 
<a href="https://discourse.slicer.org/t/how-to-change-color-of-3d-cube-inside-3d-view/769/10">The issue already been asked</a> but still I’m  trying to struggle with this. 
The idea is to modify the color of the cube from 3D view when the view is created within SlicerCAT. 
To solve this I need to understand how to get this cube as VTK or MRML object. Who is responsible for creating it? 
For example I can see that <a href="https://github.com/Slicer/Slicer/blob/115e32bdf8e478208fc2c75179cf2ecdb555d984/Libs/MRML/Core/vtkMRMLViewNode.h#L318" rel="noopener nofollow ugc">vtkMRMLViewNode</a> has BoxVisible attribute. To modify visibility one simply triggers this attribute: 
viewNode = slicer.app.layoutManager().threeDWidget(0).mrmlViewNode()
viewNod…
  </blockquote>
</aside>

<p>Also consult the Slicer script repository for examples of common tasks that can help guide you even if it is not exactly what you desire. For example here is how to change the box color, but changing box visibility could be inferred from that example.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-box-color-in-3d-view" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-box-color-in-3d-view</a></p>

---
