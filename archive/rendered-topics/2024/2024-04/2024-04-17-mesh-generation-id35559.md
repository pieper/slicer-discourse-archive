# Mesh generation

**Topic ID**: 35559
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/mesh-generation/35559

---

## Post #1 by @fil_ita (2024-04-17 14:08 UTC)

<p>Good morning,</p>
<p>First of all I would like to thank your team for the development of such an amazing tool.<br>
I am trying to mesh a geometry that, although is not from a vascular scan, I believe it is suitable for VMTK.<br>
However, based on the edge length I choose, sometimes I get the following error:</p>
<p>Error:  Invalid PLC! Two subfaces intersect.<br>
vtkvmtkTetGenWrapper.cx:433    ERR| vtkvmtkTetGenWrapper (0x55ff8e77b960): TetGen quit with an exception.</p>
<p>This gives me as an output just the surface mesh and the boundary layer.</p>
<p>Is it an error that comes from problems in my native geometry or after the generation of the boundary layer?</p>
<p>I get a similar error even if I use other opensource meshing software ( I don’t know if I can mention it in this discussion forum). I can generate the 3D mesh, but if I include the boundary layer algorithm it stops the meshing process due to “overlapping boundaries” and only outputs the surface mesh and the boundary layer like in this case.</p>
<p>Would anyone be able to help me?<br>
I have been stuck on meshing this geometry for the last 7 months…</p>
<p>Thank you so much in advance!</p>

---
