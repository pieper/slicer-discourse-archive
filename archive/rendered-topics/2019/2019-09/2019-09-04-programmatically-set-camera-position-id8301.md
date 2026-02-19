---
topic_id: 8301
title: "Programmatically Set Camera Position"
date: 2019-09-04
url: https://discourse.slicer.org/t/8301
---

# Programmatically set camera position

**Topic ID**: 8301
**Date**: 2019-09-04
**URL**: https://discourse.slicer.org/t/programmatically-set-camera-position/8301

---

## Post #1 by @rprueckl (2019-09-04 19:11 UTC)

<p>Hi,</p>
<p>I want to set camera position programmatically in this way:</p>
<pre><code class="lang-auto">int wasModifying = camera-&gt;StartModify();
camera-&gt;SetPosition(cameraPosition[0], cameraPosition[1], cameraPosition[2]);
camera-&gt;SetFocalPoint(cameraFocalPointPosition[0], cameraFocalPointPosition[1], cameraFocalPointPosition[2]);
camera-&gt;SetViewUp(0, 0, 1);
camera-&gt;EndModify(wasModifying);
</code></pre>
<p>which works in some cases. However, when I zoom in or out before the calls manually so that the camera position is significantly different than the position I want to set, the view stays black after the calls. Only when I start to rotate the view afterwards manually, it gets updated and shows the correct angle. Is there any way to force an update?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-09-04 20:05 UTC)

<p>ViewUp vector must be orthogonal to the line that connects position and focal point. Otherwise the behavior is undefined.</p>

---

## Post #3 by @rprueckl (2019-09-05 08:30 UTC)

<p>Thanks for your input, however it did not solve the problem. The missing thing was to call <code>ResetClippingRange</code>. The code below does what it should.</p>
<pre><code class="lang-auto">viewLogic-&gt;StartCameraNodeInteraction(vtkMRMLCameraNode::LookFromAxis);
camera-&gt;SetFocalPoint(cameraFocalPointPosition[0], cameraFocalPointPosition[1], cameraFocalPointPosition[2]);
camera-&gt;SetPosition(cameraPosition[0], cameraPosition[1], cameraPosition[2]);
camera-&gt;SetViewUp(0, 0, 1);
camera-&gt;GetCamera()-&gt;OrthogonalizeViewUp();
camera-&gt;ResetClippingRange();
viewLogic-&gt;EndCameraNodeInteraction();
</code></pre>

---

## Post #4 by @lassoan (2019-09-05 13:25 UTC)

<p>Yes, <code>ResetClippingRange</code> is a good point, you need that.</p>
<p><code>OrthogonalizeViewUp</code> discards current camera ViewUp vector value. So, if you care what is up direction in the view then you need to set ViewUp properly (and don’t call <code>OrthogonalizeViewUp</code>); if it does not matter which way is up in the view then just call <code>OrthogonalizeViewUp</code> (and don’t call <code>SetViewUp</code>). See details in <a href="https://github.com/Kitware/VTK/blob/master/Rendering/Core/vtkCamera.cxx" rel="nofollow noopener">vtkCamera source code</a>.</p>

---

## Post #5 by @rprueckl (2019-09-06 08:31 UTC)

<p>The camera automatically orthogonalizes any given ViewUp vector.<br>
See <a href="https://vtk.org/vtk-users-guide/" rel="noopener nofollow ugc">VTK User’s Guide</a> (page 50):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/543591a869409c09154ef6c62d249e2ce17ae04a.png" data-download-href="/uploads/short-url/c0WSt1N3qT8UR7kKXoIgnkVxuRQ.png?dl=1" title="vtk" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/543591a869409c09154ef6c62d249e2ce17ae04a_2_690x372.png" alt="vtk" data-base62-sha1="c0WSt1N3qT8UR7kKXoIgnkVxuRQ" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/543591a869409c09154ef6c62d249e2ce17ae04a_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/543591a869409c09154ef6c62d249e2ce17ae04a_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/543591a869409c09154ef6c62d249e2ce17ae04a.png 2x" data-dominant-color="F1F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vtk</span><span class="informations">1140×616 86.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
and</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/VTK/blob/ad16439a2f12c41d9de73a72b211bf775d713963/Common/Transforms/vtkPerspectiveTransform.cxx#L440-L443">
  <header class="source">

      <a href="https://github.com/Kitware/VTK/blob/ad16439a2f12c41d9de73a72b211bf775d713963/Common/Transforms/vtkPerspectiveTransform.cxx#L440-L443" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/ad16439a2f12c41d9de73a72b211bf775d713963/Common/Transforms/vtkPerspectiveTransform.cxx#L440-L443" target="_blank" rel="noopener nofollow ugc">Kitware/VTK/blob/ad16439a2f12c41d9de73a72b211bf775d713963/Common/Transforms/vtkPerspectiveTransform.cxx#L440-L443</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="440" style="counter-reset: li-counter 439 ;">
          <li>// orthogonalize viewUp and compute viewSideways</li>
          <li>vtkMath::Cross(viewUp,viewPlaneNormal,viewSideways);</li>
          <li>vtkMath::Normalize(viewSideways);</li>
          <li>vtkMath::Cross(viewPlaneNormal,viewSideways,orthoViewUp);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
This is called by <code>setViewUp(...)  -&gt; ComputeViewTransform() -&gt; Transform-&gt;SetupCamera(...)</code></p>
<p>The call to <code>OrthogonalizeViewUp()</code> is required to retrieve back the orthogonalized vector from the transform for retrieving it via <code>GetViewUp()</code> and for the convenience methods like <code>Pitch, Roll, Yaw, ...</code></p>

---

## Post #6 by @lassoan (2019-09-06 14:28 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="5" data-topic="8301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>The camera automatically orthogonalizes any given ViewUp vector.</p>
</blockquote>
</aside>
<p>That’s correct. That’s why you don’t need to call both <code>SetViewUp()</code> and <code>OrthogonalizeViewUp()</code>.</p>
<p>Note that the built-in very simplistic orthogonalization method should only be used for small angular deviations. If view up direction is nearly parallel to the view normal then the result is undefined.</p>
<p>In the cited VTK User guide example the OrthogonalizeViewUp call is unnecessary, but since the user guide is not maintained anymore, we cannot submit a PR to fix it. VTK textbook is still maintained, you can find up-to-date version <a href="https://lorensen.github.io/VTKExamples/site/VTKBook/">here</a>.</p>

---
