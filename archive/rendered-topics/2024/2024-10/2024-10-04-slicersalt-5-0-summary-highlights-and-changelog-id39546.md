---
topic_id: 39546
title: "Slicersalt 5 0 Summary Highlights And Changelog"
date: 2024-10-04
url: https://discourse.slicer.org/t/39546
---

# SlicerSALT 5.0: Summary, Highlights and Changelog

**Topic ID**: 39546
**Date**: 2024-10-04
**URL**: https://discourse.slicer.org/t/slicersalt-5-0-summary-highlights-and-changelog/39546

---

## Post #1 by @bpaniagua (2024-10-04 21:13 UTC)

<p>The SlicerSALT team is proud to announce that version 5.0 is <a href="http://salt.slicer.org/download">now available for download</a>. This release introduces new features as well as bug fixes for better performance and stability. This release of SlicerSALT includes a lot of features that concentrate in the visualization and analysis of sequential, 3D geometries (4D shape analysis). The development of SlicerSALT is supported by the NIH National Institute of Biomedical Imaging Bioengineering <a href="https://projectreporter.nih.gov/project_info_description.cfm?aid=9741133&amp;icde=46482797&amp;ddparam=&amp;ddvalue=&amp;ddsub=&amp;cr=3&amp;csb=default&amp;cs=ASC&amp;pball=">R01EB021391</a> (Shape Analysis Toolbox for Medical Image Computing Projects).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/362c1fa4f8f597687bdcf8e7481fcaf7878c3e78.jpeg" data-download-href="/uploads/short-url/7JejHDNTo3im3mR3b9UPSdq3BwY.jpeg?dl=1" title="IMG_0125"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/362c1fa4f8f597687bdcf8e7481fcaf7878c3e78_2_690x442.jpeg" alt="IMG_0125" data-base62-sha1="7JejHDNTo3im3mR3b9UPSdq3BwY" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/362c1fa4f8f597687bdcf8e7481fcaf7878c3e78_2_690x442.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/362c1fa4f8f597687bdcf8e7481fcaf7878c3e78_2_1035x663.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/362c1fa4f8f597687bdcf8e7481fcaf7878c3e78_2_1380x884.jpeg 2x" data-dominant-color="8C8D9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0125</span><span class="informations">1872×1201 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em>Shape Population Viewer module’s enhanced functionality for the visualization of 4D shapes. The user only needs to provide a folder containing meshes of the 4D objects, both boundary or skeletal representations. SPV’s interface includes controls that help animate through the sequence of 3D geometries.</em></p>
<p><strong>Changelog</strong></p>
<p><strong>Features</strong></p>
<p><a href="https://github.com/KitwareMedical/HierarchicalGeodesicModeling">Hierarchical Geodesic Modeling module</a>, for the computation and visualization/analysis of longitudinal shape models using geodesic based shape modeling.</p>
<p><a href="https://github.com/slicersalt/SRepHypothesisTesting/">S-rep Hypothesis Testing module</a>, for the calculation of hypothesis testing specially designed for the richer geometry captured by S-reps.</p>
<p><a href="https://github.com/mturja-vf-ic-bd/SlicerSurfaceLearner">Surface Learner module</a>, for the application of Deep Learning-based Image Classifiers on surface data without any coding.</p>
<p>Updated functionality in our <a href="https://github.com/KitwareMedical/SlicerSkeletalRepresentation">Skeletal Representation modules</a>, now including a way to serialize the computation of s-reps in a large dataset via the <a href="https://github.com/KitwareMedical/SlicerPipelines">SlicerPipelines functionality</a>.</p>
<p>Updated functionality in <a href="https://github.com/slicersalt/ShapePopulationViewer">Shape Population Viewer</a>, that allows the visualization of 4D geometries.</p>
<p><strong>Fixes</strong></p>
<p>Updates to the <a href="https://github.com/slicersalt/RegistrationBasedCorrespondence">Registration Based Correspondence module</a>, that now includes a way to customize the number of iterations needed for the correspondence establishment.</p>
<p>Crash fixes and stability</p>
<p>Fixes to windows packaging</p>
<p>Deprecation of Fortran and LAPACK</p>
<p>Fixes to GROUPS for SPHARM correspondence optimization</p>

---

## Post #2 by @lili-yu22 (2024-12-25 01:17 UTC)

<p>when I open a mesh.then open it’s fiducial in the shapepopulationviewer , the slicersalt 5.0 crash.how I can put the fiducial on the mesh in the shapepopulationviewer like the picture2.please help me<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c.jpeg" data-download-href="/uploads/short-url/zr8Nb8qjCQgjxK7kQ1Em401BBgg.jpeg?dl=1" title="IMG_20241220_155543_edit_8092433669597" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_384x500.jpeg" alt="IMG_20241220_155543_edit_8092433669597" data-base62-sha1="zr8Nb8qjCQgjxK7kQ1Em401BBgg" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_384x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_576x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_768x1000.jpeg 2x" data-dominant-color="B7B9B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20241220_155543_edit_8092433669597</span><span class="informations">1920×2498 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab.jpeg" data-download-href="/uploads/short-url/dntM9EZp7SmipvPReYz4hw0bHcL.jpeg?dl=1" title="Screenshot_20241219_151735_edit_56383804812228" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_690x493.jpeg" alt="Screenshot_20241219_151735_edit_56383804812228" data-base62-sha1="dntM9EZp7SmipvPReYz4hw0bHcL" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dc3bd8d5e802e3ae1afc5166cf4b61a011462ab_2_1380x986.jpeg 2x" data-dominant-color="ACBCB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20241219_151735_edit_56383804812228</span><span class="informations">1600×1144 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lili-yu22 (2024-12-27 01:04 UTC)

<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> please help me to explain the question</p>

---

## Post #4 by @bpaniagua (2025-05-05 12:40 UTC)

<p>Hi <a class="mention" href="/u/lili-yu22">@lili-yu22</a> how do you compute the mesh that you open as fiducials in SPV? Could you provide more details about what module generated that data within SlicerSALT?</p>

---

## Post #5 by @lili-yu22 (2025-05-05 13:51 UTC)

<p>the  mesh computed from  SPHARM—PDM Generator.when I load the spharm.vtk.then import fiducial files  which contain landmarks.every  mesh have sample _fid.fscv.but  I cant through above pictures getting the following pictures.thanks</p>

---

## Post #6 by @bpaniagua (2025-05-05 14:03 UTC)

<p>Can you take snapshots of the spharm mesh and the fiducials?</p>
<p>Assuming that when you say “load” you mean in SPV.</p>
<p>What are the “above pictures”? Do you mean the instructions in the tutorial?</p>

---

## Post #7 by @lili-yu22 (2025-05-05 14:53 UTC)

<p>I load the condyle mesh(spharm.vtk) in the SPV.then I open Fiducial files like the  picture 1.I thought I would get the figure I circled and marked in Picture 2, but I didn’t.My Fiducial files contain the landmark as I am presenting now<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3fde64eb1edadab73022171117f91dfbb0f2653.jpeg" data-download-href="/uploads/short-url/pGhrzkTaEwALHFaAtQZa3faesAr.jpeg?dl=1" title="IMG_20250505_224733" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3fde64eb1edadab73022171117f91dfbb0f2653_2_375x500.jpeg" alt="IMG_20250505_224733" data-base62-sha1="pGhrzkTaEwALHFaAtQZa3faesAr" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3fde64eb1edadab73022171117f91dfbb0f2653_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3fde64eb1edadab73022171117f91dfbb0f2653_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3fde64eb1edadab73022171117f91dfbb0f2653_2_750x1000.jpeg 2x" data-dominant-color="50535A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20250505_224733</span><span class="informations">1920×2560 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @bpaniagua (2025-05-05 15:12 UTC)

<p>The only thing that is missing from the second picture you shared from the tutorials is the coloring of your geometry. Is this what you mean? Also, you are showing the 3D view of the Slicer interface, not SPV. Please, correct me if I am wrong!</p>

---

## Post #9 by @lili-yu22 (2025-05-07 00:53 UTC)

<p>no，when I open a mesh *spharm.vtk in SPV then open it’s fiducia like the picture in 3D view of the Slicer interface,then the slicersalt 5.0 crash.why I can’t load fiducial in the SPVlike the second picture i shared from the tutorials .thanks</p>

---

## Post #10 by @bpaniagua (2025-05-19 12:36 UTC)

<p>Could you please show us what your data looks like in SPV? Thank you!</p>

---

## Post #11 by @lili-yu22 (2025-05-21 02:13 UTC)

<p>my fiducial files is the picture,when I choose open Fiducial files in the SPV,the slicersalt crash<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddb361161b891cfa7b691eb9685ad56537cf9eca.jpeg" data-download-href="/uploads/short-url/vDfQ1Z5MfkEcMcq5cYoaqISxZ6a.jpeg?dl=1" title="IMG_20250521_100953_edit_9008256255396" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddb361161b891cfa7b691eb9685ad56537cf9eca_2_645x499.jpeg" alt="IMG_20250521_100953_edit_9008256255396" data-base62-sha1="vDfQ1Z5MfkEcMcq5cYoaqISxZ6a" width="645" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddb361161b891cfa7b691eb9685ad56537cf9eca_2_645x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddb361161b891cfa7b691eb9685ad56537cf9eca_2_967x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddb361161b891cfa7b691eb9685ad56537cf9eca_2_1290x998.jpeg 2x" data-dominant-color="4E4B4A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20250521_100953_edit_9008256255396</span><span class="informations">1920×1488 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
