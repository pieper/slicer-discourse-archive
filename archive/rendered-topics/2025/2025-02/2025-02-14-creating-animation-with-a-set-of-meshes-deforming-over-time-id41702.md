---
topic_id: 41702
title: "Creating Animation With A Set Of Meshes Deforming Over Time"
date: 2025-02-14
url: https://discourse.slicer.org/t/41702
---

# Creating animation with a set of meshes deforming over time overlapped to ct-scan

**Topic ID**: 41702
**Date**: 2025-02-14
**URL**: https://discourse.slicer.org/t/creating-animation-with-a-set-of-meshes-deforming-over-time-overlapped-to-ct-scan/41702

---

## Post #1 by @msensale1 (2025-02-14 16:04 UTC)

<p>Hi All,</p>
<p>I have a set of meshes (vtk) that represent the same geometry deforming over time. Each time refers to a different time step. I could upload this set of meshes in Paraview and generate an animation with the moving object. I’d like to do the same in Slicer while keeping in the background the corresponding CT-scan. Is it possible to do that in Slicer? Could anyone provide guidance?</p>
<p>Many thanks,<br>
Marco</p>

---

## Post #2 by @pieper (2025-02-14 17:57 UTC)

<p>You should be able to do ths with sequences: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html" class="inline-onebox">Sequences — 3D Slicer documentation</a></p>

---

## Post #3 by @msensale1 (2025-02-17 10:33 UTC)

<p>Thank you very much for your contribution.</p>
<p>I tried to work with Sequences, but I haven’t found any method to switch from one vtk (time step) to the following seemlessly and while recording. Perhaps scripting is required?</p>
<p>Thanks,<br>
Marco</p>

---

## Post #4 by @pieper (2025-02-17 13:50 UTC)

<p>Scripting usually helps if you are trying to do something sophisticated and want to be reproducible.  But if your goal is to load a set of vtk poly data objects and iterate through displaying them you should be able to just load them all as models, put them in a sequence and animate them.</p>
<p>That said, I don’t use the Sequences module much and maybe someone who does can give you step by step instructions (or explain any gaps in the documentation so it can be improved).</p>

---

## Post #5 by @msensale1 (2025-02-17 16:49 UTC)

<p>Yes my goal is exactly to load a set of vtk polydata and iterate through displaying them. I loaded them as models and put in a sequence, but didn’t find how to animate them.</p>

---
