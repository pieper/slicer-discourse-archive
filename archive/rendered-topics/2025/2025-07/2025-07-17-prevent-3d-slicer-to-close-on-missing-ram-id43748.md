# Prevent 3D Slicer to close on missing RAM

**Topic ID**: 43748
**Date**: 2025-07-17
**URL**: https://discourse.slicer.org/t/prevent-3d-slicer-to-close-on-missing-ram/43748

---

## Post #1 by @calvinsuzuki (2025-07-17 00:30 UTC)

<p>Typically, computers with 8 GB of RAM are enough to run my module, but sometimes I need 12 GB.</p>
<p>Is there any way to prevent Slicer from silently and instantly crashing when it reaches the PC’s RAM limit?</p>
<p>The crashes occurr often when user apply Grow From Seeds, or Image Fusion.<br>
Loading is also a (rare) problem.,if user try to add a big volume or many volumes, RAM goes up too.</p>

---

## Post #2 by @muratmaga (2025-07-17 04:46 UTC)

<p>You can increase the amount of virtual memory in your computer. It will work slow, but Slicer will not crash due to OOM.</p>

---
