---
topic_id: 4683
title: "Rendering Spherical Glyphs"
date: 2018-11-08
url: https://discourse.slicer.org/t/4683
---

# Rendering spherical glyphs

**Topic ID**: 4683
**Date**: 2018-11-08
**URL**: https://discourse.slicer.org/t/rendering-spherical-glyphs/4683

---

## Post #1 by @Randy_Heiland (2018-11-08 15:45 UTC)

<p>Operating system: OSX<br>
Slicer version: 4.10.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Can Slicer render spherical glyphs associated with VTK polydata (verts). For example, given the following data file (.vtk) of 4 vertices:</p>
<pre><code># vtk DataFile Version 2.0
Verts example
ASCII
DATASET POLYDATA
POINTS 4 float
0.0 0.0 0.0
1.0 0.0 0.0
0.0 1.0 0.0
0.0 0.0 1.0
VERTICES 4 8
1 0
1 1
1 2
1 3
POINT_DATA 4
SCALARS phenotype float 
LOOKUP_TABLE default
0.0
1.0
2.0
3.0
</code></pre>
<p>can Slicer render something similar to the attached image (rendered w/ ParaView)? If so, what are the steps? I’ve found the “Data” panel which sort of show the contents of the data, but where do I go to render glyphs associated with vertices?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11622eded2eadb6d4893a5b27ad3f82a6a9e6281.jpeg" data-download-href="/uploads/short-url/2tMtlkQZeyCMK6a5U6MKcnTY1jP.jpeg?dl=1" title="pv_4verts" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11622eded2eadb6d4893a5b27ad3f82a6a9e6281_2_679x500.jpeg" alt="pv_4verts" data-base62-sha1="2tMtlkQZeyCMK6a5U6MKcnTY1jP" width="679" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11622eded2eadb6d4893a5b27ad3f82a6a9e6281_2_679x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11622eded2eadb6d4893a5b27ad3f82a6a9e6281_2_1018x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11622eded2eadb6d4893a5b27ad3f82a6a9e6281.jpeg 2x" data-dominant-color="565665"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pv_4verts</span><span class="informations">1130×832 82.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-11-08 17:08 UTC)

<p>You can display colored polydata using models module. If your polydata has only points then you need to write a few lines of Python code to run the input through a VTK glyph filter.</p>
<p>What wouod you like to achieve?</p>

---

## Post #3 by @Randy_Heiland (2018-11-08 18:04 UTC)

<p>We typically render biological cells as spheres in our open source PhysiCell software. And we’re beginning a new project which will require visualizing/analyzing/interacting with tissue maps (images). So I was exploring Slicer, to see if it meets some of our needs.</p>
<p>I’d like to learn more about the Python option for rendering spheres. I see Slicer provides a built-in Python (2.7.x) interpreter and that I can import vtk there.</p>
<p>Later, I may want to install additional 3rd party Python libs, e.g., scipy, if that’s possible.</p>

---

## Post #4 by @lassoan (2018-11-08 19:42 UTC)

<p>Slicer should be able to visualize these models quite well. There are many visualization modes, both for 2D and 3D.</p>
<blockquote>
<p>I’d like to learn more about the Python option for rendering spheres.</p>
</blockquote>
<p>You can create a colored model using a short script as shown in this notebook: <strong><a href="https://github.com/lassoan/SlicerNotebookDemos/blob/master/ColoredSpheres.ipynb" class="inline-onebox">SlicerNotebookDemos/ColoredSpheres.ipynb at master · lassoan/SlicerNotebookDemos · GitHub</a></strong>  <a href="https://mybinder.org/v2/gh/lassoan/SlicerNotebookDemos/master?filepath=ColoredSpheres.ipynb"><img src="https://mybinder.org/badge.svg" alt="Binder" width="" height=""></a></p>
<pre><code class="lang-auto">inputPointFileName = os.getcwd()+"/data/ColoredPoints.vtk"

glyph = vtk.vtkGlyph3D()

pointSourceNode = slicer.modules.models.logic().AddModel(inputPointFileName)
glyph.SetInputConnection(pointSourceNode.GetMeshConnection())

glyphSource = vtk.vtkSphereSource()
glyphSource.SetRadius(0.1)
glyph.SetSourceConnection(glyphSource.GetOutputPort())

glyphedModelNode = slicer.modules.models.logic().AddModel(glyph.GetOutputPort())
glyphedModelNode.GetDisplayNode().SetActiveScalarName("phenotype")
glyphedModelNode.GetDisplayNode().SetScalarVisibility(True)

# Display in 3D view
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
slicer.util.resetThreeDViews()
display()
</code></pre>
<blockquote>
<p>Later, I may want to install additional 3rd party Python libs, e.g., scipy, if that’s possible.</p>
</blockquote>
<p>For now, you need to launch Python scripts that use scipy in an external process (as it is done in <a href="https://github.com/Radiomics/pyradiomics">SlicerRadiomics</a>), but hopefully in a couple of months Slicer will switch to Python3 and then you can use scipy directly in the Slicer process.</p>

---
