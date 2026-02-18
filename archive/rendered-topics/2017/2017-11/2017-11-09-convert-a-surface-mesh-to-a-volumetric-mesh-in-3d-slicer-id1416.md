# Convert a surface mesh to a volumetric mesh in 3D Slicer

**Topic ID**: 1416
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/convert-a-surface-mesh-to-a-volumetric-mesh-in-3d-slicer/1416

---

## Post #1 by @Van_Sy (2017-11-09 11:56 UTC)

<p>Hello everyone,<br>
When I use 3D SLICER, I only have a surface mesh in here. But, I want to do this file in a Finite Element Sofware, I need a volumetric mesh.<br>
Can you tell me how to convert a surface mesh to a volumetric mesh in 3DSLICER?<br>
Thank you so much,<br>
Van Sy,</p>

---

## Post #2 by @lassoan (2017-11-09 12:22 UTC)

<p>You can use the recently added SegmentMesher extension (<a href="https://github.com/lassoan/SlicerSegmentMesher">https://github.com/lassoan/SlicerSegmentMesher</a>) to segments (surface meshes or labelmaps) to volumetric meshes that are suitable for FEM analysis. The extension’s packaging is not fully worked out yet, so you may need to install the mesher software (Cleaver2 and/or Tetgen) and set it in the extension manually. What operating system do you use?</p>

---

## Post #3 by @Van_Sy (2017-11-09 12:39 UTC)

<p>Dear Mr. Andras,<br>
I will use Ansys Software. Thank you for your information, I will try to use these tools, but I think that it is very useful if you make a video to teach everyone “how to use these tools to convert to a volumetric mesh from a surface mesh”. I think that this topic is very powerful.<br>
Best,</p>

---

## Post #5 by @Saima (2018-08-28 10:50 UTC)

<p>Hi Andras,<br>
When I save the results of segment mesher. I see .vtk file. when I open it it dont show me exact volumetric mesh which segment mesher generated.</p>
<p>Is there a specific way to save the files.</p>
<p>I think it is volumetric mesh.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3a04fe6c0e516b4eff6957416ed14089be58db7.png" data-download-href="/uploads/short-url/rUAzzULngIvAttQi7RjSEtrmCft.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3a04fe6c0e516b4eff6957416ed14089be58db7_2_690x388.png" alt="image" data-base62-sha1="rUAzzULngIvAttQi7RjSEtrmCft" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3a04fe6c0e516b4eff6957416ed14089be58db7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3a04fe6c0e516b4eff6957416ed14089be58db7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3a04fe6c0e516b4eff6957416ed14089be58db7_2_1380x776.png 2x" data-dominant-color="888898"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 442 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Saima (2018-08-28 09:24 UTC)

<p>Dear Andras,<br>
I used segment mesher. It is generating surface mesh instead of volumetric mesh. I used segment editor for segmenting tumor and brain. then I switched to segment mesher. It always generate surface mesh. I opened the *.vtk file of the generated model into paraview but dont see a volumetric mesh.</p>
<p>Please see the screen shot.</p>
<p>Does segmentmesher do not produce volumetric mesh? if yes what am I doing wrong? would you please correct me?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a129bf7e08bb837541e9382045e25d11ca194364.jpeg" data-download-href="/uploads/short-url/mZIjGiDGSDpL4MK9OZSfDEJiGdm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a129bf7e08bb837541e9382045e25d11ca194364_2_690x194.jpeg" alt="image" data-base62-sha1="mZIjGiDGSDpL4MK9OZSfDEJiGdm" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a129bf7e08bb837541e9382045e25d11ca194364_2_690x194.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a129bf7e08bb837541e9382045e25d11ca194364_2_1035x291.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a129bf7e08bb837541e9382045e25d11ca194364_2_1380x388.jpeg 2x" data-dominant-color="BEC0C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×1080 625 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2018-08-28 16:01 UTC)

<p>Segment mesher extension generates a volumetric mesh (unstructured grid containing tetrahedron and maybe also wedge cells). Why do you think the mesh is not a volumetric mesh?</p>

---

## Post #9 by @labixin (2019-01-07 05:06 UTC)

<aside class="quote no-group" data-username="Van_Sy" data-post="1" data-topic="1416">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/e95f7d/48.png" class="avatar"> Van_Sy:</div>
<blockquote>
<p>I want to do this file in a Finite Element Sofware</p>
</blockquote>
</aside>
<p>Hi Van Sy,<br>
I think I have met with the similar problem. I want to segment a structure (breast tumor) from MR image and then import the model to Ansys Software for finite element analysis. But I found the result of segmentation was surface mesh, which can’t be imported to ICEM for meshing (it needs to be geometry?). I wonder if you were meshing directly in Slicer (using Segment Mesher?) and then importing the volumetric mesh to Ansys just for subsequent analysis. Whatif I want to get a “geometry” from surface mesh in Slicer?<br>
Hope for some advice, thank you!<br>
Crayon</p>

---

## Post #10 by @lassoan (2019-01-07 14:49 UTC)

<p>ICEM can import surface meshes (STL files) - see for example <a href="https://www.cfd-online.com/Forums/ansys-meshing/77427-meshing-stl-surface-icem.html" rel="nofollow noopener">this</a> old forum topic. Segment Mesher can generate tetrahedral meshes that you can save in VTK unstructured grid (.vtu) file format. You may need a mesh conversion utility to convert it to a file format that can be read by your FEM software.</p>

---

## Post #11 by @brhoom (2019-01-07 15:05 UTC)

<p>This is a <a href="https://rgl.epfl.ch/publications/Gao2017Robust" rel="nofollow noopener">useful tool</a> with a source code.</p>

---

## Post #12 by @lassoan (2019-01-07 19:20 UTC)

<p>The issue is not that we wouldn’t have volumetric mesh generators in Slicer. We can generate volumetric meshes in Slicer using Cleaver2 or Tetgen via Segment Mesher extension. The issue is that the output file format (vtk unstructured grid) cannot be directly read by the commercial solvers or pre-processors.</p>
<p>The <em>robust_hex_dominant_meshing</em> mesh generator referenced above does not solve this issue, as it generates files in the same VTK file format (.vtu), medit (.mesh) file format, or a custom internal (.hybrid) file format. I think ICEM cannot read any of these.</p>
<p>Solution can be to use mesh converter tools, such as <a href="https://github.com/nschloe/meshio" rel="nofollow noopener">meshio</a>, which can read VTK volumetric mesh from .vtu file and can write it as an Ansys .msh file.</p>

---

## Post #13 by @labixin (2019-01-11 02:36 UTC)

<p>Thank you all for the discussion. ICEM can indeed import mesh from unstructured grid, but in fact failed to import from vtu or vtk format. Meshio can successfully convert .vtu file to .msh file which can read by the ICEM. Another way I tried was to convert the surface mesh created by Slicer segmentation module to solid geometry in Solidworks (IGES format). One more question please, I wonder if the output results of Slicer segmentation module just contain two types (surface mesh named model and labelmap)?</p>
<p>Best regards,<br>
Crayon</p>

---

## Post #14 by @cpinter (2019-01-11 15:39 UTC)

<p>Yes the most typical exported formats from segmentation are closed surface (model node) and binary labelmap. You can also export to planar contours and fractional labelmap with the current version.</p>
<p>Maybe we could add segmentation converter rules that use Cleaver2 / Tetgen and can generate volumetric mesh within the segmentation.</p>

---

## Post #15 by @Saima (2019-08-01 07:40 UTC)

<p>Dear Andras,<br>
I am trying to convert .vtk file into inp file using meshio.</p>
<p>the vtk file is not read by meshio. it gives error<br>
assert section == “FIELD”, “Unknown section ‘{}’.”.format(section)</p>
<p>AssertionError: Unknown section ’</p>
<p>how to resolve this error. please help.</p>

---

## Post #16 by @lassoan (2019-08-01 15:27 UTC)

<p>Meshio does not support binary .vtk files. You can save ascii .vtk file by checking “Show options” and unchecking “Compress” in Save data dialog.</p>
<p>This worked for me in the Python interactor of a recent Preview Release:</p>
<pre><code class="lang-python">pip_install('meshio')
import meshio
mesh = meshio.read(r"c:\tmp\Model.vtk")
meshio.write(r"c:\tmp\Model.inp", mesh)
</code></pre>

---

## Post #17 by @Saima (2019-08-02 00:56 UTC)

<p>Yes after unchecking compress in options it worked. thanks Andras</p>

---

## Post #19 by @Saima (2020-05-13 07:28 UTC)

<p>Hi andras,<br>
I am getting the following error when i import meshio. could you please help.</p>
<p>Thanks</p>
<p>Regards,<br>
Saima safdar</p>
<pre><code class="lang-auto">&gt;&gt;&gt; pip_install("meshio==3.3.1")
Collecting meshio==3.3.1
  Using cached meshio-3.3.1-py3-none-any.whl (106 kB)
Requirement already satisfied: numpy in ./lib/Python/lib/python3.6/site-packages (from meshio==3.3.1) (1.17.3)
Installing collected packages: meshio
  Attempting uninstall: meshio
    Found existing installation: meshio 3.0.0
    Uninstalling meshio-3.0.0:
      Successfully uninstalled meshio-3.0.0
  WARNING: The scripts meshio-convert and meshio-info are installed in '/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed meshio-3.3.1
&gt;&gt;&gt; import meshio
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/__init__.py", line 1, in &lt;module&gt;
    from . import (
  File "/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/_cli.py", line 9, in &lt;module&gt;
    from .__about__ import __copyright__, __version__
ImportError: cannot import name '__copyright__'
&gt;&gt;&gt;
</code></pre>

---

## Post #20 by @lassoan (2020-05-16 19:35 UTC)

<p>Uninstall/reinstall a different version while the application is runnning may not work. Restarting Slicer (or restarting Slicer after uninstalling the old meshio version) should work.</p>

---

## Post #21 by @Shajia_Ali (2020-09-10 15:53 UTC)

<p>OH BOY this saved me today! Thank you a lot, with cleaver it worked very good. What’s the difference between Cleaver and Tetgen? Maybe you can post a link on it. I tested both and only cleaver had an output.</p>

---

## Post #22 by @geo_p (2020-10-15 10:33 UTC)

<p>What are the analysis software used for simulating geometries generated using 3D Slicer segmentation.<br>
I was using the following pattern,<br>
3D Slicer(segmentation)&gt; FreeCAD(removing mesh errors)&gt;FEBio (static analysis)<br>
I could not mesh the imported geometry in Ansys (student version) and were not able to check the contact features of assemblies. FEBio has limited analysis options.</p>

---

## Post #23 by @lassoan (2020-10-15 21:37 UTC)

<p>You can create FE mesh directly from segmentation (without generating surface mesh and all associated meshing problems) using Segment Mesher module.</p>
<p>FEBio can read this mesh directly. FEBio does not have as many options as huge (and extremely expensive) commercial solvers, but it is free and should be suitable for many biomedical simulation problems.</p>
<p>If you want to use other solvers, you can convert Segment Mesher modules’s output from VTK unstructured grid to other formats that commercial solvers can use, using <a href="https://pypi.org/project/meshio/">meshio</a>.</p>

---

## Post #24 by @Saima (2020-12-08 04:14 UTC)

<p>Hi Andras,<br>
I am writing vtk file from within slicer using meshio. I am getting the following error. Is there any solution?</p>
<p>mesh = n.GetMesh()</p>
<blockquote>
<blockquote>
<blockquote>
<p>points = mesh.GetPoints()<br>
cells = mesh.GetCells()<br>
import meshio<br>
meshio.write_points_cells(“example.vtk”, points, cells)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/_helpers.py”, line 81, in write_points_cells<br>
cells = {key: numpy.asarray(value) for key, value in cells.items()}<br>
AttributeError: ‘vtkCommonDataModelPython.vtkCellArray’ object has no attribute ‘items’</p>
</blockquote>
</blockquote>
</blockquote>
<p>thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #25 by @lassoan (2020-12-08 04:28 UTC)

<p>I don’t recall seeing this error. Please report it to meshio developers. They are very responsive. Attach a sample data set that reproduces the issue.</p>

---

## Post #26 by @Saima (2020-12-09 04:48 UTC)

<p>Hi Andras,<br>
I have a vtkcellArray with two types of cells in it, triangle and tetra. How can I extract cell array within slicer like following.</p>
<p>In meshio if the mesh.cells is called it gives the following. I need to get the cells from within 3d slicer for a mesh and give it to meshio. Any idea? I got the points and converted to numpy array but for cells I dont know how to get the arrays.</p>
<p>{‘triangle’: array([[   0,    1,    2],<br>
[   0,   19,    1],<br>
[   4,    0,    2],<br>
…,<br>
[1989, 1984, 1991],<br>
[1996, 1991, 1984],<br>
[1987, 1993, 1994]], dtype=int32), ‘tetra’: array([[2600, 3531, 2730, 3868],<br>
[2254, 2779, 2382, 2911],<br>
[2242, 3405, 2782, 3546],<br>
…,<br>
[3710, 1693, 1478, 1477],<br>
[ 544, 4188,  584, 3182],<br>
[ 544,  584, 4188, 1388]], dtype=int32)}</p>

---

## Post #27 by @lassoan (2020-12-09 14:05 UTC)

<p>You can save the mesh as .vtk and you should be able to load it using meshio. If there is any error then report it to meshio developers (attach the file that cannot be imported or converted).</p>
<p>If you want, then of course you can recreate the data meshio data structure from a VTK object in memory (vtkCellArray class is Python-wrapped, so you can access all methods from Python), but it is expected to be about a magnitude slower than the C++ implementation (that writes to file).</p>

---

## Post #28 by @lassoan (2021-03-05 16:50 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-visualize-volumetric-mesh/16392">How to visualize volumetric mesh?</a></p>

---
