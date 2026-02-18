# Segmentation has changed images resolution

**Topic ID**: 18043
**Date**: 2021-06-09
**URL**: https://discourse.slicer.org/t/segmentation-has-changed-images-resolution/18043

---

## Post #1 by @Antonio_Giulio_Genna (2021-06-09 14:55 UTC)

<p>Operating system: Windows 8.1<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Use the same resolution as volume images<br>
Actual behavior: The segmentation has higher image resolution compared to native T1 volume<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dd832551d313cfa380d8cf76fa538c73688f8e1.jpeg" data-download-href="/uploads/short-url/b6DXMSl53FmgOlbkeNfkSjAnCnf.jpeg?dl=1" title="Original volume parameters" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4dd832551d313cfa380d8cf76fa538c73688f8e1_2_476x500.jpeg" alt="Original volume parameters" data-base62-sha1="b6DXMSl53FmgOlbkeNfkSjAnCnf" width="476" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4dd832551d313cfa380d8cf76fa538c73688f8e1_2_476x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dd832551d313cfa380d8cf76fa538c73688f8e1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dd832551d313cfa380d8cf76fa538c73688f8e1.jpeg 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Original volume parameters</span><span class="informations">559×586 48.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/148ca8fb824b652eae8ab232f37df3c2db8760ec.jpeg" data-download-href="/uploads/short-url/2VMUyIoLDxkjc6BgdPgmbXQtl7K.jpeg?dl=1" title="Segmentation parameters" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/148ca8fb824b652eae8ab232f37df3c2db8760ec_2_440x500.jpeg" alt="Segmentation parameters" data-base62-sha1="2VMUyIoLDxkjc6BgdPgmbXQtl7K" width="440" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/148ca8fb824b652eae8ab232f37df3c2db8760ec_2_440x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/148ca8fb824b652eae8ab232f37df3c2db8760ec.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/148ca8fb824b652eae8ab232f37df3c2db8760ec.jpeg 2x" data-dominant-color="F5F5F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segmentation parameters</span><span class="informations">567×643 48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi,</p>
<p>I have been segmenting brain lesions on T1 images for a while. After coregistering T1 to DTI images I hoped to use these segmentations to analyse DTI parameters (FA, MD etc.) within the segmentation.<br>
As suggested, I exported the segmentations as lablemaps. However, image resolution has changed. Slice thickness has been reduced from 1 mm (native volume) to 0.7 mm (segmentation) and z axis slices have been increased from a total of 168 (native volume) to 240 (segmentation).</p>
<p>Sadly, this unable me to overlay the segmentation to the coregistered images and derive DTI parameters.</p>
<p>I have managed to modify the slice thickness, but I cannot change the number of slices in the z axis.</p>
<p>Could you please help me?</p>
<p>All the best</p>
<p>Antonio</p>

---

## Post #2 by @lassoan (2021-06-09 20:59 UTC)

<p>You can use many volumes throughout the segmentation process, each may have different geometry (origin, spacing, axis directions and extents). The segmentation is set to the geometry of the first volume that you select as master volume, but you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">change this anytime</a>. You can also choose any volume as reference volume when you <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">export the segmentation to file</a> (segmentation will be resampled to match the geometry of the reference volume).</p>
<aside class="quote no-group" data-username="Antonio_Giulio_Genna" data-post="1" data-topic="18043">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/antonio_giulio_genna/48/8898_2.png" class="avatar"> Antonio_Giulio_Genna:</div>
<blockquote>
<p>Sadly, this unable me to overlay the segmentation to the coregistered images and derive DTI parameters.</p>
</blockquote>
</aside>
<p>What software do you use that cannot overlay two volumes that are in the same physical space just happen to have different geometries?</p>

---
