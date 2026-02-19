---
topic_id: 3958
title: "How To Import A Slicer Segmentation Into Other Tools Like Ma"
date: 2018-08-31
url: https://discourse.slicer.org/t/3958
---

# How to import a slicer segmentation into other tools like matlab?

**Topic ID**: 3958
**Date**: 2018-08-31
**URL**: https://discourse.slicer.org/t/how-to-import-a-slicer-segmentation-into-other-tools-like-matlab/3958

---

## Post #1 by @Chongran_Sun (2018-08-31 16:23 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 4.8.1<br>
Expected behavior: I saved my tumor segmentation as a nrrd file or seg.nrrd file and open them in other tools (MRIcron, matlab).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ebbfa5dae1c51baac93c9e1c5bfddd941a34f4b.png" data-download-href="/uploads/short-url/8WYlkWwDU0H0TLU35qntAYfcUwr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ebbfa5dae1c51baac93c9e1c5bfddd941a34f4b_2_596x500.png" alt="image" data-base62-sha1="8WYlkWwDU0H0TLU35qntAYfcUwr" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ebbfa5dae1c51baac93c9e1c5bfddd941a34f4b_2_596x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ebbfa5dae1c51baac93c9e1c5bfddd941a34f4b_2_894x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ebbfa5dae1c51baac93c9e1c5bfddd941a34f4b_2_1192x1000.png 2x" data-dominant-color="504E57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1680×1408 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I open the segmentation, I need to have a blank background to show the location of the tumor like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5850bd050d1a2b3103e73df9c1dbbff3085f5d8d.png" data-download-href="/uploads/short-url/cBgZUmIv4brSe6zDBHyTKihKXy5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5850bd050d1a2b3103e73df9c1dbbff3085f5d8d_2_451x500.png" alt="image" data-base62-sha1="cBgZUmIv4brSe6zDBHyTKihKXy5" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5850bd050d1a2b3103e73df9c1dbbff3085f5d8d_2_451x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5850bd050d1a2b3103e73df9c1dbbff3085f5d8d_2_676x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5850bd050d1a2b3103e73df9c1dbbff3085f5d8d.png 2x" data-dominant-color="1B1C21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×884 32.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Actual behavior: I found the location information was lost, the size of the matrix was the max diameter of the tumor, but without the blank background.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2011a912494fcb8b7fb142c4dea02dbee2fe3ff2.jpeg" data-download-href="/uploads/short-url/4zH7diqDNwHu9CQgknscuoLMNGi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2011a912494fcb8b7fb142c4dea02dbee2fe3ff2_2_371x500.jpeg" alt="image" data-base62-sha1="4zH7diqDNwHu9CQgknscuoLMNGi" width="371" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2011a912494fcb8b7fb142c4dea02dbee2fe3ff2_2_371x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2011a912494fcb8b7fb142c4dea02dbee2fe3ff2_2_556x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2011a912494fcb8b7fb142c4dea02dbee2fe3ff2.jpeg 2x" data-dominant-color="67676D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">586×788 51.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-08-31 16:33 UTC)

<aside class="quote no-group" data-username="Chongran_Sun" data-post="1" data-topic="3958">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ee59a6/48.png" class="avatar"> Chongran_Sun:</div>
<blockquote>
<p>I found the location information was lost</p>
</blockquote>
</aside>
<p>Segments are correctly positioned in physical space. By default, blank voxels are stripped to conserve memory (image origin is updated accordingly to ensure the correct position is maintained).</p>
<p>If you work with software that cannot take into account image origin, spacing, and axis directions and just rely on matching of voxel coordinates (or the software cannot handle overlapping segments stored in 4D volume), then you need to export the segmentation to a labelmap node:</p>
<ul>
<li>Go to Segmentations module</li>
<li>In “Export/Import…” section click “Export” button</li>
<li>Save the newly created “Output node”</li>
</ul>

---

## Post #3 by @ihnorton (2018-08-31 17:08 UTC)

<p>Note that mricron has fairly limited NRRD support, so you may be better off exporting as Nifti.</p>

---
