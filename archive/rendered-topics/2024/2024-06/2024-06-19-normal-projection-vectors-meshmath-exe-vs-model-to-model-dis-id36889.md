# Normal projection vectors: meshmath.exe vs. Model-to-Model Distance

**Topic ID**: 36889
**Date**: 2024-06-19
**URL**: https://discourse.slicer.org/t/normal-projection-vectors-meshmath-exe-vs-model-to-model-distance/36889

---

## Post #1 by @kmadi (2024-06-19 00:59 UTC)

<p>Hello Slicer(SALT) devs,</p>
<p>I am revising a python script to run the Model-to-Model Distance module in CLI so I can automate the process for a large batch of VTKs. Specifically, I’m looking to extract the normal projections of the distance vectors (between correspondent points) and use them for statistical testing.</p>
<p>I know that there is the “MagNormVector” field in the output VTK after running the module, and I also know that the hidden “MeshMath.exe” application (included in SlicerSALT’s /bin/ folder but has mostly been integrated into Model-to-Model Distance) includes a “magNormDir” argument to get the magnitude of the normal projections.</p>
<p>I’m aware that “MagNormVector” is 3D data and “magNormDir” is 1D, but are these functionally the same in terms of the vectors being calculated? I just want to make sure the vector math is equivalent before I commit to scripting one method over the other (especially since MeshMath is much easier to work with in CLI).</p>
<p>Thanks in advance!<br>
-KVM</p>

---
