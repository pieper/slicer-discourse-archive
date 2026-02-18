# How to pull Position and Focal Point data from default scene camera for camera angle extension

**Topic ID**: 3195
**Date**: 2018-06-15
**URL**: https://discourse.slicer.org/t/how-to-pull-position-and-focal-point-data-from-default-scene-camera-for-camera-angle-extension/3195

---

## Post #1 by @cbloodworth3 (2018-06-15 15:24 UTC)

<p>Hi folks,</p>
<p>I’m trying to create an extension which will calculate the angle of the default scene camera w.r.t. the subject in the slicer 3D scene. This would be analogous determining the C-Arm LAO/RAO and CRA/CAU angles for proper image orientation.</p>
<p>The calculation is pretty straightforward and can be done with nothing but the camera position and focal point, but I can’t seem to obtain these values using GetPosition and GetFocalPoint. Here are some code snips:</p>
<pre><code>&gt;&gt;&gt; defaultCam = slicer.mrmlScene.GetNodeByID('vtkMRMLCameraNode1')
&gt;&gt;&gt; defaultCamPosition = defaultCam.GetPosition()
&gt;&gt;&gt; print(defaultCamPosition)
_000001eb844fabd8_p_void
</code></pre>
<p>On the other hand, GetCameraAngle does function as expected:</p>
<pre><code>&gt;&gt;&gt; viewAngle1 = defaultCam.GetViewAngle()
&gt;&gt;&gt; print(viewAngle1)
30.0
</code></pre>
<p>Additionally, both SetPosition and SetFocalPoint function as expected. In fact, all of these are listed as valid member functions for the <a href="http://apidocs.slicer.org/master/classvtkMRMLCameraNode.html#a4553e1ad9a18365981b49790ef25d75a" rel="noopener nofollow ugc">vtkMRMLCameraNode Class</a>:</p>
<p>Finally, if I browse to this node in the slicer data module, all of these values are listed in the node information.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bf44f093c8cc33e19839d7d7425f016d1ed95f0.png" data-download-href="/uploads/short-url/hGy9N1D9bvJFoSYUnVOFvpWSf2E.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bf44f093c8cc33e19839d7d7425f016d1ed95f0.png" alt="image" data-base62-sha1="hGy9N1D9bvJFoSYUnVOFvpWSf2E" width="359" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">560×778 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any ideas on how to programmatically obtain the default scene camera position and focal point values?</p>
<p>Thanks for the help.</p>

---

## Post #2 by @lassoan (2018-06-15 16:39 UTC)

<p>You can use <code>GetPosition(double*)</code> variant:</p>
<pre><code>&gt;&gt;&gt; defaultCam = slicer.mrmlScene.GetNodeByID('vtkMRMLCameraNode1')
&gt;&gt;&gt; pos=[0,0,0]
&gt;&gt;&gt; defaultCam.GetPosition(pos)
&gt;&gt;&gt; pos
[54.62253179056516, 118.36363864842811, 61.73342989137638]</code></pre>

---

## Post #3 by @cbloodworth3 (2018-06-15 16:55 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="3195">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>&gt;&gt;&gt; defaultCam = slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode1’) &gt;&gt;&gt; pos=[0,0,0] &gt;&gt;&gt; defaultCam.GetPosition(pos) &gt;&gt;&gt; pos [54.62253179056516, 118.36363864842811, 61.73342989137638]</p>
</blockquote>
</aside>
<p>Thanks Andras, I suppose I misunderstood the *double variant of this function. It’s a void function which assigns ‘None’ to the output, but changes the input argument to the position. For example:</p>
<pre><code>&gt;&gt;&gt; pos = [0,0,0]
&gt;&gt;&gt; cameraPosition = defaultCam.GetPosition(pos)
&gt;&gt;&gt; print(cameraPosition)
None
&gt;&gt;&gt; pos
[3.0, 3.0, 3.0]
</code></pre>

---
