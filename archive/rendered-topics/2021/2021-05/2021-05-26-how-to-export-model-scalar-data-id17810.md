---
topic_id: 17810
title: "How To Export Model Scalar Data"
date: 2021-05-26
url: https://discourse.slicer.org/t/17810
---

# How to export Model Scalar data?

**Topic ID**: 17810
**Date**: 2021-05-26
**URL**: https://discourse.slicer.org/t/how-to-export-model-scalar-data/17810

---

## Post #1 by @mgpoirot (2021-05-26 14:37 UTC)

<p>I’m trying to work with FreeSurfer cortical scalar mappings.<br>
Luckily, Slicer is able to open these as ‘Freesurfer scalar overlay’<br>
They can be applied to a model inside FreeSurfer.</p>
<p>This is what it looks like</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf3983184b38bb83a3141a6563a60c8f2847462.jpeg" data-download-href="/uploads/short-url/ooj4gsoncCWfWJ5Sk0Bzqmm0HWa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf3983184b38bb83a3141a6563a60c8f2847462_2_541x499.jpeg" alt="image" data-base62-sha1="ooj4gsoncCWfWJ5Sk0Bzqmm0HWa" width="541" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf3983184b38bb83a3141a6563a60c8f2847462_2_541x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aaf3983184b38bb83a3141a6563a60c8f2847462_2_811x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaf3983184b38bb83a3141a6563a60c8f2847462.jpeg 2x" data-dominant-color="CDCDD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">960×887 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m trying to see if I can export this scalar mapping, for example to a .matl file so I can work on it.<br>
However, when I export the model to .obj only an empty .matl file comes along.</p>
<p>I also can’t find any place inside Slicer to interact with the scalar overlay. Where can this be found?</p>

---

## Post #2 by @lassoan (2021-05-26 15:51 UTC)

<p>You can access all point scalars as numpy arrays by calling <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPointData"><code>arrayFromModelPointData</code></a> and cell scalars by <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelCellData">‘arrayFromModelCellData’</a> and use full power of Python to process these arrays using VTK or any Python packages; in the Python console, in a script, Jupyter notebook, or in your custom Python scripted module.</p>
<p>If you must use Matlab then you can save the data set into VTK or VTP file formats, which preserve all point and cell data (maybe there are other file formats that can save some of the scalars).</p>
<p>What kind of processing do you plan to perform? There are several Slicer modules to find minimal path on these surfaces (optionally driven by point scalars), and cut, combine, and quantify surface patches.</p>

---

## Post #3 by @mgpoirot (2021-05-28 08:01 UTC)

<p>Hi Andras,<br>
Thanks a lot for the quick response! My aim is to “flatten” the scalar data to a regular image, so to generate a 2D projection (e.g. Mercator projection or something more fancy).</p>
<p>I’m working in python since all I found in literature was (built upon) Matlab toolboxes (like <a href="https://neuroimage.usc.edu/brainstorm/Tutorials/LabelFreeSurfer#Mollweide_projection" rel="noopener nofollow ugc">Brainstorm</a> or <a href="https://www.frontiersin.org/articles/10.3389/fninf.2018.00042/full" rel="noopener nofollow ugc">this MatConvNet based method</a>)</p>
<p>I’m very much in the learning phase with the python interactor for Slicer, but I’ll get back to you once I know if it has worked.</p>

---

## Post #4 by @lassoan (2021-05-28 21:08 UTC)

<aside class="quote no-group" data-username="mgpoirot" data-post="3" data-topic="17810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ce7236/48.png" class="avatar"> mgpoirot:</div>
<blockquote>
<p>My aim is to “flatten” the scalar data to a regular image, so to generate a 2D projection</p>
</blockquote>
</aside>
<p>This is called texture mapping and should be straightforward to do with VTK for such a simple shape.</p>
<p>You can generate texture coordinates using <a href="https://vtk.org/doc/nightly/html/classvtkTextureMapToSphere.html#details">vtkTextureMapToSphere</a> (but there is a filter for cylindrical and planar projections, too). Since your input geometry is spherical, you can simply write the generated texture coordinates (available as point scalars) into the point coordinates (using point_x=texture_u, point_y=texture_v, point_z=0). This flattens your sphere to a rectangle that you can visualize by rendering it as a model. You can use vtkProbeFilter as it is done in <a href="https://kitware.github.io/vtk-examples/site/Cxx/PolyData/InterpolateMeshOnGrid/">this example</a>. Since this is a purely VTK programming task, you may ask for help on the <a href="https://discourse.vtk.org">VTK forum</a>.</p>

---

## Post #5 by @mgpoirot (2021-05-31 14:46 UTC)

<p>Hi Andras,</p>
<p>Thanks for the support. I’m pretty experienced with python and medical image analysis, even with MRML. But Slicers python interaction with VTK is still quite a conundrum to me. All the functions you mention seem to lack any documentation? In <code>arrayFromModelPointData</code> for example, what even is an <code>arrayName</code> object? Even the source code doesn’t specify. I must be missing something.</p>
<p>I think it’s just my lack of understanding of VTK.</p>
<p>I have been able to close in on the scalar data (<code>scalars = getNode('vtkMRMLModelNode4').GetPolyData().GetPointData().GetScalars()</code>) but this FloatArray seems to be not subscriptable, nor can I find a function to retrieve the array content. This is something I’ll try to get at tomorrow. Would this array data be the input to <code>arrayFromModelPointData</code>?</p>
<p>Do you know if slicer has anything built in so that this scalar data is exported with the .mat file that comes with the mesh when exporting (for example to wavefront)? This functionality would probably have to perform texture mapping.</p>
<p>Thanks in advance!</p>

---

## Post #6 by @lassoan (2021-05-31 18:48 UTC)

<aside class="quote no-group" data-username="mgpoirot" data-post="5" data-topic="17810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ce7236/48.png" class="avatar"> mgpoirot:</div>
<blockquote>
<p>All the functions you mention seem to lack any documentation?</p>
</blockquote>
</aside>
<p>All the functions that I mentioned are documented <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html">here</a>. Please submit pull request on github with more details and suggestions that would make it more clear.</p>
<aside class="quote no-group" data-username="mgpoirot" data-post="5" data-topic="17810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ce7236/48.png" class="avatar"> mgpoirot:</div>
<blockquote>
<p>In <code>arrayFromModelPointData</code> for example, what even is an <code>arrayName</code> object? Even the source code doesn’t specify.</p>
</blockquote>
</aside>
<p>This is a small helper function for accessing additional attributes defined for points (<a href="https://vtk.org/doc/nightly/html/classvtkPointData.html">vtkPointData</a>) of the VTK mesh (vtkPolyData or vtkUnstructuredGrid). <code>arrayName</code> is the name of the VTK data array that you want to access. You can learn about VTK data objects from the excellent <a href="https://vtk.org/vtk-textbook/">VTK textbook</a> (I would highly recommend everyone who works in medical image computing to read it a few times).</p>
<aside class="quote no-group" data-username="mgpoirot" data-post="5" data-topic="17810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ce7236/48.png" class="avatar"> mgpoirot:</div>
<blockquote>
<p>I have been able to close in on the scalar data ( <code>scalars = getNode('vtkMRMLModelNode4').GetPolyData().GetPointData().GetScalars()</code> ) but this FloatArray seems to be not subscriptable, nor can I find a function to retrieve the array content.</p>
</blockquote>
</aside>
<p>This is a VTK data object. You can use read/write it from Python, but it is not as convenient interface as a numpy array.</p>
<aside class="quote no-group" data-username="mgpoirot" data-post="5" data-topic="17810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ce7236/48.png" class="avatar"> mgpoirot:</div>
<blockquote>
<p>Would this array data be the input to <code>arrayFromModelPointData</code> ?</p>
</blockquote>
</aside>
<p>This returns an attribute array of the point data that is chosen as the “active scalar”. This is probably the attribute that is currently used for visualization. It is safer to explicitly specify the array name that you want to retrieve than relying on which one is currently selected to be active.</p>
<aside class="quote no-group" data-username="mgpoirot" data-post="5" data-topic="17810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ce7236/48.png" class="avatar"> mgpoirot:</div>
<blockquote>
<p>Do you know if slicer has anything built in so that this scalar data is exported with the .mat file that comes with the mesh when exporting (for example to wavefront)? This functionality would probably have to perform texture mapping.</p>
</blockquote>
</aside>
<p>Yes, the point attributes (and cell attributes, field data, etc.) are all saved when you write the mesh to file. However, it depends on the file format what is saved and how. VTK/VTP/VTU files save everything. STL cannot save anything else than point coordinates. I think texture coordinates are saved into PLY and OBJ.</p>
<p>If you want to flatten the model then you don’t need to do anything like this, you can just take the texture coordinates (they are flat 2D coordinates) and write them to the point coordinates (setting the 3rd coordinate to 0.0). You may need to remove the cells which make the sphere wrap around (probably you can identify them by their large or distorted size using vtkMeshQuality filter and remove them using vtkThreshold filter).</p>

---

## Post #7 by @mgpoirot (2021-06-02 15:44 UTC)

<p>Hi Andras!</p>
<p>I’ve been able to solve it (I believe). Once I was able to access the coordinate and scalar values performing a mercator projection was easy. All points were interpolated creating a 2D texture. With this 2D texture we can do all sorts of cool things like using it as a CNN input, or using it in external rendering software<br>
Thanks a lot for the support Andras!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46ef42419bfa47b858c05c85dccf4f7c760aed37.png" data-download-href="/uploads/short-url/a7w21dEfgbQaDxqUgdYNlswuzCD.png?dl=1" title="myplot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46ef42419bfa47b858c05c85dccf4f7c760aed37_2_504x500.png" alt="myplot" data-base62-sha1="a7w21dEfgbQaDxqUgdYNlswuzCD" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46ef42419bfa47b858c05c85dccf4f7c760aed37_2_504x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46ef42419bfa47b858c05c85dccf4f7c760aed37.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46ef42419bfa47b858c05c85dccf4f7c760aed37.png 2x" data-dominant-color="9ABBB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">myplot</span><span class="informations">745×739 526 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In the figure above 10% of the data was used to show the effect of interpolation.</p>
<p>For anyone in the future wanting to project FreeSurfer scalar data to a 2D img, this is how I did it:</p>
<pre><code class="lang-auto">import numpy as np
from scipy.interpolate import griddata
from PIL import Image
resolution = 1024

# Get coordinate and scalar values
model_node = getNode('vtkMRMLModelNode4')
scalars = arrayFromModelPointData(model_node, 'thickness')
coordinates = arrayFromModelPoints(model_node)

# Convert cartesian to polar coordinates
coordinates = np.subtract(coordinates, np.mean(coordinates, axis=0))
r = np.sqrt(np.sum(np.square(coordinates), axis=1))
xc, yc, zp = [coordinates[:, ax] for ax in range(3)]
xp = np.arctan2(yc, xc)
yp = np.arcsin(zp / r)

# Define interpolation grid
xi = np.linspace(-np.pi, np.pi, resolution)
yi = np.linspace(-0.5 * np.pi, 0.5 * np.pi, resolution)
xi, yi = np.meshgrid(xi, yi)

# interpolate
zi = griddata((xp, yp), scalars, (xi, yi), method='linear')
zi = np.nan_to_num(zi)

# Save array as image
im = Image.fromarray(zi)
im.convert('RGB').save("filename.jpeg")
</code></pre>
<p>Tags: Freesurfer, Fastsurfer, cortical vertex data, cortical thickness Freesurfer scalar overlay, texture mapping, 2D projection, mercator projection, flattening</p>

---
