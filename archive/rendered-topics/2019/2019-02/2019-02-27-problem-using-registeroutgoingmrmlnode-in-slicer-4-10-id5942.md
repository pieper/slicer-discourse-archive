---
topic_id: 5942
title: "Problem Using Registeroutgoingmrmlnode In Slicer 4 10"
date: 2019-02-27
url: https://discourse.slicer.org/t/5942
---

# Problem using RegisterOutgoingMRMLNode in Slicer 4.10

**Topic ID**: 5942
**Date**: 2019-02-27
**URL**: https://discourse.slicer.org/t/problem-using-registeroutgoingmrmlnode-in-slicer-4-10/5942

---

## Post #1 by @mcfly3001 (2019-02-27 08:14 UTC)

<p>Hi Community,</p>
<p>I would again need some help with an issue I have with Slicer 4.10. I want to register an outgoing node for to an OpenIGTLink Connection (Server). The node is of type “vtkMRMLTextNode”. As soon as I call RegisterOutgoingMRMLNode the application freezes and then crashes.<br>
The same code works properly with Slicer 4.8. I found out that if I instead use a “vtkMRMLLinearTransformNode” the code runs fine with Slicer 4.10 as well. But thats not what we need.<br>
Any ideas what could be wrong or why we cannot use the TextNode anymore? Here a small code snipped which leads to the crash:</p>
<pre><code>connector_node = slicer.vtkMRMLIGTLConnectorNode()
connector_node.SetTypeServer(18946)
connector_node.SetName("DeviceNodeName")
slicer.mrmlScene.AddNode(connector_node)

tnode = slicer.vtkMRMLTextNode()
tnode.SetName("MessageTextNode")
slicer.mrmlScene.AddNode(tnode)
connector_node.RegisterOutgoingMRMLNode(tnode)
</code></pre>
<p>I also tried starting the connector node before registering but this did not help.</p>
<p>Thanks for any hints on how to correctly use this.</p>

---

## Post #2 by @pieper (2019-02-27 12:37 UTC)

<p>Are you able to use a debugger to get a stack trace?  This sounds like memory corruption of some kind.</p>

---

## Post #3 by @mcfly3001 (2019-02-27 13:04 UTC)

<p>Unfortunately not. I can debug into the Python code but can’t debug into the Slicer sources. I just downloaded the Slicer Release version without any source code or PDB files on I could attach a debugger.<br>
I also don’t get any exceptions on Python. Slicer crashes silently with the message “The Program has stopped working”.<br>
Is there an easy way to get a stack trace up and running? I once tried to compile Slicer on my own but had no luck because of the many dependencies.</p>

---

## Post #4 by @pieper (2019-02-27 13:36 UTC)

<p>I’m hoping one of the OpenIGTLink developers can replicate the crash in a developer build.  Let’s see if someone chimes in.</p>

---

## Post #5 by @lassoan (2019-02-27 14:04 UTC)

<p>I could reproduce the crash by adding a new node by calling <code>slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTextNode")</code> then adding it as an outgoing node. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you please check?</p>

---

## Post #6 by @Sunderlandkyl (2019-02-27 15:24 UTC)

<p>I found the problem (uninitialized char* is treated as a string). In the process of investigating, I’ve also found that outgoing nodes are not being registered/observed correctly.</p>
<p>I have a fix for the first issue, and I hope to have the second issue fixed shortly.</p>

---

## Post #7 by @mcfly3001 (2019-02-27 15:35 UTC)

<p>Wow, that was a quick one! The support in this community is really great by the way!</p>
<p>Will there be a new release soon with the fix? I was hoping that Slicer 4.10.2 will be release some day. I am also hoping for a fix for this issue:<br>
<a href="https://issues.slicer.org/view.php?id=4634" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4634</a></p>
<p>Thanks again for the great support.</p>

---

## Post #8 by @Sunderlandkyl (2019-02-27 15:39 UTC)

<p>The SlicerOpenIGTLink fix should be available in the next nightly (edit: and stable) build tomorrow (~8am EST).<br>
You can check for the update in the extension manager.</p>

---

## Post #9 by @mcfly3001 (2019-02-27 15:41 UTC)

<p>Does this mean I need to install the nightly build version?<br>
Or can I use the stable release and find it in the extension manager as well? Probably I will need to switch to the nightly, right?</p>
<p>Thanks.</p>

---

## Post #10 by @Sunderlandkyl (2019-02-27 15:44 UTC)

<p>It should be available in both the stable and nightly versions.</p>

---
