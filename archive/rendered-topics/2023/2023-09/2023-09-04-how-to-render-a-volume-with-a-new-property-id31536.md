---
topic_id: 31536
title: "How To Render A Volume With A New Property"
date: 2023-09-04
url: https://discourse.slicer.org/t/31536
---

# How to render a volume with a new property

**Topic ID**: 31536
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/how-to-render-a-volume-with-a-new-property/31536

---

## Post #1 by @slicer365 (2023-09-04 07:40 UTC)

<p>I saved a property file(0.vp), I want to use this property file torender the volume through the script, how to achieve, the following is the code I can complete.</p>
<pre><code class="lang-auto">     volumeNode=getNode("CTChest")
     volRenLogic = slicer.modules.volumerendering.logic()
     volRenLogic.AddVolumePropertyFromFile(r"C:\Users\Administrator\Desktop\0.vp")

     propertyNode=getNode("0")

     displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
     displayNode.SetVisibility(True)
</code></pre>

---

## Post #2 by @slicer365 (2023-09-05 16:48 UTC)

<pre><code class="lang-auto">         volRenLogic = slicer.modules.volumerendering.logic()
         volRenLogic.AddVolumePropertyFromFile(self.resourcePath('chestPre.vp'))
         volRenLogic.AddPreset(slicer.util.getNode("chestPre"))
        
         volumeNode=self.ui.imgSelector.currentNode()
         displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
        
         displayNode.GetVolumePropertyNode().Copy(slicer.util.getNode("chestPre"))
         displayNode.SetVisibility(True)
</code></pre>
<p>the codes need to add the vp file as a preset,  this is not what I want.</p>

---
