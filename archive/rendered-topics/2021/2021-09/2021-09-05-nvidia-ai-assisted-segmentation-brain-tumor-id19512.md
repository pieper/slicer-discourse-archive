---
topic_id: 19512
title: "Nvidia Ai Assisted Segmentation Brain Tumor"
date: 2021-09-05
url: https://discourse.slicer.org/t/19512
---

# Nvidia AI-assisted segmentation (brain tumor)

**Topic ID**: 19512
**Date**: 2021-09-05
**URL**: https://discourse.slicer.org/t/nvidia-ai-assisted-segmentation-brain-tumor/19512

---

## Post #1 by @Klakla (2021-09-05 07:24 UTC)

<p>HI, when I did segmentation to the tumour for image 1 by NVidia Clara AI-based automatic and determined the boundary unfortunately the result was in image 2 . the question is why when making boundary to the tumour, boundary appeared to the area of the nose?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7dfda122ceb3312aa29880975bf975d3d742b16.jpeg" data-download-href="/uploads/short-url/qeCYBj1evEuPbJtt29D7eO8j1Pg.jpeg?dl=1" title="image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7dfda122ceb3312aa29880975bf975d3d742b16_2_557x500.jpeg" alt="image1" data-base62-sha1="qeCYBj1evEuPbJtt29D7eO8j1Pg" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7dfda122ceb3312aa29880975bf975d3d742b16_2_557x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7dfda122ceb3312aa29880975bf975d3d742b16_2_835x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7dfda122ceb3312aa29880975bf975d3d742b16_2_1114x1000.jpeg 2x" data-dominant-color="626871"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image1</span><span class="informations">1280×1149 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad25c67513974c9e6d59e1204654d930daa48267.jpeg" data-download-href="/uploads/short-url/oHJxccnamQUdIgM9m9PrLLVZ69p.jpeg?dl=1" title="image2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad25c67513974c9e6d59e1204654d930daa48267_2_559x500.jpeg" alt="image2" data-base62-sha1="oHJxccnamQUdIgM9m9PrLLVZ69p" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad25c67513974c9e6d59e1204654d930daa48267_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad25c67513974c9e6d59e1204654d930daa48267_2_838x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad25c67513974c9e6d59e1204654d930daa48267_2_1118x1000.jpeg 2x" data-dominant-color="5C636F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image2</span><span class="informations">1280×1144 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mangotee (2021-09-05 08:39 UTC)

<p>Hi, for AIAA brain tumor segmentation, you need to provide brain-extracted volumes, i.e. only the brain region (the model was trained on BRATS data which is skull stripped, too). If the full head is provided, false positives occur easily, e.g. in the nasal cavity, as you observed. Worse yet, the volume looks so different from the training data that very obvious tumor regions may be entirely missed (I think that’s sth that happened here too), in which case manual post-processing (e.g. island selection) wouldn’t help anymore. Best is to perform brain extraction prior to AIAA inference. In Slicer, this can be achieved with the “Swiss Skull Stripper” module (downloadable via Slicer extension manager). Outside of Slicer, if you are using Linux (or Windows WSL/WSL2), I’ve made really good experiences with FSL’s bet/bet2 tool.</p>

---
