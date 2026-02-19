---
topic_id: 45467
title: "Interpreting Ants Registration Warp Field Directionality"
date: 2025-12-13
url: https://discourse.slicer.org/t/45467
---

# Interpreting ANTs registration warp field directionality

**Topic ID**: 45467
**Date**: 2025-12-13
**URL**: https://discourse.slicer.org/t/interpreting-ants-registration-warp-field-directionality/45467

---

## Post #1 by @lucinda (2025-12-13 17:01 UTC)

<p>Hi! I am aiming to use 3DSlicer to visualize the effects of 3d transforms created with antsRegistration. The registration didn’t include any rigid or affine stages, just one SyN stage. I’ve confirmed that the forward and inverse transform .mat files are identity transforms. I know that the actual displacements in the forward and inverse warp nifti files are the reverse of the “intuition” in antsApplyTransforms. Specifically, the movingToFixedWarp.nii.gz is defined in the Fixed image space with the displacements pointing to each voxels corresponding location in the moving image. I noticed when loading the moving image as the background and overlaying the movingToFixed transform that arrows correspond to my intuition of how that transform affects the moving image, _not_ how the vectors exist in the warp file. Is it correct to interpret the glyph arrows as indicating the intuitive direction that “moving” is deformed to match “fixed”? Thanks for any insight!</p>

---

## Post #2 by @lassoan (2025-12-13 18:03 UTC)

<p>Arrows that are shown if you visualize using Transforms module’s Display section show the transformation from the transformed coordinate system to the parent coordinate system. This is also known as “to parent” transform or “modeling” transform.</p>
<p>There is a small but important technical detail that for transforming images you actually need to be able to compute the inverse of the “to parent” transform, i.e., “from parent” or “resampling” transform.</p>
<p>Slicer (using VTK) can compute the inverse transform on the fly, so it does not matter if you have a modeling or resampling transform, you can use them in Slicer to transform any objects (images, models, markups, etc.).</p>
<p>To make the nomenclature clear and how it appears in Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/708d66ad35d6972ea55455c08085f8e9075433d3.png" data-download-href="/uploads/short-url/g3GqtNNK8ol9D23AB6lsZ3kWsxl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/708d66ad35d6972ea55455c08085f8e9075433d3_2_690x300.png" alt="image" data-base62-sha1="g3GqtNNK8ol9D23AB6lsZ3kWsxl" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/708d66ad35d6972ea55455c08085f8e9075433d3_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/708d66ad35d6972ea55455c08085f8e9075433d3_2_1035x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/708d66ad35d6972ea55455c08085f8e9075433d3_2_1380x600.png 2x" data-dominant-color="D4E6EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2428×1058 290 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>Is it correct to interpret the glyph arrows as indicating the intuitive direction that “moving” is deformed to match “fixed”?</p>
</blockquote>
<p>Yes. Due to origins of ITK (it was born as an image registration toolkit), when it writes a transform to file, it is the resampling (a.k. “from parent”) transform. Slicer knows this, and it interprets ITK transform files and displacement field files as such. ITK transform files should have a flag that specifies if the transform is “modeling” or “resampling” instead of just assuming it is always “resampling”, but ITK developers did not or could not implement this.</p>
<p>General-purpose software, such as Slicer must be able to store transform in either directions (because inversion may be computationally expensive and often lossy), so we extended ITK-based file formats with the ability to tell the transform type:</p>
<ul>
<li>for ITK transform types, we introduced new class names (<code>InverseDisplacementFieldTransform</code>, <code>InverseBSplineTransform</code>, <code>InverseThinPlateSplineKernelTransform</code>)</li>
<li>for displacement fields in NRRD format we introduced <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html#nrrd"><code>displacement field type</code> custom field</a></li>
</ul>

---

## Post #3 by @lucinda (2025-12-13 19:37 UTC)

<p>Awesome, thank you so much!!</p>

---

## Post #4 by @mikebind (2025-12-15 19:07 UTC)

<p>Recently, I was trying to understand the details of how grid transforms function in Slicer and how transforms generated using ANTs in Slicer differ from those generated using ANTs at the command line.  In addition to the issues that <a class="mention" href="/u/lassoan">@lassoan</a> very nicely explained above, there are a few other subtleties that I found confusing and took me a while to sort out.  I am attaching my summary notes from that exploration in case they will be useful to you or others coming across this thread in the future.</p>
<p><a href="https://drive.google.com/file/d/1zteHnqBIUjtI2wbVXjslbc_oX5nJ1mdI/view?usp=sharing" rel="noopener nofollow ugc">DeformationFieldCalculationNotes.pdf</a></p>

---
