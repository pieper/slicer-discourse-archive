---
topic_id: 25519
title: "Transform Model Segments"
date: 2022-10-03
url: https://discourse.slicer.org/t/25519
---

# Transform model / segments

**Topic ID**: 25519
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/transform-model-segments/25519

---

## Post #1 by @mohammed_alshakhas (2022-10-03 07:59 UTC)

<p>i would love to able to do segments models transform in similar way to the way I can do it in meshmexer  software . the wat the do it is ti creat a pivot / centre point where you can drag and rotation your models .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14508bbf8065a826ec1fc7028798fe205de64163.jpeg" data-download-href="/uploads/short-url/2TI7kiBAwY8j3iBgdlWayJEeKQz.jpeg?dl=1" title="Screen Shot 2022-10-03 at 10.50.03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14508bbf8065a826ec1fc7028798fe205de64163_2_690x431.jpeg" alt="Screen Shot 2022-10-03 at 10.50.03" data-base62-sha1="2TI7kiBAwY8j3iBgdlWayJEeKQz" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14508bbf8065a826ec1fc7028798fe205de64163_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14508bbf8065a826ec1fc7028798fe205de64163_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14508bbf8065a826ec1fc7028798fe205de64163_2_1380x862.jpeg 2x" data-dominant-color="A7A5A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-03 at 10.50.03</span><span class="informations">1920×1200 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>the transform module in slicer3d  is not intuitive and doesn’t allow the movement i wish to achieve .</p>
<p>thanks</p>

---

## Post #2 by @muratmaga (2022-10-04 03:33 UTC)

<p>A similar functionality exists:</p>
<p>Right-click on the grid icon of the model object in the Data module and choose <code>Create New Transform</code><br>
then<br>
Right-click on the same spot, and choose <code>Interaction in 3D view</code>.</p>
<p>Now you can rotate your model around around using the handlebars of the white bounding box.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/112a94c7993f2da34d6f2afc723cb1b2663efa96.png" data-download-href="/uploads/short-url/2rRluQEoJ9p3gU4FBAUd9F4ZRbw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/112a94c7993f2da34d6f2afc723cb1b2663efa96_2_666x500.png" alt="image" data-base62-sha1="2rRluQEoJ9p3gU4FBAUd9F4ZRbw" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/112a94c7993f2da34d6f2afc723cb1b2663efa96_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/112a94c7993f2da34d6f2afc723cb1b2663efa96_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/112a94c7993f2da34d6f2afc723cb1b2663efa96.png 2x" data-dominant-color="E2E4ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1252×939 70.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c0576267465d030897b3a4241264e3b35c26604.png" data-download-href="/uploads/short-url/d83CY7q1SQqZ4jMlMLR7W8EbxGI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c0576267465d030897b3a4241264e3b35c26604_2_664x500.png" alt="image" data-base62-sha1="d83CY7q1SQqZ4jMlMLR7W8EbxGI" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c0576267465d030897b3a4241264e3b35c26604_2_664x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c0576267465d030897b3a4241264e3b35c26604_2_996x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c0576267465d030897b3a4241264e3b35c26604_2_1328x1000.png 2x" data-dominant-color="E1E2E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1344×1012 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @mohammed_alshakhas (2022-10-04 08:26 UTC)

<p>thanks, I was not aware of it.</p>
<p>is it possible to show handles for movement?  the dots for movements are pretty small and not easy to play with</p>

---

## Post #4 by @muratmaga (2022-10-04 16:16 UTC)

<p>Not sure why the Transform module does not use the nice transformation widgets that Markups functionality uses. It would be nice to be consistent.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40c9e923649810ae1ba5f9868def203249163fc1.png" data-download-href="/uploads/short-url/9f99hKSFH3OEaMBkzRIQyf13Jip.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40c9e923649810ae1ba5f9868def203249163fc1.png" alt="image" data-base62-sha1="9f99hKSFH3OEaMBkzRIQyf13Jip" width="506" height="500" data-dominant-color="978BB5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×693 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @mohammed_alshakhas (2022-10-04 16:55 UTC)

<p>please add that feature <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Additionally, a collision detector would be an amazing feature to work with .</p>
<p>that would put slicer3d on a new level of usability</p>

---
