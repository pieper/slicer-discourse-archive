---
topic_id: 29853
title: "How To Get The Central Point Of 3 Slice Panel"
date: 2023-06-06
url: https://discourse.slicer.org/t/29853
---

# How to get the central point of 3 slice panel

**Topic ID**: 29853
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/how-to-get-the-central-point-of-3-slice-panel/29853

---

## Post #1 by @jay1987 (2023-06-06 02:22 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fe77a3fe28b9f6a1a12ce92cc4d4530f190203b.png" alt="image" data-base62-sha1="ifuzMj9czzXgPZ9gnTB8dHmmnKH" width="458" height="351"><br>
the requirement is to get the central point’s layer number of a volume node , i can get the 3d focus point , but i don’t known how to get the 3 sliceview focus global position like the F-1 markups point in the picture above</p>

---

## Post #2 by @lassoan (2023-06-16 16:45 UTC)

<p>If you use layout with more or less than 3 slices or if some slices are nearly parallel then an intersection point cannot be determined. Therefore, there is no Slicer core API for getting the 3D coordinates of the intersection point.</p>
<p>Instead, of getting a point coordinate, I would recommend to use markup points (you can activate point placement and ask the user to click on an image or in a 3D view) or use crosshair (you can set the crosshair position by holding down the Shift key while moving the mouse in a view).</p>
<p>If you really must use the slice intersections, then you can of course compute it for yourself, as it is done for example in SlicerHeart extension:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/52eeb23576c7eda14dbe3e602667f4c5b68c4475/ValveView/ValveView.py#L213-L273">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/52eeb23576c7eda14dbe3e602667f4c5b68c4475/ValveView/ValveView.py#L213-L273" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/52eeb23576c7eda14dbe3e602667f4c5b68c4475/ValveView/ValveView.py#L213-L273" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/52eeb23576c7eda14dbe3e602667f4c5b68c4475/ValveView/ValveView.py#L213-L273</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="213" style="counter-reset: li-counter 212 ;">
          <li>def getPlaneIntersectionPoint(self, axialNode, ortho1Node, ortho2Node):</li>
          <li>  # Compute the center of rotation (common intersection point of the three planes)</li>
          <li>  # http://mathworld.wolfram.com/Plane-PlaneIntersection.html</li>
          <li>      </li>
          <li>  #axialNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')</li>
          <li>  #ortho1Node = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeYellow')</li>
          <li>  #ortho2Node = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeGreen')</li>
          <li>
          </li>
<li>  axialSliceToRas = axialNode.GetSliceToRAS()</li>
          <li>  n1 = [axialSliceToRas.GetElement(0,2),axialSliceToRas.GetElement(1,2),axialSliceToRas.GetElement(2,2)]</li>
          <li>  x1 = [axialSliceToRas.GetElement(0,3),axialSliceToRas.GetElement(1,3),axialSliceToRas.GetElement(2,3)]</li>
          <li>
          </li>
<li>  ortho1SliceToRas = ortho1Node.GetSliceToRAS()</li>
          <li>  n2 = [ortho1SliceToRas.GetElement(0,2),ortho1SliceToRas.GetElement(1,2),ortho1SliceToRas.GetElement(2,2)]</li>
          <li>  x2 = [ortho1SliceToRas.GetElement(0,3),ortho1SliceToRas.GetElement(1,3),ortho1SliceToRas.GetElement(2,3)]</li>
          <li>
          </li>
<li>  ortho2SliceToRas = ortho2Node.GetSliceToRAS()</li>
          <li>  n3 = [ortho2SliceToRas.GetElement(0,2),ortho2SliceToRas.GetElement(1,2),ortho2SliceToRas.GetElement(2,2)]</li>
          <li>  x3 = [ortho2SliceToRas.GetElement(0,3),ortho2SliceToRas.GetElement(1,3),ortho2SliceToRas.GetElement(2,3)]</li>
          <li>
      </li>
</ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerHeart/SlicerHeart/blob/52eeb23576c7eda14dbe3e602667f4c5b68c4475/ValveView/ValveView.py#L213-L273" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jay1987 (2023-06-17 04:21 UTC)

<p>thank you lassoan , it’s really help</p>

---
