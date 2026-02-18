# Can I create a changeable Linear Transform Node and never appeared in the menu

**Topic ID**: 5619
**Date**: 2019-02-02
**URL**: https://discourse.slicer.org/t/can-i-create-a-changeable-linear-transform-node-and-never-appeared-in-the-menu/5619

---

## Post #1 by @timeanddoctor (2019-02-02 15:47 UTC)

<p>I created many Linear-Transforms  succesfully with this code:<br>
transform = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLinearTransformNode’)<br>
vTransform = vtk.vtkTransform()<br>
…<br>
transform.SetMatrixTransformToParent(vTransform.GetMatrix())</p>
<p>But there are so many transforms. So, I don’t want it appeard even in data module.<br>
Can I change the code to achive my goials and doesn’t affect the transform function, such as：<br>
they have a NodeID, or editable.</p>

---

## Post #2 by @timeanddoctor (2019-02-02 15:49 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1af8cbb16e2c740123ac3b75cf564c542d5dc6a9.jpeg" alt="360%E6%88%AA%E5%9B%BE-42702937" data-base62-sha1="3QBsiOYksJbd2bT2ULjWYQW5xhf" width="548" height="273"></p>

---

## Post #3 by @pieper (2019-02-02 21:03 UTC)

<p>Try this:</p>
<p><code>transformNode.SetHideFromEditors(True)</code></p>
<p>You probably have to set this before adding to the scene.</p>
<p>HTH</p>

---
