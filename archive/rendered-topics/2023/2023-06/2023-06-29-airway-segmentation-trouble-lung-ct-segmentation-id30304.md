---
topic_id: 30304
title: "Airway Segmentation Trouble Lung Ct Segmentation"
date: 2023-06-29
url: https://discourse.slicer.org/t/30304
---

# Airway segmentation trouble - Lung CT Segmentation

**Topic ID**: 30304
**Date**: 2023-06-29
**URL**: https://discourse.slicer.org/t/airway-segmentation-trouble-lung-ct-segmentation/30304

---

## Post #1 by @phpg (2023-06-29 16:16 UTC)

<p>Hi everyone,</p>
<p>I have been using the Lung CT Segmenter without any trouble to initiate the segmentation. However, I recently encountered an issue with the airway segmentation. The problem is that the algorithm is including the entire lung as part of the airway segment (refer to the attached images). I have attempted to adjust the level of detail (low, medium, high) and lung threshold, but I haven’t been successful in resolving the problem. The airway segmentation appears to be correct during the marking process, but when I click “Apply” to finalize the changes, the problem arises.<br>
Could anyone please help me understand what I might be doing wrong or provide a solution to this issue? Your assistance would be greatly appreciated.</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa873168b84efa0a984fc6b3ede94ac700e4c4f3.jpeg" data-download-href="/uploads/short-url/okyOOJZzRmW4j1DhZHRL8lVdPWj.jpeg?dl=1" title="Captura de Tela 2023-06-29 às 08.46.33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa873168b84efa0a984fc6b3ede94ac700e4c4f3_2_517x318.jpeg" alt="Captura de Tela 2023-06-29 às 08.46.33" data-base62-sha1="okyOOJZzRmW4j1DhZHRL8lVdPWj" width="517" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa873168b84efa0a984fc6b3ede94ac700e4c4f3_2_517x318.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa873168b84efa0a984fc6b3ede94ac700e4c4f3_2_775x477.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa873168b84efa0a984fc6b3ede94ac700e4c4f3_2_1034x636.jpeg 2x" data-dominant-color="AEAFAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Tela 2023-06-29 às 08.46.33</span><span class="informations">1920×1181 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e631e8a68434fa73fc6485ee99c47c537dbce7.jpeg" data-download-href="/uploads/short-url/cPhGufzM35nrToIOLZzRpwPMlJZ.jpeg?dl=1" title="Captura de Tela 2023-06-29 às 09.44.40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e631e8a68434fa73fc6485ee99c47c537dbce7_2_517x321.jpeg" alt="Captura de Tela 2023-06-29 às 09.44.40" data-base62-sha1="cPhGufzM35nrToIOLZzRpwPMlJZ" width="517" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e631e8a68434fa73fc6485ee99c47c537dbce7_2_517x321.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e631e8a68434fa73fc6485ee99c47c537dbce7_2_775x481.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59e631e8a68434fa73fc6485ee99c47c537dbce7_2_1034x642.jpeg 2x" data-dominant-color="B4B9BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Tela 2023-06-29 às 09.44.40</span><span class="informations">1920×1195 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2023-06-29 17:35 UTC)

<p>Are you using the latest version of the extension ? Try “very low detail” please.</p>

---

## Post #3 by @phpg (2023-06-29 17:55 UTC)

<p>Version: Chest CTAnalyzer e72868C (published: 22.02.2023)</p>
<p>Tried very low detail, but did not solve the problem.</p>

---

## Post #4 by @rbumm (2023-06-29 18:03 UTC)

<p>What does the LungCTAnalyzer version number display please?</p>

---

## Post #5 by @phpg (2023-06-29 18:12 UTC)

<p>Sorry, the version I posted some minutes ago concern Lung CT Analyzer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e337233ec69283e721dab9d83fc0a33fc6f96e3.jpeg" data-download-href="/uploads/short-url/fISK9W61RIDzogjx8E28x13RHDt.jpeg?dl=1" title="Captura de Tela 2023-06-29 às 15.12.19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e337233ec69283e721dab9d83fc0a33fc6f96e3_2_517x280.jpeg" alt="Captura de Tela 2023-06-29 às 15.12.19" data-base62-sha1="fISK9W61RIDzogjx8E28x13RHDt" width="517" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e337233ec69283e721dab9d83fc0a33fc6f96e3_2_517x280.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e337233ec69283e721dab9d83fc0a33fc6f96e3_2_775x420.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e337233ec69283e721dab9d83fc0a33fc6f96e3_2_1034x560.jpeg 2x" data-dominant-color="F1F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Tela 2023-06-29 às 15.12.19</span><span class="informations">1920×1043 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @rbumm (2023-06-29 18:54 UTC)

<p>Try to crop the volume and please try standard datasets. If necessary please share the data if you can.</p>

---
