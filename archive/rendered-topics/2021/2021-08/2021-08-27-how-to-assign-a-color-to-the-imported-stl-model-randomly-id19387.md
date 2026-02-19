---
topic_id: 19387
title: "How To Assign A Color To The Imported Stl Model Randomly"
date: 2021-08-27
url: https://discourse.slicer.org/t/19387
---

# How to assign a color to the imported stl model randomly ？

**Topic ID**: 19387
**Date**: 2021-08-27
**URL**: https://discourse.slicer.org/t/how-to-assign-a-color-to-the-imported-stl-model-randomly/19387

---

## Post #1 by @slicer365 (2021-08-27 11:31 UTC)

<p>When I import a 3D model into Slicer,</p>
<p>it will be assigned yellow by default.</p>
<p>When I import many models, all the models are yellow and need to be manually adjusted to different colors one by one.</p>
<p>Is there a way to make the color of each model random?</p>

---

## Post #2 by @lassoan (2021-08-27 22:05 UTC)

<p>Can you tell a bit more about your use case?</p>
<p>Do your really want random or you want to assign standard colors? We have color tables for anatomical structures, wouldn’t want to use these more meaningful colors instead?</p>
<p>How do you end up with many STL files? What do they contain? What do you want to do with them after loading?</p>

---

## Post #3 by @slicer365 (2021-08-27 23:10 UTC)

<p>As this picture shows,</p>
<p>this is composed of many models,</p>
<p>I downloaded from other websites,</p>
<p>but I need to import these models into Slicer for adjustment,</p>
<p>so I need to assign different colors to distinguish<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8b15ac20bcf717edeeeef3cf6569a6665ef25a.jpeg" alt="捕获" data-base62-sha1="zTfPCsVwcWxu8WvxFXy512E9Zfc" width="215" height="212"></p>
<p>In addition, when I use the Creat  Model module to create different models,colors are yellow by default. In order to distinguish different models, I need to manually assign colors.I think this is unreasonable.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac6c8ede3970152fdb786d5232064ded3513a757.jpeg" data-download-href="/uploads/short-url/oBkHZqgxm7neFLbGWlWTveMbfwP.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac6c8ede3970152fdb786d5232064ded3513a757_2_517x216.jpeg" alt="捕获" data-base62-sha1="oBkHZqgxm7neFLbGWlWTveMbfwP" width="517" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac6c8ede3970152fdb786d5232064ded3513a757_2_517x216.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac6c8ede3970152fdb786d5232064ded3513a757_2_775x324.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac6c8ede3970152fdb786d5232064ded3513a757_2_1034x432.jpeg 2x" data-dominant-color="C8C9DE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1331×558 74.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-08-27 23:36 UTC)

<p>Randomly assigning a color would be easy but would result in non-deterministic result of data loading. The colors that you choose for models are not just deterministic but also meaningful (e.g., red is arterial tree, blue is venous; other colors are chosen to have good contrast when overlaid the basic colors).</p>
<p>When you specify what a model node represents (by double-clicking on the colored rectangle) then a meaningful color is assigned to it automatically. You can specify your own list of terms if the standard terms do not contain everything that you need. You can also write a short script that assigns standard terms (and therefore colors) to nodes based on their names.</p>
<p>Maybe a subject hierarchy context menu action could be added that would assign random colors (or somewhat random colors, for example it could assign similar colors to nodes in the same branch). You should be able to implement such features in Python quite easily and could be added to Sandbox extension and if it turns out to be useful to many people then it may be even added to Slicer core.</p>

---
