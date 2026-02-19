---
topic_id: 31398
title: "Run Shape Analysis Runtime Indefinite"
date: 2023-08-28
url: https://discourse.slicer.org/t/31398
---

# Run shape analysis runtime indefinite

**Topic ID**: 31398
**Date**: 2023-08-28
**URL**: https://discourse.slicer.org/t/run-shape-analysis-runtime-indefinite/31398

---

## Post #1 by @pkashya (2023-08-28 10:27 UTC)

<p>Hi,</p>
<p>I’m running the shape analysis module on a hippocampus segmentation mask (<em>.vtk/</em>.nii/*.nrrd) and it does not seem to complete for some reason. I’m following the steps on the documentation (<a href="https://docs.google.com/presentation/d/1ycQyH7THwjlwe7PTaEwhKAOt0FbFrsrfo93Zn1wcc3E/edit#slide=id.p48" class="inline-onebox" rel="noopener nofollow ugc">SlicerSALT-SPHARM-PDM-Tutorial - Google Slides</a>). Please let me know if there is something I am missing.</p>
<p>Thanks,</p>

---

## Post #2 by @bpaniagua (2023-08-29 13:49 UTC)

<p>Hi,</p>
<p>Here are some pointers:</p>
<ol>
<li>Check the <a href="https://slicer.readthedocs.io/en/v4.11/user_guide/get_help.html">error log</a>. View → Error Log</li>
<li>Check your output folder, has any output data been created?</li>
<li>SPHARM-PDM can check that the topology is spherical, and through an error message out if its not. If the segmentation has an almost-hole (close to closed C-shape boundary) it will run and fail. This will be by either running forever or by causing numeric singularities. You can inspect the 3D shape of your segmentation by generating a 3D model in slicer (ModelMaker Module) and inspecting it in the 3D view. You can correct your segmentations with the Segment Editor Module. I would be happy to have a look if you screenshot your segmentations.</li>
</ol>
<p>Let us know how it goes after you try these few things.<br>
Thank you for using SALT!</p>
<p>Bea</p>

---

## Post #3 by @anasmh101 (2024-01-17 04:11 UTC)

<p>Hello, I have frustrating problem in using shape analysis module, in cases it works well with no issues, but in several cases I got error output models ( flipped models) as shown in screenshot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b.png" data-download-href="/uploads/short-url/4dTtefRTyaAa1JIsXQQMDiwKNWX.png?dl=1" title="shape analysis error2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b_2_690x281.png" alt="shape analysis error2" data-base62-sha1="4dTtefRTyaAa1JIsXQQMDiwKNWX" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b_2_1035x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b.png 2x" data-dominant-color="402F3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">shape analysis error2</span><span class="informations">1127×460 90.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
at first, I was using Windows version of slicer and did segmentations and the shape analysis, it worked well with no problems for some cases but now it always ends up with error<br>
then I shifted to MacOS version and made the segmentations from scratch and did the shape analysis using MacBook, the shape analysis worked well for certain cases at the beginning, but later for other CBCTs it ends up with same issue.</p>
<p>Now after reading your comment on using model maker module to fix segmentations, I applied your advice. but again the shape analysis module worked well for certain segmentations, but for other segmentations it ends up with flipped models.</p>
<p>can you please assist me in this issue ?</p>

---

## Post #4 by @styner (2024-01-19 02:47 UTC)

<p>Hi, SPHARM-PDM uses a first-order ellipsoid fit to determine parameter space alignment, and this is where a flip can come in if the structure has some rotational symmetry (which is the case for your condyles). This happens independently of the operating system.</p>
<p>The SlicerSALT module allows you to manually flip the parameter space following the SPHARM-PDM computation (dubbed final flip) if you encounter such flips. If you open the “Advanced Parameter to SPHARM-Mesh” section of the SPHARM-PDM Generator module, you can choose a Flip Option (you often need to try multiple times until you get the right option as it depends on the orientation of the original image, in the case of your screenshot it is likely flip along x and z, if the original image was in RAI orientation).</p>
<p>Hope this helps<br>
Martin</p>

---

## Post #5 by @anasmh101 (2024-01-19 14:08 UTC)

<p>Thank you so much for your reply I really appreciate your help . it works now, I have been stuck in this issue for long</p>

---
