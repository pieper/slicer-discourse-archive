---
topic_id: 6617
title: "Application Of Ct Scanning Soil Model In 3D Slicer"
date: 2019-04-26
url: https://discourse.slicer.org/t/6617
---

# Application of CT Scanning Soil Model in 3D Slicer

**Topic ID**: 6617
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/application-of-ct-scanning-soil-model-in-3d-slicer/6617

---

## Post #1 by @3D-Soil (2019-04-26 02:54 UTC)

<p>Hello, everyone, I am not a medical major, but I want to ask the question of 3D Slicer. I scanned a soil column with CT. I want to use 3D Slicer to identify different size particles in the soil column and calculate its percentage content. I want to ask how you operate it. Thank you very much.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8927d7c472c4588e16d427137e2e2868030fce52.png" data-download-href="/uploads/short-url/jzkM8gPF6ScaFXlNvGBj43KklQ6.png?dl=1" title="20190425171423" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8927d7c472c4588e16d427137e2e2868030fce52_2_690x455.png" alt="20190425171423" data-base62-sha1="jzkM8gPF6ScaFXlNvGBj43KklQ6" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8927d7c472c4588e16d427137e2e2868030fce52_2_690x455.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8927d7c472c4588e16d427137e2e2868030fce52.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8927d7c472c4588e16d427137e2e2868030fce52.png 2x" data-dominant-color="686CAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20190425171423</span><span class="informations">984×650 406 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-04-26 12:51 UTC)

<p>First you need to segment the particles that you are interested in and then you can compute basic statistics.</p>
<p>You can try if thresholding works, maybe followed by smoothing. Then you can use Islands effect to split the segment to individual segments and use Segment statistics to get size of each particle.</p>
<p>If there are many particles then splitting and any further processing may take a long time. If that’s a problem then you export the segmentation to labelmap (before splitting) and get statistics using ITK or other packages.</p>

---

## Post #3 by @3D-Soil (2019-04-27 04:13 UTC)

<p>Thank you. I used this method, but I encountered some problems. I want to use Description in Slicer Extensions to implement statistics, or Shape Variation Analyzer to operate. What do you think of this approach and how to operate it? Thank you very much for answering this question. Thank you.</p>

---
