---
topic_id: 37497
title: "How To Enable Nvidia Gpu Support For Various Operations"
date: 2024-07-22
url: https://discourse.slicer.org/t/37497
---

# How to enable NVidia GPU support for various operations

**Topic ID**: 37497
**Date**: 2024-07-22
**URL**: https://discourse.slicer.org/t/how-to-enable-nvidia-gpu-support-for-various-operations/37497

---

## Post #1 by @Figaya (2024-07-22 13:59 UTC)

<p>Hello,</p>
<p>I have come across a few posts that explain how to enable the NVidia GPU in 3D Slicer, but they focus solely on volume rendering.</p>
<p>For our specific use case, I intend to harness the NVidia GPU for segmentation and 3D segmentation tasks. We handle extremely large and complex datasets that heavily burden the CPU, utilizing almost 100% of its capacity.</p>
<p>Could you please advise on how to enable the NVidia GPU for segmentation?</p>

---

## Post #2 by @muratmaga (2024-07-22 14:53 UTC)

<p>There is no GPU based segmentation algorithms that I know of. Where the field has moved, is to use GPUs to train complex segmentation models that can be reused to create similar segmentations from new dataset much faster. Examples of those in Slicer are:</p>
<p>TotalSegmentator<br>
DentalSegmentator<br>
MEMOS<br>
Auto3DSeg<br>
MonaiLabel</p>
<p>If you can describe your segmentation task and needs more clearly we can probably provide better guidance.</p>

---

## Post #3 by @Figaya (2024-07-23 05:26 UTC)

<p>Thank you for your input.</p>
<p>I was asking in the context of non-AI-based segmentation. For instance, is it possible to utilize GPU in slicer for operations such as painting, filling between slices etc., directly in 3D, as well as for 3D interaction?</p>

---

## Post #4 by @muratmaga (2024-07-23 05:51 UTC)

<aside class="quote no-group" data-username="Figaya" data-post="3" data-topic="37497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/eb9ed0/48.png" class="avatar"> Figaya:</div>
<blockquote>
<p>For instance, is it possible to utilize GPU in slicer for operations such as painting, filling between slices etc</p>
</blockquote>
</aside>
<p>Those basic image manipulation operations are already very optimized and multithreaded and works really fast in Slicer, with a sufficiently new CPU. I suspect nobody has seen any need for the additional complexity of implementing them on GPU. So the answer is no.</p>
<aside class="quote no-group" data-username="Figaya" data-post="3" data-topic="37497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/eb9ed0/48.png" class="avatar"> Figaya:</div>
<blockquote>
<p>directly in 3D, as well as for 3D interaction?</p>
</blockquote>
</aside>
<p>I am not sure what do you mean by this?</p>

---

## Post #6 by @MJamal (2024-07-23 06:03 UTC)

<p>There is a <a href="https://discourse.slicer.org/t/can-i-choose-which-gpu-to-use/3149/5">post</a> that mentions enabling Nvidia GPUs for large meshes as well. I hope this is what you’re looking for.</p>

---

## Post #7 by @lassoan (2024-07-23 18:20 UTC)

<p><a class="mention" href="/u/figaya">@Figaya</a> as <a class="mention" href="/u/muratmaga">@muratmaga</a> wrote above, the current implementation is generally sufficiently optimized to work acceptably for common segmentation workflows on commonly used data sets. It is possible that your data, or how you are trying to use the application is somehow special and so the application performance is not optimal.</p>
<p>If you provide more details on what exactly is slower than expected then we may be able to give advice on how to improve. For example, if updates are slow when “Show 3D” is enabled then you can solve that (make update 10-100x faster) by enabling the experimental “Surface Nets” method for mesh generation and smoothing.</p>

---
