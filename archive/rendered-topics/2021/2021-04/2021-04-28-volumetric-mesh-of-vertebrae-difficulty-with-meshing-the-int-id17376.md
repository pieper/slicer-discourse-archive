---
topic_id: 17376
title: "Volumetric Mesh Of Vertebrae Difficulty With Meshing The Int"
date: 2021-04-28
url: https://discourse.slicer.org/t/17376
---

# Volumetric mesh of vertebrae - difficulty with meshing the interior

**Topic ID**: 17376
**Date**: 2021-04-28
**URL**: https://discourse.slicer.org/t/volumetric-mesh-of-vertebrae-difficulty-with-meshing-the-interior/17376

---

## Post #1 by @michxu98 (2021-04-28 21:09 UTC)

<p>Hello,</p>
<p>I am trying to obtain a volumetric mesh of a single vertebrae from a segmentation as seen here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/175b07c25253ccba8a72dd5df975c0a306ef1051.jpeg" data-download-href="/uploads/short-url/3kC0Pluep9ZgveM0DrhEmbF4wpP.jpeg?dl=1" title="Screenshot from 2021-04-27 13-57-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175b07c25253ccba8a72dd5df975c0a306ef1051_2_552x500.jpeg" alt="Screenshot from 2021-04-27 13-57-53" data-base62-sha1="3kC0Pluep9ZgveM0DrhEmbF4wpP" width="552" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175b07c25253ccba8a72dd5df975c0a306ef1051_2_552x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175b07c25253ccba8a72dd5df975c0a306ef1051_2_828x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/175b07c25253ccba8a72dd5df975c0a306ef1051_2_1104x1000.jpeg 2x" data-dominant-color="555054"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-04-27 13-57-53</span><span class="informations">2134×1932 594 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have separated one vertebrae into its own segmentation by copying the segment from the main segmentation.</p>
<p>So far I have been able to generate a volumetric mesh with in segment mesher with cleaver but it looks like the interior volumes are not being meshed correctly and the cortex is very thick:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a82330c977f581bcb1db8e849f37e39c257fff5b.jpeg" data-download-href="/uploads/short-url/nZpBQJxOBYkjNikqFWA4FbIroSv.jpeg?dl=1" title="Screenshot from 2021-04-28 12-13-29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a82330c977f581bcb1db8e849f37e39c257fff5b_2_690x463.jpeg" alt="Screenshot from 2021-04-28 12-13-29" data-base62-sha1="nZpBQJxOBYkjNikqFWA4FbIroSv" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a82330c977f581bcb1db8e849f37e39c257fff5b_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a82330c977f581bcb1db8e849f37e39c257fff5b_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a82330c977f581bcb1db8e849f37e39c257fff5b.jpeg 2x" data-dominant-color="D9D8D5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-04-28 12-13-29</span><span class="informations">1352×908 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I exported an stl file containing the surface mesh and used a clip in paraview to show the interior regions that are missing:</p>
<p>(the purple is the surface mesh and the grey is the volumetric mesh)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeee16fd314a425ef85a08d3f7fc1ecdf79bc2e1.jpeg" data-download-href="/uploads/short-url/y5FK48K1mmbPj4OYwfdDJ5tDAYh.jpeg?dl=1" title="Screenshot from 2021-04-28 12-14-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eeee16fd314a425ef85a08d3f7fc1ecdf79bc2e1_2_690x499.jpeg" alt="Screenshot from 2021-04-28 12-14-27" data-base62-sha1="y5FK48K1mmbPj4OYwfdDJ5tDAYh" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eeee16fd314a425ef85a08d3f7fc1ecdf79bc2e1_2_690x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eeee16fd314a425ef85a08d3f7fc1ecdf79bc2e1_2_1035x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeee16fd314a425ef85a08d3f7fc1ecdf79bc2e1.jpeg 2x" data-dominant-color="C9C1D2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-04-28 12-14-27</span><span class="informations">1282×928 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Would appreciate any advice on how to best preserve the structure for the volume mesh. Thanks!</p>
<p>Slicer version: 4.11.20210226</p>

---

## Post #2 by @lassoan (2021-04-28 23:05 UTC)

<p>In most cases, you can fill internal holes in a segment using Wrap Solidify effect (provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">SurfaceWrapSolidify extension</a>). This tool can deal with quite complex shapes, but each vertebra has a hole in it and the effect cannot deal with that. So, you have to split the segment into two along either coronal or sagittal axis, solidify each, then merge them into one segment again. This should work if you only need to solidify a few verteabrae.</p>
<p>If you need to segment many vertebrae then splitting&amp;mergin each could be tedious. In this case, you can segment the spine so that you don’t have internal holes in the first place. You can achieve this by using Grow from seeds effect. If you paint seeds inside the bone then the hypodense regions in the bone will be filled, too.</p>

---

## Post #3 by @Ron (2021-04-29 00:56 UTC)

<p>Andras hi</p>
<p>Let me add some details to Michelle’s post.  The spine was segmented using grow from seed module, which works remarkably well. For the segmentation, the volume is cropped and created as isotropic 0.3125^3, prior to using grow from seed.  These are cancer spines, thus requiring hours of fixing due to lack of resolution (0.3125^2 by 0.6-1.5) resulting in the need to separate the facet joints, destroyed geometry etc.<br>
One of the problems that we are facing is that the spines are highly lytic with the cancellous bone often having a range of 50-150 HU, being remarkably low, and close to the discs (40-115) or tumor tissue and even the muscle tissue.  I have found that setting the threshold to about 150 allows the module to perform a good initial segmentation of the geometry with the set up of seed locality to 6.5-7.5 up to 9 to maintain the bleed-out to the surrounding discs, tissue to a minimum. As a result, the cancellous bone within the vertebral geometry is not fully captured, as can be seen on the segment masks.<br>
I have used wrap solidify with the threshold set to 0 and (outer surface, carve-hole at 7mm) to fully segment the vertebra, as can be seen on the image.  The resulting model created seems to yield a surface mesh<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b2b1e4db94f32844e3465c5e0096257ca0c7b60.jpeg" data-download-href="/uploads/short-url/fi3t8MDcNAc7pwHdznxJrP3Q2Vq.jpeg?dl=1" title="13693-L1 mask with wrap model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b2b1e4db94f32844e3465c5e0096257ca0c7b60_2_676x500.jpeg" alt="13693-L1 mask with wrap model" data-base62-sha1="fi3t8MDcNAc7pwHdznxJrP3Q2Vq" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b2b1e4db94f32844e3465c5e0096257ca0c7b60_2_676x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b2b1e4db94f32844e3465c5e0096257ca0c7b60_2_1014x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b2b1e4db94f32844e3465c5e0096257ca0c7b60_2_1352x1000.jpeg 2x" data-dominant-color="544E58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">13693-L1 mask with wrap model</span><span class="informations">2464×1820 493 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>.<br>
This is one of the models that we are trying to use as the input for the meshing.  I am not sure what parameter I am missing in oredr to get the volume model from this module.<br>
As we are trying to figure out the pipeline (CT-FEA), how best should we proceed to allow us to apply segment mesher for creating the volumetric tet mesh?  How do we apply material models?</p>
<p>Thank you for your consideration, Ron</p>

---

## Post #4 by @lassoan (2021-04-29 01:13 UTC)

<p>Once you have the solidified (and merged) segment, you can use SegmentMesher module to create a volumetric mesh. Or export as a surface mesh and use <a href="https://discourse.slicer.org/t/meshing-self-intersecting-faces/13588/2">any other mesher</a>.</p>
<p>You can specify material models, loads, boundary conditions, etc. in the preprocessor of your solver. If it helps, you can save the CT density values at each mesh point using “Probe volume with model” module.</p>
<p>People have asked about vertebral FEM modeling many times on this forum, but unfortunately we did not get much updates form them later, so we don’t know what workflow they ended up implementing - but a few tips:</p>
<ul>
<li>Not many FEM tool can read VTK unstructured grids, but FEBio/FEBio Studio can, and it is free and works quite nicely for biomedical applications.</li>
<li>If you want to use SegmentMesher output in software that cannot read VTK unstructured grid files then you can use meshio Python package to convert to other formats.</li>
</ul>

---

## Post #5 by @Ron (2021-04-29 01:25 UTC)

<p>Andras</p>
<p>Thanks you for the very quick reply.  A we will be more than happy to update the community.  We have at present 45 spines segmented with each one having/will have multiple follow up scanning, 3, 6, 9, 12M.</p>
<p>We have many vertebra’s to do / per spine as we are looking at the effect of cancer on vertebral strength. So the split/ merge approach may not work. If I try to use values lower than 150 for the grow from seed, than the whole volume (entire torso) get painted.  Would it be possible to run a second segmentation within the bounds of the initial segmentation with a lower seed value to solve this problem?</p>
<p>Its a lot of work, but I look at this as the hard road to get true labeled model for development of AI approach, we expect to have 430 spines * 4 time points.</p>
<p>Ron</p>

---

## Post #6 by @Ron (2021-04-29 01:40 UTC)

<p>Andras</p>
<p>I  think I may have somewhat “hijacked” Michelle original question regarding the thick cortex at the vertebral body, being much greater then what we are able to visualize on the CT, Ron</p>

---

## Post #7 by @lassoan (2021-04-29 02:09 UTC)

<p>If you have already spent a lot of time with segmenting the vertebrae then splitting, solidifying/merging should be less work than segmenting again. You can fully automate the process by Python scripting.</p>
<aside class="quote no-group" data-username="Ron" data-post="5" data-topic="17376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>If I try to use values lower than 150 for the grow from seed, than the whole volume (entire torso) get painted</p>
</blockquote>
</aside>
<p>This is the expected behavior. You can add an “other” segment that contains seeds outside the vertebrae. You can remove any leaks by painting this “other” segment nearby. You can even use Grow from seeds if there is not contrast difference, you just need to paint more seeds (and always paint seeds both sides of places where no intensity difference exists but you still want to have a contour).</p>
<aside class="quote no-group" data-username="Ron" data-post="5" data-topic="17376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>we expect to have 430 spines * 4 time points</p>
</blockquote>
</aside>
<p>This is a large number, so it may make sense to spend some time experimenting with various methods and automate things as much as possible using Python scripting. For segmenting a new time point of the same patient, you may utilize image registration (e.g., SlicerElastix).</p>
<aside class="quote no-group" data-username="Ron" data-post="6" data-topic="17376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>original question regarding the thick cortex at the vertebral body</p>
</blockquote>
</aside>
<p>You can make the volumetric mesh resolution very fine to capture arbitrarily small details, but since this would lead to very large and complex meshes, most commonly you create a simple mesh and just vary material properties across the mesh.</p>

---

## Post #8 by @Ron (2021-04-29 02:22 UTC)

<p>Andras</p>
<p>Alas, I do not know how to program in python.  I believe Michelle does. May I trouble you to help Michelle in this regard?</p>
<p>I will try this approach.</p>
<p>Yes, we fully expect to have to get to registration at a later stage of the project, thanks for the initial direction.</p>
<p>We may have to go down this route as vertebral mechanics is very sensitive to cortex thickness and the picture gets much more complicated once we deal with vertebrae with mixed lesions (Breast, Lung, and Prostate) or osteosclerotic (Breast, Prostate) for which the association between bone material and architecture starts to break down.  Some of these bone have up to 90% bone volume vs the normal 10-15%</p>
<p>Ron</p>

---

## Post #9 by @Ron (2021-04-29 03:06 UTC)

<p>Andras</p>
<p>one quick Q.  how do you split and merge?</p>

---

## Post #10 by @lassoan (2021-04-30 02:49 UTC)

<p>You can split using any of the effects with masking option. See an example in the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">craniotomy segmentation recipe</a>.</p>

---

## Post #11 by @Ron (2021-04-30 17:01 UTC)

<p>Andras<br>
Thank you for your response. As you may see, in collaboration with MIT, we are trying to establish the pipeline for segmenting the cancer spines ( both at radiation planning and longitudinal follow-up) and converting the multi vertebral segmentation to FE.  We will include discs models later with the hope of incorporating DTI-to FE-based models as well as muscle-based models.  I have used MIMCS, TruGrid, ABAQUS to do portions of the pipeline but never to this scale.  I would very much like to try and use Slicer for this development, not only for the issue of cost but as a platform to develop tools for clinical for better management of these very infirm patients. We have multiple questions regarding the imaging and development of code to carry out operations on the image data ( how best to reslice the vertebrae for analytical computation of strength) establishing AI / Atlas-based approaches for segmentation.  My question is it worth opening a topic for the spine?  I will welcome any interest in collaboration on this project.  alternatively we can just post issues as they arise.  thanks</p>

---

## Post #12 by @lassoan (2021-04-30 18:59 UTC)

<p>We can continue the discussion here but it is probably more clear if you create a new topic for each specific question you have. You can also join one of the <a href="https://discourse.slicer.org/c/community/hangout/20">weekly Slicer teleconferences</a> to discuss in person.</p>
<p><a class="mention" href="/u/michael_hardisty">@Michael_Hardisty</a> could also have some useful inputs, as they did quite a bit of work on this topic using Slicer.</p>

---

## Post #13 by @pieper (2021-04-30 19:19 UTC)

<p>This sounds like a very interesting project and I hope Slicer becomes a useful part of your workflows. If you end up wanting to develop and disseminate a customized set of tools for this problem domain, such as a SlicerSpine extension, we could also create a top level Slicer Community like we have for SlicerHeart, SlicerDMRI, etc.</p>

---
