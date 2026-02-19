---
topic_id: 23248
title: "Volume Rendering Works Via Python Console But Not Via Extens"
date: 2022-05-02
url: https://discourse.slicer.org/t/23248
---

# [Volume Rendering] Works via python console but not via extension code

**Topic ID**: 23248
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/volume-rendering-works-via-python-console-but-not-via-extension-code/23248

---

## Post #1 by @strider_hunter (2022-05-02 21:05 UTC)

<p>Hi,<br>
When I use the following code in my Slicer Extension (Slicer 4.11.20210226), I am unable to get a volume render in the 3D view (a custom vtkMRMLViewNode).</p>
<pre><code class="lang-auto">node = slicer.util.getNode('&lt;nodename&gt;') # a vtkMRMLScalarVolumeNode
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(node)
displayNode.SetVisibility(True)
</code></pre>
<p>But when I copy paste the same to the python console, it works! Upon checking the volume rendering module, I noticed that my extension code does not set the eye icon to visible, but copy-pasting the code in the python console does that. In my extension, I also use the following displayNode functions to verify if the visibility was set properly and their output is all 1.</p>
<p><code>print (' ------ [myUtil.set3DBackground()]: ', displayNode.GetVisibility(), displayNode.GetVisibility2D(), displayNode.GetVisibility3D())</code></p>
<p>What may I be missing here?</p>
<hr>
<p>Note: Prior to the volume rendering, my extension updates the 3D array that makes up the <code>vtkMRMLScalarVolumeNode</code> being rendered.</p>

---

## Post #2 by @mau_igna_06 (2022-05-02 23:58 UTC)

<p>May be use a timer callback to set up the volume rendering because you need to give some time to the scalar volume to update I think</p>

---

## Post #3 by @strider_hunter (2022-05-04 07:58 UTC)

<p>Thanks! It worked with the timer!</p>
<pre><code class="lang-auto">def set3DBackgroundTimed(node):
    displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(node)
    displayNode.SetVisibility(True)

qt.QTimer.singleShot(1000, lambda: set3DBackgroundTimed(node))
</code></pre>

---
