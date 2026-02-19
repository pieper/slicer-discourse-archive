---
topic_id: 44802
title: "How Do I Turn Inside Out An Model"
date: 2025-10-17
url: https://discourse.slicer.org/t/44802
---

# How do I "turn inside out" an model?

**Topic ID**: 44802
**Date**: 2025-10-17
**URL**: https://discourse.slicer.org/t/how-do-i-turn-inside-out-an-model/44802

---

## Post #1 by @eNable_Polska (2025-10-17 18:50 UTC)

<p>I’m tasked with creating a model of the airways, down to the smallest possible viewing distance. The initial study is an HRCT of the lungs. I used the “Lung CT Segmenter” tool with the “Airway segmentation,” “Use AI,” and “High detail” options. As a result, I achieved very good segmentation of the airways, but with the lungs included. I’ve attached a preview of the model with transparency enabled. How can I “remove the lungs” from this model while retaining the airways? Is there a way to do this in Slicer, or do I need to find another tool? Any ideas on how to do this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cec6bbd9fb5d7e602a0643543335e89ff79cffa.jpeg" data-download-href="/uploads/short-url/k6FngmnUGnycifXoyzvTRou5fWW.jpeg?dl=1" title="obraz" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cec6bbd9fb5d7e602a0643543335e89ff79cffa_2_528x500.jpeg" alt="obraz" data-base62-sha1="k6FngmnUGnycifXoyzvTRou5fWW" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cec6bbd9fb5d7e602a0643543335e89ff79cffa_2_528x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cec6bbd9fb5d7e602a0643543335e89ff79cffa_2_792x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cec6bbd9fb5d7e602a0643543335e89ff79cffa_2_1056x1000.jpeg 2x" data-dominant-color="A19EA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">obraz</span><span class="informations">1174×1111 311 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’d appreciate any advice on how to solve this problem.</p>
<p>Regards.</p>
<p>Krzysztof</p>

---

## Post #2 by @lassoan (2025-10-17 19:03 UTC)

<p>In this 3D rendering it looks like that you have a lung segment and an airways segment, both yellow. You can delete the lung segment if you don’t need it.</p>
<p>If you only have one segment then this rendering is very misleading. Attach a few screenshot of the slice views. If you have multiple segments then make sure each has a distinct color.</p>

---

## Post #3 by @eNable_Polska (2025-10-17 19:22 UTC)

<p>Unfortunately, this is just one segment, so there’s nothing to subtract <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I’ll anonymize the data and share the entire project; maybe you’ll figure out how to do it correctly.<br>
I can use other tools to create the airways, but I can’t get any further than the lobar bronchi. The Lung Segmenter can go deeper, but it connects the lungs to the airways.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/639b5915000dee7bdfd2a28657def63b15715a11.jpeg" data-download-href="/uploads/short-url/eda6gy4LpGv1e9dQ4uKekg3fkJz.jpeg?dl=1" title="obraz" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/639b5915000dee7bdfd2a28657def63b15715a11_2_630x500.jpeg" alt="obraz" data-base62-sha1="eda6gy4LpGv1e9dQ4uKekg3fkJz" width="630" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/639b5915000dee7bdfd2a28657def63b15715a11_2_630x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/639b5915000dee7bdfd2a28657def63b15715a11_2_945x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/639b5915000dee7bdfd2a28657def63b15715a11_2_1260x1000.jpeg 2x" data-dominant-color="848A95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">obraz</span><span class="informations">1460×1157 420 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @eNable_Polska (2025-10-17 19:49 UTC)

<p>link <a href="https://drive.google.com/file/d/1ZEFgQVluaBvTTIL_-GDM3A3owqfJJVSH/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1ZEFgQVluaBvTTIL_-GDM3A3owqfJJVSH/view?usp=sharing</a></p>

---

## Post #5 by @muratmaga (2025-10-18 04:32 UTC)

<p>You can’t really remove the lungs, because they are part of the segmentation. (you can try to further threshold the lowest range, but i suspect you will also loose details).</p>
<p>If you want to make the internal branches more prominent without altering the segmentation so that they are not occluded by lungs, then I think you want to explore Colorize Volume module in the Sandbox extension, which gives you more control over visualizations than surface based rendering in the segment editor.</p>
<p>Does this look more similar to what you want to do? I also probably use a slightly darker color than this light blue. You will probably have bit more contrast that way.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/352cd7a89313fef89b31e59cc5b415b86a623e73.jpeg" data-download-href="/uploads/short-url/7ApnA86dxoc81TFxxEjOxmqpIH1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/352cd7a89313fef89b31e59cc5b415b86a623e73_2_690x426.jpeg" alt="image" data-base62-sha1="7ApnA86dxoc81TFxxEjOxmqpIH1" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/352cd7a89313fef89b31e59cc5b415b86a623e73_2_690x426.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/352cd7a89313fef89b31e59cc5b415b86a623e73_2_1035x639.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/352cd7a89313fef89b31e59cc5b415b86a623e73.jpeg 2x" data-dominant-color="D0D3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×741 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I also encountered this error in the Colorize Volume. So we are limited to 16 segments max?</p>
<pre><code class="lang-auto">Links failed: ERROR: Implementation limit of 16 active fragment shader samplers (e.g., maximum number of supported image units) exceeded, fragment shader uses 18 samplers
</code></pre>

---

## Post #6 by @eNable_Polska (2025-10-18 05:57 UTC)

<p>Thanks for the tip, but I’m not interested in the visualization you can get with the colorization module. I can do that, and I’m familiar with this solution (very useful, by the way). The problem is that my surgeons are very insistent on creating a model with as many airway branches as possible, even down to the level of the segmental bronchi. While segmenting and modeling down to the level of the lobar bronchi is easy, I still can’t segment. Only in the Lung CT module… do I see further branches, but they’re connected to the lungs. And that’s a problem that needs to be solved.</p>
<p>Excuse my English, I work with a translator and sometimes write nonsense <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2025-10-21 04:56 UTC)

<p>I’ll look at the image data you shared, but before that I have a basic question: why the small airways are that inportant? The lung surgeons that I talked to were much more interested in the vasculature, especially the veins, as they designate the boundaries of segments. Bronchi and arteries are near the center of each segment, so if you want to plan and guide sublobar resections then they are not all that informative.</p>

---

## Post #8 by @eNable_Polska (2025-10-23 18:36 UTC)

<p>Two things:</p>
<ol>
<li>First, the surgeon’s attempt to go very deep into the airways resulted from overzealousness. He wanted to see the segmental bronchi with their blood vessels, he told me. After a long discussion, noting that this might be very difficult to achieve based on the available studies, we agreed that segmentation of the airways and circulatory system down to the level of the lobar bronchi (the so-called lung hilum) would be sufficient. When asked why he needed such a model, he replied that he wanted to view it in VR in various positions to help plan the patient’s positioning for thoracoscopy and lung surgery. In further discussion, we agreed that the range to the second division of the airways (the lobar bronchi) would be sufficient. Obtaining this range of segmentation is no longer a major problem; several AI-based tools can do it, and as a last resort, I use “nnintereactive” for manual segmentation. It seems this problem has been solved; performing segmentation in this range won’t be difficult.</li>
<li>In the example I added to the thread, it seemed to me that lobar and segmented bronchi were visible in the lung area. I created a full lung model and, through simple Boolean operations, obtained what I thought were bronchi. Then, using nninteractive, I segmented the trachea and measured the bronchi. And here’s the surprise! It turned out that the manually segmented bronchi didn’t match what the Lung segmenter had identified as the respiratory tract. I think this is the circulatory system, not the bronchi. This is difficult to assess objectively because HRCT of the lungs is non-contrast.</li>
</ol>
<p>An additional problem in our case is that we work with children, and most AI tools designed for larger patients “go haywire” when working with children, especially small newborns. In such cases, the only work required is manual labor.</p>

---
