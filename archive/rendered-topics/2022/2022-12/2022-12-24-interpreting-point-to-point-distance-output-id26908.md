---
topic_id: 26908
title: "Interpreting Point To Point Distance Output"
date: 2022-12-24
url: https://discourse.slicer.org/t/26908
---

# Interpreting point-to-point distance output

**Topic ID**: 26908
**Date**: 2022-12-24
**URL**: https://discourse.slicer.org/t/interpreting-point-to-point-distance-output/26908

---

## Post #1 by @muratmaga (2022-12-24 18:09 UTC)

<p>I am testing the fixed Model to Model distance extension. It can now calculate the point-to-point correspondence on windows. But I am having a hard time making sense of the resultant heatmap. As a reminder this is the same 3D model that a geometric transformation applied, resulting in a slightly different shape. This is the output I get.</p>
<p>Lets focus on the incisors as it displays the problem clearly. How can the front of the incisor is colored about -1.5mm, while the back of it is +1.5mm. The scalar plotted is the signed point to point distance.</p>
<p>If you measure approximately the corresponding distances on the source and target models, the magnitude of the difference at both front and back is right, but I don’t understand the sign difference in the model 2 model output.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75929504ceadf6e7176ca2cf5c603c42ac8886f9.jpeg" data-download-href="/uploads/short-url/gM5UIjjDqLwdZhlzkjXsl5eZp8d.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75929504ceadf6e7176ca2cf5c603c42ac8886f9_2_690x451.jpeg" alt="image" data-base62-sha1="gM5UIjjDqLwdZhlzkjXsl5eZp8d" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75929504ceadf6e7176ca2cf5c603c42ac8886f9_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75929504ceadf6e7176ca2cf5c603c42ac8886f9_2_1035x676.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75929504ceadf6e7176ca2cf5c603c42ac8886f9_2_1380x902.jpeg 2x" data-dominant-color="8E97AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1257 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2022-12-27 17:57 UTC)

<p>any input on this?<br>
<a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #3 by @pieper (2022-12-27 18:24 UTC)

<p>Did you put the data someplace where people can easily replicate the issue?</p>

---

## Post #4 by @muratmaga (2022-12-27 19:48 UTC)

<p>You can try with any of these<br>
<a href="https://app.box.com/s/plth0mmkovmqrvizoa9j5t3y9dibx0j6" class="onebox" target="_blank" rel="noopener">https://app.box.com/s/plth0mmkovmqrvizoa9j5t3y9dibx0j6</a></p>
<p>I usually set the mean as target and pc1 as source.</p>

---

## Post #5 by @pieper (2022-12-29 17:47 UTC)

<p>When you get the signed distance it is as <a href="https://vtk.org/doc/nightly/html/classvtkImplicitPolyDataDistance.html#details:~:text=input%20vtkPolyData.-,Implicit%20function%20that%20computes%20the%20distance%20from%20a%20point%20x%20to,the%20function%20is%20the%20angle%2Dweighted%20pseudonormal%20at%20the%20nearest%20point.,-Baerentzen%2C%20J.%20A">defined here</a> and that probably works well for simple shapes but not so well for these complex surfaces.  The <code>x-p</code> vectors for the front and back of the tooth would be similar length and the same size, but the surface normals are opposite, so that would be why the sign shifts.  The AbsolutePointToPointDistance (first image below) makes sense to me but the signed distance (second image) doesn’t have much meaning for this data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/774f8b2359ad99b7bec7ddfcc386b4342a95141e.png" data-download-href="/uploads/short-url/h1teTbJeXNHeEnAHXJbzvE1u0QC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/774f8b2359ad99b7bec7ddfcc386b4342a95141e_2_690x264.png" alt="image" data-base62-sha1="h1teTbJeXNHeEnAHXJbzvE1u0QC" width="690" height="264" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/774f8b2359ad99b7bec7ddfcc386b4342a95141e_2_690x264.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/774f8b2359ad99b7bec7ddfcc386b4342a95141e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/774f8b2359ad99b7bec7ddfcc386b4342a95141e.png 2x" data-dominant-color="BECDC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1034×397 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad06f3e81a98d44c4ae7156cfd70908b3b9e77bc.jpeg" data-download-href="/uploads/short-url/oGFuUEgDlqAoiMIOSmHwp7HN4tu.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad06f3e81a98d44c4ae7156cfd70908b3b9e77bc_2_690x230.jpeg" alt="image" data-base62-sha1="oGFuUEgDlqAoiMIOSmHwp7HN4tu" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad06f3e81a98d44c4ae7156cfd70908b3b9e77bc_2_690x230.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad06f3e81a98d44c4ae7156cfd70908b3b9e77bc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad06f3e81a98d44c4ae7156cfd70908b3b9e77bc.jpeg 2x" data-dominant-color="B9D4B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1017×339 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2022-12-30 02:58 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="26908">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The <code>x-p</code> vectors for the front and back of the tooth would be similar length and the same size, but the surface normals are opposite, so that would be why the sign shifts.</p>
</blockquote>
</aside>
<p>Not quite sure why the surface normal would matter for a point to point distance calculation. For every vertex on source model, there is corresponding vertex on the target. It should simply calculate the distance between these vertices (in a paired sense), and the sign of the distance should come from this calculation (positive for distance larger in the target, and negative for the opposite).</p>
<p>Whatever the justification might be for it, it doesn’t make much sense to me.</p>

---

## Post #7 by @pieper (2022-12-30 15:09 UTC)

<p>I think the current behavior does make sense and the root of the issues is the lack of a consistent interpretation for “sign” in general for a surface like this one.  You are correct that the point-to-point distance is very clear, and that is a positive number, the square root of the sum of the squares, defined only by the two points involved.  But the “sign” would need to be with respect to some outside reference.  In a simple case, say scaling a sphere about the center, the signed distance as calculated by the filter makes sense, because the surface normal of the sphere is a good approximation of the overall shape so that when the scale makes the sphere smaller the sign is negative and when you scale it larger the sign is positive.  When the surface normals are not representative of the overall shape you get situations like the back of the tooth.</p>
<p>Perhaps what you really want is to calculate the principle moments or axes of the object and then get the dot product of the distance vector with those vectors to define the sign of the distance (effectively like approximating the object with an ellipsoid).  I don’t see that the ModelToModel module implements this.  It would be pretty simple to script up in python in Slicer using the SegmentStatistics module and some numpy manipulations.</p>
<p>In general defining the sign is going to be application-dependent, so picking the reference for the sign should be a part of the analysis design.  For example I can imagine two skulls like yours where everything would be the same but the teeth would be larger in one than the other.  In that case you’d want to define the sign of the distance in terms of the local axes of the tooth, not the full model of the head.  Again I think the building blocks are all there in Slicer and just some code is needed.</p>

---

## Post #8 by @lassoan (2023-01-01 00:52 UTC)

<p>It may also help if you remove the bulk linear transformation component and only visualize the remaining local deformation component.</p>

---
