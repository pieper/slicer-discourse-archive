---
topic_id: 16163
title: "Send Customized Data Over Openigtlink"
date: 2021-02-23
url: https://discourse.slicer.org/t/16163
---

# Send customized data over OpenIGTLink

**Topic ID**: 16163
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/send-customized-data-over-openigtlink/16163

---

## Post #1 by @priya.vada4 (2021-02-23 17:01 UTC)

<p>Hi</p>
<p>Is it possible to send a customized polydata over OpenIGTLink. In an earlier version, I was able to send the data by setting the igtl::PolyDataMessage::Pointer and then sending the data by directly calling vtkMRMLIGTLConnectorNode::SendData to send the polydata message.</p>
<p>It looks like in the new version of OpenIGTLink, SendData method has been removed.  Do I need to set the polydata to a vtkMRMLModelNode and then push the node over OpenIGTLink? Can you let me know how if there is an easier way of sending the customized polydata message.</p>
<p>Thanks<br>
Priya</p>

---

## Post #2 by @lassoan (2021-02-23 19:30 UTC)

<aside class="quote no-group" data-username="priya.vada4" data-post="1" data-topic="16163">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/d26b3c/48.png" class="avatar"> priya.vada4:</div>
<blockquote>
<p>It looks like in the new version of OpenIGTLink, SendData method has been removed.</p>
</blockquote>
</aside>
<p>You can send the model by setting it as an output node and calling <code>Modified()</code> on it.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is there a way for one-time sending of a node (without setting it as an output node) in latest SlicerOpenIGTLink?</p>

---

## Post #3 by @Sunderlandkyl (2021-02-23 20:55 UTC)

<p>No, the only method that I can see currently is to call:</p>
<pre><code class="lang-auto">connectorNode.RegisterOutgoingMRMLNode(node)
connectorNode.PushNode(node)
connectorNode.UnregisterOutgoingMRMLNode(node)
</code></pre>
<p>I’ll take a look to see if I can add some additional methods to simplify one-off messages:</p>
<ul>
<li>Send OpenIGTLink message directly</li>
<li>Send message from node without having to register/unregister the node</li>
</ul>

---

## Post #4 by @priya.vada4 (2021-02-23 23:54 UTC)

<p>I may be missing something here since it doesn’t look like it works. As a toy example, I tried to extract the polydata from a model and then send it over OpenIGTLink by creating a vtkMRMLModelNode and pushing the node. The code snippet is included below:</p>
<pre><code>//Creating some dummy polydata
vtkPolyData* polyData = modelNode-&gt;GetPolyData();


// send the data
vtkSmartPointer&lt;vtkMRMLModelNode&gt; modelClientNode = vtkSmartPointer&lt;vtkMRMLModelNode&gt;::New();
modelClientNode-&gt;SetAndObservePolyData(polyData);
modelClientNode-&gt;Modified();
connectorNode-&gt;RegisterOutgoingMRMLNode(modelClientNode);
connectorNode-&gt;PushNode(modelClientNode);
connectorNode-&gt;UnregisterOutgoingMRMLNode(modelClientNode);
</code></pre>
<p>I don’t receive the polydata on the server side. Please let me know your suggestions.</p>
<p>Thanks<br>
Priya</p>

---

## Post #5 by @Sunderlandkyl (2021-02-24 00:35 UTC)

<p>The model node needs to be added to the scene so that a node reference can be added to the connector node.</p>

---

## Post #6 by @priya.vada4 (2021-02-24 04:21 UTC)

<p>Thanks for your suggestion. I still seem to be getting the following error:</p>
<p><code>Unable to create vtkPolyData from incoming POLYDATA message. Failed to unpack the message</code></p>

---

## Post #7 by @Sunderlandkyl (2021-02-24 15:31 UTC)

<p>Interesting, I just tested with the latest stable and I was able to send a polydata between them.</p>
<p>What version of Slicer are you using?<br>
Could you send me a “.vtk” for the polydata that gave the error.</p>

---

## Post #8 by @priya.vada4 (2021-02-24 16:48 UTC)

<p>I am using Slicer 4.13.0-2021-01-13. It occurs with every vtk model that I try to send. Not sure where the problem is.</p>
<p>In fact, even if I try to send the model from the OpenIGTLink module in Slicer (not programmatically), I run into the same problem with the following error:</p>
<p><code>Unable to create vtkPolyData from incoming POLYDATA message. Failed to unpack the message</code></p>

---
