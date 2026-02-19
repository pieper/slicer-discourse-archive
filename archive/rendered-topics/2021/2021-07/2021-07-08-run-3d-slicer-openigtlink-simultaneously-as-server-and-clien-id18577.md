---
topic_id: 18577
title: "Run 3D Slicer Openigtlink Simultaneously As Server And Clien"
date: 2021-07-08
url: https://discourse.slicer.org/t/18577
---

# Run 3D slicer openIGTLink simultaneously as server and client

**Topic ID**: 18577
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/run-3d-slicer-openigtlink-simultaneously-as-server-and-client/18577

---

## Post #1 by @Matteo_Boles (2021-07-08 13:55 UTC)

<p>Hello,<br>
I would like to run 3D slicer simultaneously as server and client because I need it as client to get the tracked position with polaris vicra of the tip of a probe and also I need it as a server to send out some parameters to Matlab where I am using pyigtl.</p>
<p>Is it possible to run at the same time as client and server?</p>

---

## Post #2 by @Sunderlandkyl (2021-07-08 15:40 UTC)

<p>Yes, you can add any number of connectors in OpenIGTLinkIF as both clients and servers.<br>
Just make sure that they are using different ports, and that you add your outgoing nodes to the server connector.</p>

---
