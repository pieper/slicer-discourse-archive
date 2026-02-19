---
topic_id: 21021
title: "Islands Segmentation Via Python Script"
date: 2021-12-11
url: https://discourse.slicer.org/t/21021
---

# Islands segmentation via python script

**Topic ID**: 21021
**Date**: 2021-12-11
**URL**: https://discourse.slicer.org/t/islands-segmentation-via-python-script/21021

---

## Post #1 by @Valentina_Nepi (2021-12-11 18:28 UTC)

<p>Hi everyone.<br>
I am trying to create and island segmentation directly via python script bypassing the 3dslicer gui.<br>
In the GUI i do these operations:</p>
<ul>
<li>load two diffents files, a label map and a master volume</li>
<li>import the label map on the the master volume</li>
<li>create a new segmenation and edit chosing remover islands to delete islands smaller that a voxel value size</li>
</ul>
<p>Everyone know if is it possible?</p>
<p>Thanks in advantage</p>

---

## Post #2 by @rbumm (2021-12-13 15:27 UTC)

<p>Hi Valentina,</p>
<p>All this should be doable with a python script.<br>
I would involve the Segment Editor like this (untested):</p>
<pre><code class="lang-auto"># Initialization 
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(yourOutputSegmentation)
segmentEditorWidget.setMasterVolumeNode(yourVolume)

# Systematically remove small islands
segmentEditorNode.SetSelectedSegmentID("YourSegmentID")
segmentEditorWidget.setActiveEffectByName("Islands")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumSize","1000")
effect.setParameter("Operation","KEEP_LARGEST_ISLAND")
segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone) 
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere)  
effect.self().onApply()

# Deactivates all effects
segmentEditorWidget.setActiveEffect(None)
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)
</code></pre>

---

## Post #3 by @Valentina_Nepi (2021-12-13 16:06 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="2" data-topic="21021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>All this should be doable with a python script.<br>
I would involve the Segment Editor like this (untested):</p>
<pre><code class="lang-auto"># Initialization 
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(yourOutputSegmentation)
segmentEditorWidget.setMasterVolumeNode(yourVolume)

# Systematically remove small islands
segmentEditorNode.SetSelectedSegmentID("YourSegmentID")
segmentEditorWidget.setActiveEffectByName("Islands")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumSize","1000")
effect.setParameter("Operation","KEEP_LARGEST_ISLAND")
segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone) 
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere)  
effect.self().onApply()

# Deactivates all effects
segmentEditorWidget.setActiveEffect(None)
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)
</code></pre>
</blockquote>
</aside>
<p>thank you Rudolf! is similar to the one I’ve done! I will test your!<br>
Since you are so kind, I ask you some suggestion! for the next step I would extract features for this new segmentation generated putting it as input region and then do a quantification of the segment statistics. do you have some good idea?<br>
thank you in advantage</p>

---

## Post #4 by @rbumm (2021-12-13 16:24 UTC)

<aside class="quote no-group" data-username="Valentina_Nepi" data-post="3" data-topic="21021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/valentina_nepi/48/13474_2.png" class="avatar"> Valentina_Nepi:</div>
<blockquote>
<p>do you have some good idea</p>
</blockquote>
</aside>
<p>Actually, yes. You need to call the SegmentStatisticsLogic() in your script which is quite easy (untested):</p>
<pre><code class="lang-auto">resultsTable = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableNode', 'Your analysis results')

# Compute stats
import SegmentStatistics

segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", yourOutputSegmentation.GetID())
segStatLogic.getParameterNode().SetParameter("ScalarVolume", yourInputVolume.GetID())
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled", "True" if self.generateStatistics else "False")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.voxel_count.enabled", "False")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.volume_mm3.enabled", "False")
segStatLogic.computeStatistics()
segStatLogic.exportToTable(self.resultsTable)
self.outputStats = segStatLogic.getStatistics()
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled", "True")
</code></pre>

---

## Post #5 by @Valentina_Nepi (2021-12-13 16:43 UTC)

<p>I’ll try soon! about bin width? could you tell me how to select it before the extraction?</p>

---

## Post #6 by @rbumm (2021-12-13 17:19 UTC)

<p>It is not good to populate this thread with add-on questions because other users will not find the new follow-up topic. I suggest you try your way and maybe ask a new question in support.</p>

---

## Post #7 by @Valentina_Nepi (2021-12-13 18:39 UTC)

<p>Ok Rudolf that you so much! your help has been preciuos!</p>

---
