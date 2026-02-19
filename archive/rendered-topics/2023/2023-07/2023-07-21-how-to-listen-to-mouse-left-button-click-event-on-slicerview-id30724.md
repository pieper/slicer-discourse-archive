---
topic_id: 30724
title: "How To Listen To Mouse Left Button Click Event On Slicerview"
date: 2023-07-21
url: https://discourse.slicer.org/t/30724
---

# How to listen to mouse left button click event on slicerview

**Topic ID**: 30724
**Date**: 2023-07-21
**URL**: https://discourse.slicer.org/t/how-to-listen-to-mouse-left-button-click-event-on-slicerview/30724

---

## Post #1 by @jay1987 (2023-07-21 08:41 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c08fdfe1c16d51c3d4af7f4a351e7aad15c21436.jpeg" alt="image" data-base62-sha1="rttVifHohx7rSVOcgv2ZjS4ebEa" width="455" height="435"><br>
The requirement I received is to add mouse left click event listening only on the green window,then record the volume position information in a list,i don’t known how to add mouse left click event listening only on the green window</p>

---

## Post #2 by @lassoan (2023-07-21 14:00 UTC)

<p>You would normally not want to intercept user interaction events, as it would interfere would higher-level processing of the events. Instead, you can create a markup node and activate placement mode. See how it is done in the non-AI segmentation mode of lung CT segmentation module in <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/">LungCTAnalyzer extension</a>.</p>

---

## Post #3 by @jay1987 (2023-07-23 07:10 UTC)

<p>Wow,It’s really a really nice solution that I didn’t think of,Thank you lassoan!</p>

---
