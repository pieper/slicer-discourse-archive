# IGT vtkMRMLIGTLConnectorNode best way to know how long to wait for connection and node access?

**Topic ID**: 5417
**Date**: 2019-01-18
**URL**: https://discourse.slicer.org/t/igt-vtkmrmligtlconnectornode-best-way-to-know-how-long-to-wait-for-connection-and-node-access/5417

---

## Post #1 by @NormandRobert (2019-01-18 23:31 UTC)

<p>Operating system: Ubuntu16.04.4<br>
Slicer version: 4.8.1</p>
<p>navigationHostName=‘fusion’<br>
navigationPortNumber=‘18944’<br>
connectorNodeNav = slicer.vtkMRMLIGTLConnectorNode()<br>
connectorNodeNav.SetTypeClient(navigationHostName,int(navigationPortNumber))<br>
slicer.mrmlScene.AddNode(connectorNodeNav)<br>
connectorNodeNav.Start()</p>
<p>print “NumberOfIncomingMRMLNodes=”, connectorNodeNav.GetNumberOfIncomingMRMLNodes()</p>
<p>How long to wait before  I get correct values?<br>
Line above yields 0 in interpreter if I paste code above in one go and 3 as expected if I wait a bit before pasting the last line.  This code in a module always yields zero.  Advice? Block on something?</p>

---

## Post #2 by @lassoan (2019-01-19 03:17 UTC)

<aside class="quote no-group" data-username="NormandRobert" data-post="1" data-topic="5417">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/normandrobert/48/4818_2.png" class="avatar"> NormandRobert:</div>
<blockquote>
<p>How long to wait before I get correct values?</p>
</blockquote>
</aside>
<p>Connections are managed in background threads. If you want to know when a client is connected then add an observer to the connector node.</p>

---
