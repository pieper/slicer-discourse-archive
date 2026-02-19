---
topic_id: 19254
title: "How To Project Fiducials On The Other Side Of A Symmetry Pla"
date: 2021-08-18
url: https://discourse.slicer.org/t/19254
---

# How to project fiducials on the other side of a symmetry plane ?

**Topic ID**: 19254
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/how-to-project-fiducials-on-the-other-side-of-a-symmetry-plane/19254

---

## Post #1 by @Saggittaman (2021-08-18 14:58 UTC)

<p>Hello everyone,</p>
<p>I created a model with a symmetry plane and I would like to project a bunch of fiducials from one side to the other side of this plane symmetrically. Do someone know if it’s possible to do this and if yes how to ?</p>
<p>Thanks a lot in advance !</p>

---

## Post #2 by @muratmaga (2021-08-18 16:54 UTC)

<p>I think this part of the PseudoLMGenerator module from SlicerMorph will be helpful for you:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/5307593cb16a186d75448f63d94327c0ec5edb63/PseudoLMGenerator/PseudoLMGenerator.py#L662-L708">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/5307593cb16a186d75448f63d94327c0ec5edb63/PseudoLMGenerator/PseudoLMGenerator.py#L662-L708" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/5307593cb16a186d75448f63d94327c0ec5edb63/PseudoLMGenerator/PseudoLMGenerator.py#L662-L708" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/5307593cb16a186d75448f63d94327c0ec5edb63/PseudoLMGenerator/PseudoLMGenerator.py#L662-L708</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="662" style="counter-reset: li-counter 661 ;">
          <li>def clipAndMirrorWithPlane(self, inputData, plane):  </li>
          <li>  normal=[0,0,0]</li>
          <li>  origin=[0,0,0]  </li>
          <li>  plane.GetNormalWorld(normal)</li>
          <li>  plane.GetOriginWorld(origin)</li>
          <li>    </li>
          <li>  vtkPlane = vtk.vtkPlane()</li>
          <li>  vtkPlane.SetOrigin(origin)</li>
          <li>  vtkPlane.SetNormal(normal)</li>
          <li>  clipper = vtk.vtkClipPolyData()</li>
          <li>  clipper.SetClipFunction(vtkPlane)</li>
          <li>  clipper.SetInputData(inputData)</li>
          <li>  clipper.Update()</li>
          <li>  </li>
          <li>  mirrorMatrix = vtk.vtkMatrix4x4()</li>
          <li>  mirrorMatrix.SetElement(0, 0, 1 - 2 * normal[0] * normal[0])</li>
          <li>  mirrorMatrix.SetElement(0, 1, - 2 * normal[0] * normal[1])</li>
          <li>  mirrorMatrix.SetElement(0, 2, - 2 * normal[0] * normal[2])</li>
          <li>  mirrorMatrix.SetElement(1, 0, - 2 * normal[0] * normal[1])</li>
          <li>  mirrorMatrix.SetElement(1, 1, 1 - 2 * normal[1] * normal[1])</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/5307593cb16a186d75448f63d94327c0ec5edb63/PseudoLMGenerator/PseudoLMGenerator.py#L662-L708" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
