---
topic_id: 19758
title: "Getting Stream Of Probe Position From Another Application In"
date: 2021-09-20
url: https://discourse.slicer.org/t/19758
---

# Getting stream of probe position from another application into Slicer/SlicerIGT

**Topic ID**: 19758
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/getting-stream-of-probe-position-from-another-application-into-slicer-slicerigt/19758

---

## Post #1 by @srivastavava (2021-09-20 12:47 UTC)

<p>Hi there,</p>
<p>I am trying to integrate Slicer/SlicerIGT to work with a preexisitng application which publishes the coordinates of a probe relative to a model in a specific coordinate system. I want the probe position to be displayed wrt to a 3D model created in SlicerIGT. I guess I’ll have to align the 3D models in Slicer to the coordinate system in the other application and would have to then communicate the coordinates using some sort of TCP/UDP socket interface. What would be the best way to do it using Slicer/SlicerIGT ?</p>

---

## Post #2 by @lassoan (2021-09-21 16:55 UTC)

<p>SlicerIGT supports the OpenIGTLink protocol for real-time sending/receiving of transforms, images, models, point sets, arrays, strings, etc. OpenIGTLink is a very simple socket-based protocol that you can easily implement in your application from scratch, or use any of the <a href="http://openigtlink.org/developers/">existing implementations in various programming languages</a>.</p>

---
