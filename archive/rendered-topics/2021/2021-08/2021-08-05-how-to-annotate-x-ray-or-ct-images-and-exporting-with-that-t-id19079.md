---
topic_id: 19079
title: "How To Annotate X Ray Or Ct Images And Exporting With That T"
date: 2021-08-05
url: https://discourse.slicer.org/t/19079
---

# How to annotate X-Ray or CT images and exporting with that/these annotation information(s) ? 

**Topic ID**: 19079
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/how-to-annotate-x-ray-or-ct-images-and-exporting-with-that-these-annotation-information-s/19079

---

## Post #1 by @geonse (2021-08-05 12:15 UTC)

<p>Hi everyone,</p>
<p>I’m completely new for the tool and I’d like to ask that is it possible to annotate medical images let’s say for a brain tumor and exporting that annotation information such as coordinates (Xmin Ymin Xmax Ymax) ?</p>
<p>If it is possible is there any documentation for this because I’ve not seen any about it.</p>
<p>The main question is that can I use 3D Slicer for annotation tool for making images ready to be trained in AI models?</p>

---

## Post #2 by @pieper (2021-08-05 12:46 UTC)

<p>Yes, it’s very common to annotate images in Slicer for AI.  See <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a> for example.  Also you can easily save annotations <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#markups">in various formats</a>.</p>

---

## Post #3 by @geonse (2021-08-11 08:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7b2dc7ac1b915cdbfca153dab23d321584d0ce7.jpeg" data-download-href="/uploads/short-url/x3HvfSptx23plOASOF4LhD8MrHN.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b2dc7ac1b915cdbfca153dab23d321584d0ce7_2_690x361.jpeg" alt="1" data-base62-sha1="x3HvfSptx23plOASOF4LhD8MrHN" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b2dc7ac1b915cdbfca153dab23d321584d0ce7_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b2dc7ac1b915cdbfca153dab23d321584d0ce7_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7b2dc7ac1b915cdbfca153dab23d321584d0ce7_2_1380x722.jpeg 2x" data-dominant-color="76777E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1006 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/1197e3e4c0e5280151be1997f6a584ed83e8e453.jpeg" data-download-href="/uploads/short-url/2vDxuNuO4guCrARj7HUPy9xFhCP.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1197e3e4c0e5280151be1997f6a584ed83e8e453_2_690x361.jpeg" alt="2" data-base62-sha1="2vDxuNuO4guCrARj7HUPy9xFhCP" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1197e3e4c0e5280151be1997f6a584ed83e8e453_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1197e3e4c0e5280151be1997f6a584ed83e8e453_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1197e3e4c0e5280151be1997f6a584ed83e8e453_2_1380x722.jpeg 2x" data-dominant-color="76777E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1007 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @geonse (2021-08-11 08:47 UTC)

<p>Hi,</p>
<p>I was using Nvidia Clara extension but couldn’t get the result the way I want. What I want is to annotate, let’s say brain tumor, and save the annotations of every slices in text format. As you know, Clara identifies tumor for every slices in ct images when you locate the tumor in only one slice, the rest is taken care.</p>
<p>This is the format I need:</p>
<p>Slice_name, xmin, ymin, xmax, ymax<br>
Slice_001     0        130     512    429</p>
<p>the coordinates indicates the rectangle of annotation. I share two different slices of brain tumor case done by nvidia clara tool in 3D Slices preview version. How can I extract annotation information in the format I described? I mean, if Nvidia Clara identifies tumor in every slices, there must be coordinates of annotations for every slices, right?</p>
<p>Kind regards.</p>

---

## Post #5 by @pieper (2021-08-11 13:24 UTC)

<p>Such slice-by-slice bounding boxes are okay, but full segmentations are more meaningful and that’s why we mostly focus on them as in the MONAILabel code.  You would probably be better to shift your work in that direction.</p>
<p>But if you need to know coordinates you can extract them by getting the mins and maxes from the list of coordinates returned by <code>numpy.where</code> as in this example.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=numpy.where#get-the-values-of-all-voxels-for-a-label-value" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=numpy.where#get-the-values-of-all-voxels-for-a-label-value</a></p>

---
