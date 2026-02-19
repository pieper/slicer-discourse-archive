---
topic_id: 4895
title: "Slicerigt Error Received Unknown Device Type Position Device"
date: 2018-11-27
url: https://discourse.slicer.org/t/4895
---

# SlicerIGT error: Received unknown device type POSITION, device=StylusToReference

**Topic ID**: 4895
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/slicerigt-error-received-unknown-device-type-position-device-stylustoreference/4895

---

## Post #1 by @banderies (2018-11-27 20:42 UTC)

<p>I am receiving an error from VTK when I connect a Polaris Vicra with SlicerIGT: Received unknown device type POSITION, device=StylusToReference. This is on Slicer 4.10.0. I have no problem on Slicer 4.8.1. I noticed that OpenIGTLink is now separate from SlicerIGT on 4.10.0 so I am assuming this has something to do with it. The extension manager only seems to be working on 4.10.0, otherwise I would just use 4.8.1. On versions other than 4.10.0, the extension manager never finishes “Loading extensions.”</p>

---

## Post #2 by @lassoan (2018-11-28 05:40 UTC)

<p>Use TRANSFORM instead of POSITION in the Plus device set configuration file.</p>

---

## Post #3 by @banderies (2018-12-03 04:00 UTC)

<p>I am currently using the OpenIGTLink program from NDI which is not configurable. I will let them know about this.</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2018-12-03 04:10 UTC)

<p>You can use <a href="https://www.plustoolkit.org" rel="nofollow noopener">PLUS toolkit</a> instead.</p>

---
