---
topic_id: 27302
title: "Change In Volume Comparison"
date: 2023-01-17
url: https://discourse.slicer.org/t/27302
---

# Change in volume comparison

**Topic ID**: 27302
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/change-in-volume-comparison/27302

---

## Post #1 by @Chiemsee (2023-01-17 15:01 UTC)

<p>Hello community!</p>
<p>I’ve been using Slicer quite extensively for segmentation for pediatric cardiac surgery the last years and have a new challenge now:<br>
To see how wounds evolve in time, I’m looking for a way to compare 3D-Scans taken at different stages regarding changes in volume. The output should be visual (e.g. the new tissue that has built) and qualitative.</p>
<p>What functions/addons can you recommend for this?</p>
<p>Thanks. Alexander<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14faaa6a8c34f2cb07d8d0418d1407b7cf2b776.png" data-download-href="/uploads/short-url/yqJKPlynaoLng3ttew7fGmwkHlk.png?dl=1" title="foot1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f14faaa6a8c34f2cb07d8d0418d1407b7cf2b776_2_669x500.png" alt="foot1" data-base62-sha1="yqJKPlynaoLng3ttew7fGmwkHlk" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f14faaa6a8c34f2cb07d8d0418d1407b7cf2b776_2_669x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14faaa6a8c34f2cb07d8d0418d1407b7cf2b776.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14faaa6a8c34f2cb07d8d0418d1407b7cf2b776.png 2x" data-dominant-color="737474"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">foot1</span><span class="informations">767×573 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63f3cc4a1044b17f1716cb9051504bf802c05779.png" data-download-href="/uploads/short-url/egdBthp2TtwURXL3rYj3CnuUMXL.png?dl=1" title="foot2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63f3cc4a1044b17f1716cb9051504bf802c05779_2_595x500.png" alt="foot2" data-base62-sha1="egdBthp2TtwURXL3rYj3CnuUMXL" width="595" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63f3cc4a1044b17f1716cb9051504bf802c05779_2_595x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63f3cc4a1044b17f1716cb9051504bf802c05779.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63f3cc4a1044b17f1716cb9051504bf802c05779.png 2x" data-dominant-color="767676"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">foot2</span><span class="informations">723×607 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-01-17 19:20 UTC)

<p>You could start from trying to reproduce some of the commonly used quantifiable characteristics of wound healing. For example, you could measure granulation/necrotic/slough surface area and how it is changing in time.</p>
<p>You can load the surface scan with full color texture into Slicer (using TextureModel module of SlicerIGT extension) and draw a closed curve using Markups module to annotate areas. You can then use surface area measurement of the closed curve (or if the surface is not flat then cut out the surface patch using Dynamic modeler module and get the surface area of the patch in Models module).</p>

---
