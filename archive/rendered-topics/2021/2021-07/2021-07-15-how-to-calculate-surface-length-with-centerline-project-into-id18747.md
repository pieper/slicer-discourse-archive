# How to calculate surface length with centerline project into surface

**Topic ID**: 18747
**Date**: 2021-07-15
**URL**: https://discourse.slicer.org/t/how-to-calculate-surface-length-with-centerline-project-into-surface/18747

---

## Post #1 by @junqiangchen (2021-07-15 10:58 UTC)

<p>hi,i have centerline and centerlinesection,i want to calculate surfce line length,like this,green line is centerline and blue line is surface line,how to get this blue line?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23843525fd5b06f08ac31240862a8ee085e5c0a7.jpeg" data-download-href="/uploads/short-url/54bXPkmwEMYh5PUuZqZjawaMSjl.jpeg?dl=1" title="捕获1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23843525fd5b06f08ac31240862a8ee085e5c0a7_2_690x461.jpeg" alt="捕获1" data-base62-sha1="54bXPkmwEMYh5PUuZqZjawaMSjl" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/23843525fd5b06f08ac31240862a8ee085e5c0a7_2_690x461.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23843525fd5b06f08ac31240862a8ee085e5c0a7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23843525fd5b06f08ac31240862a8ee085e5c0a7.jpeg 2x" data-dominant-color="7C7262"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获1</span><span class="informations">726×486 34.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e9fa9f376e4ac1464a9ab71c47cd009e837485.jpeg" data-download-href="/uploads/short-url/2pCW6Cj58pTyyHCEAy3UM0UFIeV.jpeg?dl=1" title="捕获2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10e9fa9f376e4ac1464a9ab71c47cd009e837485_2_452x500.jpeg" alt="捕获2" data-base62-sha1="2pCW6Cj58pTyyHCEAy3UM0UFIeV" width="452" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10e9fa9f376e4ac1464a9ab71c47cd009e837485_2_452x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e9fa9f376e4ac1464a9ab71c47cd009e837485.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e9fa9f376e4ac1464a9ab71c47cd009e837485.jpeg 2x" data-dominant-color="61574C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获2</span><span class="informations">622×687 36.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/176087bc936c2b6a4ed7c6802da44410993fc1b4.jpeg" data-download-href="/uploads/short-url/3kNNp9kYUY8eUe2G5jhTsfgeZY8.jpeg?dl=1" title="捕获3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176087bc936c2b6a4ed7c6802da44410993fc1b4_2_360x500.jpeg" alt="捕获3" data-base62-sha1="3kNNp9kYUY8eUe2G5jhTsfgeZY8" width="360" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/176087bc936c2b6a4ed7c6802da44410993fc1b4_2_360x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/176087bc936c2b6a4ed7c6802da44410993fc1b4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/176087bc936c2b6a4ed7c6802da44410993fc1b4.jpeg 2x" data-dominant-color="73695A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获3</span><span class="informations">506×702 37.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2021-07-15 13:27 UTC)

<p>How did you draw the blue line ? It you do it as a markups curve, the length is available in its properties.</p>

---

## Post #3 by @chir.set (2021-07-15 13:37 UTC)

<p>You may also resample a markups curve on the surface of a model as ‘Shortest distance on surface.’</p>

---

## Post #4 by @AshvinGupta (2021-07-15 15:18 UTC)

<p>Hello, just wondering, did you update your Slicer and VMTK? My 3d Slicer was working fine however after updating it the centreline module does not work anymore so am beginning to think this might just be a problem on my end?</p>

---

## Post #5 by @chir.set (2021-07-15 21:55 UTC)

<p>Please see <a href="https://discourse.slicer.org/t/vmtk-extract-centerline-fails-with-vmtk-using-vtk9/18644" class="inline-onebox">VMTK extract centerline fails with VMTK using VTK9</a></p>

---

## Post #6 by @junqiangchen (2021-07-20 07:18 UTC)

<p>this result get from Commercial medical analysis software</p>

---

## Post #7 by @lassoan (2021-07-20 12:02 UTC)

<p>The blue line is easy to get. You just need to iterate through all the curve points, and offset the curve point position by the radius in the binormal direction.</p>
<p>You can get the binormal direction from the cross product of the tangent vector of the curve and the normal vector of the curve. You can get the normal vector of the curve from the cross product of the previous and next tangent vectors.</p>

---

## Post #8 by @junqiangchen (2021-07-21 04:15 UTC)

<p>thank you lassoan, i use centerline normal vector and centerlinesection maxdiamter to produce the line,and calculate the intersection points between line and surface,like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a88796b7e8408f66b17a7917f189d67b693eeae.png" data-download-href="/uploads/short-url/64grOnGR5xWKzV2zpzG77p812W2.png?dl=1" title="图片1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a88796b7e8408f66b17a7917f189d67b693eeae_2_482x500.png" alt="图片1" data-base62-sha1="64grOnGR5xWKzV2zpzG77p812W2" width="482" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a88796b7e8408f66b17a7917f189d67b693eeae_2_482x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a88796b7e8408f66b17a7917f189d67b693eeae.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a88796b7e8408f66b17a7917f189d67b693eeae.png 2x" data-dominant-color="5E6476"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片1</span><span class="informations">543×563 83.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2021-07-21 11:51 UTC)

<p>Yes, intersection with a plane (therefore using the same position and normal) generates similar curves, too, if the vessel has one single strong curve and so the vessel remains in one plane. If you have multiple curves in different directions then the vessel deviates from the plane and the intersection curves do not capture well the vessel shape anymore.</p>

---
