---
topic_id: 19523
title: "Unable To Get Vtkcamera From Vtkmrmlcameranode From C Only"
date: 2021-09-06
url: https://discourse.slicer.org/t/19523
---

# Unable to get `vtkCamera*` from `vtkMRMLCameraNode*` (from C++ only)

**Topic ID**: 19523
**Date**: 2021-09-06
**URL**: https://discourse.slicer.org/t/unable-to-get-vtkcamera-from-vtkmrmlcameranode-from-c-only/19523

---

## Post #1 by @keri (2021-09-06 01:55 UTC)

<p>Hi,</p>
<p>From module widget (<code>qSlicerMyModuleWidget.cxx</code>) I was trying to get active camera of a 3D view and apply transform to it.</p>
<p>The only two working ways to do that were:</p>
<pre><code class="lang-cpp">  qMRMLThreeDWidget* threeDWidget = app-&gt;layoutManager()-&gt;threeDWidget('View1');
  vtkCamera* camera =
      threeDWidget-&gt;threeDView()-&gt;renderer()-&gt;GetActiveCamera();
</code></pre>
<p>and</p>
<pre><code class="lang-cpp">  qMRMLThreeDWidget* threeDWidget = app-&gt;layoutManager()-&gt;threeDWidget('View1');
  vtkCamera* camera =
     threeDWidget-&gt;threeDView()-&gt;activeCamera();
</code></pre>
<p><strong>But there are other high level ways to get camera from vtkMRMLCameraNode.</strong><br>
For example:</p>
<pre><code class="lang-cpp">  vtkMRMLCameraNode* cameraNode =
      threeDWidget-&gt;threeDView()-&gt;cameraNode();

  if (!cameraNode)
    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": No active camera node found";

  vtkCamera* camera = cameraNode-&gt;GetCamera();  // there I get an exception "read access violation" even the exception abovev was not triggered
</code></pre>
<p>I get an exception on line where I’m trying to get <code>vtkCamera*</code>. Is it normal behaviour?</p>
<p>Also I’ve tried to get comeras’s logic and then retrieve from that camera and apply transform to camera (preliminary I linked to the <code>vtkSlicerCamerasModuleLogic</code>):</p>
<pre><code class="lang-cpp">  vtkSlicerCamerasModuleLogic* camerasLogic =
    vtkSlicerCamerasModuleLogic::SafeDownCast(this-&gt;moduleLogic("Cameras"));
  if (!camerasLogic)
    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": Cameras module is not found";

  vtkMRMLCameraNode* cameraNode =
      camerasLogic-&gt;GetViewActiveCameraNode(viewNode);

  if (!cameraNode)
    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": No active camera node found";

  vtkCamera* camera = cameraNode-&gt;GetCamera();

  if (!camera)
    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": No active camera found";

  vtkNew&lt;vtkTransform&gt; transform;
  transform-&gt;Scale(2, 1, 1);
  camera-&gt;SetModelTransformMatrix(transform-&gt;GetMatrix());    // here I gen an exception read access violation: `vtkObject::GetDebug()`
</code></pre>
<p>I get an exception now only when I try to apply transform.</p>
<p>All of this seemed to me strange so I decided to ask here… perhaps I don’t understand how <code>vtkMRMLCameraNode</code> is initialized?</p>
<p>By the way <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-views-renderers-and-cameras" rel="noopener nofollow ugc">python example script works fine</a></p>

---

## Post #2 by @lassoan (2021-09-06 12:53 UTC)

<p>All the code snorts above shows work. Probably your try to access the wrong objects, or access them to early, or from the wrong thread. Can you send a Github link to your module so that we can see the complete context of the method calls?</p>

---

## Post #3 by @keri (2021-09-06 13:29 UTC)

<p>Yes, here is the <a href="https://github.com/tierra-colada/Seismic" rel="noopener nofollow ugc">link to an extension I just uploaded to github</a>.<br>
I work with SlicerCAT but the module <code>Zoom</code> depends on the native Slicer (you don’t need other modules).</p>
<p>The module is in progress.<br>
You can find three <code>GainWidgets</code> (slider+spinbox). Try to use this widget for 3D view (only 3D view widgets are connected for now). I think you will understand what this widget is aimed for and if the community found it useful I could later add this widget to CTK library</p>

---

## Post #4 by @lassoan (2021-09-08 03:41 UTC)

<p>The Zoom module works well for me. Probably you have memory corruption because of using outdated DLLs - most likely due to either an incomplete build or because you have copied DLLs around.</p>
<aside class="quote no-group" data-username="keri" data-post="3" data-topic="19523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>You can find three <code>GainWidgets</code> (slider+spinbox). Try to use this widget for 3D view (only 3D view widgets are connected for now). I think you will understand what this widget is aimed for and if the community found it useful I could later add this widget to CTK library</p>
</blockquote>
</aside>
<p>There is already a slider+spin widget in CTK: <a href="http://commontk.org/index.php/Documentation/ImageGallery">ctkSliderWidget</a>. Instead of creating a new widget maybe you could improve this existing one.</p>

---

## Post #5 by @keri (2021-09-08 12:40 UTC)

<p>You are right, I have rebuilt the solution and now there is no problem to get the camera.<br>
I didn’t have an idea that the reason is outdated libs…<br>
Thank you!</p>

---
