# Problem with crossing tubes

**Topic ID**: 20323
**Date**: 2021-10-24
**URL**: https://discourse.slicer.org/t/problem-with-crossing-tubes/20323

---

## Post #1 by @apparrilla (2021-10-24 19:46 UTC)

<p>Hi everyone!</p>
<p>I want to make a tube model with MarkupsToModel Module but I have 2 segments pretty close each other:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58ccf7645e555d60f9bd6f25861969587eb7cd44.png" data-download-href="/uploads/short-url/cFz9F1pQDU9FY9IFWqAomlOxk44.png?dl=1" title="3d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58ccf7645e555d60f9bd6f25861969587eb7cd44_2_284x250.png" alt="3d" data-base62-sha1="cFz9F1pQDU9FY9IFWqAomlOxk44" width="284" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58ccf7645e555d60f9bd6f25861969587eb7cd44_2_284x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58ccf7645e555d60f9bd6f25861969587eb7cd44_2_426x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58ccf7645e555d60f9bd6f25861969587eb7cd44_2_568x500.png 2x" data-dominant-color="A2A5AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d</span><span class="informations">921×809 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I look to Red Slice, it shows something strange:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c0b8816bb87c2a1fa74a4301f24aa36de2dcdc.png" data-download-href="/uploads/short-url/4Xr8rIJium48y8Xhn49gcU213fm.png?dl=1" title="Red Slice" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22c0b8816bb87c2a1fa74a4301f24aa36de2dcdc_2_304x250.png" alt="Red Slice" data-base62-sha1="4Xr8rIJium48y8Xhn49gcU213fm" width="304" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22c0b8816bb87c2a1fa74a4301f24aa36de2dcdc_2_304x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22c0b8816bb87c2a1fa74a4301f24aa36de2dcdc_2_456x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22c0b8816bb87c2a1fa74a4301f24aa36de2dcdc_2_608x500.png 2x" data-dominant-color="040400"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Red Slice</span><span class="informations">695×570 6.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I´ve clipped the tube model with Green Slice Plane and this is the result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d69836b556ec817bfac05d26aecc62275dfcfc46.jpeg" data-download-href="/uploads/short-url/uCoii6RyERfj5sV0JJ3AJe6hHtY.jpeg?dl=1" title="Clip.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d69836b556ec817bfac05d26aecc62275dfcfc46_2_231x250.jpeg" alt="Clip.PNG" data-base62-sha1="uCoii6RyERfj5sV0JJ3AJe6hHtY" width="231" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d69836b556ec817bfac05d26aecc62275dfcfc46_2_231x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d69836b556ec817bfac05d26aecc62275dfcfc46_2_346x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d69836b556ec817bfac05d26aecc62275dfcfc46_2_462x500.jpeg 2x" data-dominant-color="999995"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Clip.PNG</span><span class="informations">1074×1161 72.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any way to fix it to get just a solid model? I´ve tried Surface Toolbox but I can´t get a solid model.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-10-24 23:25 UTC)

<p>This is a solid model. Every surface mesh will look empty inside if you cut them.</p>
<p>The model is self-intersecting, which may cause problems. There is no universal solution for this, but if you describe you high-level goals (what you would like to model with these curves, for what clinical application) then we can suggest specific solutions.</p>

---

## Post #3 by @apparrilla (2021-10-25 05:45 UTC)

<p>Of course, I put some fiducials over a bone model and make a tube model to be cutted with the bone. Sometimes direction changes are very closed and I have this kind of problem. As you can imagine, the cut operation is failed.<br>
I send the model to segmentation and make a “fill holes” and export it again as model, but it is a time consuming workflow…</p>

---

## Post #4 by @lassoan (2021-10-25 11:36 UTC)

<p>What is the clinical application? Would you like to simulate superficial grinding of the bone? Or you would like to cut out a surface patch of the bone? Or you would like to create a 3D és surgical guide?</p>

---

## Post #5 by @apparrilla (2021-10-25 15:40 UTC)

<p>It is for surgical guides. I want to cut the tube with the bone surface.</p>

---

## Post #6 by @lassoan (2021-10-25 15:46 UTC)

<p>Probably the simplest is to use the Segment Editor for this. You can draw tubes directly on the 3D view using Paint effect by enabling “Edit in 3D view” option.</p>
<p>There are of course many other options, depending on exactly what kind of surgical guides you want to create. See for example the sophisticated <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/">module for automatic surgical guide generation for mandible reconstruction</a> by <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> that uses a combination of markups and Segment Editor and Combine models module.</p>
<p>If you can draw a sketch of how you would like your surgical guide to look like then we can give more specific advice.</p>

---

## Post #7 by @apparrilla (2021-10-25 21:05 UTC)

<p>Segment Editor, in my hands, used to have a low resolutions outputs for most input CT´s or a need to 2x-3x oversampling with logaritmic increase of memory and computations loads. What I look for is to manage this issue with models because resolution outputs are, again in my hands, better.<br>
I think it should be intersting for many other porposes to add any kind of tool to Surfafe ToolBox to fix the intersecting faces problem in models, even for imported ones…<br>
Looking for bibliography about it, I´ve found this paper:<br>
<a href="https://doi.org/10.1016/j.gmod.2014.09.002" class="onebox" target="_blank" rel="noopener nofollow ugc">https://doi.org/10.1016/j.gmod.2014.09.002</a><br>
It should be possible to develop something like this with vtk? Try to forgive my ignorance, please.</p>
<p>Thanks again</p>

---

## Post #8 by @lassoan (2021-10-25 23:01 UTC)

<p>In most cases, you can use the segment editor to get accurate <em>anatomical</em> surfaces without significant increase in memory size. You can crop the volume to minimal size and resample with isotropic spacing, which typically does not increase the volume size. You only need to apply further oversampling in rare cases: if you want to segment thin anatomical membranes, which are not visible in the image, just the user knows they are there.</p>
<p>Once you have the anatomical surface, you can use that to create a surgical guide by converting it to a shell (using Hollow effect) and crop it to the region that will be surgically exposed; and then combine it with CAD models or cut tool guidance holes or slots into it using “Combine models” module. This approach is implemented in a fully automated way in BoneReconstructionPlanner extension that I referenced above.</p>
<aside class="quote no-group quote-modified" data-username="apparrilla" data-post="7" data-topic="20323">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>Looking for bibliography about it, I´ve found this paper:<br>
<a href="https://doi.org/10.1016/j.gmod.2014.09.002" class="inline-onebox">Redirecting</a><br>
It should be possible to develop something like this with vtk?</p>
</blockquote>
</aside>
<p>You are much better off avoiding generating invalid meshes than trying to fix them later. However, if you want to use a mesh fixing algorithm then you can.</p>
<p>The mesh fixing algorithm that you have found has a reference paper that collected <a href="https://scholar.google.com/scholar?cites=2470291121142931538&amp;as_sdt=2005&amp;sciodt=0,5&amp;hl=en">177 citations in 11 years</a>, which is not much. This may suggest that the method does not work well and/or it may just reflect that people are reluctant to try it because of the very restrictive license (GPL license + no commercial use is explicitly prohibited). This license makes it impossible to integrate it into other libraries, such as VTK. However, you can give it a try using <a href="https://pymeshfix.pyvista.org/">PyVista</a>, which is a Pythonic interface for VTK with a few small additions, such as this pymeshfix package.</p>

---

## Post #9 by @apparrilla (2021-10-26 22:31 UTC)

<p>PyMeshFix looks the way I´m looking for:<br>
With pymeshfix.clean_from_file(“inputFile”,“outputFile”) I can get a model file to import like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7310a498787cbb922603068bcb648d46493e9804.png" data-download-href="/uploads/short-url/gpUz7ttmSQMKtVGgVNP7UjHWkMk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7310a498787cbb922603068bcb648d46493e9804_2_271x250.png" alt="image" data-base62-sha1="gpUz7ttmSQMKtVGgVNP7UjHWkMk" width="271" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7310a498787cbb922603068bcb648d46493e9804_2_271x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7310a498787cbb922603068bcb648d46493e9804_2_406x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7310a498787cbb922603068bcb648d46493e9804_2_542x500.png 2x" data-dominant-color="A4A6AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">692×638 33.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b2a0947719110bf708437b196f7eec0a2aa0310.png" data-download-href="/uploads/short-url/8roerEbW5EuggQO3tPEUReAPqTK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b2a0947719110bf708437b196f7eec0a2aa0310.png" alt="image" data-base62-sha1="8roerEbW5EuggQO3tPEUReAPqTK" width="273" height="250" data-dominant-color="020201"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">577×527 5.05 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried also this code:</p>
<blockquote>
<p>import pymeshfix as mf<br>
import pyvista as pv<br>
model = getNode(“Model”)<br>
pd = model.GetPolyData()<br>
mesh = pv.PolyData(pd)<br>
meshfix = mf.MeshFix(mesh)<br>
meshfix.repair()<br>
repaired = meshfix.mesh</p>
</blockquote>
<p>But I can´t update model polidata with the repaired mesh because it is a Polydata not a vtkPolyData.<br>
How can I do it?</p>
<p>Thanks</p>

---

## Post #10 by @lassoan (2021-10-26 23:22 UTC)

<p>If you cannot get the vtkPolyData from that pyvista Polydata object then you can write it to a file and read that file into Slicer.</p>

---

## Post #11 by @apparrilla (2021-11-02 18:47 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I use pymeshfix in script with no problem but if I add “import pymeshfix” to a scripted module, Python interactor send me constinously this kind of error:</p>
<pre><code class="lang-auto">Input port 0 of algorithm vtkTubeFilter(0000017C8ADE3EF0) has 0 connections but is not optional.
</code></pre>
<p>Import lines in modules:</p>
<pre><code class="lang-auto">try:
  import pymeshfix
except ModuleNotFoundError as e:
  #if slicer.util.confirmOkCancelDisplay("This module requires 'pymeshfix' Python package. Click OK to install it now."):
  slicer.util.pip_install("pymeshfix")
  import pymeshfix
</code></pre>
<p>Any idea why is it?<br>
Thanks in advance…</p>

---

## Post #12 by @lassoan (2021-11-02 19:10 UTC)

<p>It means that a VTK tube filter is used somewhere and its input is not set. If you don’t create such a tube filter then you can probably ignore this error for now.</p>

---

## Post #13 by @xiang_luo (2021-12-24 07:36 UTC)

<p>Recently, I had meet the same problem. And the clinical application is to make tube structure more realistic, e.g. pulmonary bronchi, artery-vein. Segmentation（lots of manual and CT quaility effects） from CT was hard to reconstuct smooth and tube-like structure mesh used for measures, so i try to use vtkTubeFilter to fit the mesh, but the bronchi and artery-vein has many bifurcation, then two tube mesh has self-intersecting in the bifurcation. Is there any way to solve this? Or is there other way to simulate a mesh to a smooth tube-like mesh?</p>

---

## Post #14 by @xiang_luo (2021-12-28 11:04 UTC)

<p>Hi, I can’t use pymeshfix to merge two self-intersection mesh to one like yours, can you provide the src stl file for me to test if there some problen in my pymeshfix?</p>

---

## Post #15 by @lassoan (2021-12-28 16:36 UTC)

<p>If you have trouble fixing up the tube filter output then you can use the curve  as input of a <a href="https://vtk.org/doc/nightly/html/classvtkImplicitModeller.html">vtkImplicitModeler</a>. That filter is guaranteed to produce a solid tube.</p>

---

## Post #17 by @xiang_luo (2021-12-30 13:21 UTC)

<p>i see the <a href="https://kitware.github.io/vtk-examples/site/Cxx/VisualizationAlgorithms/Hello/" rel="noopener nofollow ugc">examples</a> of <a href="https://vtk.org/doc/nightly/html/classvtkImplicitModeller.html" rel="noopener nofollow ugc">vtkImplicitModeler</a>, it seems the tube simulation of tube-like structure, e.g. vessel and bronchi. But i didn’t find more examples about the function, can it produce the different tube with different distance between the line? How to implement this effects?</p>

---

## Post #18 by @lassoan (2021-12-30 13:38 UTC)

<p>If you need varying radius then your can apply a tube filter with a smaller radius (subtracting a constant value) and then inflate it with the implicit modeler (using the value that was subtracted as distance value). If the radius varies in a large range then you may need to append multiple tubes (smaller tubes using the same centerline) to make sure large-diameter tube sections are filled by the implicit modeler.</p>

---

## Post #19 by @xiang_luo (2021-12-30 15:21 UTC)

<p>Thanks for your quick apply. Before this, i using tube filter with various radius and increase a sphere(blue) to fit tube-like structure(red).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ea3e67618828ba2bb826dbba69cae1cbf0c999a.jpeg" data-download-href="/uploads/short-url/dve2hI9R4tnL0KJxbeKYC2ohhSa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ea3e67618828ba2bb826dbba69cae1cbf0c999a_2_649x500.jpeg" alt="image" data-base62-sha1="dve2hI9R4tnL0KJxbeKYC2ohhSa" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ea3e67618828ba2bb826dbba69cae1cbf0c999a_2_649x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ea3e67618828ba2bb826dbba69cae1cbf0c999a_2_973x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ea3e67618828ba2bb826dbba69cae1cbf0c999a.jpeg 2x" data-dominant-color="5F5F80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×762 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>. But the problem described in the post occurs, the self-intersection tube looks very ugly and abnoraml. So next i will try the method you seggested with vtkImplicitModeler. Hope to solve the problem and get smooth tube simulation to the origin mesh(red).</p>

---

## Post #20 by @lassoan (2021-12-30 15:39 UTC)

<p>Implicit modeler fixes the self-intersections. You need to balance between resolution of the internal labelmap resolution of the implicit modeler and accuracy of the output. If you have a model with a large bounding box and you want very high accuracy (e.g., you have very thin vessels) then the internal labelmap will be very large (many voxels) so you may need dozens of GB of memory and computation will be very slow.</p>
<p>If this issue prevents you from getting the model you need, then there is one more approach you can try: use vtkbool library. It is available in Slicer  Preview Releases via Combine Models module, in Sandbox extension. You can combine sphere-terminated tube segments using mesh Boolean operators. It is of course many magnitudes slower than a simple tube filter, so you might want to detect sharp bends and only use Boolean operations there, and use simple tube filter elsewhere.</p>

---

## Post #21 by @xiang_luo (2021-12-30 15:44 UTC)

<p>Okay, Thanks! I will try the method you suggented. BTW, i think this is a great good in mesh simulation in medical domain to solve the resolution and manual segmentation error in CT. Is there any feature development work about this?</p>

---
