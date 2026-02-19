---
topic_id: 43785
title: "Is It Possible To Use Closed Curve Node To Cut Segmentatin N"
date: 2025-07-20
url: https://discourse.slicer.org/t/43785
---

# Is it possible to use closed curve node to cut segmentatin node or model node?

**Topic ID**: 43785
**Date**: 2025-07-20
**URL**: https://discourse.slicer.org/t/is-it-possible-to-use-closed-curve-node-to-cut-segmentatin-node-or-model-node/43785

---

## Post #1 by @jay1987 (2025-07-20 13:36 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2b95437d2c51e0733ed30d4ec46b9a045e82a2a.jpeg" data-download-href="/uploads/short-url/yDeC1IwNdNvi55YIukSxqxqr2XM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2b95437d2c51e0733ed30d4ec46b9a045e82a2a.jpeg" alt="image" data-base62-sha1="yDeC1IwNdNvi55YIukSxqxqr2XM" width="452" height="386"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">452×386 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i have a closed curve node on a segmentation node , is it possible to use curved node to cut the segmentation node use script like the function of scissors?</p>

---

## Post #2 by @muratmaga (2025-07-20 13:42 UTC)

<p>Yes. Dynamic modeler module does that.</p>

---

## Post #3 by @jay1987 (2025-07-20 14:30 UTC)

<p>thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> !!</p>

---

## Post #4 by @jay1987 (2025-07-20 16:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6aaffe85e010c503b50d2a8bd272c2686e93a49b.jpeg" data-download-href="/uploads/short-url/fdNG1kQe5ILQSTTMoDkPBOXu3KH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6aaffe85e010c503b50d2a8bd272c2686e93a49b.jpeg" alt="image" data-base62-sha1="fdNG1kQe5ILQSTTMoDkPBOXu3KH" width="499" height="459"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">499×459 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
is it possible to make this segmentation strickly in side the curve node</p>

---

## Post #5 by @mau_igna_06 (2025-07-20 23:11 UTC)

<p>Hi, I think this should help:</p><aside class="quote quote-modified" data-post="6" data-topic="10384">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/mesh-multiple-objects/10384/6">Mesh multiple objects</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    With latest “curve drawing on surface” feature (to be announced next week, but already available in latest Slicer Preview Release) you can extract one side of a surface very easily: 

Draw a closed curve on the surface
Make the curve snap to surface (enable Markups module / Curve settings / Curve type → shortest distance on surface, model node → model node that you would like to cut)
Copy-paste this code snippet to the Python console

# Get input data
curveNode = getNode('C')
modelNode = getNode…
  </blockquote>
</aside>


---
