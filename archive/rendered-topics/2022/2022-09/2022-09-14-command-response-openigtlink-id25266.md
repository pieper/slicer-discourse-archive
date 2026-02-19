---
topic_id: 25266
title: "Command Response Openigtlink"
date: 2022-09-14
url: https://discourse.slicer.org/t/25266
---

# Command response openigtlink

**Topic ID**: 25266
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/command-response-openigtlink/25266

---

## Post #1 by @Srijeet_Chatterjee (2022-09-14 14:40 UTC)

<p>Hello everyone,</p>
<p>My question is, how can I print a received a command message in the igtlinkremote or python interactor?</p>
<p>I am sending a command from slicer using:</p>
<pre><code>    cn=slicer.mrmlScene.GetNodeByID("vtkMRMLIGTLConnectorNode1")
mc=slicer.vtkSlicerOpenIGTLinkCommand()
mc.SetCommandName("SomeCommand")
mc.SetCommandContent("{}")
slicer.modules.openigtlinkremote.logic().SendCommand(mc,cn.GetID())
</code></pre>
<p>The server after execution of the command sends reply back to the client using the OpenIGTLink. But I don’t see anything in the Openigtlink Remote responses. I have also tried adding an observer like:</p>
<pre><code>   mc.AddObserver(cn.CommandResponseReceivedEvent,print) 
</code></pre>
<p>However, it just prints 1 and nothing on sending the command. Could anyone please help me regarding how to print the replies?</p>
<p>Thanks,<br>
Best Regards,<br>
Srijeet</p>

---
