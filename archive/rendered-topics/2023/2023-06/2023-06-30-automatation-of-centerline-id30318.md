---
topic_id: 30318
title: "Automatation Of Centerline"
date: 2023-06-30
url: https://discourse.slicer.org/t/30318
---

# Automatation of Centerline

**Topic ID**: 30318
**Date**: 2023-06-30
**URL**: https://discourse.slicer.org/t/automatation-of-centerline/30318

---

## Post #1 by @Charlie_Hayward (2023-06-30 11:18 UTC)

<p>Hi all, I am looking to automate the vmtkcenterlines function in order to be able to run it on a server. It seems that my option is to have open profiles and use seed selector. This causes an issue because I need the entire processing to be automated, to open the profiles I would need to utilize something like vmtksurfaceclipper which requires a GUI. Is there any way to either automatically generate centerlines without open profiles or automatically clip ends to create open profiles?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2023-07-21 14:10 UTC)

<p>You can have a look how it got fully automated in 3D Slicer’s Extract Centerline module. See source code <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L327">here</a>.</p>

---

## Post #3 by @lassoan (2023-10-26 02:55 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/aneurysm-removal-and-reconstruct-the-parent-vessel/32304/6">aneurysm removal and reconstruct the parent vessel</a></p>

---
