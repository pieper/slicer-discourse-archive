---
topic_id: 14816
title: "How To Convert Model Node Points To Volume Node"
date: 2020-11-30
url: https://discourse.slicer.org/t/14816
---

# How to convert model node (points) to Volume node?

**Topic ID**: 14816
**Date**: 2020-11-30
**URL**: https://discourse.slicer.org/t/how-to-convert-model-node-points-to-volume-node/14816

---

## Post #1 by @shahrokh (2020-11-30 13:13 UTC)

<p>Hello Dear Developers and Users</p>
<p>I have a model that contains 48425 points or cells. These points are the result of sampling of pulmonary vessels in CT images by the <a href="https://chestimagingplatform.org/" rel="noopener nofollow ugc">Chest Imaging Platform</a> (which are known as <em>particles system</em>) .</p>
<p>The following figure is a representation of these points in 3D CT space.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d400bd4c455324d2231a40e6e25cbc07e167c7.jpeg" data-download-href="/uploads/short-url/gFvBeXtDwGgFfi3EyA0RN02AoaX.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74d400bd4c455324d2231a40e6e25cbc07e167c7_2_690x398.jpeg" alt="Screenshot" data-base62-sha1="gFvBeXtDwGgFfi3EyA0RN02AoaX" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74d400bd4c455324d2231a40e6e25cbc07e167c7_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74d400bd4c455324d2231a40e6e25cbc07e167c7_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d400bd4c455324d2231a40e6e25cbc07e167c7.jpeg 2x" data-dominant-color="8C8EB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1189×686 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This model has the following scalars (with certain size matrices):<br>
scale(1X48425), val(1X48425), hmode(1X48425), hevec0(3X48425), hevec1(3X48425), hevec2(3X48425), h0(1X48425), h1(1X48425), h2(1X48425) and hess (9X48425).</p>
<p>I want to make/create a volume node of this model with the same dimensions as the CT matrix whose pixel values of this volume node are equal to the values of one of the scalars mentioned above (e.g. scale or hevec0) in the positions of each particles in this model.<br>
The figure shows the list of these scalars.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de4f65d3b81f10b354e471a19727d7d0b2edf5ff.jpeg" data-download-href="/uploads/short-url/vIE6EGRzMoufqHxMaAwohvwh4l1.jpeg?dl=1" title="s" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de4f65d3b81f10b354e471a19727d7d0b2edf5ff_2_690x388.jpeg" alt="s" data-base62-sha1="vIE6EGRzMoufqHxMaAwohvwh4l1" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de4f65d3b81f10b354e471a19727d7d0b2edf5ff_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de4f65d3b81f10b354e471a19727d7d0b2edf5ff_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de4f65d3b81f10b354e471a19727d7d0b2edf5ff_2_1380x776.jpeg 2x" data-dominant-color="A6A8B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">s</span><span class="informations">1920×1080 380 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Please guide me.<br>
Best regards.<br>
Shahrokh</p>

---
