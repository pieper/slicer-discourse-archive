---
topic_id: 23256
title: "Get Set Gui Data From Python"
date: 2022-05-03
url: https://discourse.slicer.org/t/23256
---

# Get/Set GUI data from Python

**Topic ID**: 23256
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/get-set-gui-data-from-python/23256

---

## Post #1 by @Marc-3d (2022-05-03 09:37 UTC)

<p>Hi everyone,</p>
<p>I am trying write a Python script that accesses the “volume” node and “ROI” nodes that the user has manually selected in the “Volume Rendering” module.</p>
<p>Does anyone have any clues on how to access this information from Python?</p>
<p>Thank you in advance  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @cpinter (2022-05-03 09:57 UTC)

<p>This should help:</p>
<pre><code class="lang-auto">volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.GetFirstVolumeRenderingDisplayNode(volumeNode)
roiNode = displayNode.GetROINode()
</code></pre>

---

## Post #3 by @Marc-3d (2022-05-03 11:30 UTC)

<p>Thank for the answer, but what is “volumeNode” in your example? An empty “vtkMRMLScalarVolumeNode”?</p>

---

## Post #4 by @mau_igna_06 (2022-05-03 12:48 UTC)

<p><code>volumeNode = getNode("nodeNameInTheDataModule")</code></p>

---

## Post #5 by @Marc-3d (2022-05-11 16:02 UTC)

<p>The problem is that I don’t know the name of the volumeNode in advance, or it’s ID.</p>
<p>I ended up figuring out how to access the GUI element that holds the list of volumes. Maybe it helps someone else in the future <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<pre><code>vol_node = slicer.modules.volumerendering.widgetRepresentation().findChild(slicer.qMRMLNodeComboBox(), "VolumeNodeComboBox").currentNode();</code></pre>

---
