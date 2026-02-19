---
topic_id: 442
title: "Change Color Of Segmentation Node"
date: 2017-06-06
url: https://discourse.slicer.org/t/442
---

# Change color of segmentation node

**Topic ID**: 442
**Date**: 2017-06-06
**URL**: https://discourse.slicer.org/t/change-color-of-segmentation-node/442

---

## Post #1 by @jks1995 (2017-06-06 14:40 UTC)

<p>How could I control the color of a ‘vtkMRMLSegmentationNode’?</p>

---

## Post #2 by @_jmichael (2017-06-06 14:55 UTC)

<p>Documentation for the segmentation module can be found here: <a href="https://www.slicer.org/wiki/Documentation/4.6/Modules/Segmentations" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.6/Modules/Segmentations</a></p>
<p>For colour, take a look at the figure on the right of the two figures under ‘Use Cases’. Double clicking the squares at the left of the table brings up an interface to change the segmentation’s colour.</p>

---

## Post #3 by @jks1995 (2017-06-06 14:57 UTC)

<p>Thanks for the reply! To be more specific, I wanted to control this through code.</p>

---

## Post #4 by @Fernando (2017-06-06 15:13 UTC)

<p>Some code I use to do that:</p>
<pre>
import vtkSegmentationCorePython  # http://na-mic.org/Mantis/view.php?id=4271
segmentation = segmentationNode.GetSegmentation()
stringArray = vtk.vtkStringArray()
segmentation.GetSegmentIDs(stringArray)
displayNode = segmentationNode.GetDisplayNode()
colorVector = vtk.vtkVector3d()
for i in range(stringArray.GetNumberOfValues()):
    segmentID = stringArray.GetValue(i)
    segment = segmentation.GetSegment(segmentID)
    name = segment.GetName()
    color = (100, 150, 200)
    color = np.array(color, float) / 255
    try:
        segment.SetColor(color)
    except AttributeError:  # older versions of Slicer
        colorVector.Set(*color)
        displayNode.SetSegmentColor(segmentID, colorVector)
</pre>
<p>(I don’t know why the code formatting is not working).  [I added the fix for the code formatting -Steve]</p>

---

## Post #5 by @Fernando (2017-06-06 15:18 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thanks for the edit <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #6 by @Fernando (2017-06-06 15:20 UTC)

<p><a class="mention" href="/u/jks1995">@jks1995</a> if my answer helped you, you can mark it with “This reply solves my problem” so that the next person that comes can quickly find the solution.</p>

---

## Post #7 by @lassoan (2017-06-06 15:58 UTC)

<p>Several convenience functions have been added recently to vtkMRMLSegmentation node, which should make it really simple to perform commonly needed operations.</p>
<p>For example, to add a new segment with a specific color, use <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a840a6b209ad581c3947db5f4311082d2"><code>vtkMRMLSegmentationNode::AddSegment...</code> methods</a>:</p>
<p><code>segmentID = segmentationNode.AddSegmentFromBinaryLabelmapRepresentation (imageData,"my segment name", [1,0,0.5])</code></p>
<p>If you later need to change any property then use the returned segmentID:<br>
<code>segmentationNode.GetSegment(segmentID).SetColor(0.3, 0.3, 0.5)</code></p>
<p>Let me know if there is any commonly needed operation that is cumbersome to do using the current segmentation API.</p>

---

## Post #8 by @jks1995 (2017-06-06 20:47 UTC)

<p>Thanks for the reply. I tried using this, but the AddSegmentFromBinaryLabelmapRepresentation method gave an error saying it needed an oriented label map instead of a label map. whats the best approach for taking a label map to an oriented label map?</p>

---

## Post #9 by @lassoan (2017-06-06 21:13 UTC)

<p>What is your input?</p>
<p>vtkImageData =&gt; Create a vtkOrientedImageData object and ShallowCopy the content of your vtkImageData object. vtkOrientedImageData allows you to specify arbitrary axis directions.</p>
<p>vktMRMLLabelMapNode =&gt; Use vtkSlicerSegmentationsModuleLogic’s <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a7800e526ccf33d4181fdb2e82a7f8623">CreateSegmentFromLabelmapVolumeNode</a> or  <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#adf111c9bcd3ceb28d49028f6fc6a2506">ImportLabelmapToSegmentationNode</a> methods.</p>
<pre><code>sl = slicer.modules.segmentations.logic()
sl.ImportLabelmapToSegmentationNode(labelmapNode, segmentationNode)</code></pre>

---

## Post #10 by @jks1995 (2017-06-07 14:33 UTC)

<p>I haven been able to create the segmentation using the segmentations logic, but unable to access any color aspects of the node at that point. So, I have done<br>
slicer.modules.segmentations.logic()<br>
sl.ImportLabelmapToSegmentationNode(labelmapNode, segmentationNode)</p>
<p>But if i try to run:<br>
segmentationNode.GetDisplayNode().SetSegmentColor(segmentID, [0.3, 0.3, 0.5])</p>
<p>I get an error there is no attribute SetSegmentColor.</p>

---

## Post #12 by @lassoan (2017-06-07 15:21 UTC)

<p>Sorry, I was looking at an older API. Color is actually stored in the segment:</p>
<pre><code>import vtkSegmentationCorePython as vtkSegmentationCore
segmentationNode = getNode('Segmentation')
segmentation = segmentationNode.GetSegmentation()
segment = segmentation.GetSegment(segmentation.GetNthSegmentID(0))
segment.SetColor(0,0,1)</code></pre>

---

## Post #13 by @jks1995 (2017-06-07 15:37 UTC)

<p>Thank you for the replies!</p>
<p>The segmentation node just gives me a vtkObject when I call GetSegment, though.</p>
<aside class="quote no-group">
<blockquote>
<p>seg_node = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’)<br>
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(out, seg_node)<br>
segmentation = seg_node.GetSegmentation()<br>
segment = segmentation.GetSegment(segmentation.GetNthSegmentID(0))<br>
segment.SetColor(0,0,1)</p>
</blockquote>
</aside>

---

## Post #14 by @lassoan (2017-06-07 15:39 UTC)

<p>Run <code>import vtkSegmentationCorePython as vtkSegmentationCore</code> to get access to segmentation objects (we’ll probably import this module by default in the future)</p>

---
