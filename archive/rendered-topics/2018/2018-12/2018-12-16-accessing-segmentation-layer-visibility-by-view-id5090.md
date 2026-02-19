---
topic_id: 5090
title: "Accessing Segmentation Layer Visibility By View"
date: 2018-12-16
url: https://discourse.slicer.org/t/5090
---

# Accessing Segmentation Layer Visibility By View

**Topic ID**: 5090
**Date**: 2018-12-16
**URL**: https://discourse.slicer.org/t/accessing-segmentation-layer-visibility-by-view/5090

---

## Post #1 by @bsmarine (2018-12-16 03:31 UTC)

<p>Hi All,</p>
<p>I’m curious if there is a way to show particular segmentation nodes on each of four different views in a two over two layout programmatically. An example of doing this for background volumes would be as follows:</p>
<pre><code>volumes_of_interest = [pre_T1, pre_ADC, post_T1, post_ADC]

viewNodes = slicer.mrmlScene.getNodesByClass('vtkMRMLSliceCompositeNode')
for i,viewNode in enumerate(viewNodes):

        viewNode.SetBackgroundVolumeID(self.volumesLoad[i].GetID())
</code></pre>
<p>In our use case we make unique segmentations on two different MRI sequences before and after an intervention. Being able to view and touch-up all four segmentations would be helpful.</p>
<p>I understand that Segmentations play by different rules. I tried exploring SetDisplayVisibility, but it seems to only act globally on all views.</p>
<p>Any suggestions are much appreciated.</p>
<p>Best,</p>
<p>Brett</p>

---

## Post #2 by @lassoan (2018-12-16 13:56 UTC)

<p>You can add multiple segmentation display nodes to have one for each view. Then set view node ID and visibility in each display node.</p>

---

## Post #3 by @bsmarine (2018-12-16 14:52 UTC)

<p>What do you mean by specifically by a segmentation display node?</p>
<p>In the API vtkMRMLDisplayableNode doesn’t seem have a view node ID attribute and vtkMRMLSegmentationNode doesn’t seem to have a visibility attribute.</p>

---

## Post #4 by @lassoan (2018-12-16 15:11 UTC)

<aside class="quote no-group" data-username="bsmarine" data-post="3" data-topic="5090">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bsmarine/48/3898_2.png" class="avatar"> bsmarine:</div>
<blockquote>
<p>What do you mean by specifically by a segmentation display node</p>
</blockquote>
</aside>
<p><a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html" class="onebox" target="_blank" rel="noopener">http://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html</a></p>
<p>Create one using <code>slicer.mrmlScene.AddNewNodeByClass</code> and add it to the segmentation node using its <code>AddAndObserveDisplayNodeID</code> method.</p>
<aside class="quote no-group" data-username="bsmarine" data-post="3" data-topic="5090">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bsmarine/48/3898_2.png" class="avatar"> bsmarine:</div>
<blockquote>
<p>In the API vtkMRMLDisplayableNode doesn’t seem have a view node ID attribute and vtkMRMLSegmentationNode doesn’t seem to have a visibility attribute.</p>
</blockquote>
</aside>
<p>These are display node methods.</p>
<p>Example:</p>
<pre><code class="lang-auto"># Get segmentation node, for the rest, we assume that there are 3 segments, with default names/ids
segmentationNode=getNode('Segmentation')

# Get display node that is used by default for all views
segmentationDisplayNode1=segmentationNode.GetDisplayNode()

# Add one more display node
segmentationDisplayNode2=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationDisplayNode')
segmentationNode.AddAndObserveDisplayNodeID(segmentationDisplayNode2.GetID())

# Display node 1: show only in Red slice view, show only segment 3
segmentationDisplayNode1.SetViewNodeIDs(['vtkMRMLSliceNodeRed'])
segmentationDisplayNode1.SetSegmentVisibility('Segment_1',False)
segmentationDisplayNode1.SetSegmentVisibility('Segment_2',False)

# Display node 2: show only in Yellow nad Green slice views, show only segment 1
segmentationDisplayNode2.SetViewNodeIDs(['vtkMRMLSliceNodeYellow', 'vtkMRMLSliceNodeGreen'])
segmentationDisplayNode2.SetSegmentVisibility('Segment_2',False)
segmentationDisplayNode2.SetSegmentVisibility('Segment_3',False)
</code></pre>

---

## Post #5 by @bsmarine (2018-12-26 04:35 UTC)

<p>Hi Andras,</p>
<p>This is really helpful! Thanks so much for providing the examples.</p>
<p>I also found this DisplayNode method that similarly achieves only showing segmentations in select views.</p>
<pre><code>segmentationDisplayNode = segmentNode.GetDisplayNode()    
sliceNode = 'vtkMRMLSliceNodeRed'
segmentationDisplayNode.SetDisplayableOnlyInView(sliceNode.GetID())</code></pre>

---
