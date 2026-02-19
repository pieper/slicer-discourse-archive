---
topic_id: 5597
title: "How To Load New Volume While Keeping The View Parameters Suc"
date: 2019-01-31
url: https://discourse.slicer.org/t/5597
---

# How to load new volume while keeping the view parameters, such as 3D orientation, 2D slice number?

**Topic ID**: 5597
**Date**: 2019-01-31
**URL**: https://discourse.slicer.org/t/how-to-load-new-volume-while-keeping-the-view-parameters-such-as-3d-orientation-2d-slice-number/5597

---

## Post #1 by @Jeff_CAO (2019-01-31 10:50 UTC)

<p>Hi, everyone. I am a slicer beginner. I am going to write a application based on slicer in python. A problem makes me struggled. <strong>I need to reload a volume both in 2D viewers and render this volume. More importantly, I need to keep the orientations in 3D and 2D layer slice number (or everything except the volume data)</strong>. I tried to extract the <em>scene</em> node first, and reserve scene properties. But whenever I use the reload button to change the volume data, then it returns none <em>scene</em>.  Your suggestions would be really appreciated. Thanks.</p>

---

## Post #2 by @timeanddoctor (2019-01-31 10:54 UTC)

<p>Maybe you can take a transform (“General registration (BRAINS)” and “General registration (Elastix)” modules) between them to align…after load Dicom with different RAS</p>

---

## Post #3 by @stephan (2019-01-31 19:04 UTC)

<p>You can use vtkMRMLSliceNode::GetSliceToRAS() to retrieve the current slice view position.</p>
<p>Example for the Red slice view:</p>
<pre><code>viewMatrixRed = vtk.vtkMatrix4x4()
viewMatrixRed.DeepCopy(slicer.app.layoutManager().sliceWidget("Red").mrmlSliceNode().GetSliceToRAS())
</code></pre>
<p>then, after loading your new volume, set the Red slice view to the settings saved in viewMatrixRed:</p>
<pre><code>slicer.app.layoutManager().sliceWidget("Red").mrmlSliceNode().GetSliceToRAS().DeepCopy(viewMatrixRed)
</code></pre>
<p>The only thing I was not able to get working quickly is to force updating the Red view. So it is not instantly re-drawn at the new new slice position.<br>
But if you, for now, pan the view a little (drag while holding the middle mouse button), it is updated and the saved slice setting is shown.<br>
If someone else could pitch in how to force the slice view to update / re-draw, that would be perfect.</p>

---

## Post #4 by @lassoan (2019-02-02 02:55 UTC)

<aside class="quote no-group" data-username="stephan" data-post="3" data-topic="5597">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>If someone else could pitch in how to force the slice view to update / re-draw, that would be perfect.</p>
</blockquote>
</aside>
<p>You can call <code>slicer.app.layoutManager().sliceWidget("Red").mrmlSliceNode()-&gt;UpdateMatrices()</code> to update slice views after modifying SliceToRAS</p>
<p>If the goal is to load the volume but leave the viewers intact, add <code>{"show": False}</code> to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadVolume"><code>slicer.util.loadVolume(...)</code></a> properties parameter. You can then show the volume without moving slice views using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers"><code>slicer.util.setSliceViewerLayers()</code></a> method.</p>

---
