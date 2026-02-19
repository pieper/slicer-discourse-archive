---
topic_id: 3431
title: "Volume Rendering With Python"
date: 2018-07-09
url: https://discourse.slicer.org/t/3431
---

# Volume Rendering with Python

**Topic ID**: 3431
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/volume-rendering-with-python/3431

---

## Post #1 by @trnhx001 (2018-07-09 14:49 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.9.0<br>
Hi All,</p>
<p>I am trying to use python to do volume rendering and set parameters for it. These are  few lines of attempt. However, I run into the problem when trying to get Volume Proper Node to set the preset “CT-Bone”. It says the volumePropertyNode is nonetype object. I wonder why this happens. Thank you for your help.</p>
<pre><code class="lang-auto">#Tune volume rendering parameters
volRenLogic = slicer.modules.volumerendering.logic()

preset = volRenLogic.GetPresetByName('CT-Bone')
presetNode = slicer.mrmlScene.AddNode(preset)
volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
displayNode = volRenLogic.CreateVolumeRenderingDisplayNode()


volumePropertyNode = displayNode.GetVolumePropertyNode()
volumePropertyNode.Copy(preset)

volRenLogic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode, presetNode)
slicer.mrmlScene.AddNode(displayNode)
displayNode.UnRegister(volRenLogic)
volumeNode.AddAndObserveDisplayNodeID(preset.GetID())
</code></pre>

---

## Post #2 by @lassoan (2018-07-09 18:02 UTC)

<p>CreateVolumeRenderingDisplayNode only creates display node and not volume property node. I think UpdateDisplayNodeFromVolumeNode can create and set volume property node, or you can manually create a vtkMRMLVolumePropertyNode, add to the scene, and set in the display node.</p>

---

## Post #3 by @cpinter (2018-07-11 14:48 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="3063">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/f1d935/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-volume-rendering-preset-using-python/3063">How to set volume rendering preset using Python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi developers, 
Using a Python script I am trying to load a volume, set the slice views and also a volume rendering preset. While loading and setting the slice views works out well, the volume rendering always shows up with the default settings and not the targeted preset. Could someone please give me a hint of what’s missing? Is there a way to adjust the preset parameter “shift” in advance? 
Since I am new to Slicer development I would also be happy about any hint of how to  improve the code (i…
  </blockquote>
</aside>


---
