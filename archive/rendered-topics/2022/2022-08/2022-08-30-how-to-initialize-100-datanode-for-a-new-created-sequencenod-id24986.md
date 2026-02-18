# How to initialize 100 DataNode for a new created SequenceNode without adding into the scene?

**Topic ID**: 24986
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/how-to-initialize-100-datanode-for-a-new-created-sequencenode-without-adding-into-the-scene/24986

---

## Post #1 by @sunshine (2022-08-30 00:03 UTC)

<p>Hi everyone,</p>
<p>I am trying to write my first extension module related to sequence annotation but am stuck at the <code>SequenceNode</code> initialization step.</p>
<p>I have a <code>SequenceBrowser</code> with one <code>SequenceNode</code> containning 100 <code>vtkMRMLScalarVolumeNode</code>.<br>
I would like to add a new <code>SequenceNode</code> using 100 MarkUp <code>PointList</code>, i.e., <code>vtkMRMLMarkupsFiducialNode</code>.</p>
<p>How can I fill up the newly created <code>SequenceNode</code> with 100 empty <code>PointList</code> without adding any  <code>PointList</code> to the scene file?<br>
How can I instance an empty <code>PointList</code> without adding to the scene, and what are the possible functions I can use to fill up the newly created <code>SequenceNode</code>?</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @sunshine (2022-08-30 03:47 UTC)

<p>So glad I made it by myself !! <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"><br>
Empty node_PointList: <code>slicer.vtkMRMLMarkupsFiducialNode()</code><br>
Fill Sequence: <code> nodeSeq_Annotation.SetDataNodeAtValue(node_EmptyPointList, str_IndexValue_Time)</code></p>
<pre><code class="lang-auto">#  Fill up the SequenceNode with all empty 'PointList'
num_DataNodes = nodeSeqBrowser.GetNumberOfItems()
nodeSeq_Image = nodeSeqBrowser.GetSequenceNode(slicer.util.getNode('Existing_ProxyNodeName'))
for idx_DataNode in range(num_DataNodes):
    str_IndexValue_Time = nodeSeq_Image.GetNthIndexValue(idx_DataNode)
    nodeSeq_Annotation.SetDataNodeAtValue(slicer.vtkMRMLMarkupsFiducialNode(), str_IndexValue_Time)
</code></pre>

---
