---
topic_id: 7368
title: "Transform Single Segment In Python Module"
date: 2019-07-01
url: https://discourse.slicer.org/t/7368
---

# Transform single segment in python module

**Topic ID**: 7368
**Date**: 2019-07-01
**URL**: https://discourse.slicer.org/t/transform-single-segment-in-python-module/7368

---

## Post #1 by @Eloise (2019-07-01 11:36 UTC)

<p>Hi all,</p>
<p>I have a segmentation node (vtkMRMLSegmentationNode) that contains several segments (in this case, they represent organs) and I would like to apply a different linear transform (computed locally to the same reference fixed volume) to each of these segments and then combine the transformed segments in a new segmentation node.<br>
So to achieve this, I export each single segment into a segmentation node (with GetSegment and AddSegment functions) that I transform with SetAndObserveTransformNodeID, and then export the transformed segment and add it to a final transformed segmentation node (with all the other transformed segments).<br>
I don’t know if it is the right way to do this or if there is any easier solution, but it seems that the segments are not transformed, as if the transformation was not harden. Also, the segmentation nodes created do not seem accessible in the Slicer views, the eye icon is shaded.</p>
<p>Thanks for your help,</p>
<p>Eloïse</p>

---

## Post #2 by @lassoan (2019-07-01 13:16 UTC)

<p>You can only apply transformation to an entire segmentation, so moving out each each segment to a separate segmentation node is the right way.</p>
<p>If you apply a linear transform to a segmentation then hardening a transform does not need resampling. Hardening can be fully represented in change of segmentation origin, spacing, and axis directions.</p>
<p>If you want all your transformed segments in the same grid you can move back all the segments into the same segmentation node and then export to merged labelmap.</p>

---

## Post #3 by @Eloise (2019-07-01 14:56 UTC)

<p>Thanks for your answer!<br>
The problem is that the segments are not transformed when I use SetAndObserveTransformNodeID</p>
<pre><code>#create the output/merged transformed segmentation node that will contain all transformed segments
outputTransformedSegmentationNode = slicer.vtkMRMLSegmentationNode()
outputTransformedSegmentationNode.SetName('TransformedSegmentationMask')
slicer.mrmlScene.AddNode(outputTransformedSegmentationNode)
</code></pre>
<p>then for each given segment :</p>
<pre><code>#Get organ segment from its Id
organSegment = segmentationNode.GetSegmentation().GetSegment(segmentId)
        
 #Export segment to segmentation node 
organSegmentationNode = slicer.vtkMRMLSegmentationNode()
organSegmentationNode.SetName('OrganSegmentationTransformed' + segmentId)
organSegmentationNode.GetSegmentation().AddSegment(organSegment)
slicer.mrmlScene.AddNode(organSegmentationNode)

#apply local transform
organSegmentationNode.SetAndObserveTransformNodeID(localTransformLabelmapNode.GetID())

#Extract transformed segment 
transformedSegment = organSegmentationNode.GetSegmentation().GetSegment(segmentId)
        
#And add the transformedSegment to the outputTransformedSegmentationNode
outputTransformedSegmentationNode.GetSegmentation().AddSegment(transformedSegment)
</code></pre>
<p>At last :</p>
<pre><code>mergedTransformedLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()
slicer.mrmlScene.AddNode(mergedTransformedLabelmapNode)
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(outputTransformedSegmentationNode, visibleSegmentIds, mergedTransformedLabelmapNode, inputM1LocalVolume)
</code></pre>
<p>But the segments in the output label map are not transformed. Is there anything I am missing or not doing correctly?</p>

---

## Post #4 by @lassoan (2019-07-01 15:17 UTC)

<p>After your set the parent transform you also need to harden it.</p>

---

## Post #5 by @Eloise (2019-07-01 15:43 UTC)

<p>Thanks, works great!<br>
One last thing : I iterate through the segments of the input segmentation node and apply the strategy described above, and both the input segmentation node and the output segmentation node (both containing all segments) are transformed at last. how can I keep the input segmentation node the same (and prevent the transformation of the segments it contains) ?</p>

---

## Post #6 by @lassoan (2019-07-01 17:57 UTC)

<aside class="quote no-group" data-username="Eloise" data-post="5" data-topic="7368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eloise/48/3948_2.png" class="avatar"> Eloise:</div>
<blockquote>
<p>how can I keep the input segmentation node the same (and prevent the transformation of the segments it contains) ?</p>
</blockquote>
</aside>
<p>Keep the original segmentation node as is (untransformed), and move back all transformed segments back to this segmentation node.</p>

---

## Post #7 by @Eloise (2019-07-02 08:43 UTC)

<p>I made a deep copy of the segments before applying the transformation to their segmentation nodes, in order to put them back untransformed in the original merged segmentation node and it works.<br>
Thanks a lot for your answers.</p>

---

## Post #8 by @marianaslicer (2020-11-01 12:17 UTC)

<p>Good Morning,</p>
<p>I found this topic very helpful. I just have one question regarding segment selector widget of my python module. The code line to add the segment to the new segmentation node  (<code>organSegmentationNode.GetSegmentation().AddSegment(organSegment)</code>) makes the selector widget to return to the first segment of the segmentation. Thus, I need to click twice in the desired segment and unnecessary data is added to the mrml scene.</p>
<p>I don’t know if I’m doing something wrong so I would appreciate someone’s help.</p>
<pre><code># input segmentation node and segment selector
self.inputContourSelector = slicer.qMRMLSegmentSelectorWidget()
self.inputContourSelector.setMRMLScene(slicer.mrmlScene)
parametersFormLayout.addRow("Desired Contour: ", self.inputContourSelector)
self.inputContourSelector.connect('currentSegmentChanged(QString)', self.onContourChange)

def onContourChange(self, targetContour):
    segmentations = slicer.util.getNodesByClass('vtkMRMLSegmentationNode')
    segmentationNode = segmentations[0]
    organSegment = segmentationNode.GetSegmentation().GetSegment(targetContour)
       
    organSegmentationNode = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(organSegmentationNode)
    organSegmentationNode.SetName('OrganSegmentationTransformed' + targetContour)
    organSegmentationNode.GetSegmentation().AddSegment(organSegment)
</code></pre>
<p>Output when I select the <strong>segmentation</strong></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745feb3f714dac8fd36bfe533de105973e09c4c1.png" alt="image" data-base62-sha1="gBuTiDNYCBkrq7ohvTF0IIcto4h" width="630" height="91"></p>
<p>Output when I select the desired contour <strong>(CTV1) for the first time</strong>:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe582a88637f048cd08a5f4c6c69231d321ea91d.png" alt="image" data-base62-sha1="Ai2aHpYR1YXSMTEjGfIaM9pN2xL" width="623" height="185"></p>
<p>Output when I select the desired contour <strong>(CTV1) for the second time</strong>:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6c89833e762f9b2fc9abf0e12dbd80d362d700.png" alt="image" data-base62-sha1="ibfb4itrekLRGzCihdH9hdcjDS8" width="627" height="220"></p>
<p>Thanks,<br>
Mariana</p>

---

## Post #9 by @lassoan (2020-11-01 19:40 UTC)

<aside class="quote no-group" data-username="marianaslicer" data-post="8" data-topic="7368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marianaslicer/48/8555_2.png" class="avatar"> marianaslicer:</div>
<blockquote>
<p>The code line to add the segment to the new segmentation node ( <code>organSegmentationNode.GetSegmentation().AddSegment(organSegment)</code> ) makes the selector widget to return to the first segment of the segmentation.</p>
</blockquote>
</aside>
<p>This is a bug, I’ve entered a bug report - <a href="https://github.com/Slicer/Slicer/issues/5287" class="inline-onebox">qMRMLSegmentSelectorWidget loses current segment selection if segment is added · Issue #5287 · Slicer/Slicer · GitHub</a>. Until it is fixed, you can store the currently selected segment ID before you add a new segment and then restore the selection after the new segment is added.</p>

---

## Post #10 by @marianaslicer (2020-11-02 09:55 UTC)

<p>Thank you for your response and for report the bug! I will follow your advice.</p>

---

## Post #11 by @marianaslicer (2020-12-09 13:56 UTC)

<p>Hi Andras,</p>
<p>I noticed that the bug was fixed, but I am having exactly the same problem. I tried to used the <a href="https://apidocs.slicer.org/master/classqMRMLSegmentSelectorWidget.html#a9d0cd79a172dbc63e63944dd117a1f45" rel="noopener nofollow ugc">setCurrentNodeID</a> and <a href="https://apidocs.slicer.org/master/classqMRMLSegmentSelectorWidget.html#a7c2d453df5dc268bfe3512dd41924590" rel="noopener nofollow ugc">setCurrentSegmentID</a> of the SegmentSelectorWidget in order to maintain the segmentID after add the segment to the new segmentationNode but without success.</p>
<p>Any idea why this continues to happen? Thank you very much!</p>

---

## Post #12 by @lassoan (2020-12-09 15:08 UTC)

<p>You need to use the latest Slicer Preview Release. I’ve tested it and it works well for me, selection in the widget is preserved when new segment is added.</p>

---

## Post #13 by @marianaslicer (2020-12-10 11:36 UTC)

<p>Sorry I was using the 3.11.20200930 3D Slicer version. I tried to used the latest Slicer Preview Release and it worked for me too. Thank you a lot.</p>

---

## Post #14 by @lassoan (2020-12-12 06:30 UTC)

<p>A post was merged into an existing topic: <a href="/t/3d-slicer-for-virtual-reality-using-oculus-quest/8653/6">3D Slicer for virtual reality using Oculus Quest</a></p>

---
