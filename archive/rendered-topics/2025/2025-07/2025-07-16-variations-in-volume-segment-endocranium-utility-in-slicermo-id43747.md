---
topic_id: 43747
title: "Variations In Volume Segment Endocranium Utility In Slicermo"
date: 2025-07-16
url: https://discourse.slicer.org/t/43747
---

# Variations in Volume: Segment Endocranium Utility in Slicermorph

**Topic ID**: 43747
**Date**: 2025-07-16
**URL**: https://discourse.slicer.org/t/variations-in-volume-segment-endocranium-utility-in-slicermorph/43747

---

## Post #1 by @sck84 (2025-07-16 20:06 UTC)

<p>Hello,</p>
<p>I am segmenting the endocranial cavity of mouse skulls using the Segment Endocranium utility in SlicerMorph. I noticed that there are pretty significant differences in the resulting segments when I run it a series of times. I have not altered the parameters - I’m using 1.5mm for Smoothing kernel size, and 3.0mm for maximum hole size. After using the segment statistics module, I have found that the first run produces the smallest segment, with some aspects of the segment missing (compare the white segment with the others - material on the ventral surface is missing). The second produced the largest. I ran it four more times with the same parameters, changing nothing. All four were exactly the same (bone_solid (1-4)).</p>
<p>Is this normal? I expected some amount of variation, but do you have to run it three or more times to achieve an “average?”</p>
<p>Would I have better consistency when segmenting a large number of specimens if I used Wrap Solidify?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a9ea365d22557fd4e6dc09cf8eed314b9700466.jpeg" data-download-href="/uploads/short-url/cVEQTYv4epL0KMPShO8rD0A0CdE.jpeg?dl=1" title="Table" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a9ea365d22557fd4e6dc09cf8eed314b9700466_2_690x377.jpeg" alt="Table" data-base62-sha1="cVEQTYv4epL0KMPShO8rD0A0CdE" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a9ea365d22557fd4e6dc09cf8eed314b9700466_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a9ea365d22557fd4e6dc09cf8eed314b9700466_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a9ea365d22557fd4e6dc09cf8eed314b9700466_2_1380x754.jpeg 2x" data-dominant-color="A8A597"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Table</span><span class="informations">1920×1050 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62254921a5121ede147b6cf061cf5016ab7e25ea.jpeg" data-download-href="/uploads/short-url/e0eFVD7nb2oIB6yGaccuuB40GJY.jpeg?dl=1" title="bone_solid" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62254921a5121ede147b6cf061cf5016ab7e25ea_2_375x500.jpeg" alt="bone_solid" data-base62-sha1="e0eFVD7nb2oIB6yGaccuuB40GJY" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62254921a5121ede147b6cf061cf5016ab7e25ea_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62254921a5121ede147b6cf061cf5016ab7e25ea_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62254921a5121ede147b6cf061cf5016ab7e25ea_2_750x1000.jpeg 2x" data-dominant-color="71749D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bone_solid</span><span class="informations">1920×2560 1.1 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e393b079917571e8577089a806157f1ace890be.jpeg" data-download-href="/uploads/short-url/mzI3uoenVUdbvibhINlrNbcSUa2.jpeg?dl=1" title="bone_3_solid" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e393b079917571e8577089a806157f1ace890be_2_375x500.jpeg" alt="bone_3_solid" data-base62-sha1="mzI3uoenVUdbvibhINlrNbcSUa2" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e393b079917571e8577089a806157f1ace890be_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e393b079917571e8577089a806157f1ace890be_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e393b079917571e8577089a806157f1ace890be_2_750x1000.jpeg 2x" data-dominant-color="837798"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bone_3_solid</span><span class="informations">1920×2560 1.07 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e576722c97b1b7d5f65becdd3ebf68ba7f19836.jpeg" data-download-href="/uploads/short-url/i1Fq6BaKirmJQZx8UvlNE9Ajw6W.jpeg?dl=1" title="bone_5_solid" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e576722c97b1b7d5f65becdd3ebf68ba7f19836_2_375x500.jpeg" alt="bone_5_solid" data-base62-sha1="i1Fq6BaKirmJQZx8UvlNE9Ajw6W" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e576722c97b1b7d5f65becdd3ebf68ba7f19836_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e576722c97b1b7d5f65becdd3ebf68ba7f19836_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e576722c97b1b7d5f65becdd3ebf68ba7f19836_2_750x1000.jpeg 2x" data-dominant-color="7E7D87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bone_5_solid</span><span class="informations">1920×2560 988 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-07-16 20:23 UTC)

<aside class="quote no-group" data-username="sck84" data-post="1" data-topic="43747">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/898d66/48.png" class="avatar"> sck84:</div>
<blockquote>
<p>Would I have better consistency when segmenting a large number of specimens if I used Wrap Solidify?</p>
</blockquote>
</aside>
<p>Segment Endocranium uses WarpSolidify under the hood, so it won’t make any difference.</p>
<aside class="quote no-group" data-username="sck84" data-post="1" data-topic="43747">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/898d66/48.png" class="avatar"> sck84:</div>
<blockquote>
<p>I run it a series of times. I have not altered the parameters - I’m using 1.5mm for Smoothing kernel size, and 3.0mm for maximum hole size.</p>
</blockquote>
</aside>
<p>For real replicability, you should start from the scratch. From your screenshot, it is clear that you run the replicates in existing segmentation. Presence of other structures may change the outcome. So each time create a “new segmentation” before you execute the Segment Endocranium, and try. There should be no difference (unless you change the parameters)…</p>

---
