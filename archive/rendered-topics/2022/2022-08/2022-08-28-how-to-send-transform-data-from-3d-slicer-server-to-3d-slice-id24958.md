---
topic_id: 24958
title: "How To Send Transform Data From 3D Slicer Server To 3D Slice"
date: 2022-08-28
url: https://discourse.slicer.org/t/24958
---

# How to send transform data from 3D Slicer(Server) to 3D slicer(client) use openIGTLink like Tracking Simulator?

**Topic ID**: 24958
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/how-to-send-transform-data-from-3d-slicer-server-to-3d-slicer-client-use-openigtlink-like-tracking-simulator/24958

---

## Post #1 by @xiaosnowqiang (2022-08-28 03:01 UTC)

<p>Hello guys,I want use 3D Slicer with the Transforms module as server send data to another 3D Slicer (client), the connect network is OK ,but i don’t know how to send my Transforms module data to another slicer  Volume Reslicer Driver module.<br>
Can someone help me ,<br>
Thanks for any reply<br>
-Jian</p>

---

## Post #2 by @lassoan (2022-08-28 11:01 UTC)

<p>If you add the transform as an output transform then the transform will be sent to all connected clients/servers automatically. If you enable “push on connect” then the initial value is automatically sent when a new connection is eatablished.</p>

---
