---
topic_id: 18347
title: "Combining Surface Registration And Model To Model Distance F"
date: 2021-06-26
url: https://discourse.slicer.org/t/18347
---

# Combining surface registration and model-to-model distance functionalities

**Topic ID**: 18347
**Date**: 2021-06-26
**URL**: https://discourse.slicer.org/t/combining-surface-registration-and-model-to-model-distance-functionalities/18347

---

## Post #1 by @seanchoi0519 (2021-06-26 07:24 UTC)

<p>I have an established workflow and I’d like to streamline &amp; combine the functionalities of - ALPACA, model-to-model distance, and shape-population-viewer (in order).</p>
<p>For example, if possible, I’d like to take the product of ALPACA (aligned models) and automatically feed them into model-to-model distance for distance computation, in 1 click.</p>
<p>I noticed that Model-to-model distance module does not have .py file so I cannot edit/make changes. How can I best approach this? Any advice would be appreciated.</p>
<p>Model-to-model documentation: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Extensions/ModelToModelDistance - Slicer Wiki</a></p>

---

## Post #2 by @seanchoi0519 (2021-06-26 13:54 UTC)

<p>Andras, thanks for this piece of code - I was able to successfully integrate it into my code without having to use model-to-model &amp; shape population viewer.</p>
<p>There are just a few changes I’d like to make - it looks like with this piece of code it can only show a positive difference (for ex. the area where it’s the target model has been trimmed too much with respect to the source model, but not vice versa). How can I make it show a negative difference?</p>
<p>Also how can I alter the colour range? For example -0.5 to 0.5 similar to how it’s done in shape population viewer</p>
<p>thanks a lot</p>

---

## Post #3 by @lassoan (2021-06-26 14:31 UTC)

<p>The distance filter computes signed distance by default, so probably you just need to tune the color mapping.</p>

---

## Post #4 by @seanchoi0519 (2021-06-26 21:27 UTC)

<p>Thanks for the tip Andras. Would you know what piece of code I need to change the “Displayed Range” section? I’ve tried setScalarRange however it does not seem to change anything.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5944418f5bda8aa6056f1d2a4107e78447d284f0.png" data-download-href="/uploads/short-url/cJGJraX65wOx5BLX2spjkQlH9Ze.png?dl=1" title="Screen Shot 2021-06-27 at 8.15.17 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5944418f5bda8aa6056f1d2a4107e78447d284f0_2_690x220.png" alt="Screen Shot 2021-06-27 at 8.15.17 AM" data-base62-sha1="cJGJraX65wOx5BLX2spjkQlH9Ze" width="690" height="220" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5944418f5bda8aa6056f1d2a4107e78447d284f0_2_690x220.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5944418f5bda8aa6056f1d2a4107e78447d284f0_2_1035x330.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5944418f5bda8aa6056f1d2a4107e78447d284f0.png 2x" data-dominant-color="3B3C3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-27 at 8.15.17 AM</span><span class="informations">1300×416 36.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any advice would be great</p>

---

## Post #5 by @seanchoi0519 (2021-06-26 23:22 UTC)

<p>I would like to change it to “Manual” and range (-0.2, 0.2) through code.</p>

---

## Post #6 by @lassoan (2021-06-26 23:37 UTC)

<p>There are several color presets that display different colors for positive/negative values. You can also create custom ones as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-table">these examples</a>.</p>

---

## Post #7 by @seanchoi0519 (2021-06-27 05:02 UTC)

<p>Thank you, I’ve created a custom one by editing the .txt. file.<br>
Would you know how I can programatically alter the “Scalar Range Mode” and the “Displayed Range” as shown in the screenshot above?</p>

---

## Post #8 by @seanchoi0519 (2021-06-27 10:53 UTC)

<p>Issue resolved: this code worked.</p>
<pre><code>display.SetScalarRangeFlag(0) // returns 'manual'
display.SetScalarRange(-0.1, 0.1) // 'changes the range manually'</code></pre>

---
