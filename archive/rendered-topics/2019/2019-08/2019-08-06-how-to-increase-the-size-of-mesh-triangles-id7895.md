---
topic_id: 7895
title: "How To Increase The Size Of Mesh Triangles"
date: 2019-08-06
url: https://discourse.slicer.org/t/7895
---

# How to increase the size of mesh triangles

**Topic ID**: 7895
**Date**: 2019-08-06
**URL**: https://discourse.slicer.org/t/how-to-increase-the-size-of-mesh-triangles/7895

---

## Post #1 by @Mohsen_Taheri (2019-08-06 15:25 UTC)

<p>Hi,</p>
<p>For a specific purpose I need to coarsen the mesh or increase the area of mesh triangles.<br>
I appreciate if anyone help me</p>

---

## Post #2 by @lassoan (2019-08-07 04:50 UTC)

<p>You can use “Decimation” option in “Surface toolbox” module for this.</p>
<p>You can include decimation step in segmentation’s automatic binary labelmap to closed surface converter: in Segmentations module / Representation section, click “Update” button next to “Closed surface”, click on the “Binary labelmap -&gt; Closed surface” conversion path, and adjust “Decimation factor” parameter.</p>

---

## Post #3 by @Chris_Rorden (2019-08-07 12:45 UTC)

<p>If you want to simplify/decimate an existing mesh, there are a number of tools that can help you out. <a href="http://www.alecjacobson.com/weblog/?p=4444" rel="noopener nofollow ugc">Alec Jacobson</a> has a nice page that describes several algorithms (mostly for Matlab). The two big ideas are whether you want an adaptive method (where original shape is preserved by selectively deleting vertices in flat areas) or not (<a href="https://brainder.org/2016/05/31/downsampling-decimating-a-brain-surface/" rel="noopener nofollow ugc">which can have benefits</a>). The other (related) choice is whether surviving vertices maintain their original location, or whether vertex collapse interpolates the position of the surviving vertex to best maintain original shape.</p>
<ul>
<li>
<p><a href="https://github.com/HusseinBakri/3DMeshBulkSimplification" rel="noopener nofollow ugc">Python code</a> exists for these tasks.</p>
</li>
<li>
<p>The graphical interface of <a href="http://www.meshlab.net" rel="noopener nofollow ugc">MeshLab</a> has a whole range of options in Filters/Remeshing,Simplification,Reconstruction that you can tune for your uses.</p>
</li>
<li>
<p><a href="https://github.com/sp4cerat/Fast-Quadric-Mesh-Simplification" rel="noopener nofollow ugc">Sven Forstmann</a> has an elegant implementation of <a href="https://www.cs.cmu.edu/~./garland/Papers/quadrics.pdf" rel="noopener nofollow ugc">Surface Simplification Using Quadric Error Metrics</a> that is provided as a standalone executable but been ported to many languages (C, C#, Pascal, Java, JavaScript).</p>
</li>
<li>
<p><a href="https://www.nitrc.org/plugins/mwiki/index.php/surfice:MainPage" rel="noopener nofollow ugc">Surfice</a> includes an graphical interface of Sven’s algorithm. You can drag and drop a mesh to open it, choose Advanced/Simplify to reduce it, and Advanced/Save to save the result. The image below shows an original mesh created with Slicer (left) after 90% of the vertices have been removed (right).</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9c126eb6ed71211ba6790ed499067f0fd20c971.jpeg" data-download-href="/uploads/short-url/zDqIq3QUvI8ele7bWO4Zs1Q5S0x.jpeg?dl=1" title="orig" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9c126eb6ed71211ba6790ed499067f0fd20c971_2_690x381.jpeg" alt="orig" data-base62-sha1="zDqIq3QUvI8ele7bWO4Zs1Q5S0x" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9c126eb6ed71211ba6790ed499067f0fd20c971_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9c126eb6ed71211ba6790ed499067f0fd20c971.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9c126eb6ed71211ba6790ed499067f0fd20c971.jpeg 2x" data-dominant-color="ABA6AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">orig</span><span class="informations">986×545 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Juicy (2019-08-10 22:15 UTC)

<p>I have personally found that if you are using STL files then it is best to do the decimation in another program such as blender or mesh mixer rather than use surface toolbox.</p>
<p>I have found the decimation tools in blender for example, give more even looking, aesthetically pleasing mesh upon decimation while still keeping all the fine details. The decimation in surface toolbox seems to give very uneven triangles (huge is some areas and really tiny in others) especially with large reductions in triangle count. I would encourage you to make the comparison yourself.</p>
<p>You should really try and limit what you do to the model in a post processing program such as blender though as you have no way of checking the model against the original scan as you do in slicer. as long as you dont move the models position in blender you should be able to re import it back into slicer to check it over top of the original scan. Always ensure that your model still accurately represents the anatomy when making any changes.</p>

---

## Post #5 by @lassoan (2019-08-11 03:31 UTC)

<p>VTK’s decimation filter preserve original mesh points, does not do any remeshing, so it is mainly used for very high fidelity reduction of the dense mesh that marching cubes or flying edge method generates from labelmaps. If you need more than about 60-80% reduction then you probably need to remesh.</p>
<p>It would be relatively easy to make available mesh simplification filters in Slicer (for example, some of those <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> listed above), but I don’t know very strong use cases. Why do you need mesh simplification with remeshing? Can you describe your application and workflow?</p>

---

## Post #6 by @Juicy (2019-08-11 09:48 UTC)

<p>I use Slicer and Blender together to model surgical guides and surgical implants.</p>
<p>First we segment the bones in the region of interest from a CT scan and save it as an STL. The STL is then opened in Blender. The first thing we usually do when opening the STL file in Blender is decimate the mesh. The triangle count is often around 3 million tris for a skull model which is straight out of Slicer. This makes for very slow performance on our computers and a really un-necessarily high resolution mesh. We usually decimate the mesh so it has around 10-20% of the original triangle count. The decimation on blender seems to re-mesh the model as well and gives a nice even triangle distribution and doesn’t seem to loose too much fine detail.</p>
<p>We then model a surgical guide or implant around the bone anatomy and usually use a boolean subtraction (with some clearance) so that the model fits onto the bone well. It is also good to have coarse mesh so that the face(s) on the model which result from the boolean subtraction do not also have tiny mesh faces, making them hard to edit (if needed).</p>
<p>The implants or guides are then either 3D printed or CNC machined.</p>
<p>A decimation tool (which also re-meshes) in slicer would be useful as it would allow us to check the model while it is still overlaid on top of the CT scan for any discrepancy. It would also save exporting a huge STL file and having the initial sluggishness of loading it up in blender and decimating it there.</p>

---

## Post #7 by @lassoan (2019-08-11 19:06 UTC)

<p>You can smooth segments in Segment Editor (Smoothing effect). You can also create molds, invert geometry, combine it with CAD models using Logical operators effect. Do you need to use Blender for these?</p>
<p>3D models exported from these segmentations are indeed very dense, but 3D printers and CNC machines should be able to deal with these. Do you find that large models cause problems?</p>

---

## Post #8 by @Mohsen_Taheri (2019-08-11 19:45 UTC)

<p>Actually I used Surface toolbox and  Meshmixer and the result of both of them was satisfying.<br>
The reason that I needed a lighter version of the mesh was to reduce the computation time of the program that I am using to fit a model.</p>

---
