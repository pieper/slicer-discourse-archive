---
topic_id: 21131
title: "Getnthcontrolpointorientationmatrix How Should We Consider I"
date: 2021-12-18
url: https://discourse.slicer.org/t/21131
---

# GetNthControlPointOrientationMatrix : How should we consider it?

**Topic ID**: 21131
**Date**: 2021-12-18
**URL**: https://discourse.slicer.org/t/getnthcontrolpointorientationmatrix-how-should-we-consider-it/21131

---

## Post #1 by @chir.set (2021-12-18 18:26 UTC)

<p>A markups fiducial node has this function : GetNthControlPointOrientationMatrix.</p>
<p>While tinkering with it, it does not get modified if a transform is applied to the fiducial node, nor if it is placed in a reformatted slice view. If we modify this matrix with SetNthControlPointOrientationMatrix, the applied matrix is always retrieved unaltered.</p>
<p>Is it only a storage place intended for developers ?<br>
Would the markups internals require/modifiy it ? In what circumstances?</p>
<p>Thanks for any input.</p>

---

## Post #2 by @mau_igna_06 (2021-12-18 18:45 UTC)

<p>Please try this:</p>
<pre><code class="lang-auto">orientationMatrix = vtk.vtkMatrix3x3()
getNode('F').GetNthControlPointOrientationMatrix(0,matrix)
#should be the identity
print(matrix)

matrix.SetElement(1,1,-1)
matrix.SetElement(2,2,-1)
#matrix has changed
print(matrix)

#change the orientationMatrix by our changed matrix
getNode('F').SetNthControlPointOrientationMatrix(0,matrix)

#read the new orientationMatrix value, it should not be the identity
matrix2 = vtk.vtkMatrix3x3()
getNode('F').GetNthControlPointOrientationMatrix(0,matrix2)
print(matrix2)

#It's okey
</code></pre>

---

## Post #3 by @chir.set (2021-12-18 19:10 UTC)

<p>It’s very clear, thank you.</p>
<p>But is it only a storage place ? If we modify it, how would it affect the fiducial node or a slice node ? I mean, does Slicer rely on it to do something ? Can we just store here an orientation matrix parameter that we would be needing later ?</p>

---

## Post #4 by @mau_igna_06 (2021-12-18 19:17 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="21131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>But is it only a storage place ? If we modify it, how would it affect the fiducial node or a slice node ? I mean, does Slicer rely on it to do something ? Can we just store here an orientation matrix parameter that we would be needing later ?</p>
</blockquote>
</aside>
<p>I think it should work as storage for markups for what I have seen on a fast search through the C++ code. I don’t know about sliceNodes.</p>
<p>Yes I think you can save here an orientationMatrix that you would be needing later</p>

---

## Post #5 by @chir.set (2021-12-18 19:20 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="4" data-topic="21131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Yes I think you can save here an orientationMatrix that you would be needing later</p>
</blockquote>
</aside>
<p>That would simplify things a lot, thank you.</p>

---

## Post #6 by @pieper (2021-12-18 19:27 UTC)

<p>Fiducial orientations are a holdover from the original implementation in slicer2 - many of the coolest features of Delphine’s original work have never been ported to later slicer versions.</p>
<p><a href="http://dspace.mit.edu/handle/1721.1/87240" class="onebox" target="_blank" rel="noopener">http://dspace.mit.edu/handle/1721.1/87240</a></p>

---

## Post #7 by @lassoan (2021-12-19 15:09 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="21131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>While tinkering with it, it does not get modified if a transform is applied to the fiducial node, nor if it is placed in a reformatted slice view. If we modify this matrix with SetNthControlPointOrientationMatrix, the applied matrix is always retrieved unaltered.</p>
</blockquote>
</aside>
<p>In general all node properties are set and retrieved in the node’s coordinate system. You can apply the node’s parent transform to the positions, orientations, etc. to get that in world coordinate system. If you only have linear parent transforms then this is a simple matrix multiplication.</p>
<p>There are convenience functions with “World” or “RAS” suffix in their name that get/set information in world coordinate system. See for example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7b8eaec72a9563613caab7b0fb044a6b6d7b3d4b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.cxx#L762">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7b8eaec72a9563613caab7b0fb044a6b6d7b3d4b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.cxx#L762" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7b8eaec72a9563613caab7b0fb044a6b6d7b3d4b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.cxx#L762" target="_blank" rel="noopener">Slicer/Slicer/blob/7b8eaec72a9563613caab7b0fb044a6b6d7b3d4b/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.cxx#L762</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="752" style="counter-reset: li-counter 751 ;">
          <li>  ControlPoint *controlPoint = this-&gt;GetNthControlPointCustomLog(pointIndex, "GetNthControlPointPosition");</li>
          <li>  if (!controlPoint)</li>
          <li>    {</li>
          <li>    return nullptr;</li>
          <li>    }</li>
          <li></li>
          <li>  return controlPoint-&gt;Position;</li>
          <li>}</li>
          <li></li>
          <li>//-----------------------------------------------------------</li>
          <li class="selected">int vtkMRMLMarkupsNode::GetNthControlPointPositionWorld(int pointIndex, double worldxyz[3])</li>
          <li>{</li>
          <li>  ControlPoint *controlPoint = this-&gt;GetNthControlPointCustomLog(pointIndex, "GetNthControlPointPositionWorld");</li>
          <li>  if (!controlPoint)</li>
          <li>    {</li>
          <li>    return 0;</li>
          <li>    }</li>
          <li>  this-&gt;TransformPointToWorld(controlPoint-&gt;Position, worldxyz);</li>
          <li>  return 1;</li>
          <li>}</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @chir.set (2021-12-19 19:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="21131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are convenience functions with “World” or “RAS” suffix in their name that get/set information in world coordinate system.</p>
</blockquote>
</aside>
<p>Yes, I noticed that, and tend to use the ‘World’ suffixed functions every time.</p>

---

## Post #9 by @chir.set (2021-12-19 20:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="21131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are convenience functions with “World” or “RAS” suffix in their name that get/set information in world coordinate system.</p>
</blockquote>
</aside>
<p>I noticed strange results with the World variants here :</p>
<pre><code class="lang-auto">matrix = vtk.vtkMatrix3x3()
f = slicer.util.getNode("F")
f.GetNthControlPointOrientationMatrixWorld(0, matrix)
# matrix is identity

matrix.SetElement(0, 1, 2.0)
matrix.SetElement(1, 2, -2.0)
print(matrix)

f.SetNthControlPointOrientationMatrixWorld(0, matrix)

matrix2 = vtk.vtkMatrix3x3()
f.GetNthControlPointOrientationMatrixWorld(0, matrix2)
print(matrix2)
# matrix2 : all 9 values are 0

seq = GetNthControlPointOrientationMatrixWorld(0)
# ValueError: cannot create object of unknown type "vtkVector_IdLi9EE"
</code></pre>
<p>I guess no one is relying on this, but it’s worth reporting.</p>

---

## Post #10 by @lassoan (2021-12-20 02:57 UTC)

<p>Setting orientation of a control point in a non-transformed markup node using the <code>SetNthControlPointOrientationMatrixWorld</code> method indeed did not work correctly. It is <a href="https://github.com/Slicer/Slicer/commit/f01d58a2d6760a9e41b4a195f7f18cf92f1fa04e">fixed</a> now. Since control point orientation is not used for anything else than recording it and storing it, it is not tested very widely and thoroughly and so the bug remain unnoticed.</p>
<p>What do you plan to use the control point orientation for?</p>

---

## Post #11 by @chir.set (2021-12-20 07:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="21131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you plan to use the control point orientation for?</p>
</blockquote>
</aside>
<p>In a self-contained tool, I need to record the orientation part of the SliceToRAS matrix. It will be different at each fiducial control point. This Get/Set facility seems to be available but not used in Slicer itself. So it gets in very handy.</p>
<p>As a side note, this orientation matrix is not saved with the markups node. Attaching this data to the control points will therefore be volatile, scene-wide only. It’s yet welcome.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="21131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is <a href="https://github.com/Slicer/Slicer/commit/f01d58a2d6760a9e41b4a195f7f18cf92f1fa04e" rel="noopener nofollow ugc">fixed</a> now.</p>
</blockquote>
</aside>
<p>Thank you.</p>

---
