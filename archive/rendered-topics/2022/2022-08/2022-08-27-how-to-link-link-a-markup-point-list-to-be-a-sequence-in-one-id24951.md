---
topic_id: 24951
title: "How To Link Link A Markup Point List To Be A Sequence In One"
date: 2022-08-27
url: https://discourse.slicer.org/t/24951
---

# How to link link a MarkUp point list to be a sequence in one SequenceBrowser using python script?

**Topic ID**: 24951
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/how-to-link-link-a-markup-point-list-to-be-a-sequence-in-one-sequencebrowser-using-python-script/24951

---

## Post #1 by @sunshine (2022-08-27 21:16 UTC)

<p>Hi everyone,</p>
<p>I am trying to write a module that can manually add landmarks using the MarkUp point list (vtkMRMLMarkupsFiducialNode) to different SequenceBrowsers.</p>
<p>I hope to link the point list node to one sequence of the target SequenceBrowser, and add an attribute of “pointListExist = True” to the SequenceBrowser.</p>
<p>What are the possible functions I should use to achieve it?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @lassoan (2022-08-27 22:15 UTC)

<p>You can create a new sequence node and add it to the sequence browser by calling <a href="https://apidocs.slicer.org/master/classvtkMRMLSequenceBrowserNode.html#aba16a856688831e670c26c9f4cd7fc34">AddProxyNode</a>.</p>

---

## Post #3 by @sunshine (2022-08-28 01:13 UTC)

<p>Hi Andras,</p>
<p>Thank you so much for your help! I made it using AddProxyNode.</p>
<pre><code class="lang-auto">node_Browser 	= slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSequenceBrowserNode')
node_Seq 		= slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", 'nodeSeq_pList_SeqBrowser_1')
node_Browser.AddProxyNode(getNode('pList_1'), node_Seq, False)
</code></pre>
<p>Could you please help me understand what is a ProxyNode? I would like to ask because I may not want it this way.<br>
For all the other Proxy Node before and after a sequence recording, the ProxyNode share the same for different SequenceBrowsers; however, if I use AddProxyNode to link node_PoinList to the SequenceBrowser, I need multiple node_PointList (from ‘pList_1’ to ‘pList_n’)  to be the ProxyNode for different SequenceBrowser, which is not ideal.</p>
<p>Could you please let me know what should I do?</p>

---

## Post #4 by @lassoan (2022-08-28 10:04 UTC)

<aside class="quote no-group" data-username="sunshine" data-post="3" data-topic="24951">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3ec8ea/48.png" class="avatar"> sunshine:</div>
<blockquote>
<p>Could you please help me understand what is a ProxyNode?</p>
</blockquote>
</aside>
<p>The proxy node brings one item from the sequence into the scene.</p>
<p>Typically, each proxy node is used by one sequence browser node. However, if you are careful (e.g., don’t simultaneously replay two sequences that use the same proxy nodes) then you can use the same proxy nodes in multiple browsers, by setting <code>copy</code> argument to<code>False</code>when calling <code>AddProxyNode</code>.</p>

---

## Post #5 by @sunshine (2022-08-28 15:31 UTC)

<p>So, in my case that each <code>pList_Seq_n</code> should be not only an independent PointList node that can be displayed in module MarkUp, but also should be the ProxyNode of <code>'SequenceBrowser_n'</code> added by</p>
<pre><code class="lang-auto">node_SeqBrowser_n.AddProxyNode(getNode('pList_n'), node_Seq_n, True)
</code></pre>
<p>am I correct?</p>
<p>If yes, does that mean the actual PointList_n is saved twice, one in the format of <code>'vtkMRMLMarkupsFiducialNode'</code>, and the other one in the format of <code>"vtkMRMLSequenceNode"</code> ?</p>

---

## Post #6 by @lassoan (2022-08-28 18:32 UTC)

<p>If you have one sequence node with many items then you can retrieve (and represent in the scene) one item by each browser node. So, there is some duplication, but by default a shallow-copy is performed from the sequence item into the proxy node, so bulk data (such as voxel array of an image) is not copied.</p>

---

## Post #7 by @sunshine (2022-08-28 19:49 UTC)

<p>Thank you so much, Andras!</p>
<p>I am not sure if using the MarkUp PointList (<code>vtkMRMLMarkupsFiducialNode</code>) would be the same case because it seems that there is not a node called MarkUp point (only PointList).</p>
<p>I need to call the MarkUp module to help SetActive a PointList node in order to add/drop a new control point, which means the copy has to be a shallow copy. Did I make sense?</p>
<p>In the meantime, to make sure I can find all PointList nodes in MarkUp module for different SequenceBrowser, I need to set <code>copy=True</code> when assigning a PointList to be the ProxyNode of a SequenceBrowser,</p>
<pre><code class="lang-auto">node_SeqBrowser_n.AddProxyNode(getNode('pList_n'), node_Seq_n, True)
</code></pre>
<p>would this achieve a sequence format, so that I can display the Point (if exists)  of at different frames in a SequenceBrowser?</p>

---

## Post #8 by @sunshine (2022-08-29 03:09 UTC)

<p>I might be confused about how to synchronize the MarkUp PointList (<code>vtkMRMLMarkupsFiducialNode</code>) to a SequenceBrowser.</p>
<p>Instead of making the <code>node_PointList</code> a <code>ProxyNode</code>, I should make the ControlPoint a <code>ProxyNode</code>,  because each frame corresponds to one <code>ControlPoint</code>, am I correct?</p>
<p>However, <code>ControlPoint</code> is not a node. What should I do to make the <code>PointList</code> a synchronized <code>SequenceNode</code> in a <code>SequenceBrowser</code>?</p>
<p>Or, maybe I can create a <code>PointList</code> for every single frame in the <code>SequenceBrowser</code>, so that the <code>PointList</code> is the <code>ProxyNode</code>. In this case, what are the possible functions I should use to add/save the nodes of <code>PointList</code> in the <code>SequenceBroswer</code>?<br>
In this case, I should not use <code>slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")</code>, because it will then be added to the <code>MarkUp</code> module and shown in the <code>Data</code> module. How to make it only available in SequenceBrowser as a Sequence?</p>

---

## Post #9 by @lassoan (2022-08-29 04:02 UTC)

<p>Changes in a proxy node are automatically saved into the sequence node if you <a href="https://apidocs.slicer.org/master/classvtkMRMLSequenceBrowserNode.html#ab2671ed3ee9eb413bb122f91b9c1029a">enable <code>SaveChanges</code> for the sequence</a>.</p>

---

## Post #12 by @sunshine (2022-08-30 03:51 UTC)

<p>So glad I made it !! <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"> To make it work, the newly added <code>SequenceNode</code> must be filled up by all empty <code>PointList</code>, otherwise the later annotated <code>DataNode</code> will always be affected by the previous added <code>DataNode</code> and the SequenceNode will not be able to Update during the PlayBack</p>
<p>Empty node_PointList: <code>slicer.vtkMRMLMarkupsFiducialNode()</code><br>
Fill Sequence: <code> nodeSeq_Annotation.SetDataNodeAtValue(node_EmptyPointList, str_IndexValue_Time)</code></p>
<pre><code class="lang-auto">nodeSeqBrowser.AddProxyNode(node_SeqBrowserProxy_Annotation, nodeSeq_Annotation, False)
nodeSeqBrowser.SetSaveChanges(nodeSeq_Annotation, True)


#  Fill up the SequenceNode with all empty 'PointList'
num_DataNodes = nodeSeqBrowser.GetNumberOfItems()
nodeSeq_Image = nodeSeqBrowser.GetSequenceNode(slicer.util.getNode('Existing_ProxyNodeName'))
for idx_DataNode in range(num_DataNodes):
    str_IndexValue_Time = nodeSeq_Image.GetNthIndexValue(idx_DataNode)
    nodeSeq_Annotation.SetDataNodeAtValue(slicer.vtkMRMLMarkupsFiducialNode(), str_IndexValue_Time)
</code></pre>

---
