---
topic_id: 33954
title: "Vmtk Extract Centerline Extracts Centerline Curves With Both"
date: 2024-01-24
url: https://discourse.slicer.org/t/33954
---

# VMTK Extract Centerline extracts centerline curves with both a curve and a straight line

**Topic ID**: 33954
**Date**: 2024-01-24
**URL**: https://discourse.slicer.org/t/vmtk-extract-centerline-extracts-centerline-curves-with-both-a-curve-and-a-straight-line/33954

---

## Post #1 by @ruili (2024-01-24 16:20 UTC)

<p>Hello! I have been using the Extract Centerline module from the SlicerVMTK extension to extract the centerline of a vessel struction. The extracted ‘Centerline Model’ is relatively accurate, however, the ‘Centerline Curves’ for each branch sometimes has a straight line right next to the curve. I am attaching screenshots from my scene here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cfbe2b36d6cf95f982117d0c3eb6d112ee4ef96.png" data-download-href="/uploads/short-url/hPERR2QTd6CTdURvEvhl9LUC1dY.png?dl=1" title="Screenshot 2024-01-24 at 16.03.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cfbe2b36d6cf95f982117d0c3eb6d112ee4ef96_2_491x500.png" alt="Screenshot 2024-01-24 at 16.03.29" data-base62-sha1="hPERR2QTd6CTdURvEvhl9LUC1dY" width="491" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cfbe2b36d6cf95f982117d0c3eb6d112ee4ef96_2_491x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cfbe2b36d6cf95f982117d0c3eb6d112ee4ef96.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cfbe2b36d6cf95f982117d0c3eb6d112ee4ef96.png 2x" data-dominant-color="18190A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-01-24 at 16.03.29</span><span class="informations">727×740 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In the above screenshot, the surface model is yellow, bright green is the ‘Centerline Model’, and purple line is one of the ‘Centerline Curves’. Note how a part of it follows the centerline model correctly, but it also has another straight line directly connecting the endpoint and the branching point.</p>
<p>Does any one know what is causing this problem by any chance? This problem is different from <a href="https://discourse.slicer.org/t/vmtk-centerline-extraction-trouble/16983/2">this post</a> where the centerline curve is completely a straight line.</p>
<p>Many thanks,</p>
<p>Rui</p>

---

## Post #2 by @chir.set (2024-01-24 16:36 UTC)

<aside class="quote no-group" data-username="ruili" data-post="1" data-topic="33954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> ruili:</div>
<blockquote>
<p>what is causing this problem by any chance</p>
</blockquote>
</aside>
<p>This has been <a href="https://github.com/vmtk/SlicerExtension-VMTK/commit/d51df8201c24100a225d8155ed1ab837b484dcf6" rel="noopener nofollow ugc">fixed</a> and should not happen in a preview build. Please ensure you are using the latest preview build.</p>

---

## Post #3 by @ruili (2024-01-25 16:17 UTC)

<p>I see. Thank you! Just for everyone else’s information, I was using slicer version 5.6.1 released on 2023-12-12, so you should use a newer version <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
