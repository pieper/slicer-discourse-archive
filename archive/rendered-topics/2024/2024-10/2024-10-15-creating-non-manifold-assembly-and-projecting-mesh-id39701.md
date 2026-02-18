# Creating non-manifold assembly and projecting mesh

**Topic ID**: 39701
**Date**: 2024-10-15
**URL**: https://discourse.slicer.org/t/creating-non-manifold-assembly-and-projecting-mesh/39701

---

## Post #1 by @farhanm (2024-10-15 00:39 UTC)

<p>Hi everyone,<br>
I am a PhD student at the Weiss Biomechanics Lab, University of Utah. I am working on creating volumetric meshes from microCT scan images. Currently, I use MIMICS (v 24.0) for segmentation and 3-Matic (v 16.0) for aligning five parts, improving the mesh, and most importantly, creating non-manifold assemblies from these parts. I also use the “Project Mesh” tool in 3-Matic to create compatible meshes at the interface surfaces of two adjacent parts. Finally, I generate volumetric meshes for the parts and export them in .inp format. I was wondering if there is a way to perform these tasks using 3D Slicer. I looked at some of the plugins in 3D Slicer, but as far as I understood, none of them is very helpful in my case.</p>
<p>I hope I have expressed my question clearly, and I appreciate any suggestions you may have.</p>
<p>Best,<br>
Farhan Muhib</p>

---

## Post #2 by @lassoan (2024-10-15 00:45 UTC)

<p>Have you tried <a href="https://github.com/lassoan/SlicerSegmentMesher">SegmentMesher extension</a>? It can create multi-material volumetric meshes for biomechanical analysis with shared points at the material interfaces, using Cleaver2 mesher (also from Utah).</p>
<p>Slicer can save volumetric meshes as VTK unstructured grid, with material ID specified in cell scalars. I think FEBio can read these mesh files directly, but if for some reason you need Abaqus .inp files then you can create them from VTK mesh files using a converter, such as the meshio Python package.</p>

---
