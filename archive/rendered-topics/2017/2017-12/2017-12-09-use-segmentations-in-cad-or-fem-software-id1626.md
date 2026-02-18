# Use segmentations in CAD or FEM software

**Topic ID**: 1626
**Date**: 2017-12-09
**URL**: https://discourse.slicer.org/t/use-segmentations-in-cad-or-fem-software/1626

---

## Post #1 by @gregorio (2017-12-09 13:21 UTC)

<p>Operating system: windows 8.1 Pro<br>
Slicer version: 4.3.1<br>
Expected behavior: to have the possibility to transform surface models (mesh in stl format) to smooth geometry models (nurbs e.g. in IGES format)<br>
Actual behavior: 3D models are surface meshes, not real geometries</p>

---

## Post #2 by @cpinter (2017-12-09 15:37 UTC)

<p>Hi Gregorio,</p>
<p>First of all, please use Slicer 4.8 (or 4.8.1 as it’ll be released in a few days), there have been a great amount of improvements in the four years since 4.3.</p>
<p>You can smooth models in the Surface Toolbox module.</p>
<p>What do you mean by “real geometry”?</p>

---

## Post #3 by @lassoan (2017-12-10 01:24 UTC)

<p>If you need volumetric meshes instead of surface meshes, use Segment Mesher extension. It can create tetrahedral meshes using Cleaver 2 or TetGen.</p>

---

## Post #4 by @gregorio (2017-12-11 07:05 UTC)

<p>Thank you for the prompt reply.</p>
<p>For geometry, I mean a surface/volume that I can use with CAD and/or Finite Element Analysis, and eventually mesh it only in a second moment.</p>
<p>It is a common but not simple problem, to segment anatomical images and to work with surfaces that are not meshes (i.e. triangles and nodes, such as the .stl format or .vtk format in 3D slicer).</p>
<p>The procedure is well faced by the Mimics program, segmentation --&gt; mesh --&gt; CAD surface, but it is a pay program.</p>
<p>Thanks again</p>

---

## Post #5 by @lassoan (2017-12-11 16:53 UTC)

<aside class="quote no-group" data-username="gregorio" data-post="4" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/fbc32d/48.png" class="avatar"> gregorio:</div>
<blockquote>
<p>I mean a surface/volume that I can use with CAD and/or Finite Element Analysis</p>
</blockquote>
</aside>
<p>For getting a surface mesh, segment a structure using Segment Editor, then export it to a model node in Segmentations module, then save as .STL file.</p>
<p>For getting a volumetric mesh with tetrahedral elements, segment a structure using Segment Editor, then create a mesh using Segment Mesher module (available in Segment Mesher extension), then save it as a VTK unstructured grid file.</p>

---

## Post #6 by @gregorio (2017-12-12 10:16 UTC)

<p>Thank you. But in this way, we are always talking about just meshes. I would need CAD geometries, it is something different, that can eventually be meshed in a second moment. I mean, if you know CAD or FEM softwares, when you start with them you begin with a “part”, that is something before “mesh”.</p>

---

## Post #7 by @lassoan (2017-12-12 14:01 UTC)

<p>Volumetric meshes are “solid” objects. You may have to convert the volumetric mesh to a format that is recognized by your CAD software as a solid (it’s a trivial file format conversion operation). For example, you can load your volumetric mesh into <a href="https://www.paraview.org/">Paraview</a> and see if it can save it into a suitable format.</p>

---

## Post #8 by @gregorio (2017-12-13 07:53 UTC)

<p>I’m afraid it is something more difficult, after I had make different tests in the past for conversion. The point is that with the conversion you maintain a “tessellated” surface, with all the triangles/tetrahedrals faces, so it changes the format but not the substance, mesh is not really overcame in favour of a smooth, “unmeshed”, surface</p>

---

## Post #9 by @vilem (2017-12-13 11:46 UTC)

<p>Hello Gregorio,<br>
for getting the valid surface model from STL data you have to use the specialized software - and some experience - we’re doing that job when scanning the parts and need to modified them in CAD software or machine them (and need to get the IGES or STEP format). in case you are interested please contact me on my email - <a href="mailto:vilem.vrbicky@3dtech.cz">vilem.vrbicky@3dtech.cz</a></p>

---

## Post #10 by @pieper (2017-12-13 14:21 UTC)

<aside class="quote no-group" data-username="gregorio" data-post="1" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/fbc32d/48.png" class="avatar"> gregorio:</div>
<blockquote>
<p>possibility to transform surface models (mesh in stl format) to smooth geometry models (nurbs e.g. in IGES format)</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/gregorio">@gregorio</a> it’s true Slicer doesn’t support making nurbs from medical image data.  The reason is that these representations are typically used to make more “abstract” or “idealized” (smoother) models whereas many Slicer applications would rather stick with more “granular” or “data driven” representations such as volumes or dense locally linear models (triangles).  Thus we use filtering operations to trade off data fidelity with model smoothness.</p>
<p>None of the options (nurbs, triangles, volumes, etc) are perfect for all situations so developers need to choose where to put the effort to best solve particular kinds of use cases.  In the past I know that people have had good luck performing image segmentation in Slicer and then using the generated model as a framework for creating nurbs or other models in something like Blender or SolidWorks, but it’s not automatic.</p>

---

## Post #11 by @gregorio (2017-12-14 10:25 UTC)

<p>Thank you at all.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> I agree, but to do the job with free softwares is still an open challenge, the discussion confirms it to me</p>

---

## Post #12 by @lassoan (2017-12-14 15:03 UTC)

<p>According to my limited experience with CAD software (used for designing solid parts) is that they usually don’t cope well with complex free-form objects created from medical images. They either just show it as a mesh and you cannot do much with them, and/or it really slows them down. Some software have special add-ons for processing meshes, I guess those try to fit nurbs, etc., but I haven’t tried those. However, these are inherently very limited, because they cannot efficiently simplify very complex shapes and they may assume that material properties are uniform in the whole object.</p>
<p>For medical images, usually the workflow is something like this:</p>
<ul>
<li>In CAD design software:
<ul>
<li>design your mechanical parts</li>
<li>export parts as mesh (STL)</li>
</ul>
</li>
<li>In medical imaging/modeling software (such as 3D Slicer or Mimics):
<ul>
<li>import CAD models</li>
<li>import patient images</li>
<li>create patient-specific models by segmenting patient images</li>
<li>combine CAD models with patient-specific models (in Slicer: using Segment editor, see <a href="https://www.youtube.com/watch?v=Uht6Fwtr9hE">simple video tutorial</a> here)</li>
<li>create volumetric mesh suitable for FEA (in Slicer: <a href="https://github.com/lassoan/SlicerSegmentMesher">Segment mesher extension</a>, use <code>Probe volume with model</code> module to set material properties inside the volumetric mesh)</li>
</ul>
</li>
<li>In FEA software:
<ul>
<li>In preprocessor: define boundary conditions, material properties, etc.</li>
<li>In solver: run FEA</li>
<li>In post-processor: view data, export relevant information to meshes</li>
</ul>
</li>
<li>In medical imaging/modeling software:
<ul>
<li>Import FEA result meshes</li>
<li>Perform final patient-specific analysis</li>
</ul>
</li>
</ul>
<p>Note that in this workflow CAD design software does not have to deal with complex meshes.</p>

---

## Post #13 by @moondrake99 (2018-02-27 20:20 UTC)

<p>I regularly have to to do FEM analysis on 3D images of biological tissues obtained my microscopy. And I agree with gregorio it is somewhat a mess.</p>
<p>My workflow is now:<br>
ImageJ for segmenting, create a volume mesh the resulting images with iso2mesh, import the mesh in COMSOL (commercial FEM solution), convert the mesh in comsol back  to a geometry (fails often, as comsol is not good at it), then make a mesh again.</p>
<p>It is slightly better that going through STL (which cause far more problems), but it is still silly. It would be preferable to have software that could produce NURBS from the 3D stacks directly. I think the reason why some FEM packages prefer to work with geometry instead of meshes is that it makes defining boundaries( faces ) and boolean operations simpler.</p>
<p>Of course I can use a mesh directly for FEM, but it will prevent me from using quite powerful geometry operations that are sometimes necessary for building a model.</p>
<p>Going through a mesh and then NURBS and then mesh again creates far far more artefacts than a simple “smooth” would do. And I disagree on principle anyway that making a tetrahedal mesh for tissue is somehow more precise than using NURBS. Cells are far more smooth than even the finest mesh… Especially when working with internal boundaries or defining contact pairs, having a geometry is a must.</p>
<p>But I have yet to find any software that can do this well. Just fitting/filling my cell structures with overlapping spheres would be better than what I get with some meshes. I have seen vtk plugins that get nurbs from pointclouds, so it must be possible to whip something up, but I am not sure if/when I have the time for this.</p>

---

## Post #14 by @lassoan (2018-02-27 21:21 UTC)

<aside class="quote no-group" data-username="moondrake99" data-post="13" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5daacb/48.png" class="avatar"> moondrake99:</div>
<blockquote>
<p>My workflow is now:</p>
<p>ImageJ for segmenting, create a volume mesh the resulting images with iso2mesh, import the mesh in COMSOL (commercial FEM solution), convert the mesh in comsol back  to a geometry (fails often, as comsol is not good at it), then make a mesh again.</p>
</blockquote>
</aside>
<p>Have you tried Segment Mesher extension in Slicer? Cleaver2 generates high-quality volumetric meshes directly from segmentation (from binary labelmap representation; and if needed we can make it work from fractional labelmap representation, too). There are no unnecessary conversions.</p>

---

## Post #15 by @lassoan (2018-02-27 21:32 UTC)

<aside class="quote no-group" data-username="moondrake99" data-post="13" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5daacb/48.png" class="avatar"> moondrake99:</div>
<blockquote>
<p>Of course I can use a mesh directly for FEM, but it will prevent me from using quite powerful geometry operations that are sometimes necessary for building a model.</p>
</blockquote>
</aside>
<p>The workflow that we have envisioned with Slicer is that you create your models in CAD modeling software, import them into Slicer, combine them with free-form anatomical shapes obtained from 3D images, and then you can export labelmap, surface mesh, or volumetric mesh for 3D printing, visualization, or further processing in other software.</p>
<p>Segment Editor module has several tools for combining CAD models with anatomical shapes in various ways, but it you are not sure how certain operations can be achieved then let us know.</p>

---

## Post #16 by @moondrake99 (2018-02-28 11:48 UTC)

<p>Andras: thanks for the reply. I will look again, but it looks like you admit that the Slicer is not the right tool for what gregorio and I want to do: import 3D structures of segmented tissue in some FEM packages. This is fine ofcourse! But I just hoped there would be some interest in seeing this as a valid problem.</p>
<p>We do not want high quality volumetric meshes. They all get converted to NURBS again in the FEM package (and sometimes badly at that).  So why bother? We would like segmentation-&gt;NURBS-&gt;FEM. Not segmentation-&gt;mesh-&gt;nurbs-&gt;mesh-&gt;FEM.</p>
<p>slicer’s mesh may be leagues better than COMSOL’s mesher, and it is probably a shortcoming of COMSOL that it does not allow boolean/boundary definitions, assemblies, etc etc with imported meshes. And I will complain to them about this.</p>
<p>But it seems to me there is a valid use for segmentation-&gt;NURBS as well. And we are merely looking for a tool that lets us do this. The features of Slicer are nice, and it would be wonderful to have this ability. But I also understand you cannot support everything.</p>
<p>It seems that recent versions of  InVesalius may be able to do this better. So I am going to check that out.</p>

---

## Post #17 by @lassoan (2018-02-28 12:56 UTC)

<p>Thanks for the additional information. What is still not clear for me that if you can do all compositing of CAD models with anatomical structures in Slicer then why do you need NURBS export? Why cannot you use the volumetric mesh that Slicer generates directly in the FEM solver? I don’t think that FEM solvers represent structures as NURBS. Modeling programs do, but the idea is that the output of Slicer does not need further modeling.</p>

---

## Post #18 by @brhoom (2018-02-28 13:17 UTC)

<p><a class="mention" href="/u/gregorio">@gregorio</a>  and <a class="mention" href="/u/moondrake99">@moondrake99</a></p>
<p>is it possible to provide some images/videos showing comparison cases e.g slicer output and output from other tools.</p>

---

## Post #19 by @lassoan (2018-02-28 17:51 UTC)

<aside class="quote no-group" data-username="moondrake99" data-post="16" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5daacb/48.png" class="avatar"> moondrake99:</div>
<blockquote>
<p>import 3D structures of segmented tissue in some FEM packages</p>
</blockquote>
</aside>
<p>By FEM package, do you mean modeling tool, where you edit/combine 3D models? It is their limitation that they can only work with NURBS representation, and not with arbitrary segmented labelmaps (and not very well with complex triangle meshes).</p>
<p>This is the problem that Slicer solves, as it can edit/combine surface meshes and arbitrarily complex segmented labelmaps. Of course, modeling capabilities of Slicer are very limited compared to what modeling tools can do, but should be powerful enough so that you can use it as the last step of your workflow. Slicer’s output should not need further editing (so no NURBS representation is needed), you can feed it directly into FEM solvers/pre-processors.</p>
<p>It could be still nice to have NURBS-based editing in Slicer for simple, smooth shapes; but this is a special case and it is not very high on the priority list.</p>

---

## Post #20 by @moondrake99 (2018-03-02 12:39 UTC)

<p>brhoom: yes. But this will take me some time (which I am rather short of atm). Will try.<br>
lassoan:</p>
<p>By FEM package i mean a tool that does both the solving, but also preprocessing. And yes, it has some CAD ability in that it can edit and combine models. This has good reasons. One could for example examine the effect of a change in structure on whatever physics one is interested in. To change the structure, it helps tremedously to have some 3D processing in this package. You can also use solver approaches that can refine the mesh based on the model solution (finer mesh in areas with steep gradients).</p>
<p>I have needed to use both things in the past. But the current problem is perhaps simpler:</p>
<p>A typical but simplified example would be to do a diffusion model inside a single cell. Images are e.g. from SBF-SEM. Imagine I have a cytoplasm and many mitochondria. I segment the cells and the mitochondria.</p>
<p>The main problem now is that for the FEM analysis, I need to define the surface of the mitochondria (the membrane) as a kind of flux discontinuity as it’s permeability is quite low, but it is only very thin. A way to deal with such thin elastic layers is to have a surface mesh on the outside of the mitochondria and on the “inside” of the cell (basically the holes you would get if you would substract the mito-volume from the cellular volume). These two meshes can be coupled (sometimes called contact or identity pairs) and given a simple relation (in this case, something like C1-C2=F/G, where C are concentrations on the contact mesh sides, G is a conductance and F is a normal diffusive flux). Such couplings put some constraints on the 2 surface meshes (I forgot the details, but I assume they have to be roughly matching to prevent errors).</p>
<p>The whole thing is than solved in what my current favourite FEM package calls “assembly mode”. It roughly means you actually have 2 separate FEM models that are coupled with some equation(the simple 1D permeability above). These may even be different physics.</p>
<p>I have not found a way to create such meshes with other tools. And if I had, I am not sure I could make my current FEM package use such mesh in assembly mode (as it would not know elements of the mesh are to be coupled without doing the operation itself or an exchange file-format that lists them).</p>
<p>A second problem is that a mesh of a blobby object like a cell is quite irregular. Now, I may want to define a boundary condition (e.g. an influx of stuff) on only part of this cell surface (for example, where it intersects with another shape). You are right I can do the compositing in Slicer, but a mesh is just a mesh and I have no idea what mesh elements are the ones that I need to define different boundary conditions on.</p>
<p>If I do the compositing in the FEM package, it keeps track of such boundaries and I can set different conditions on that.</p>
<p>The physics coupling and separation of mesh and geometry is the whole reason I use a bloody expensive FEM package instead of the quite good free solvers. But the disadvantage is that I have to use THEIR compositing (which is not that good). And you are right that it is their limitation that the compositing works with NURBS. The solution some people found is to pay even more and buy simpleware or mimics who are apparently good at creating a NURBS representation out of meshes. To be fair, even comsol provides a mesh-&gt;nurbs converter, but it is not an easy problem and does not work perfect for me (it is my main time sink).</p>

---

## Post #21 by @lassoan (2018-03-02 13:54 UTC)

<p>A post was merged into an existing topic: <a href="/t/panoramic-image-view/2203">Panoramic image/view</a></p>

---

## Post #22 by @lassoan (2018-03-02 16:44 UTC)

<p>Thank you for the detailed explanation. I think I now understand your needs better.</p>
<ol>
<li>Updating of CAD models</li>
</ol>
<p>It can be certainly useful to update your CAD model as you combine it with anatomical shapes. We plan to implement real-time synchronization with selected modeling software (Blender and FreeCAD) so that if you modify your CAD model, the changes show up immediately in Slicer. This would make it easier to create an updated volumetric mesh whenever you adjust your CAD model.</p>
<ol start="2">
<li>Mesh generation</li>
</ol>
<p>COMSOL’s mesh generation capabilities are very nice, but you don’t need to use them, if you generate your volumetric mesh in another software. COMSOL can load volumetric meshes in COMSOL or NASTRAN format (see “Importing COMSOL Meshes” slide <a href="http://www.michelsencentre.com/doc/meshing_general_introduction_V3a.pdf">here</a>). This is the approach that Materialise Mimics and Simpleware ScanFE use and you can do it with Slicer, too: save the volumetric mesh as a VTK unstructured grid file (.vtu) and convert it to COMSOL or NASTRAN using <a href="https://github.com/victorsndvg/FEconv">FEconv</a>. With a little work, FEconv could be added to Slicer as an extension and then you could save the volumetric mesh directly from Slicer to a variety of FE mesh file formats.</p>
<ol start="3">
<li>Converting surface meshes NURBS/BRep solids</li>
</ol>
<p>We are using SolidWorks and Autodesk Fusion 360 and they of course cannot automatically convert meshes to solids (NURBS or BRep). This is similar to how vector graphics programs deal with bitmap images: they can load them, nicely display them, and can convert to vector graphics - kind of, with some data loss.</p>
<p>Reverse engineering tools sometimes work for simple geometric shapes (<a href="https://knowledge.autodesk.com/support/fusion-360/learn-explore/caas/sfdcarticles/sfdcarticles/How-to-Convert-a-Mesh-to-a-BRep-in-Fusion-360.html">Fusion 360 sets the limit at about 10000 facets</a>), but if you want to have usable result then you have to re-create the object manually (see for example <a href="https://www.youtube.com/watch?v=8Z0IiVKt5Hg">this tutorial</a>).</p>

---

## Post #23 by @gregorio (2018-03-19 15:31 UTC)

<p><a class="mention" href="/u/moondrake99">@moondrake99</a> thank you very much for the way you carried out the discussion. I’m sorry for my absence in the meantime, but I found you highlighted the problem in a more exhaustive way than I can.</p>
<p>I try to explain again my simplier challenge, the reason why I need geometry: with anatomical structures, in particular in the knee and with contact problems in FEM, it would be better to  have volumetric HEXAHEDRAL meshes than tetrahedral meshes. More in general, to have a certain control on mesh process (number and TYPE of elements): with free softwares, I am finding problems in converting native trianglular (tetrahedral) meshes into smooth surfaces (CAD geometries, i.e. nurbs) that I can mesh in the way I want (possibly hexhaedral meshes and in an automatic way: “I.A.FEMesh” software makes it but meanly manually).</p>
<p>Here a recent reference strictly related to my problem:<br>
“Automated hexahedral meshing of knee cartilage structures – application to data from the osteoarthritis initiative”</p>
<p><a href="https://www.tandfonline.com/doi/abs/10.1080/10255842.2017.1383984?journalCode=gcmb20" class="onebox" target="_blank" rel="nofollow noopener">https://www.tandfonline.com/doi/abs/10.1080/10255842.2017.1383984?journalCode=gcmb20</a></p>

---

## Post #24 by @Saima (2018-07-10 07:42 UTC)

<aside class="quote no-group" data-username="gregorio" data-post="1" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/fbc32d/48.png" class="avatar"> gregorio:</div>
<blockquote>
<p>D models are surface meshes,</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I was looking at this extension. Does it need a segmented image as input to produce mesh? is there any explanation on how to use segment mesher extension? Is there any extension available that can create volumetric tetrahedral meshes directly form images in 3-d slicer?</p>

---

## Post #25 by @lassoan (2018-07-10 14:43 UTC)

<aside class="quote no-group" data-username="Saima" data-post="24" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Does it need a segmented image as input to produce mesh?</p>
</blockquote>
</aside>
<p>You need a segmentation node as input. You can create segmentation node from an existing labelmap volume or model node (surface mesh). If all you have is an grayscale input volume, then you can create a segmentation node using Segment editor module.</p>
<aside class="quote no-group" data-username="Saima" data-post="24" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>is there any explanation on how to use segment mesher extension?</p>
</blockquote>
</aside>
<p>Yes. See documentation here: <a href="https://github.com/lassoan/SlicerSegmentMesher" class="inline-onebox">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a></p>
<aside class="quote no-group" data-username="Saima" data-post="24" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Is there any extension available that can create volumetric tetrahedral meshes directly form images in 3-d slicer?</p>
</blockquote>
</aside>
<p>Without segmentation? Would you like to fill the image volume with uniformly sized tetrahedra? If you segment structures then you can create a volumetric mesh for those using Segment mesher extension.</p>

---

## Post #26 by @Saima (2018-07-30 09:16 UTC)

<p>Dear Lasso,<br>
I tried to use the segment mesher extension. Followed these steps:</p>
<p>Downloaded Braintumor data<br>
Labeled tumor and brain using editor in segmentation</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b06a27a99bb7f4cb52a21ad4cf1f5a05f27426c.jpeg" data-download-href="/uploads/short-url/aHI1ycCFuN0D9XvBfRWqDXHpQKM.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b06a27a99bb7f4cb52a21ad4cf1f5a05f27426c_2_690x388.jpg" alt="image" data-base62-sha1="aHI1ycCFuN0D9XvBfRWqDXHpQKM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b06a27a99bb7f4cb52a21ad4cf1f5a05f27426c_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b06a27a99bb7f4cb52a21ad4cf1f5a05f27426c_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b06a27a99bb7f4cb52a21ad4cf1f5a05f27426c_2_1380x776.jpg 2x" data-dominant-color="B0AEB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 593 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Mesh generation &gt;&gt; Clever</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/897f255008effc6197689caa52c544a760801366.jpeg" data-download-href="/uploads/short-url/jClOXErdYMhiEWxMWD1nOz4eBGS.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/897f255008effc6197689caa52c544a760801366_2_690x388.jpg" alt="image" data-base62-sha1="jClOXErdYMhiEWxMWD1nOz4eBGS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/897f255008effc6197689caa52c544a760801366_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/897f255008effc6197689caa52c544a760801366_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/897f255008effc6197689caa52c544a760801366_2_1380x776.jpg 2x" data-dominant-color="AEADB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 611 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Settings<br>
Selected labels as inputs<br>
Output models new &gt;&gt; output model1 and output model 2</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba714312ea8444e6642bfdc342935a313a47425b.jpeg" data-download-href="/uploads/short-url/qBlthgRZWwmaY3tadOoSARjEWxB.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba714312ea8444e6642bfdc342935a313a47425b_2_690x388.jpg" alt="image" data-base62-sha1="qBlthgRZWwmaY3tadOoSARjEWxB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba714312ea8444e6642bfdc342935a313a47425b_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba714312ea8444e6642bfdc342935a313a47425b_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba714312ea8444e6642bfdc342935a313a47425b_2_1380x776.jpg 2x" data-dominant-color="ADADB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 545 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9391af0a8b1973144d86475a8d1ab7dfbbe08b63.jpeg" data-download-href="/uploads/short-url/l3sjtDjrnzkP1Xu86i9PT05oGgb.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9391af0a8b1973144d86475a8d1ab7dfbbe08b63_2_690x388.jpg" alt="image" data-base62-sha1="l3sjtDjrnzkP1Xu86i9PT05oGgb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9391af0a8b1973144d86475a8d1ab7dfbbe08b63_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9391af0a8b1973144d86475a8d1ab7dfbbe08b63_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9391af0a8b1973144d86475a8d1ab7dfbbe08b63_2_1380x776.jpg 2x" data-dominant-color="AEAEB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 537 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Apply and got the results you can see in the image in 3D view.</p>
<p>Can I get mesh generation for each of the label separately?<br>
How to extract the nodes of the mesh generated for the structure in python?</p>
<p>In segmentMesher I did the following. Please see the screen shot.<br>
In segmentation I can only select segmentation. I do not see any other option.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec768406a14d520e39041cb99d4c6046ef97144f.jpeg" data-download-href="/uploads/short-url/xJQBjjmPv0W98ctvJzfmtlra2OH.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec768406a14d520e39041cb99d4c6046ef97144f_2_690x388.jpg" alt="image" data-base62-sha1="xJQBjjmPv0W98ctvJzfmtlra2OH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec768406a14d520e39041cb99d4c6046ef97144f_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec768406a14d520e39041cb99d4c6046ef97144f_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec768406a14d520e39041cb99d4c6046ef97144f_2_1380x776.jpg 2x" data-dominant-color="B5B3BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 495 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What I am doing wrong. Please tell me.<br>
Thank you<br>
REgards,<br>
Saima Safdar</p>

---

## Post #27 by @lassoan (2018-07-30 10:09 UTC)

<p>Use recent nightly version of Slicer. You can Segment using Segment Editor module and create volumetric mesh using Segment mesher extension.</p>

---

## Post #28 by @Saima (2018-07-30 12:17 UTC)

<p>Did segmentation with segment editor for brain portion.<br>
Then using Segment Mesher it generated the following.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0ee4ff1104c8508ddd61b3dcce471fbd77ad4d9.jpeg" data-download-href="/uploads/short-url/rwKfS7oGFBvKLZM3IPBUqDHIvTr.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0ee4ff1104c8508ddd61b3dcce471fbd77ad4d9_2_690x388.jpg" alt="image" data-base62-sha1="rwKfS7oGFBvKLZM3IPBUqDHIvTr" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0ee4ff1104c8508ddd61b3dcce471fbd77ad4d9_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0ee4ff1104c8508ddd61b3dcce471fbd77ad4d9_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c0ee4ff1104c8508ddd61b3dcce471fbd77ad4d9_2_1380x776.jpg 2x" data-dominant-color="9F95A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 623 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How to access all the nodes(points) for the mesh generated for the brain portion?</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #29 by @lassoan (2018-07-30 12:30 UTC)

<p>Segment index is stored in the mesh for each cell as cell scalar data.</p>

---

## Post #30 by @Saima (2018-07-31 07:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="29" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ent index is stored in the mesh for each cell as cell scalar data.</p>
</blockquote>
</aside>
<p>mesh = n.GetMesh()</p>
<blockquote>
<blockquote>
<blockquote>
<p>mesh<br>
(vtkCommonDataModelPython.vtkUnstructuredGrid)</p>
</blockquote>
</blockquote>
</blockquote>
<p>Dear Lasso I need to understand its architecture.</p>
<p>Aim is to extract the vertexes and its x, y, z locations of only the brain portion of the mesh generated. Please help.<br>
Any way to get the description for the methods and the pipeline to use.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #31 by @lassoan (2018-07-31 08:00 UTC)

<p>You can extract any portion of the mesh by using Slicer’s Python console, using VTK filters that extract cells that have scalars in the specified range. Probably threshold filter would work and it takes only a few lines of Python code.</p>
<p>If you are not familiar with VTK then read the VTK textbook (<a href="https://blog.kitware.com/vtk-textbook-and-users-guide-now-available-for-download/">https://blog.kitware.com/vtk-textbook-and-users-guide-now-available-for-download/</a>) or use other mesh pre-processing software that can extract sub-meshes, such as Paraview or MeshLab.</p>

---

## Post #32 by @Saima (2018-07-31 10:52 UTC)

<p>thank you Andras. I will contact you once I done.</p>

---

## Post #33 by @Saima (2018-08-02 06:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="31" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>filters t</p>
</blockquote>
</aside>
<pre><code>for j in range(mesh.GetNumberOfCells()):
...  cellObject = mesh.GetCell(j)
...  pts = cellObject.GetPoints()
...  data = pts.GetData()
...  for i in range(data.GetNumberOfTuples()):
...   print("%s",data.GetTuple(i))
... 
('%s', (-72.65650177001953, 62.96849822998047, 56.67499923706055))
('%s', (-72.65650177001953, 89.84349822998047, 56.67499923706055))
('%s', (-91.40650177001953, 89.84349822998047, 56.67499923706055))
('%s', (-72.65650177001953, 68.21849822998047, 78.30000305175781))
('%s', (-72.65650177001953, 116.71849822998047, 56.67499923706055))
('%s', (-72.65650177001953, 116.71849822998047, 29.799999237060547))
('%s', (-91.40650177001953, 97.96849822998047, 48.54999923706055))
('%s', (-91.40650177001953, 116.71849822998047, 48.54999923706055))
</code></pre>
<p>Dear Andras is this right?<br>
These are points locations  x,y,z for every tetra. which I understand.</p>
<p>Please tell me if I am doing anything wrong.<br>
Another thing is I want to color a specific cell in the generated mesh. How to do this?</p>
<p>I am also looking into vtkextractcells.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #34 by @lassoan (2018-08-02 07:26 UTC)

<p>I cannot really follow what you are trying to do, but you can find complete example of extracting submesh corresponding to a specific material <a href="https://www.vtk.org/gitweb?p=VTK.git;a=blob;f=Examples/Graphics/Python/SingleYoungsMaterialInterface.py">here</a>:</p>
<pre><code># Extract submeshes corresponding to 2 different material Ids
cellData.SetActiveScalars( "Material Id" )
threshold2 = vtkThreshold()
threshold2.SetInputData( mesh )
threshold2.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_CELLS, vtkDataSetAttributes.SCALARS );
threshold2.ThresholdByLower( 2 )
threshold2.Update()
meshMat2 = threshold2.GetOutput()
threshold3 = vtkThreshold()
threshold3.SetInputData( mesh )
threshold3.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_CELLS, vtkDataSetAttributes.SCALARS );
threshold3.ThresholdByUpper( 3 )
threshold3.Update()
meshMat3 = threshold3.GetOutput()</code></pre>

---

## Post #35 by @Saima (2018-08-02 08:09 UTC)

<p>I am trying to extract every point id along with its x,y,z coordinates.</p>
<p>Specifically, the aim is to extract locations of all the cells of the segmented portion of the mesh</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e86bd9d454b885a82813a1f2071e140a75bead.jpeg" data-download-href="/uploads/short-url/kXBFBm4fdMjlbjbFTuNIa3ArHmB.jpg?dl=1" title="IMG_20180802_160424" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92e86bd9d454b885a82813a1f2071e140a75bead_2_375x500.jpg" alt="IMG_20180802_160424" data-base62-sha1="kXBFBm4fdMjlbjbFTuNIa3ArHmB" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92e86bd9d454b885a82813a1f2071e140a75bead_2_375x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92e86bd9d454b885a82813a1f2071e140a75bead_2_562x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92e86bd9d454b885a82813a1f2071e140a75bead_2_750x1000.jpg 2x" data-dominant-color="B3B2B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20180802_160424</span><span class="informations">3120×4160 2.51 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #36 by @lassoan (2018-08-02 08:45 UTC)

<p>You can extract sub-mesh using VTK threshold filter and then access all the point coordinates in a numpy array by calling <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html"><code>slicer.util.arrayFromModelPoints()</code></a>.</p>

---

## Post #37 by @lassoan (2018-08-03 09:34 UTC)

<p>A post was split to a new topic: <a href="/t/python-debugging-in-eclipse/3644">Python debugging in Eclipse</a></p>

---

## Post #38 by @Saima (2018-08-11 05:13 UTC)

<p>Dear Andras,<br>
Is it possible to generate surface mesh for brain using segment mesher. What will be the steps for doing it?</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #39 by @lassoan (2018-08-11 08:44 UTC)

<p>You can get a surface mesh by exporting segmentation to model node. If you need the surface mesh corresponding to the volumetric mesh with direct correspondence to volumetric mesh point IDs, then you can use VTK geometry filter on the volumetric mesh.</p>

---

## Post #40 by @Saima (2018-08-15 04:56 UTC)

<p>Dear Andras,<br>
Yes I need to generate a surface mesh corresponding to the volumetric mesh. Can you please give details on how to do it?<br>
getnode-&gt;getmesh&gt;setoutputdata for extract filter = mesh&gt;extactinsideon&gt; ???&gt;mapper&gt;actor&gt;renderer&gt;renderwindow&gt;render windowinteractor</p>
<p>everytime when mesher is used cube is generated within which the geometry of interest(brain) exists. is it possible to have the volumetric mesh for only the segmented portion of the geometry or you have to extract it from cube?</p>
<p>Regards<br>
Saima Safdar</p>

---

## Post #41 by @cpinter (2018-08-15 12:21 UTC)

<p>From <a href="https://discourse.slicer.org/t/3d-model-of-only-the-outer-surface-of-a-bone-3d-model-of-a-bone/2714/6">this</a> thread:<br>
“Cleaver generates a “background” mesh so that you can simulate embedding your structures in some material (soft tissue, etc). If you don’t need these mesh elements, then don’t use them. Each cell is assigned to a segment, specified by  <code>labels</code>  cell attribute. You can use this attribute to assign material properties or remove parts of the mesh, etc.”</p>

---

## Post #42 by @Saima (2018-08-20 11:53 UTC)

<p>This is a simple question I am asking here. I do not know how to get going with slicer interpreter. every-time the application crashes due to some error I lost all my written code. is there any way to retrieve your last code in interpreter. I have to write again and again. How to setup environment for coding in slicer using scripting</p>

---

## Post #43 by @pieper (2018-08-20 12:10 UTC)

<p>I find the best thing is to create an extension with a scripted module and use the Reload buttons to execute the associated test.  This way you can easily reproduce your work and add functionality incrementally.</p>
<p>See the slides and info here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Start_Here" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Start_Here</a></p>
<aside class="quote no-group" data-username="Saima" data-post="42" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>is there any way to retrieve your last code in interpreter.</p>
</blockquote>
</aside>
<p>The log file has a record of everything you typed in.</p>

---

## Post #44 by @Saima (2018-08-20 12:19 UTC)

<p>Thank you so much for replying. What about the edit it opens up for you in a notepad which is not good enough. What to do about this?</p>

---

## Post #45 by @ihnorton (2018-08-20 15:46 UTC)

<p>There are many editors available with good Python support – PyCharm (Community is free but does not support remote debugging), Spyder, Visual Studio Code, even Notepad++ has good basic Python highlighting and indenting.</p>
<p>By the way, along the lines Steve mentioned, if I don’t want to make a “full” module yet, then I usually still write my code in a file and load it with <a href="https://docs.python.org/2/library/functions.html#execfile"><code>execfile</code></a> in case there is a crash while interacting with C++ APIs.</p>

---

## Post #46 by @lassoan (2018-08-20 15:52 UTC)

<aside class="quote no-group" data-username="Saima" data-post="42" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>every-time the application crashes due to some error I lost all my written code</p>
</blockquote>
</aside>
<p>Everything that you typed in the console are automatically saved in application logs. After you restart Slicer, in menu choose: Help / Report a bug, select any of the previous session from the list, and you’ll see the commands you typed.</p>
<p>Previously, when I was not developing a module, I’ve been mostly copy-pasting from editors. However, now there is a new, very nice alternative: <a href="https://discourse.slicer.org/t/jupyter-notebooks-are-now-usable-in-3d-slicer/3438">using Slicer from Jupyter notebooks</a>. Instead of manual copy-pasting, you enter your code as small blocks of text, which is very easy to edit and re-run.</p>

---

## Post #47 by @Saima (2018-08-24 04:59 UTC)

<p>Dear Andras,<br>
I do not understand the implicit function. If I want to get  only the brain+tumur+ventricles mesh how do I define the implicit function?</p>
<p>Thank you</p>
<p>Looking forward</p>

---

## Post #48 by @lassoan (2018-08-24 13:38 UTC)

<p>Sorry, I don’t know what implicit function you are referring to.</p>

---

## Post #49 by @Saima (2018-08-27 02:56 UTC)

<p>In extract geometry filter. there is an implicit function. I do not understand the purpose of using this implicit function?<br>
Would you please explain what is its purpose?</p>

---

## Post #50 by @lassoan (2018-08-27 03:35 UTC)

<p>I see, yes, vtkExtractGeometry is for extracting a sub-mesh using an implicit function, which is not what you need. I meant that you can use <a href="https://www.vtk.org/doc/nightly/html/classvtkGeometryFilter.html">vtkGeometryFilter</a> to extract boundary surface of an unstructured grid.</p>

---

## Post #51 by @Saima (2018-08-27 10:55 UTC)

<p>Andras, would you please tell me about the purpose of setextractionmodetospecified regions().</p>

---

## Post #52 by @lassoan (2018-08-27 11:48 UTC)

<p>To get boundary surface, you need to use <a href="https://www.vtk.org/doc/nightly/html/classvtkGeometryFilter.html">vtkGeometryFilter</a>, not vtkExtractGeometry.</p>

---

## Post #53 by @Saima (2018-08-28 12:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="52" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>surface, you need</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I am using filter like this. Could you please help me in understanding the pipeline for using filters?</p>
<p>First I am using connectivity filter to seperate the meshes. I am not sure I am using correctly the specified regions. then vtkgeometryfilter.</p>
<pre><code>connect = vtk.vtkConnectivityFilter()
connect.SetInputData(mesh)
connect.SetExtractionModeToSpecifiedRegions()
connect.AddSpecifiedRegion(1)
connect2 = vtk.vtkConnectivityFilter()
connect2.SetInputData(mesh)
connect2.SetExtractionModeToSpecifiedRegions()
connect2.AddSpecifiedRegion(2)
connect3 = vtk.vtkConnectivityFilter()
connect3.SetInputData(mesh)
connect3.SetExtractionModeToSpecifiedRegions()
connect3.AddSpecifiedRegion(3)

brain = vtk.vtkGeometryFilter()
brain.SetInputConnection(connect3.GetOutputPort())

brainMapper = vtk.vtkPolyDataMapper()
brainMapper.SetInputConnection(brain.GetOutputPort())

brainActor = vtk.vtkActor()
brainActor.SetMapper(brainMapper)
</code></pre>
<p>Usual stuff:</p>
<pre><code>ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

ren.AddActor(brainActor)
</code></pre>
<p>Could you please tell me what I am doing right. Am I using it correctly?<br>
I could not get the results (surface mesh corresponding to the volumetric mesh with direct correspondence to volumetric mesh point IDs, then you can use VTK geometry filter on the volumetric mesh)</p>

---

## Post #54 by @lassoan (2018-08-28 16:13 UTC)

<p>To get help on how to use VTK, the VTK mailing list may be a better forum.</p>
<p>Anyway, some hints: If you need corresponding point IDs between selection/filtering input and output then read up on pedigree IDs. For example, vtkExtractSelectedThresholds may be able to extract sub-meshes defined by scalar range and provide pedigree IDs (point ID of the source mesh for each new point).</p>

---

## Post #55 by @Saima (2018-08-29 05:39 UTC)

<p>Dear Andras,<br>
I used threshold to get the geometry of interest.</p>
<p>Next is to get all the points corresponding to volumetric mesh with direct correspondence to volumetric mesh point ids. I will follow what you suggested me and come back again.</p>
<p>Thank you so much for helping.</p>
<p>Andras could you please tell me is there any way to get auto completion in jupyter for vtk and slicer.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #56 by @lassoan (2018-08-29 11:58 UTC)

<aside class="quote no-group" data-username="Saima" data-post="55" data-topic="1626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Andras could you please tell me is there any way to get auto completion in jupyter for vtk and slicer.</p>
</blockquote>
</aside>
<p>It works in latest nightly build. If it does not work for you then please report it in a separate topic.</p>

---

## Post #57 by @Saima (2018-12-19 04:15 UTC)

<p>Hi Andras,<br>
What does cleaver meshing options represent. And what does tetGen meshing options represents.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #58 by @lassoan (2018-12-19 04:30 UTC)

<p>These are two volumetric mesh generator libraries. See details on their websites: <a href="https://sciinstitute.github.io/cleaver.pages" rel="nofollow noopener">Cleaver2</a>, <a href="http://www.tetgen.org/" rel="nofollow noopener">TetGen</a>. I would recommend Cleaver2, as it is more robust, has better support for multi-material meshes, and has free, non-restrictive license.</p>

---

## Post #60 by @JonNithal (2025-05-08 12:01 UTC)

<p>Hii <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I was just wondering if there have been any updates or further progress on the plans you mentioned, especially around syncing CAD models with Slicer or improving mesh export workflows. I’m still exploring this area and would really appreciate hearing if anything new has come up.</p>
<p>Thanks!</p>

---
