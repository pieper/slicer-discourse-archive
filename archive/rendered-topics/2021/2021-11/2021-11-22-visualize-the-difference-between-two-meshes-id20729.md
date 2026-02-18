# Visualize the difference between two meshes

**Topic ID**: 20729
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/visualize-the-difference-between-two-meshes/20729

---

## Post #1 by @suranga (2021-11-22 16:07 UTC)

<p>I have two volumetric liver meshes in .vtk format (i.e. ground-truth and predicted versions) and I want to plot the error i.e., for example, the difference between the ground-truth and the predicted liver meshes on the predicted mesh / mesh coordinates with a different colour (colour code based on displacement magnitudes) to visualize how much deviation that each point has ? Is it possible in 3D slicer ? If so can you elaborate the steps with an example please ?</p>

---

## Post #2 by @lassoan (2021-11-23 07:07 UTC)

<p>Does the N-th point in the first mesh correspond to the N-th point in the other mesh? If yes, then you can easily color the mesh by displacement. You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPoints">get the point positions in a numpy array</a>, subtract them from each other, and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPointData">add the resulting displacement as point scalars to the mesh</a>. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>
<p>Alternatively, you can get a dense b-spline displacement field from the scattered points using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ScatteredTransform">ScatteredTransform extension</a>, convert it to a displacement field image, and then use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/probevolumewithmodel.html">Probe Volume with Model module</a> to set the displacement values into model point data.</p>

---
