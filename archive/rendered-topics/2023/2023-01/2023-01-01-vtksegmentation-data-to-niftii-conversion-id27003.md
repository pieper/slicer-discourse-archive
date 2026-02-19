---
topic_id: 27003
title: "Vtksegmentation Data To Niftii Conversion"
date: 2023-01-01
url: https://discourse.slicer.org/t/27003
---

# vtkSegmentation data to niftii conversion

**Topic ID**: 27003
**Date**: 2023-01-01
**URL**: https://discourse.slicer.org/t/vtksegmentation-data-to-niftii-conversion/27003

---

## Post #1 by @Rajesh_Ds (2023-01-01 17:19 UTC)

<p>I have a   vtkSegmentation data  instance obtained as a segmentation results, using python code and slicer’s  lungCT_analyzer modules code. I would like to get the same in niftii format (i.e .nii.gz), so that I can visually analyze the segmentation results on some sample lung CT dataset and process these segmentations further.  Any help would be highly appreciated please…!!!</p>

---

## Post #2 by @rbumm (2023-01-01 20:10 UTC)

<p>Please go to the “Segmentations” module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ca109be5e9605f843f938d3a9ba4b7e848e7bec.png" data-download-href="/uploads/short-url/fuYAx7TmYSCoirKC60ArOlhlhAE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6ca109be5e9605f843f938d3a9ba4b7e848e7bec_2_689x260.png" alt="image" data-base62-sha1="fuYAx7TmYSCoirKC60ArOlhlhAE" width="689" height="260" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6ca109be5e9605f843f938d3a9ba4b7e848e7bec_2_689x260.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6ca109be5e9605f843f938d3a9ba4b7e848e7bec_2_1033x390.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ca109be5e9605f843f938d3a9ba4b7e848e7bec.png 2x" data-dominant-color="A8A7A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1240×469 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and under “Export to files” choose “NIFTI” and “Export”</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba016f5c923ccf44f792d3b360e7a8a946cb39a4.png" alt="image" data-base62-sha1="qxtSO3DwEk9bz8t4cDp0e8HjU0I" width="567" height="210"></p>

---

## Post #3 by @Rajesh_Ds (2023-01-02 02:41 UTC)

<p>Thank you  and the python code to do the same ? Do we have a python function under vtk  libraries, to export vtk Segmentation type (made of multiple vtkImageObjectData type segments) data to niftii format ?</p>

---

## Post #4 by @Rajesh_Ds (2023-01-02 07:24 UTC)

<p>I have obtained the segmentation  using the GetSegmentation() method from vtkSegmentation class</p>

---

## Post #5 by @rbumm (2023-01-02 10:01 UTC)

<p><a href="https://discourse.slicer.org/t/overlapping-segmentions-export-to-nifti/15773">This thread</a> may help, <a href="https://discourse.slicer.org/t/overlapping-segmentions-export-to-nifti/15773/13">see here</a>.</p>

---
