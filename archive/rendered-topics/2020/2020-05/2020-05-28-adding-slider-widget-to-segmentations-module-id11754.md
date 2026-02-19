---
topic_id: 11754
title: "Adding Slider Widget To Segmentations Module"
date: 2020-05-28
url: https://discourse.slicer.org/t/11754
---

# Adding slider widget to Segmentations module

**Topic ID**: 11754
**Date**: 2020-05-28
**URL**: https://discourse.slicer.org/t/adding-slider-widget-to-segmentations-module/11754

---

## Post #1 by @loubna (2020-05-28 17:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acc454980ffa6948e6177fdeb835f0a43a8cf532.png" data-download-href="/uploads/short-url/oEmLb7cbCkN49QIvgMeOWxXWnzs.png?dl=1" title="slicer-img" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acc454980ffa6948e6177fdeb835f0a43a8cf532_2_303x500.png" alt="slicer-img" data-base62-sha1="oEmLb7cbCkN49QIvgMeOWxXWnzs" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acc454980ffa6948e6177fdeb835f0a43a8cf532_2_303x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acc454980ffa6948e6177fdeb835f0a43a8cf532_2_454x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acc454980ffa6948e6177fdeb835f0a43a8cf532.png 2x" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer-img</span><span class="informations">538×885 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hi,</p>
<p>I am trying to add slider widget on the main window of segmentation module (see atteched image). I would want this slider to interact with my reconstruction method (i.e. allow me to change the tolerance value which control the quality of reconstruction) that i am going to add to the developped reconstruction module  in order to reconstruct simple object from contours in slicerRt. Are there any steps that I can go about into implementing this?</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-05-28 18:08 UTC)

<p>If you implement a new conversion rule then all you need is to register it in the vtkSegmentationConverterFactory and it will appear in the segmentations module GUI. You can define conversion parameters in the rule, which users can adjust by clicking on “Update” button in the appropriate line in “Representations” section. You can use <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx">converter rules in SlicerRT extension</a> as example.</p>

---
