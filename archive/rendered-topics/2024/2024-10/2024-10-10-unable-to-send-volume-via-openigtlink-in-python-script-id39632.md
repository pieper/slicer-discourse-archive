---
topic_id: 39632
title: "Unable To Send Volume Via Openigtlink In Python Script"
date: 2024-10-10
url: https://discourse.slicer.org/t/39632
---

# Unable to Send Volume via OpenIGTLink in Python Script

**Topic ID**: 39632
**Date**: 2024-10-10
**URL**: https://discourse.slicer.org/t/unable-to-send-volume-via-openigtlink-in-python-script/39632

---

## Post #1 by @Vincenzo_Yuto_Civale (2024-10-10 10:39 UTC)

<p>I’m trying to send an outgoing volume with OpenIGTLink in a script Python.<br>
The volume node is successfully put in OutGoing of OpenIGTLinkIF Node, but the client doesn’t receive it.</p>
<pre><code class="lang-auto">success = connectionNode.RegisterOutgoingMRMLNode(volumeNode)
if success:
  connectionNode.PushNode(volumeNode)
</code></pre>
<p>From GUI when I set the PushOnConnect On, the volume is send.</p>
<p>Am I doing something wrong in script?</p>

---

## Post #2 by @lassoan (2024-10-10 22:02 UTC)

<p>An outgoing node is automatically sent to the connected clients/servers whenever the node is modified.</p>
<p>If the node is not modified then you need to push it:</p>
<ul>
<li>manually by pressing a button in the OpenIGTLink module GUI or calling the corresponding method in Python</li>
<li>automatically when a new client/server connects by enabling “push on connect” (by checking the checkbox in the OpenIGTLink module GUI or calling the corresponding method in Python)</li>
</ul>

---
