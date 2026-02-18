# Difference between the dimensions of the CT and RT dose

**Topic ID**: 38386
**Date**: 2024-09-15
**URL**: https://discourse.slicer.org/t/difference-between-the-dimensions-of-the-ct-and-rt-dose/38386

---

## Post #1 by @azam (2024-09-15 05:05 UTC)

<p>Hi everyone<br>
I have CT, RT dose and RT structure files that I have exported from the treatment planning system. As you can see in the figure, the dimensions of the CT image and RT dose are different. How do these two files match and provide correct dosimetric results?<br>
Also about RT structure. That is, based on which common parameter, the RT dose and RT structure files are correctly matched and the DVH parameters are calculated?</p>
<p>thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b80066660594037cf24d4fe8939de6ec7eef97b.png" data-download-href="/uploads/short-url/d3rK0F0MpyC1Aek0HHTg7k9kXKX.png?dl=1" title="picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b80066660594037cf24d4fe8939de6ec7eef97b.png" alt="picture1" data-base62-sha1="d3rK0F0MpyC1Aek0HHTg7k9kXKX" width="461" height="374" data-dominant-color="F3F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture1</span><span class="informations">762×619 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-09-16 23:40 UTC)

<p>Usually dose is computed at much lower resolution than the CT image. The origin, spacing, axis directions, extent of these images are different, but generally there is no need to match them (unless you work with some software that does not operate in physical space but requires that voxels match).</p>
<p>RT structure sets is usually generated from anatomical images, i.e., CT images.</p>
<p>When DVH is computed then usually the geometry of the RT structure set is used. By default, resolution of the RT structure set is the same as the image it was computed from; but for small and thin structures oversampling may be used (you can either specify a fixed factor or enable automatic oversampling). You can see the exact behavior in the <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/Logic/vtkSlicerDoseVolumeHistogramModuleLogic.cxx">source code</a> and much more information on <a href="https://labs.cs.queensu.ca/perklab/publications/?tsr=&amp;yr=&amp;type=&amp;auth=86&amp;tps_button=Search">voxelization papers by @Sunderlandkyl</a>.</p>

---

## Post #3 by @azam (2025-07-06 07:17 UTC)

<p>Hi Lasso<br>
thanks, but I have another question!<br>
I expect the RT dose file (111,111,161) to cover the CT image with dimensions (512,512,225). If I crop the CT image and its dimensions change, do I need to make any changes in RT dose file (i.e. change its dimensions or etc.)?<br>
Thank you</p>

---

## Post #4 by @lassoan (2025-07-06 11:30 UTC)

<p>Each data object in DICOM and in Slicer are fully, independently defined in physical space. Position does not change, if you just crop a data object, so everything remains valid.</p>

---
