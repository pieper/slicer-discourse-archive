---
topic_id: 46817
title: "Need Advice On Segmentation Of Ct Scanned Fossil Specimen Lu"
date: 2026-04-23
url: https://discourse.slicer.org/t/46817
---

# Need advice on Segmentation of CT scanned fossil specimen (lungfish)

**Topic ID**: 46817
**Date**: 2026-04-23
**URL**: https://discourse.slicer.org/t/need-advice-on-segmentation-of-ct-scanned-fossil-specimen-lungfish/46817

---

## Post #1 by @sturiones (2026-04-23 16:20 UTC)

<p>Hi, folks!</p>
<p>I am not an expert in 3D Slicer, I need advice from the community. I have a TM-scanned fossil fish skull with inner structures (canals for nerves and vessels) of rather low contrast (the slice below is after Local Contrast Enhancement in ImageJ). I tried thresholding and Total segmentator, but without success. What might be the most promising method to segment the inner canals?</p>
<p>My PC: Windows 10; Intel(R) Core™ i5-10400F CPU 2.9GHz; RAM 32,0 GB</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e782cfdb8dde092fb23ec269975d0e1999e8e71.jpeg" data-download-href="/uploads/short-url/i2NDtbNlzNvhn4U51oRfH72gCk1.jpeg?dl=1" title="Rhinodipterus-iter200183" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e782cfdb8dde092fb23ec269975d0e1999e8e71_2_690x498.jpeg" alt="Rhinodipterus-iter200183" data-base62-sha1="i2NDtbNlzNvhn4U51oRfH72gCk1" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e782cfdb8dde092fb23ec269975d0e1999e8e71_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e782cfdb8dde092fb23ec269975d0e1999e8e71.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e782cfdb8dde092fb23ec269975d0e1999e8e71.jpeg 2x" data-dominant-color="393939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Rhinodipterus-iter200183</span><span class="informations">1024×740 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-04-24 02:16 UTC)

<p>What is TM-scanning? I am not sure what that imaging modality is.</p>
<p>I can’t recognize any structures in this cross-section, but you should give the NNinteractive prompt-based segmentation extension a try. You simply iterate over by giving negative (does not belong) and positive (belongs) prompts (points, curves, ROIs etc) and guide the AI.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/coendevente/SlicerNNInteractive">
  <header class="source">

      <a href="https://github.com/coendevente/SlicerNNInteractive" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/70a5f256941ed87befbf88ff707012cc/coendevente/SlicerNNInteractive" class="thumbnail">

  <h3><a href="https://github.com/coendevente/SlicerNNInteractive" target="_blank" rel="noopener nofollow ugc">GitHub - coendevente/SlicerNNInteractive: A 3D Slicer extension for efficient segmentation...</a></h3>

    <p><span class="github-repo-description">A 3D Slicer extension for efficient segmentation with nnInteractive.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
