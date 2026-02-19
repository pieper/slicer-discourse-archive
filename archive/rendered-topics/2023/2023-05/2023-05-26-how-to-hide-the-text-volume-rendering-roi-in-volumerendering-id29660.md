---
topic_id: 29660
title: "How To Hide The Text Volume Rendering Roi In Volumerendering"
date: 2023-05-26
url: https://discourse.slicer.org/t/29660
---

# How to hide the text "Volume Rendering ROI" in VolumeRendering Module?

**Topic ID**: 29660
**Date**: 2023-05-26
**URL**: https://discourse.slicer.org/t/how-to-hide-the-text-volume-rendering-roi-in-volumerendering-module/29660

---

## Post #1 by @Shannon_Chow (2023-05-26 02:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12f0182c2325d3c2344c70f8e03d610e5644e2ca.jpeg" data-download-href="/uploads/short-url/2HwZEsT2RXHHIpD0otKwicKummK.jpeg?dl=1" title="ROI Text" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f0182c2325d3c2344c70f8e03d610e5644e2ca_2_690x430.jpeg" alt="ROI Text" data-base62-sha1="2HwZEsT2RXHHIpD0otKwicKummK" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f0182c2325d3c2344c70f8e03d610e5644e2ca_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f0182c2325d3c2344c70f8e03d610e5644e2ca_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f0182c2325d3c2344c70f8e03d610e5644e2ca_2_1380x860.jpeg 2x" data-dominant-color="32303D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI Text</span><span class="informations">1497×934 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
How to hide the “Volume Rendering ROI” in each image?<br>
In 4.x, there is no this text. But with 5.x, when enable ROI crop in Volume Rendering, the texts appear.</p>

---

## Post #2 by @lassoan (2023-05-26 03:55 UTC)

<p>You can show/hide the ROI by clicking on the eye icon in Volume Rendering module. You can shot the ROI and just hide the label using Markups module: Display / Advanced / Properties label → uncheck.</p>

---
