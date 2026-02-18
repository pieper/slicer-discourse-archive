# SPHARM-PDM from triangular meshes

**Topic ID**: 6938
**Date**: 2019-05-27
**URL**: https://discourse.slicer.org/t/spharm-pdm-from-triangular-meshes/6938

---

## Post #1 by @Fiona_Pye (2019-05-27 13:04 UTC)

<p>I would like to apply the SPHARM-PDM to triangular meshes for palaeontological morphometrics. I first saw this method applied in SPHARM-MAT of Styner (2006)<br>
<a href="http://www.iu.edu/~spharm/SPHARM-docs/C03_Spherical_Parameterization.html#exercise-3-1-surface-meshes-cald" class="onebox" target="_blank" rel="nofollow noopener">http://www.iu.edu/~spharm/SPHARM-docs/C03_Spherical_Parameterization.html#exercise-3-1-surface-meshes-cald</a><br>
I’m not sure if this is a related project, but seems to do very similar things.</p>
<p>I think that my mesh format is an issue for the first step (Post Process Segmentation) as it isn’t voxel data.<br>
Is the surface mesh in step 2 triangular? If so I could maybe use command line control to skip the first step and the rest might work?</p>
<p>SPHARM-PDM can take vtp files as an input, and I think I found a way to convert my stl data to this format. Would this produce the right type of data for this process?</p>
<p>Thank you for your help<br>
Fiona</p>

---

## Post #2 by @styner (2019-05-27 14:01 UTC)

<p>SPHARM-MAT (by Li Shen) and our SPHARM-PDM is very similar and is based on the same underlying principles. The implementations are different and data does not easily mix in the middle of processing, though final processed data have some commonalities.</p>
<p>If you want to use SlicerSALT (and its SPHARM-PDM/Shape Analysis Module) in your setting, you can definitely do so. The pipeline cannot directly use your triangulation as it needs to be converted to a specific style of triangulation (which has an expected connectivity that is needed in the parametrization/optimization process). A SlicerSALT based analysis would thus first convert your triangulation back to high res voxel-data (the resolution can be adjusted if necessary) and then the desired style of triangulation is generated from that voxel data.</p>
<p>So, you can use SlicerSALT and its ShapeAnalysisModule (that uses SPHARM-PDM), but you cannot use your surfaces mid-processing, but rather have to start with your surfaces as input to the module (I think STL should be fine as it can be read by SlicerSALT).</p>
<p>Martin</p>

---

## Post #3 by @muratmaga (2019-05-27 14:49 UTC)

<p><a class="mention" href="/u/fiona_pye">@Fiona_Pye</a> keep in mind that the methods that generate correspondence between structures automatically (whether SPHARM based or not) are typically developed and applied in context of high N of a single species. If you are working with highly morphologically disparate groups, you may initially want to take a critical view of the results.</p>
<p>Having said that, if establishing biological homology is not a strong constraint in your analysis, they may work well.</p>

---

## Post #4 by @styner (2019-05-27 15:14 UTC)

<p>That’s correct. I would add that even with an analysis of very similarly shaped structures (such as is the case in neuroimaging studies), one should perform a quality assessment of the established correspondence too.</p>
<p>If you run into correspondence issues, SlicerSALT allows you to define fiducials on the surfaces to help with that.</p>
<p>Best<br>
Martin</p>

---

## Post #5 by @Fiona_Pye (2019-05-29 14:14 UTC)

<p>Hi <a class="mention" href="/u/styner">@styner</a> and <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>Thank you for your fast and helpful responses, I really appreciate it.<br>
So sorry for getting my references mixed up!</p>
<p>I can open STL files in SlicerSalt, however I have not found a way to convert to VTP within it.  I managed to convert the STL to VTP in ParaView so hopefully this will be okay (it did start to run in the ShapeAnalysisModule)</p>
<p>My scans are very high resolution, each having between 2.5 million and 12 million polygons. It says in the instruction manual that the sphere and resulting meshes have 1002 points. Will the module simplify my models down to this level, or should I adjust the resolution first?</p>
<p>Unfortunately I don’t have a huge number of specimens but I am not searching for biological homology. I would like to compare the different shapes of the fossils and see if these distinctions can be used to identify them.</p>
<p>Thanks again for all of your help<br>
Best wishes<br>
Fiona</p>

---

## Post #6 by @styner (2019-05-29 16:14 UTC)

<p>You can modify the reconstruction level (default is icosahedron subdivision level 10, which translates to 1002 vertices). Though increasing the subdivision level to reconstruct millions of vertices is probably not advisable (regarding computation time and memory requirement).</p>
<p>Re homology: you need to establish correspondence to compare the shape of your fossils. The simplest way to establish this is via closest point correspondence. That is sufficient if simply want to compare differences on a pair-wise basis, but not for populations of data. Then you need something more sophisticated (such as provided by SPHARM-PDM). Do you have 1 specimen per fossil and look for differences between individual fossils, or rather small groups of fossils and look for differences between the groups?</p>
<p>Also: what type of fossils are you looking at? Are the surfaces simply connected or do they have holes/handles?</p>
<p>Martin</p>

---

## Post #7 by @Fiona_Pye (2019-05-30 13:26 UTC)

<p>Hi Martin,</p>
<p>My access to powerful computers is very limited, so I need to keep it as low demand as possible. Hopefully level 10 will be sufficient!</p>
<p>I am studying conodonts, they are basically the teeth of the first vertebrate and have a cone shape (<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7a136c6a1a8abad37254ff18b854e645dd6075.png" data-download-href="/uploads/short-url/fLk4dMoSB0FcsPeswuN68TbemIl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7a136c6a1a8abad37254ff18b854e645dd6075_2_690x387.png" alt="image" data-base62-sha1="fLk4dMoSB0FcsPeswuN68TbemIl" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7a136c6a1a8abad37254ff18b854e645dd6075_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7a136c6a1a8abad37254ff18b854e645dd6075_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7a136c6a1a8abad37254ff18b854e645dd6075.png 2x" data-dominant-color="C5CBDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>. They are very simple in shape, so classical landmark analysis style morphometrics isn’t great for them. They don’t have any holes or anything, so yes they are simply connected.</p>
<p>I have one fossil of each tooth type (7 total) from one species and am hoping to find differences between these. The total comparison, along with the spherical harmonics is why I am really interested in SPHARM-PDM. If this works, it could be extended to include other species (where then homology will play a part) or looking at differences between small groups of fossils.</p>
<p>Thanks again<br>
Fiona</p>

---

## Post #8 by @muratmaga (2019-05-30 17:01 UTC)

<p>These are fairly simple shapes. Perhaps you can reduce your meshes to quite a bit and give slicer-salt a try. Surface toolbox in Slicer has tools (decimation, smoothing etc) that might be useful for you.</p>

---

## Post #9 by @Fiona_Pye (2019-05-31 11:08 UTC)

<p>Hi Murat and Martin,</p>
<p>The surface toolbox is amazing for reducing my meshes, thank you very much!<br>
However, the post process segmentation of SPHARM-PDM just won’t accept my meshes. I read in the forum somewhere that the mesh to label map only works with dense meshes, so this might be the issue with my STL files.</p>
<p>As an alternative I am importing the TIFF files and segmenting, to produce a label map volume as an nrrd file (with the ends definitely sealed off so I have a truly solid surface) and the Shape Analysis Module now runs until the end of step two, where it produces the para.vtk and surf.vtk and then it stops with errors. It seems to be this bug which has been previously noted <a href="https://github.com/Kitware/SlicerSALT/issues/138" rel="nofollow noopener">https://github.com/Kitware/SlicerSALT/issues/138</a><br>
I will try to get a computer with Linux to get around this.</p>
<p>Thanks again for all of your help,<br>
Fiona</p>

---

## Post #10 by @styner (2019-05-31 12:49 UTC)

<p>Hi Fiona,<br>
comments/ questions:</p>
<ol>
<li>
<p>which version of Slicer Salt are you running, which platform?</p>
</li>
<li>
<p>are you running the SPHARM shape analysis module, or rather the individual steps (e.g the SegPostProcess module) separately?</p>
</li>
<li>
<p>if you are having problems with surface to label conversion, you can run that separately and (use Mesh to Label Map module).</p>
</li>
<li>
<p>what is the error that you are getting when running it on the labelmaps that you generated from the TIFF files? Did you load the surf.vtk file into Slicer and see whether the surface looks okay?</p>
</li>
<li>
<p>with respect to your shape, best play around with the settings for the surface reconstruction (subdivision and SPHARM degree) to make sure you get a reasonable reconstruction.</p>
</li>
</ol>
<p>Martin</p>

---

## Post #11 by @Fiona_Pye (2019-05-31 15:04 UTC)

<p>Hi Martin,</p>
<ol>
<li>
<p>I am running SlicerSalt for Windows (on Windows 10) from the executable file. I also have the most recent version of full slicer with SPHARM-PDM installed.</p>
</li>
<li>
<p>I have been running the ShapeAnalysis module as a whole to see how far it gets. I will try doing it piece by piece.</p>
</li>
<li>
<p>I will have a look at the Mesh to Label map alone, but I wouldn’t be surprised if the STL files just aren’t suitable.</p>
</li>
<li>
<p>There is no issue with the label maps from the Tiffs, the label map conversion goes nicely and l the surf.vtk looks good. The error came in at step 3 and was an “unknown exception” as described in the other topic.</p>
</li>
<li>
<p>Yeah I can see that this takes a bit of trial and error, once I get it fully running I will try this out.</p>
</li>
</ol>
<p>Thanks again<br>
Fiona</p>

---

## Post #12 by @muratmaga (2019-05-31 15:31 UTC)

<p><a class="mention" href="/u/fiona_pye">@Fiona_Pye</a>, out of curiosity where does your meshes come from? If these are from microCT scans, you can skip the mesh generation step, and use the labelmaps.</p>

---

## Post #13 by @bpaniagua (2019-05-31 15:42 UTC)

<p>Hi Fiona,</p>
<p>I am late to the game, but I see you got fantastic advice from <a class="mention" href="/u/styner">@styner</a> and <a class="mention" href="/u/muratmaga">@muratmaga</a>.<br>
I believe we built in the option in SPHARM to get vtk’s as an input. In order to generate a vtk out of a vtp you can use Paraviews “extract surface” filter.</p>
<p>This SPHARM option just uses a Slicer module that scan converts a surface into a label map, you could try to run it on one of your cases and see how it goes. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MeshToLabelMap" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MeshToLabelMap</a></p>
<p>All the best,<br>
Bea</p>

---

## Post #14 by @Fiona_Pye (2019-06-04 08:37 UTC)

<p>Hi Bea and <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>The STL meshes that I have were generated for a previous study on these fossils. The original scans were acquired at the SLS Synchrotron. The group who did the original study provided me with the TIF files and STL meshes they produced. I don’t think I have labelmaps to start with unfortunately, because that would make life a lot easier!</p>
<p>Can you convert STL into vtk this way? All these file types are new to me, and I don’t know why I went for vtp rather than vtk to start. I will have a look anyway. Also, though my meshes should be a solid surface, they are a bit messy so I think this is also an issue. I haven’t yet worked out a good way to fix this in my meshes (I tried the fill holes thing in MeshLab that someone mentioned), and decided to try generating them as clean as possible as voxel volume data rather than surface meshes. This got me the furthest along the process of anything yet!</p>
<p>Yeah I am not sure what is the issue with this, I will have a look into it.</p>
<p>Thank you for your help<br>
Fiona</p>

---

## Post #15 by @bpaniagua (2019-06-12 17:41 UTC)

<p>Hi Fiona,</p>
<p>Have you tried using MeshToLabelMap?<br>
Converting from STL to VTK is straightforward, but MeshToLabelMap should work with both.</p>
<p>Thanks,<br>
Bea</p>

---

## Post #16 by @Fiona_Pye (2019-06-17 13:51 UTC)

<p>Hi Bea,</p>
<p>So when I input my STL into Mesh to Label Map, it tells me that I have to provide valid spacing information (&gt;0), however for the spacing the auto is -1,-1,-1. Is this error referring to this, or do I need a reference image to run this? If so, I don’t actually understand what kind of reference image is required.</p>
<p>Secondly, a colleague has a Linux computer, and SpharmPDM ran all the way through on newly segmented test samples, so this is good!</p>
<p>Thank you for your help and patience!<br>
Fiona</p>

---

## Post #17 by @bpaniagua (2019-06-18 16:20 UTC)

<p>Hi Fiona,</p>
<p>Yes, I believe you will need a reference image. Do you have any of the original segmentations that you used? If it is the same machine it will keep all the metadata you need to run the module.</p>
<p>Bea</p>

---

## Post #18 by @Fiona_Pye (2019-06-25 13:18 UTC)

<p>Hi Bea,</p>
<p>Do you mean the segmentations which were used to make the STL files? If so, unfortunately not, these were generated about 10 years ago by my supervisor.</p>
<p>A second question, my samples are all different sizes so do I need to standardise for this before I run SPHARM-PDM or does the method ignore/account for size differences and just consider shape?</p>
<p>Thanks<br>
Fiona</p>

---

## Post #19 by @bpaniagua (2019-06-25 19:52 UTC)

<p>Hi Fiona,</p>
<p>Then you will have to create a reference image. You can do that with ITK <a href="https://itk.org/ITKExamples/src/Core/Common/CreateAnImage/Documentation.html" rel="nofollow noopener">https://itk.org/ITKExamples/src/Core/Common/CreateAnImage/Documentation.html</a></p>
<p>What do you mean, different sizes? Can you provide an example?<br>
In general SPHARM-PDM will have the same triangulation scaled as far as there is inherent correspondence.</p>
<p>HTH,<br>
Bea</p>

---

## Post #20 by @Fiona_Pye (2019-06-27 11:00 UTC)

<p>Hi Bea,</p>
<p>Thank you, I will try this out.</p>
<p>So essentially some of specimens are twice the size of others because they all come from different individuals. Would I need to resize them so they are all the correct relative sizes to each other before SPHARM-PDM?</p>
<p>Thanks a lot<br>
Fiona</p>

---

## Post #21 by @styner (2019-06-27 16:44 UTC)

<p>In general, for the processing, the size difference would not matter, as the processing is agnostic to the specific size (and there is no rescaling of the size of objects anywhere).</p>
<p>In your case you just need to make sure you create a reference image that accommodates all your input meshes (independent of their size). Thus, best choose your largest mesh and choose a fine enough sampling to create the reference image.</p>
<p>Martin</p>

---

## Post #22 by @Fiona_Pye (2019-07-05 16:40 UTC)

<p>Hi Martin,</p>
<p>The ends of my specimens are broken, so we are now “cutting” the ends off them using new segmentations in slicer.<br>
Would I still need to create a reference image from the largest specimen, or will my segmentations be okay just run directly in SPHARM-PDM?<br>
Sorry this is a bit confusing, there is a lot here which is new to me!</p>
<p>Secondly for the spherical mapping, Brechenbuehler 1995 says that the first and last vertices which are mapped are the furthest apart in the z axis, so this will be the first and last points in the z stack of the segmentation? Does this mean that you can imagine the centre of sphere to be the centre of the object?</p>
<p>Thank you so much for all your help and patience<br>
I really appreciate it<br>
Fiona</p>

---

## Post #24 by @styner (2019-07-12 16:55 UTC)

<p>If you start with surfaces, rather than segmentation images, you have to first convert the surfaces to binary volumes/images. And for that process you need a reference image. So, yes, you still need it.</p>
<p>Re spherical mapping: those first &amp; last vertices are just used for the initial mapping (basically the south and north pole of the initial spherical parametrization). That parametrization is then updated/optimized to establish an equal-area-ratio mapping. The centre of the sphere (or spherical parametrization is not at the center of the object), but rather it’s a unit sphere (the center is at 0,0,0).</p>
<p>Martin</p>

---

## Post #25 by @Fiona_Pye (2019-08-19 11:09 UTC)

<p>Hi Martin,</p>
<p>Thank you very much for the clarification. I am finally producing really nice models and I am very happy with these. Thanks again for all of your help (and sorry for the slow reply!)</p>
<p>Fiona</p>

---
