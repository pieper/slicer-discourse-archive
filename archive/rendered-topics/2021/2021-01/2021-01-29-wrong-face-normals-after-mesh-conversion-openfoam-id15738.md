---
topic_id: 15738
title: "Wrong Face Normals After Mesh Conversion Openfoam"
date: 2021-01-29
url: https://discourse.slicer.org/t/15738
---

# Wrong face normals after Mesh conversion (OpenFOAM)

**Topic ID**: 15738
**Date**: 2021-01-29
**URL**: https://discourse.slicer.org/t/wrong-face-normals-after-mesh-conversion-openfoam/15738

---

## Post #1 by @haontaler (2021-01-29 14:42 UTC)

<p>Hello everyone,</p>
<p>I am not sure if this is the correct forum to post questions about VMTK mesh generation and conversion as it is not available in Slicer directly afaik. But I hope that you can still give me a hint to solve my problem.</p>
<p>I generate a volume mesh using VMTK and want to use it for my OpenFOAM CFD simulations. So vmtkmeshgenerator → tetrahedralize → vmtkmeshwrite to fluent .msh → fluent3DMeshToFoam.<br>
This works well when I don’t generate a boundary layer with VMTK and checkMesh(OpenFOAM utility to check mesh quality) is happy with the result. As soon as I add a boundary layer, checkMesh complains about Boundary openness, open cells, incorrect orientation of faces and some more.<br>
I looked at the nonClosedCells in Paraview and found that after either the conversion from .vtu to .msh or from .msh to OpenFOAM, some surface normals get flipped (point inside).<br>
Has someone experienced something similar?</p>
<p>I also want to thank everyone who contributes to the VMTK and the community, the tool is quite awesome <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @pll_llq (2021-01-29 19:35 UTC)

<p>Out of prior experience OpenFOAM doesn’t care about the normal directions. Can you post the checkMesh log after you add boundary layers?</p>

---

## Post #3 by @haontaler (2021-01-30 15:33 UTC)

<p>Thank you for the answer!<br>
Maybe the normals are not even the problem. But it was a difference I observed in ParaView when I compared the .vtu and the OpenFOAM mesh. Anyways, I added the output of checkMesh. Without boundary layer all checks pass.</p>
<p>Mesh stats<br>
points:           262435<br>
faces:            2858629<br>
internal faces:   2723203<br>
cells:            1395458<br>
faces per cell:   4<br>
boundary patches: 18<br>
point zones:      0<br>
face zones:       1<br>
cell zones:       1</p>
<p>Overall number of cells of each type:<br>
hexahedra:     0<br>
prisms:        0<br>
wedges:        0<br>
pyramids:      0<br>
tet wedges:    0<br>
tetrahedra:    1395458<br>
polyhedra:     0</p>
<p>Checking topology…<br>
Boundary definition OK.<br>
Cell to face addressing OK.<br>
Point usage OK.<br>
Upper triangular ordering OK.<br>
Face vertices OK.<br>
Number of regions: 1 (OK).</p>
<p>Checking patch topology for multiply connected surfaces…<br>
Patch               Faces    Points   Surface topology<br>
surface3            134655   67421    ok (non-closed singly connected)<br>
surface4            44       29       ok (non-closed singly connected)<br>
surface5            53       35       ok (non-closed singly connected)<br>
surface6            45       30       ok (non-closed singly connected)<br>
surface7            45       30       ok (non-closed singly connected)<br>
surface8            45       30       ok (non-closed singly connected)<br>
surface9            45       30       ok (non-closed singly connected)<br>
surface10           42       28       ok (non-closed singly connected)<br>
surface11           47       31       ok (non-closed singly connected)<br>
surface12           47       31       ok (non-closed singly connected)<br>
surface13           41       27       ok (non-closed singly connected)<br>
surface14           44       29       ok (non-closed singly connected)<br>
surface15           47       31       ok (non-closed singly connected)<br>
surface16           44       29       ok (non-closed singly connected)<br>
surface17           44       29       ok (non-closed singly connected)<br>
surface18           47       31       ok (non-closed singly connected)<br>
surface19           45       30       ok (non-closed singly connected)<br>
surface20           46       31       ok (non-closed singly connected)</p>
<p>Checking faceZone topology for multiply connected surfaces…<br>
FaceZone            Faces    Points   Surface topology<br>
default-interior    2723203  262435   multiply connected (shared edge)<br>
&lt;&lt;Writing 262406 conflicting points to set nonManifoldPoints</p>
<p>Checking basic cellZone addressing…<br>
CellZone            Cells        Points       Volume       BoundingBox<br>
blood               1395458      262435       45977.86658932771 (119.41390991 91.79798126199999 54.573120117) (265.490448 360.74209595 372.64675903)</p>
<p>Checking geometry…<br>
Overall domain bounding box (119.41390991 91.79798126199999 54.573120117) (265.490448 360.74209595 372.64675903)<br>
Mesh has 3 geometric (non-empty/wedge) directions (1 1 1)<br>
Mesh has 3 solution (non-empty) directions (1 1 1)<br>
***Boundary openness (-7.382893700545746e-05 -0.0002968648354511357 5.438690675129859e-05) possible hole in boundary description.<br>
***Open cells found, max cell openness: 1, number of open cells 194<br>
&lt;&lt;Writing 194 non closed cells to set nonClosedCells<br>
&lt;&lt;Writing 15 cells with high aspect ratio to set highAspectRatioCells<br>
Minimum face area = 0.0005043367761588986. Maximum face area = 3.372726896690943.  Face area magnitudes OK.<br>
***Zero or negative cell volume detected.  Minimum negative volume: -3.641907377523641e-15, Number of negative volume cells: 8<br>
&lt;&lt;Writing 8 zero volume cells to set zeroVolumeCells<br>
Mesh non-orthogonality Max: 167.3542963814607 average: 25.91906820336919<br>
*Number of severely non-orthogonal (&gt; 70 degrees) faces: 610.<br>
***Number of non-orthogonality errors: 161.<br>
&lt;&lt;Writing 771 non-orthogonal faces to set nonOrthoFaces<br>
***Error in face pyramids: 207 faces are incorrectly oriented.<br>
&lt;&lt;Writing 205 faces with incorrect orientation to set wrongOrientedFaces<br>
***Max skewness = 521.9001544542002, 32 highly skew faces detected which may impair the quality of the results<br>
&lt;&lt;Writing 32 skew faces to set skewFaces<br>
Coupled point location match (average 0) OK.</p>
<p>Failed 6 mesh checks.</p>
<p>End</p>

---

## Post #4 by @haontaler (2021-01-30 17:58 UTC)

<p>I lowered the edgelengthfactor for vmtkmeshgenerator and this finer mesh (with boundary layer) passes all checkMesh tests.</p>

---
