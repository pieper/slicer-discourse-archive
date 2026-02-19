---
topic_id: 5666
title: "Export Dicom Spect Values Higher Than 2 16"
date: 2019-02-06
url: https://discourse.slicer.org/t/5666
---

# Export DICOM SPECT, values higher than 2^16

**Topic ID**: 5666
**Date**: 2019-02-06
**URL**: https://discourse.slicer.org/t/export-dicom-spect-values-higher-than-2-16/5666

---

## Post #1 by @nbarbosap (2019-02-06 20:51 UTC)

<p>Slicer version: 4.8.1</p>
<p>I’m registering a few SPECT/CT images using the common registration. Everything works relly well and the images seems to be as good as I expect !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70deeb891ec66d606bf1ba9f5e454e0394591ecf.png" data-download-href="/uploads/short-url/g6v50hrWtYa31ZCIOX5Eg931Kt9.png?dl=1" title="image%20(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_690x388.png" alt="image%20(1)" data-base62-sha1="g6v50hrWtYa31ZCIOX5Eg931Kt9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_1380x776.png 2x" data-dominant-color="949497"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image%20(1)</span><span class="informations">1920×1080 423 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My problem is when I try to “export” the DICOM file. My image  values are higher than 2^16, so, when I export the images, all the values higher than 2^16, appears with no value (an horrible black hole).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d282815440c96ddac7edc1d7a2e61b0723e2964.jpeg" data-download-href="/uploads/short-url/49VSFhu3tY9WHqnk2dCfeDMSsHq.jpeg?dl=1" title="image%20(2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_690x388.jpeg" alt="image%20(2)" data-base62-sha1="49VSFhu3tY9WHqnk2dCfeDMSsHq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_1380x776.jpeg 2x" data-dominant-color="909093"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image%20(2)</span><span class="informations">1920×1080 381 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I “export” the images without affect the maximum values??.. I need to use this images on another software to quantify the retained activity into the patient, so, It´is not viable rescale the pixel values to be lower than 2^16. I need the pixels values as they are.</p>

---

## Post #3 by @cpinter (2019-02-06 21:29 UTC)

<p>I merged the two identical topics into one.</p>
<p>The problem is that the scalar type of the volume written by the CreateDICOMSeries module cannot represent that high numbers. What does the data probe (bottom left corner) show for voxel values if you hover those regions with the mouse?</p>
<p>DICOM gurus: Does SPECT support intercept/slope? Could we use that?</p>

---

## Post #4 by @nbarbosap (2019-02-07 13:02 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> for your interest…</p>
<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="5666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>What does the data probe (bottom left corner) show for voxel values if you hover those regions with the mouse?</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d70e796d7aa0c223faf0a6595a8cc654b5a0672.jpeg" data-download-href="/uploads/short-url/b34F3VrnacbT5EfQzSfwym0Z2r8.jpeg?dl=1" title="Imagen2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d70e796d7aa0c223faf0a6595a8cc654b5a0672_2_690x388.jpeg" alt="Imagen2" data-base62-sha1="b34F3VrnacbT5EfQzSfwym0Z2r8" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d70e796d7aa0c223faf0a6595a8cc654b5a0672_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d70e796d7aa0c223faf0a6595a8cc654b5a0672_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d70e796d7aa0c223faf0a6595a8cc654b5a0672_2_1380x776.jpeg 2x" data-dominant-color="8E8F93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Imagen2</span><span class="informations">1920×1080 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2019-02-07 13:52 UTC)

<p>Probably the easiest thing to do is modify the pixel values directly via python to clamp values to the max representable value.</p>
<p>Like the example here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume</a></p>

---
