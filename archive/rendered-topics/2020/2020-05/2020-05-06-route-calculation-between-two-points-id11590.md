---
topic_id: 11590
title: "Route Calculation Between Two Points"
date: 2020-05-06
url: https://discourse.slicer.org/t/11590
---

# Route calculation between two points

**Topic ID**: 11590
**Date**: 2020-05-06
**URL**: https://discourse.slicer.org/t/route-calculation-between-two-points/11590

---

## Post #1 by @Jini (2020-05-06 17:56 UTC)

<p>thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
we I can calculation the route from example two point with slicer?</p>

---

## Post #2 by @Jini (2020-05-17 08:58 UTC)

<p>How can I do a route calculation in Cartesian coordinates with slicer? Is there a tool for the calculation?</p>

---

## Post #3 by @lassoan (2020-05-17 14:18 UTC)

<p>Slicer can compute route between two points on a mesh surface or a network of lines. If your input is an image you need to segment it first. If you wan find route in the centerline then you can use VMTK extension’s centerline extraction module (clicking on “Preview” is enough, no need to run the full computation).</p>
<div class="onebox lazyYT" data-youtube-id="UpfDP6ejCjg" data-youtube-title="Finding shortest path between two points in the bronchial tree" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque">
  <a href="https://www.youtube.com/watch?v=UpfDP6ejCjg" target="_blank">
    <img src="https://img.youtube.com/vi/UpfDP6ejCjg/hqdefault.jpg" width="480" height="270" title="Finding shortest path between two points in the bronchial tree">
  </a>
</div>


---

## Post #4 by @Jini (2020-05-17 17:28 UTC)

<p>I would like to be able to calculate the vector of the route. For that I have to get the x, y, z values? Where can I read the vectors of these points in the slicer?</p>

---

## Post #5 by @lassoan (2020-05-17 17:42 UTC)

<p>Can you tell a bit more about what you would like to achieve?</p>

---

## Post #6 by @Jini (2020-05-18 08:47 UTC)

<p>I would like to invite two segmentation models into slicer and determine the deformation of the two models using the route calculation in Cartesian coordinates. For the route calculation in Cartesian coordinates, I need vectors and angles. I must to set the zero point (3D axis, xyz) on segmentation Modell to calculate from there ?</p>

---

## Post #7 by @lassoan (2020-05-18 17:19 UTC)

<p>Now I’m even more confused about what you mean by route calculation. Can you post an annotated screenshot or draw a sketch that explains what you want to achieve?</p>
<p>If you want to spatially align segments by translating/rotating/warping then you can use SegmentRegistration extension.</p>

---

## Post #8 by @Jini (2020-05-19 19:18 UTC)

<p>I post tommoro a picture what i mean with route calulation in the model <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #9 by @Jini (2020-05-20 09:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0353f988dbab4b66af6b2f00b69e0af30f824e0.jpeg" data-download-href="/uploads/short-url/ygYFYRMVYFG8FLs54w9tco28yNq.jpeg?dl=1" title="IMG_3316" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0353f988dbab4b66af6b2f00b69e0af30f824e0_2_666x500.jpeg" alt="IMG_3316" data-base62-sha1="ygYFYRMVYFG8FLs54w9tco28yNq" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0353f988dbab4b66af6b2f00b69e0af30f824e0_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0353f988dbab4b66af6b2f00b69e0af30f824e0_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0353f988dbab4b66af6b2f00b69e0af30f824e0_2_1332x1000.jpeg 2x" data-dominant-color="B0AFAB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_3316</span><span class="informations">4032×3024 797 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the picture you can see what I mean with roue calculation.</p>

---

## Post #10 by @lassoan (2020-05-20 15:52 UTC)

<p>Do you just want to compute vectors between points?</p>

---

## Post #11 by @Jini (2020-05-20 17:43 UTC)

<p>I want to calculate vectors in Cartesian coordinates. I want to calculate the distance (vector) between the points for example from two models. For this, I must to set the zero point on axis for the first model and calculate the distance to other models from there. The angle calculation is also important, to consider the deformation of the two models.</p>

---

## Post #12 by @Jini (2020-05-20 17:45 UTC)

<p>If I get the vectors and angles from slicer, I can also calculate them with an excel table. For this I need the values in a 3D room.</p>

---

## Post #13 by @lassoan (2020-05-20 17:49 UTC)

<p>You can get point coordinates of models using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPoints">slicer.util.arrayFromModelPoints</a>. VTK has functions for finding closest points, you can also get distances between closest points of two models, etc. If you describe specifically what you want to compute then we can recommend which methods to use.</p>

---

## Post #14 by @Jini (2020-05-22 08:15 UTC)

<p>What the tool Vector to scalar volume does?</p>

---

## Post #15 by @lassoan (2020-05-23 04:53 UTC)

<p>Vector to scalar volume module converts a vector volume (each voxel of the volume is a vector) to a scalar volume (each voxel of the volume is a scalar value).</p>

---

## Post #16 by @Jini (2020-05-26 09:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8ee30e8c75273ccfabd0d6753beb59dde0a0aa6.png" data-download-href="/uploads/short-url/uX3sfimJLmPoabW8lasX3XHy2BE.png?dl=1" title="Fiducial" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8ee30e8c75273ccfabd0d6753beb59dde0a0aa6_2_690x358.png" alt="Fiducial" data-base62-sha1="uX3sfimJLmPoabW8lasX3XHy2BE" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8ee30e8c75273ccfabd0d6753beb59dde0a0aa6_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8ee30e8c75273ccfabd0d6753beb59dde0a0aa6_2_1035x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8ee30e8c75273ccfabd0d6753beb59dde0a0aa6_2_1380x716.png 2x" data-dominant-color="737278"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fiducial</span><span class="informations">1920×998 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this a usefull for catesiche cordination calculation? What is R, A ans S in this Markups?<br>
I dont understand we I get a Vector from this Fiducial marker?</p>

---

## Post #17 by @Jini (2020-05-26 09:35 UTC)

<p>I think S is z-Achse and A is y-Achse and R is x-Achse ?</p>

---

## Post #18 by @Jini (2020-05-26 13:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16ba559e43b0abfa73614e75d152581549f21e41.jpeg" data-download-href="/uploads/short-url/3f3IThGhPrnfI4IByecaGiHvtAt.jpeg?dl=1" title="02.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16ba559e43b0abfa73614e75d152581549f21e41_2_690x374.jpeg" alt="02.PNG" data-base62-sha1="3f3IThGhPrnfI4IByecaGiHvtAt" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16ba559e43b0abfa73614e75d152581549f21e41_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16ba559e43b0abfa73614e75d152581549f21e41_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16ba559e43b0abfa73614e75d152581549f21e41_2_1380x748.jpeg 2x" data-dominant-color="93939F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02.PNG</span><span class="informations">1920×1042 652 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Why I can not do by markups<br>
List: with create new markupsfiducial as ?</p>

---

## Post #19 by @Jini (2020-05-27 09:36 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d94dbcb9a17ae33c6da6338c9cf83a8d635959b.png" data-download-href="/uploads/short-url/mu1TezrY2apTUOOw28jXC2ANmAj.png?dl=1" title="Markups 4.10 and 4.11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d94dbcb9a17ae33c6da6338c9cf83a8d635959b_2_690x351.png" alt="Markups 4.10 and 4.11" data-base62-sha1="mu1TezrY2apTUOOw28jXC2ANmAj" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d94dbcb9a17ae33c6da6338c9cf83a8d635959b_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d94dbcb9a17ae33c6da6338c9cf83a8d635959b_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d94dbcb9a17ae33c6da6338c9cf83a8d635959b_2_1380x702.png 2x" data-dominant-color="F7F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Markups 4.10 and 4.11</span><span class="informations">1690×860 87.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hello Lassoan, in the new version from Slicer we have no List for markups (see please picture).<br>
I segment all with new Version 4.11. and i can not do markups with old Version.</p>
<p>We I can create markups for two model in new Version 4.11. ?</p>
<p>Thank you for your help.</p>
<p>Best regards</p>

---

## Post #20 by @lassoan (2020-06-08 03:04 UTC)

<aside class="quote no-group" data-username="Jini" data-post="16" data-topic="11590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/5daacb/48.png" class="avatar"> Jini:</div>
<blockquote>
<p>What is R, A ans S in this Markups?</p>
</blockquote>
</aside>
<p>These are patient coordinate system axes. R=right, A=anterior, S=superior.</p>
<aside class="quote no-group" data-username="Jini" data-post="19" data-topic="11590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/5daacb/48.png" class="avatar"> Jini:</div>
<blockquote>
<p>Hello Lassoan, in the new version from Slicer we have no List for markups</p>
</blockquote>
</aside>
<p>I would recommend to use a recent Slicer Preview Release. You can rename a markups node by double-clicking on its name (or right-click on it and choose Rename).</p>

---
