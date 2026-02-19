---
topic_id: 26793
title: "Lung Ct Analyzer Now Supports Lung Lobes And Emphysema Stati"
date: 2022-12-17
url: https://discourse.slicer.org/t/26793
---

# Lung CT Analyzer now supports lung lobes and emphysema statistics

**Topic ID**: 26793
**Date**: 2022-12-17
**URL**: https://discourse.slicer.org/t/lung-ct-analyzer-now-supports-lung-lobes-and-emphysema-statistics/26793

---

## Post #1 by @rbumm (2022-12-17 19:15 UTC)

<p>Lung lobe segmentation has recently become a 2-minute process with Lung CT Segmenter calls of the  <a href="https://github.com/lassoan/SlicerTotalSegmentator" rel="noopener nofollow ugc">TotalSegmentator AI extension</a>.</p>
<p>Consequently, Lung CT Analyzer 2.62 now includes <strong>lung lobe analysis</strong> of pulmonary infiltrates, lung collapse, and emphysema. A special emphysema result table and display are available which will be helpful in lung volume reduction surgery (LVRS) and the surveillance of COPD.</p>
<p>In this COPD case, 35% of the right upper lobe is affected, so this anatomical structure could be a  primary target for LVRS.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f781385c40d6ca7662959a83d7c2fb10b6b1c1fc.png" data-download-href="/uploads/short-url/zjwMRv8e81DPymQqQrtPNqHlxJa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f781385c40d6ca7662959a83d7c2fb10b6b1c1fc_2_690x305.png" alt="image" data-base62-sha1="zjwMRv8e81DPymQqQrtPNqHlxJa" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f781385c40d6ca7662959a83d7c2fb10b6b1c1fc_2_690x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f781385c40d6ca7662959a83d7c2fb10b6b1c1fc_2_1035x457.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f781385c40d6ca7662959a83d7c2fb10b6b1c1fc_2_1380x610.png 2x" data-dominant-color="AEB0B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×847 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2022-12-17 19:27 UTC)

<p>The pathology (green) is detected well:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5127acb5e30361c20d47bc545c706f40c6384497.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5127acb5e30361c20d47bc545c706f40c6384497.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5127acb5e30361c20d47bc545c706f40c6384497.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #3 by @Gonzalo_Rojas_Costa (2022-12-21 15:02 UTC)

<p>What minimum version of Slicer is required to run this new version of Lung CT Analyzer?</p>

---

## Post #4 by @rbumm (2022-12-21 15:48 UTC)

<p>3D Slicer 5.2.1 stable and a CUDA-enabled Nvidia GPU (RTX1060 or better) are recommended and well tested.</p>

---

## Post #5 by @AldairLegua (2024-07-28 22:26 UTC)

<p>Saludos, una consulta este analisis podria compararse al analisis para covid 19 ?.</p>
<p>Gracias</p>

---

## Post #6 by @rbumm (2024-07-30 09:40 UTC)

<p>Yes, the emphysema analysis is similar to the COVID analysis. In this case, the percentage of low lung tissue densities is measured.</p>

---
