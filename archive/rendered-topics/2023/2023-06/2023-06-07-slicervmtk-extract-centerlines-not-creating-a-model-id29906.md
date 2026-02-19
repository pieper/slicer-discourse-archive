---
topic_id: 29906
title: "Slicervmtk Extract Centerlines Not Creating A Model"
date: 2023-06-07
url: https://discourse.slicer.org/t/29906
---

# SlicerVMTK Extract Centerlines Not Creating a Model

**Topic ID**: 29906
**Date**: 2023-06-07
**URL**: https://discourse.slicer.org/t/slicervmtk-extract-centerlines-not-creating-a-model/29906

---

## Post #1 by @darsh (2023-06-07 22:15 UTC)

<p>Hi, I started using Slicer recently to create a model of pulmonary arteries and arterioles. After creating my segmentation and cleaning it up, I’m trying to use the SlicerVMTK extension to find centerlines for each vessels. I set a couple of manual endpoints and then use the auto-detect feature. Then, I check the end of each vessel and make sure it has a node. In the Outputs tab, I create a new Centerline model under the ‘Tree’ tab. After applying, Slicer loads for a bit and my segmentation becomes opaque, but no centerlines ever appear. I have also tried different combinations of network curves, network models, tree curves, and tree models, and only the network curves populate centerlines. This doesn’t work for my project since I need to export the centerlines as a .vtp file, which the curves can’t do. Other times, the centerlines miss lots of vessels and branch at random places. Any help is appreciated!</p>

---

## Post #2 by @lassoan (2023-06-07 22:24 UTC)

<aside class="quote no-group" data-username="darsh" data-post="1" data-topic="29906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/73ab20/48.png" class="avatar"> darsh:</div>
<blockquote>
<p>I set a couple of manual endpoints and then use the auto-detect feature</p>
</blockquote>
</aside>
<p>If you specify manual endpoints first then run auto-detect, then auto-detect will remove your manually specified endpoints.</p>
<p>Normally you either use auto-detect (and then delete or slightly move endpoints) or you specify endpoints manually.</p>
<aside class="quote no-group" data-username="darsh" data-post="1" data-topic="29906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/73ab20/48.png" class="avatar"> darsh:</div>
<blockquote>
<p>After applying, Slicer loads for a bit and my segmentation becomes opaque, but no centerlines ever appear.</p>
</blockquote>
</aside>
<p>If the endpoints are set reasonably then I don’t know why this would happen. We can have a look if you share your data or at least screenshots (make sure that no patient information is shared).</p>
<aside class="quote no-group" data-username="darsh" data-post="1" data-topic="29906">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/73ab20/48.png" class="avatar"> darsh:</div>
<blockquote>
<p>I have also tried different combinations of network curves, network models, tree curves, and tree models, and only the network curves populate centerlines.</p>
</blockquote>
</aside>
<p>Network models and curves use the same method, so if you can get the result as curves then you can get the result as model as well. Make sure you select unique output nodes (don’t use the same node as input or centerline output or network output).</p>

---

## Post #3 by @darsh (2023-06-08 12:44 UTC)

<p>Here is are some pictures after adding endpoints and applying the centerlineModel:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7302f0ffe22b88dd9971e385b03212cebc12d800.jpeg" data-download-href="/uploads/short-url/gprd5cKGCc6M8p2yWwHLAHEWUlW.jpeg?dl=1" title="Screenshot 2023-06-08 at 8.23.08 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7302f0ffe22b88dd9971e385b03212cebc12d800_2_690x431.jpeg" alt="Screenshot 2023-06-08 at 8.23.08 AM" data-base62-sha1="gprd5cKGCc6M8p2yWwHLAHEWUlW" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7302f0ffe22b88dd9971e385b03212cebc12d800_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7302f0ffe22b88dd9971e385b03212cebc12d800_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7302f0ffe22b88dd9971e385b03212cebc12d800_2_1380x862.jpeg 2x" data-dominant-color="B8B4D0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-08 at 8.23.08 AM</span><span class="informations">1920×1200 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f387bde110c09e71f03628ecf9b47296c7ba980.jpeg" data-download-href="/uploads/short-url/kqZifB2u2a3eeNBfRDolvQZx0ZO.jpeg?dl=1" title="extractCenterlineFrontalPic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f387bde110c09e71f03628ecf9b47296c7ba980_2_603x500.jpeg" alt="extractCenterlineFrontalPic" data-base62-sha1="kqZifB2u2a3eeNBfRDolvQZx0ZO" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f387bde110c09e71f03628ecf9b47296c7ba980_2_603x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f387bde110c09e71f03628ecf9b47296c7ba980_2_904x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f387bde110c09e71f03628ecf9b47296c7ba980_2_1206x1000.jpeg 2x" data-dominant-color="9A91BE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">extractCenterlineFrontalPic</span><span class="informations">1672×1386 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc463a14a6a2138029c887d5299025e83eedfc28.jpeg" data-download-href="/uploads/short-url/zZIMxDBiIK2IA98bSRo4jpMb8YU.jpeg?dl=1" title="posteriorViewEndpointsAfterCenterlines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc463a14a6a2138029c887d5299025e83eedfc28_2_603x500.jpeg" alt="posteriorViewEndpointsAfterCenterlines" data-base62-sha1="zZIMxDBiIK2IA98bSRo4jpMb8YU" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc463a14a6a2138029c887d5299025e83eedfc28_2_603x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc463a14a6a2138029c887d5299025e83eedfc28_2_904x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc463a14a6a2138029c887d5299025e83eedfc28_2_1206x1000.jpeg 2x" data-dominant-color="9C92C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">posteriorViewEndpointsAfterCenterlines</span><span class="informations">1672×1386 348 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(I turned the opacity up to better see the endpoints here)</p>

---

## Post #4 by @darsh (2023-06-08 12:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c82fd7536c38b74af8414db1be124f34baacc81.jpeg" data-download-href="/uploads/short-url/dcoztA1IR0WELH34zLPEMLSvhYJ.jpeg?dl=1" title="leftViewAfterExtractCenterlines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c82fd7536c38b74af8414db1be124f34baacc81_2_684x500.jpeg" alt="leftViewAfterExtractCenterlines" data-base62-sha1="dcoztA1IR0WELH34zLPEMLSvhYJ" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c82fd7536c38b74af8414db1be124f34baacc81_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c82fd7536c38b74af8414db1be124f34baacc81_2_1026x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c82fd7536c38b74af8414db1be124f34baacc81_2_1368x1000.jpeg 2x" data-dominant-color="9C92BD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">leftViewAfterExtractCenterlines</span><span class="informations">1898×1386 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5a1bca65f68d3c00ec999698965df5c1f83d40d.jpeg" data-download-href="/uploads/short-url/z2XuZZQIUdukxWsETcO29lVNay1.jpeg?dl=1" title="rightViewAfterExtractCenterlines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a1bca65f68d3c00ec999698965df5c1f83d40d_2_684x500.jpeg" alt="rightViewAfterExtractCenterlines" data-base62-sha1="z2XuZZQIUdukxWsETcO29lVNay1" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a1bca65f68d3c00ec999698965df5c1f83d40d_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a1bca65f68d3c00ec999698965df5c1f83d40d_2_1026x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a1bca65f68d3c00ec999698965df5c1f83d40d_2_1368x1000.jpeg 2x" data-dominant-color="9B92BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rightViewAfterExtractCenterlines</span><span class="informations">1898×1386 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
