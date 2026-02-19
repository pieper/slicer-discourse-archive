---
topic_id: 15936
title: "Wrapsolidify Surface"
date: 2021-02-10
url: https://discourse.slicer.org/t/15936
---

# WrapSolidify surface

**Topic ID**: 15936
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/wrapsolidify-surface/15936

---

## Post #1 by @siaeleni (2021-02-10 15:40 UTC)

<p>Hello,</p>
<p>I use Wrap Solifidy feature in order to create the outer surface of a model, but I get some strange results like the photo attached. Do you have any idea why?</p>
<p>Thanks!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0158eaf6d5231d4037b84e4a1d2a2349ae7ca77.jpeg" alt="notsmooth" data-base62-sha1="p7IdIrst8SMHDzDhUflcSlNOv6D" width="374" height="234"></p>

---

## Post #2 by @lassoan (2021-02-10 15:47 UTC)

<p>This happens because shrinking step sometimes finds the inner surface of the shell. This is fixed in <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/pull/6">this pull request</a>, so updating to latest version of the extension in latest Slicer Stable Release or latest Slicer Preview Release should fix the problem. If you still encounter these artifacts then locate <code>SegmentEditorEffect.py</code> file on your computer and change 100 to a smaller number (50, 20, 10).</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/9e9e15ea0a9cc7a03f75a6aaf8451e755967695f/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L484" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/blob/9e9e15ea0a9cc7a03f75a6aaf8451e755967695f/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L484" target="_blank" rel="noopener">sebastianandress/Slicer-SurfaceWrapSolidify/blob/9e9e15ea0a9cc7a03f75a6aaf8451e755967695f/SegmentEditorWrapSolidify/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py#L484</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="474" style="counter-reset: li-counter 473 ;">
<li>    maxRadius = max(diameters)/2.0</li><li>    sphereSource = vtk.vtkSphereSource()</li><li>    # to make sure the volume is fully included in the sphere, radius must be sqrt(2) times larger</li><li>    sphereSource.SetRadius(maxRadius*1.5)</li><li></li><li>    # Set resolution to be about one magnitude lower than the final resolution</li><li>    # (by creating an initial surface element for about every 100th final element).</li><li>    sphereSurfaceArea = 4 * math.pi * maxRadius*maxRadius</li><li>    voxelSurfaceArea = spacing * spacing</li><li>    numberOfSurfaceElements = sphereSurfaceArea/voxelSurfaceArea</li><li class="selected">    numberOfIinitialSphereSurfaceElements = numberOfSurfaceElements/100</li><li>    sphereResolution = math.sqrt(numberOfIinitialSphereSurfaceElements)</li><li>    # Set resolution to minimum 10</li><li>    sphereResolution = max(int(sphereResolution), 10)</li><li>    sphereSource.SetPhiResolution(sphereResolution)</li><li>    sphereSource.SetThetaResolution(sphereResolution)</li><li>    sphereSource.SetCenter((bounds[0]+bounds[1])/2.0, (bounds[2]+bounds[3])/2.0, (bounds[4]+bounds[5])/2.0)</li><li>    sphereSource.Update()</li><li>    initialRegionPd = sphereSource.GetOutput()</li><li>elif self.region == REGION_SEGMENT:</li><li>  # create initial region from segment (that will be grown)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Let us know how if it worked.</p>

---
