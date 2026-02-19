---
topic_id: 37284
title: "Understanding Fibertractmeasurements Output"
date: 2024-07-09
url: https://discourse.slicer.org/t/37284
---

# Understanding FiberTractMeasurements output

**Topic ID**: 37284
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/understanding-fibertractmeasurements-output/37284

---

## Post #1 by @Calth822 (2024-07-09 14:03 UTC)

<p>Hello, I following the WMA tutorial and I have understood all steps except for the last step of tutorial, " 8. Fiber tract diffusion measurements".</p>
<p>I have been able to follow the tutorial and extract the diffusion measurements to the CSV file as per the tutorial (see image)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d352545b3c9b18810b31d0b7f40747f684825b40.png" data-download-href="/uploads/short-url/u9r8stToLbFpLwDhOXM3nritfNe.png?dl=1" title="Screenshot 2024-07-08 194405" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d352545b3c9b18810b31d0b7f40747f684825b40_2_690x371.png" alt="Screenshot 2024-07-08 194405" data-base62-sha1="u9r8stToLbFpLwDhOXM3nritfNe" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d352545b3c9b18810b31d0b7f40747f684825b40_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d352545b3c9b18810b31d0b7f40747f684825b40_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d352545b3c9b18810b31d0b7f40747f684825b40_2_1380x742.png 2x" data-dominant-color="D4D4D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-08 194405</span><span class="informations">1921×1033 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However I do not understand some of the columns present in the file and I have not found any documentation to specify what they mean.</p>
<p>I understand the following columns:</p>
<ul>
<li>Num_points</li>
<li>Num_Fibers</li>
<li>Mean_Length</li>
<li>HemisphereLocation</li>
<li>cluster_idx</li>
</ul>
<p>But I am unsure of the following and why there are two of the same for some measurements when I assumed there should only be one:</p>
<ul>
<li>FA1</li>
<li>FA2</li>
<li>Trace1</li>
<li>Trace2</li>
</ul>
<p>Any help in understanding these columns would be greatly appreciated</p>

---

## Post #2 by @pieper (2024-07-09 15:14 UTC)

<p>There are two FA and Trace values because the pipeline uses the 2-tensor option of <a href="https://github.com/pnlbwh/ukftractography">UKF Tractography</a>.</p>

---
