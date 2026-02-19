---
topic_id: 848
title: "Change Gpu Rendering Parameters From Pythonconsole"
date: 2017-08-09
url: https://discourse.slicer.org/t/848
---

# Change GPU rendering parameters from pythonconsole

**Topic ID**: 848
**Date**: 2017-08-09
**URL**: https://discourse.slicer.org/t/change-gpu-rendering-parameters-from-pythonconsole/848

---

## Post #1 by @tkuraku (2017-08-09 17:43 UTC)

<p>Hi,</p>
<p>I would like to change the Rendering to “VTK GPU Ray Casting” as well as manipulate the “GPU Memory Size”, “Quality Control”, and “Interactive Speed” from python.</p>
<p>Can someone help me do this?</p>
<p>thank you!</p>

---

## Post #2 by @pieper (2017-08-09 18:12 UTC)

<p>Hi -</p>
<p>You need to get the vtkMRMLVolumeRenderingDisplayNode from the volume and you can set the properties on it.</p>
<p>Something like if you download MRHead sample data and make it visible in VolumeRendering:</p>
<pre><code class="lang-auto">n = getNode('MRHead')
dn = n.GetNthDisplayNode(1)
</code></pre>
<p>dn will have methods to control the rendering.  They don’t always have the same names as the GUI.</p>
<p>Here are the methods:</p>
<p><a href="http://apidocs.slicer.org/master/classvtkMRMLVolumeRenderingDisplayNode.html" class="onebox" target="_blank">http://apidocs.slicer.org/master/classvtkMRMLVolumeRenderingDisplayNode.html</a></p>
<p>The type of rendering is controlled by whether a CPU or GPU concrete subclasses is in the list for the the Volume you can control.</p>
<p>Here’s where they are manipulated by the GUI:</p>
<p><code>https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/VolumeRendering/Widgets/qSlicerGPURayCastVolumeRenderingPropertiesWidget.cxx</code></p>
<p>and here’s where they are used in the rendering:</p>
<p><code>https://github.com/Slicer/Slicer/blob/ff4a605ef55fdda4fbd8c20cee41e4b184461f72/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx</code></p>
<p>Hope you can figure out what you need from the context there.</p>
<p>-Steve</p>

---
