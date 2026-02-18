# "Jump slices" but for camera in 3D view

**Topic ID**: 13336
**Date**: 2020-09-04
**URL**: https://discourse.slicer.org/t/jump-slices-but-for-camera-in-3d-view/13336

---

## Post #1 by @mangotee (2020-09-04 12:04 UTC)

<p>Hi,<br>
a quick question - in the markups module, we can “jump slices”, e.g. onto a fiducial, and we can center slice views onto that fiducial. That way, we can easily focus on a point in 3D. Is there a way to automatically achieve this for the 3D view? I am aware that the camera can be positioned with 6 DOF. But let’s say I can constrain this, specifically, I’d like to view onto the scene from “right” axis:</p>
<pre><code>lm = slicer.app.layoutManager()
view = lm.threeDWidget(0).threeDView()
view.lookFromViewAxis(ctk.ctkAxesWidget.Right) 
</code></pre>
<p>And then I would like to set the camera anterior/superior coordinates to the coordinates of the fiducial I wanna “look at” (I think I could manipulate the camer’s location along the L/R axis via its zoom parameter).</p>

---

## Post #2 by @lassoan (2020-09-04 14:31 UTC)

<p>You can set the camera focal point to the fiducial point to make the camera look at and rotate around that point. You may adjust the camera position, view up direction, and viewing angle as well, if you also want to control from where you look at and how large things appear.</p>
<p>You can find an example of setting the focal point here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/1ce740cc25e6f22f7a2816767656fd414a5973c7/Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumeRenderingPlugin.cxx#L222-L265" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/1ce740cc25e6f22f7a2816767656fd414a5973c7/Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumeRenderingPlugin.cxx#L222-L265" target="_blank" rel="noopener">Slicer/Slicer/blob/1ce740cc25e6f22f7a2816767656fd414a5973c7/Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumeRenderingPlugin.cxx#L222-L265</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="222" style="counter-reset: li-counter 221 ;">
<li>bool resetFieldOfView = settings.value("SubjectHierarchy/ResetFieldOfViewOnShowVolume", true).toBool();</li>
<li>if (resetFieldOfView)</li>
<li>  {</li>
<li>  double rasBounds[6] = { 0.0 };</li>
<li>  volumeNode-&gt;GetRASBounds(rasBounds);</li>
<li>  double cameraFocalPoint[3] =</li>
<li>    {</li>
<li>    (rasBounds[0] + rasBounds[1]) / 2.0,</li>
<li>    (rasBounds[2] + rasBounds[3]) / 2.0,</li>
<li>    (rasBounds[4] + rasBounds[5]) / 2.0,</li>
<li>    };</li>
<li>  qMRMLLayoutManager* layoutManager = qSlicerApplication::application()-&gt;layoutManager();</li>
<li>  if (layoutManager)</li>
<li>    {</li>
<li>    for (int i = 0; i &lt; layoutManager-&gt;threeDViewCount(); i++)</li>
<li>      {</li>
<li>      qMRMLThreeDWidget* threeDWidget = layoutManager-&gt;threeDWidget(i);</li>
<li>      if (!threeDWidget)</li>
<li>        {</li>
<li>        continue;</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/1ce740cc25e6f22f7a2816767656fd414a5973c7/Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumeRenderingPlugin.cxx#L222-L265" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
