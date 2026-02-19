---
topic_id: 12184
title: "Positioning Models"
date: 2020-06-23
url: https://discourse.slicer.org/t/12184
---

# Positioning models

**Topic ID**: 12184
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/positioning-models/12184

---

## Post #1 by @Rodrigo_Visconti (2020-06-23 19:14 UTC)

<p>Please tell me how can I position a preprogrammed model in my segmentation easily. I’m having trouble doing it. Thanks</p>

---

## Post #2 by @lassoan (2020-06-23 20:16 UTC)

<p>What do you mean by a “preprogrammed model”?</p>

---

## Post #3 by @Rodrigo_Visconti (2020-06-23 20:33 UTC)

<p>I mean a model to make the border of my segmentation to fit into other printed piece. I made a support for my printed valves and I need to align them. The border has this meaning.</p>

---

## Post #4 by @Rodrigo_Visconti (2020-06-23 20:36 UTC)

<p>This border is in stl format.</p>

---

## Post #5 by @lassoan (2020-06-23 21:23 UTC)

<p>Can you post screenshots or some other illustrations of what you want to achieve?</p>

---

## Post #6 by @Rodrigo_Visconti (2020-06-23 21:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b63d815dda14df99f3670bee0f64b30128aa88d5.jpeg" data-download-href="/uploads/short-url/q0aFND3pyFTRQ1k3E89RRkXzt2d.jpeg?dl=1" title="20200623_183412" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b63d815dda14df99f3670bee0f64b30128aa88d5_2_690x335.jpeg" alt="20200623_183412" data-base62-sha1="q0aFND3pyFTRQ1k3E89RRkXzt2d" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b63d815dda14df99f3670bee0f64b30128aa88d5_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b63d815dda14df99f3670bee0f64b30128aa88d5_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b63d815dda14df99f3670bee0f64b30128aa88d5_2_1380x670.jpeg 2x" data-dominant-color="6C6D70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20200623_183412</span><span class="informations">4032×1960 1.32 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The grey is the model I want to compare and the brown is the segmentation how to align both? I’m trying with transforms but I’m losing much time with it</p>

---

## Post #7 by @lassoan (2020-06-23 21:50 UTC)

<p>Visual alignment of 3D shapes on a 2D screen is very inaccurate and time-consuming.</p>
<p>For your case, a much better and faster registration method is marking corresponding points on the objects and computing transform using Fiducial Registration Wizard module (in SlicerIGT extension).</p>

---

## Post #8 by @Rodrigo_Visconti (2020-06-23 22:05 UTC)

<p>Thanks. Do you have any tutorial about this issue?</p>

---

## Post #9 by @lassoan (2020-06-26 01:58 UTC)

<p>I’ve created a short video that shows how to use Fiducial registration wizard:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="TBHr2wizGTM" data-video-title="Align 3D objects using landmarks in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=TBHr2wizGTM" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/TBHr2wizGTM/maxresdefault.jpg" title="Align 3D objects using landmarks in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #10 by @lassoan (2020-06-26 15:28 UTC)

<p>A post was merged into an existing topic: <a href="/t/leaflet-mold-generator/8696/18">Leaflet mold generator</a></p>

---

## Post #11 by @Rodrigo_Visconti (2020-06-29 02:47 UTC)

<p>Thanks. Much easier and very helpful</p>

---
