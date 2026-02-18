# Using segmentstatistics module in python script

**Topic ID**: 2140
**Date**: 2018-02-21
**URL**: https://discourse.slicer.org/t/using-segmentstatistics-module-in-python-script/2140

---

## Post #1 by @brhoom (2018-02-21 14:29 UTC)

<p>Dear all,<br>
How can I call and use segmentstatistics module in a simple way. I tried this code but I get an error</p>
<pre><code>    volSeg  =  slicer.util.getNode('Segmentation')
    volInput =  self.inputSelector.currentNode() 

    segStat = slicer.modules.segmentstatistics.widgetRepresentation().self()
    segStat.grayscaleNode = volInput
    segStat.labelNode  = volSeg   
    segStat.onApply()
    segStat.onExportToTable()
    segTbl = slicer.util.getNode('Segmentation statistics*')
</code></pre>
<p>This is the error:</p>
<pre><code>Slicer-4.8.0/lib/Slicer-4.8/qt-scripted-modules/SegmentStatistics.py", line 176, in onApply
self.logic.getParameterNode().SetParameter("Segmentation", self.segmentationSelector.currentNode().GetID()) AttributeError: 'NoneType' object has no attribute 'GetID'</code></pre>

---

## Post #2 by @lassoan (2018-02-21 17:34 UTC)

<p>When you need to use a Slicer module from another module, you must almost always use the module’s logic directly, instead of manipulating the other module’s user interface.</p>
<p>In general, you can find example of how to use the module logic in <a href="https://github.com/Slicer/Slicer/blob/69358596167cbc99d39acfa98a5cfa2a1e4042dd/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L639-L857">module tests</a>.</p>
<p>For example, you can use Segment statistics module like this:</p>
<pre><code>segmentationNode  =  slicer.util.getNode('Segmentation')
masterVolumeNode =  slicer.util.getNode('MRHead')
resultsTableNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableNode')

import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.getParameterNode().SetParameter("ScalarVolume", masterVolumeNode.GetID())
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled","False")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.voxel_count.enabled","False")
segStatLogic.computeStatistics()
segStatLogic.exportToTable(resultsTableNode)
segStatLogic.showTable(resultsTableNode)</code></pre>

---

## Post #3 by @brhoom (2018-02-22 20:59 UTC)

<p>Thanks a lot, that was helpful. I didn’t know about the testing modules.  The code above works for me with these modifications:</p>
<pre><code>    resultsTableNode = slicer.vtkMRMLTableNode()
    slicer.mrmlScene.AddNode(resultsTableNode)
    segStatLogic.exportToTable(resultsTableNode)
    segStatLogic.showTable(resultsTableNode)</code></pre>

---

## Post #4 by @lassoan (2018-02-22 21:17 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="2140">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>resultsTableNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLTableNode’)</p>
</blockquote>
</aside>
<p>Creates a node and adds to the scene, similarly to your version:</p>
<pre><code>resultsTableNode = slicer.vtkMRMLTableNode()
slicer.mrmlScene.AddNode(resultsTableNode)
</code></pre>
<p>However, AddNewNodeByClass has the advantage that it is shorter and it creates nodes taking into account <a href="http://apidocs.slicer.org/master/classvtkMRMLScene.html#ae302c5ed4aabb2910bc35dcc9aa2513f">default node properties</a> that are defined in the scene (you can override default properties for any nodes, such as default colors, file save formats, etc).</p>

---

## Post #5 by @Saima (2018-10-26 12:26 UTC)

<p>Hi Andras,<br>
Could you please tell me how to do it for segment mesher. what parameters need to be set for segment mesher to run it using script.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #6 by @Saima (2018-10-30 05:18 UTC)

<p>Hi Andras,<br>
I am writing a scriopt for segment mesher . how to use it using scripting. I have tried below. Please guide. I do not know the complete list of parameters to set for segment mesher.</p>
<p>Creating importing segmentation node<br>
[success, patientMask] = slicer.util.loadLabelVolume(‘D:/Boston Data/Patient Mask Label.nrrd’, returnNode = True)<br>
segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(patientMask,segmentationNode)</p>
<p>segMesh = slicer.modules.segmentmesher<br>
//creating output model node<br>
model = slicer.vtkMRMLModelNode()<br>
slicer.mrmlScene.AddNode(model)</p>
<p>//setting parameters<br>
parameters= {}<br>
parameters[‘input Segmentation’] = segmentationNode.GetID()<br>
parameters[‘output model’] = model.GetID()</p>
<p>//Runing CLi<br>
slicer.cli.runSync(segMesh,None,parameters)</p>
<p>Please help.</p>
<p>Regards,<br>
Saima Safdar</p>

---
