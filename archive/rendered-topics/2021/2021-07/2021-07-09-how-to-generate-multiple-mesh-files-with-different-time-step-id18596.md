---
topic_id: 18596
title: "How To Generate Multiple Mesh Files With Different Time Step"
date: 2021-07-09
url: https://discourse.slicer.org/t/18596
---

# how to generate multiple mesh files with different time steps

**Topic ID**: 18596
**Date**: 2021-07-09
**URL**: https://discourse.slicer.org/t/how-to-generate-multiple-mesh-files-with-different-time-steps/18596

---

## Post #1 by @junqiangchen (2021-07-09 02:16 UTC)

<p>Hi,<br>
than you for sharing the PARTICLE TRACING example with vmtk,i have problem that how to generate different timestep meshs,can anyone share some example code or tools how to use it generate different timestep meshes?<br>
best wishes!!<br>
chenjunqiang</p>

---

## Post #2 by @lassoan (2021-07-11 15:23 UTC)

<p>See requirements listed <a href="http://www.vmtk.org/tutorials/ParticleTracing.html">here</a>:</p>
<blockquote>
<p>In order to properly compute traces it is mandatory to have <em>n</em> mesh files resulting from a pulsatile cfd simulation. Each mesh file represent a timestep and must have, as a vtkDataArray, 3 velocity components in the axial directions ( usually <em>u, v</em> and <em>w</em> ), or the velocity vector.</p>
</blockquote>

---

## Post #3 by @junqiangchen (2021-07-12 01:12 UTC)

<p>thanks lassoan,can you share some example how to achieve it?</p>

---

## Post #4 by @lassoan (2021-07-12 01:32 UTC)

<p>You probably need to ask for help on the community forum of the CFD solver that you use.</p>

---
