# TetGen: Stuck in final mesh improvement (vmtkmeshgenerator)

**Topic ID**: 30603
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/tetgen-stuck-in-final-mesh-improvement-vmtkmeshgenerator/30603

---

## Post #1 by @Anewre (2023-07-14 13:17 UTC)

<p>Dear all,</p>
<p>It seems this issue has been raised before, but since I was not successful in deriving a solution from previous Topics, I would like to bring it up once more.</p>
<p>I am trying to mesh a complex vascular geometry using vmtk. In particular, I use the following script:</p>
<pre><code class="lang-auto">vmtksurfacesmoothing -ifile /home/zbigniew/Pulpit/artery_fragment.stl -passband 0.1 -iterations 30 -ofile /home/zbigniew/Pulpit/artery_smoothed.vtp

vmtksurfacereader -ifile /home/zbigniew/Pulpit/artery_smoothed.vtp --pipe vmtkrenderer --pipe vmtksurfaceviewer -display 0 --pipe vmtksurfaceviewer -i @vmtksurfacereader.o -color 1 0 0 -display 1 

vmtksurfaceclipper -ifile /home/zbigniew/Pulpit/artery_smoothed.vtp -ofile /home/zbigniew/Pulpit/artery_clipped.vtp

vmtksurfacereader -ifile /home/zbigniew/Pulpit/artery_clipped.vtp --pipe vmtkcenterlines -seedselector openprofiles --pipe vmtkflowextensions -adaptivelength 1 -extensionratio 2 -normalestimationratio 1 -interactive 0 --pipe vmtksurfacewriter -ofile /home/zbigniew/Pulpit/artery_final.vtp

vmtkmeshgenerator -ifile /home/zbigniew/Pulpit/artery_final.vtp -ofile /home/zbigniew/Pulpit/artery_mesh.vtu -edgelength 0.5

vmtkmeshtetrahedralize -ifile /home/zbigniew/Pulpit/artery_mesh.vtu -ofile /home/zbigniew/Pulpit/artery_mesh_tetra.vtu

vmtkmeshboundaryinspector -ifile /home/zbigniew/Pulpit/artery_mesh_tetra.vtu -entityidsarray CellEntityIds 
</code></pre>
<p>The script seems to be running quite well, however, when reaching the vmtkmeshgenerator step, I get the following output:</p>
<pre><code class="lang-auto">Iteration 1/10
Iteration 2/10
Iteration 3/10
Iteration 4/10
Iteration 5/10
Iteration 6/10
Iteration 7/10
Iteration 8/10
Iteration 9/10
Iteration 10/10
Final mesh improvement
TetGen command line options: pq1.414000q10.000000q165.000000YsT1.000000e-08zQm
</code></pre>
<p>Upon reaching the line with “Tetgen command line options”, the script gets infinitely stuck.<br>
There seems to be an issue with TetGen, and a previous topic suggested the use of GMSH to work around it. However, I have no experience with GMSH which renders me unable to utilize this work-around.</p>
<p>I am curious if anyone on this forum is aware of a method to use this script successfully in their workflow.<br>
I am especially interested in using vmtk for meshing, since it allows for the creation and definition of a fluid domain and, in addition, a vascular wall with “outward” extrusion using surface normals. If anyone is aware of an open-source software that can accomplish something similar for a complex vascular geometry, this would also “solve” my issue.</p>
<p>With kind regards,</p>

---

## Post #2 by @lassoan (2023-07-14 13:51 UTC)

<p>I’ve experienced TetGen hanging/crashing, too. However, since TetGen comes with very restrictive AGPL/commercial license I did not investigate (does not make sense to spend time with fixing/improving some software that then I’m not allowed to freely use).</p>
<p>GMSH uses restrictive license, too (GPL). However, you can try <a href="https://github.com/wildmeshing/fTetWild">fTetWild</a>.</p>

---

## Post #3 by @Anewre (2023-07-14 14:17 UTC)

<p>Thank you for your swift and considerate reply. I will try out fTetWild, at first glance it might provide a solution for the problem I am trying to solve. In particular, I am hoping it provides a way to extrude internal boundary layers (for resolution of viscous layer effects) and a way to extrude external boundary layers (to create a vessel wall for FSI). I will keep you updated on my progress. Have a nice weekend.</p>

---
