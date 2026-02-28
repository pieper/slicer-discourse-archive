---
topic_id: 46331
title: "Segmentation And Volume Misaligned After Using Biomedisa"
date: 2026-02-27
url: https://discourse.slicer.org/t/46331
---

# Segmentation and Volume Misaligned After Using Biomedisa

**Topic ID**: 46331
**Date**: 2026-02-27
**URL**: https://discourse.slicer.org/t/segmentation-and-volume-misaligned-after-using-biomedisa/46331

---

## Post #1 by @FabricioFO (2026-02-27 14:38 UTC)

<p>The problem is the following: I segment nasal turbinates in rodents and use Biomedisa. When I take my CT scans, I need to orient them in 3D Slicer, so I create a Transform and adjust the orientation. After that, I generate the slices that will be used by Biomedisa.</p>
<p>After this step, I upload them to Biomedisa, retrieve the file it generates, and load it into 3D Slicer. I click on the option in Data, “convert labelmap to segmentation node.” Then, I use ImageStack from SlicerMorph to upload the CT scans.</p>
<p>I then take the Transform I created earlier with the slices and, in another scene, apply it to the segmentation that came from Biomedisa and to the volume I uploaded—but they end up completely separated.</p>
<p>What am I doing wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96.jpeg" data-download-href="/uploads/short-url/y5aU81ZqbycDkEldmwrvvQllpfE.jpeg?dl=1" title="alinhamento" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_690x387.jpeg" alt="alinhamento" data-base62-sha1="y5aU81ZqbycDkEldmwrvvQllpfE" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedfb247effd055f202d9bd103db2f9174270f96_2_1380x774.jpeg 2x" data-dominant-color="87888C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">alinhamento</span><span class="informations">1919×1079 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046.png" data-download-href="/uploads/short-url/sbwOIFQ5Om9ENJ68Tkr8uAzzILs.png?dl=1" title="forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_690x387.png" alt="forum" data-base62-sha1="sbwOIFQ5Om9ENJ68Tkr8uAzzILs" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c58a82921312fdad35f4a024eba43388379f9046_2_1380x774.png 2x" data-dominant-color="7E7E83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">forum</span><span class="informations">1919×1079 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2026-02-27 22:03 UTC)

<p>Have you tried using the Biomedisa extension? This would keep everything in Slicer.  I’m guessing that perhaps your issue is related to rearranging image axes in the export-import process.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VJXDxwp6eHY" data-video-title="Tutorial: How to use Biomedisa’s Smart Interpolation in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VJXDxwp6eHY" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://i.ytimg.com/vi/VJXDxwp6eHY/hqdefault.jpg" title="Tutorial: How to use Biomedisa’s Smart Interpolation in 3D Slicer" width="480" height="360">
  </a>
</div>


---
