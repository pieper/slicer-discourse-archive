---
topic_id: 35574
title: "How To Log Click On A Button In Segment Editor"
date: 2024-04-17
url: https://discourse.slicer.org/t/35574
---

# How to log click on a button in segment editor?

**Topic ID**: 35574
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/how-to-log-click-on-a-button-in-segment-editor/35574

---

## Post #1 by @lskog (2024-04-17 23:51 UTC)

<p>Hello everyone, while trying to create personal module for slicer a problem occured. I need to log then the user click on “add” button in segment editor and changes tools. I want to create a timer, which will log how long it takes to make a segment. A lost hope to create the whole extension, but still want to make it work through built-in console. Any suggestions on how to log buttons?<br>
Thanks</p>

---

## Post #2 by @lassoan (2024-04-17 23:56 UTC)

<p>User Statistics module in Sandbox extension collects data about what modules are used, which Segment Editor effects are used and for how long, on what segments. It takes into account idle time (if the user leaves the computer or switches to another application then the clock stops). It is a Python scripted module, so you can extend it to record any additional details.</p>

---

## Post #3 by @lskog (2024-04-18 21:02 UTC)

<p>Thank you! We are currently trying to use this module in our work, or adapt its functions to our purposes. I hope it is possible for me not to mark the problem as solved right now, because I am sure, that I’ll face something again.</p>

---

## Post #4 by @lskog (2024-04-25 07:59 UTC)

<p>Thank you again for your reply. It was exciting experience. The feature was realized)</p>

---

## Post #5 by @lassoan (2024-04-30 02:39 UTC)

<p>Great to hear that you managed to implement what you needed. If you think this could be a useful feature in general then I would encourage tou to contribute it back to the community by sending a pull request to the Sandbox repository with your proposed changes.</p>

---
