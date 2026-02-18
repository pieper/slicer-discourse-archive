# How to fix the y-axis of a plot module chart?

**Topic ID**: 29958
**Date**: 2023-06-10
**URL**: https://discourse.slicer.org/t/how-to-fix-the-y-axis-of-a-plot-module-chart/29958

---

## Post #1 by @David.Xu (2023-06-10 06:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16e4fb4fd0feb11205ab95aef9daec48786a5c03.png" data-download-href="/uploads/short-url/3gx5UwNEmWjV59BKLXTierNQBIT.png?dl=1" title="1686361324738" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16e4fb4fd0feb11205ab95aef9daec48786a5c03_2_690x387.png" alt="1686361324738" data-base62-sha1="3gx5UwNEmWjV59BKLXTierNQBIT" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16e4fb4fd0feb11205ab95aef9daec48786a5c03_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16e4fb4fd0feb11205ab95aef9daec48786a5c03.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16e4fb4fd0feb11205ab95aef9daec48786a5c03.png 2x" data-dominant-color="393F4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1686361324738</span><span class="informations">953×535 23.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3ac8fa7daff8d9a3c2f97940f1c794f468338b4.png" data-download-href="/uploads/short-url/ucysk4p3kHO8kgQFfry3Ypcbbfu.png?dl=1" title="1686361344376" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3ac8fa7daff8d9a3c2f97940f1c794f468338b4_2_690x388.png" alt="1686361344376" data-base62-sha1="ucysk4p3kHO8kgQFfry3Ypcbbfu" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3ac8fa7daff8d9a3c2f97940f1c794f468338b4_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3ac8fa7daff8d9a3c2f97940f1c794f468338b4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3ac8fa7daff8d9a3c2f97940f1c794f468338b4.png 2x" data-dominant-color="3A3F4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1686361344376</span><span class="informations">953×536 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I fix the y-axis coordinates from 0 to 2?</p>

---

## Post #2 by @rbumm (2023-06-10 14:46 UTC)

<p>You can use the “Plots” module and set the y-axis range like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffdeff94b7bcae140b696ebbff80d9856c7c9626.png" data-download-href="/uploads/short-url/AvxwEQaRkATlUEn6E9ux103WETk.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffdeff94b7bcae140b696ebbff80d9856c7c9626_2_690x280.png" alt="image" data-base62-sha1="AvxwEQaRkATlUEn6E9ux103WETk" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffdeff94b7bcae140b696ebbff80d9856c7c9626_2_690x280.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffdeff94b7bcae140b696ebbff80d9856c7c9626_2_1035x420.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffdeff94b7bcae140b696ebbff80d9856c7c9626_2_1380x560.png 2x" data-dominant-color="EBEBE7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×780 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @pearsonm (2023-06-11 00:07 UTC)

<p>If you want to use Python there is also an example in the script repository <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#using-slicer-util-plot-utility-function" rel="noopener nofollow ugc">Using slicer.util.plot() utility function</a></p>

---

## Post #4 by @David.Xu (2023-06-11 13:56 UTC)

<p>thank you for your replies, it’s done right now.</p>

---
