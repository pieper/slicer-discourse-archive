---
topic_id: 23722
title: "Dilation Erosion Element Type"
date: 2022-06-06
url: https://discourse.slicer.org/t/23722
---

# Dilation erosion element type

**Topic ID**: 23722
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/dilation-erosion-element-type/23722

---

## Post #1 by @massisenergy (2022-06-06 05:43 UTC)

<p>Dear,</p>
<p>Does 3DSlicer offer any more element types (sphere, circle, rectangle etc.) than squared pixels?</p>
<p>For example, I have a tomography image which is high resolution (very small pixel size). That, upon surface-export, results in a jagged isosurface with very large number of triangles which I do not need.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ec935df3d423f07cc7af969660913b30d7989c1.jpeg" data-download-href="/uploads/short-url/4olpL8oxFNKPabpOq5UPmu9jmxP.jpeg?dl=1" title="StepsProducedForSphericalSurface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ec935df3d423f07cc7af969660913b30d7989c1.jpeg" alt="StepsProducedForSphericalSurface" data-base62-sha1="4olpL8oxFNKPabpOq5UPmu9jmxP" width="613" height="499" data-dominant-color="59595A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">StepsProducedForSphericalSurface</span><span class="informations">680×554 91.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I could use a sphere or ball as my dilation-erosion element of chosen size, I could get a lot smoother, non-pixelated (and less number of triangle) surface for my use case.</p>
<p>Any information / advice on this will be highly appreciated.</p>
<p>With regards,<br>
massisenergy</p>

---

## Post #2 by @mau_igna_06 (2022-06-06 08:15 UTC)

<p>You can get reducing the numer of triangles by using decimation on your mesh… If I were you I would set it to 6% and see how it gets</p>

---

## Post #3 by @massisenergy (2022-06-06 16:52 UTC)

<p>Hello,</p>
<p>Thanks for your suggestion. Unfortunately ‘Decimate’ doesn’t work for my use case. It couldn’t remove the jagged edges, rather resulted in bad quality triangles.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2826efa4bd7f62d8d5c04ae04c88aaab0968ebe2.jpeg" data-download-href="/uploads/short-url/5JcwbcBtqi4wRkl12pNvFcuNHHQ.jpeg?dl=1" title="ScreenShot 2022-06-06 at 9.24.48 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2826efa4bd7f62d8d5c04ae04c88aaab0968ebe2_2_446x375.jpeg" alt="ScreenShot 2022-06-06 at 9.24.48 PM" data-base62-sha1="5JcwbcBtqi4wRkl12pNvFcuNHHQ" width="446" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2826efa4bd7f62d8d5c04ae04c88aaab0968ebe2_2_446x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2826efa4bd7f62d8d5c04ae04c88aaab0968ebe2_2_669x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2826efa4bd7f62d8d5c04ae04c88aaab0968ebe2_2_892x750.jpeg 2x" data-dominant-color="9A7853"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenShot 2022-06-06 at 9.24.48 PM</span><span class="informations">1920×1613 641 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then I tried using the <code>Surface Models</code> &gt; <code>Advanced</code> &gt; <code>Smoothing</code>. After playing with the parameters (Iterations: 100, Relaxation: 0.1) , I could reduce the jagging a lot <strong>but not without a ~15% decrease in the overall volume</strong>!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a6b5fc295d4b5b6b7a40e1c9e40d4b50c75ee44.jpeg" data-download-href="/uploads/short-url/63g6iEHUt8cSCEFzav3J0zxL9L6.jpeg?dl=1" title="ScreenShot 2022-06-06 at 10.17.17 PM Large" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a6b5fc295d4b5b6b7a40e1c9e40d4b50c75ee44_2_690x431.jpeg" alt="ScreenShot 2022-06-06 at 10.17.17 PM Large" data-base62-sha1="63g6iEHUt8cSCEFzav3J0zxL9L6" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a6b5fc295d4b5b6b7a40e1c9e40d4b50c75ee44_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a6b5fc295d4b5b6b7a40e1c9e40d4b50c75ee44_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a6b5fc295d4b5b6b7a40e1c9e40d4b50c75ee44.jpeg 2x" data-dominant-color="636C5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenShot 2022-06-06 at 10.17.17 PM Large</span><span class="informations">1280×800 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0809c3a451b50c5f8477525a791be16f2440ef9e.jpeg" data-download-href="/uploads/short-url/196JQIFoPbnNDLuzYl3Uq3lm1Zk.jpeg?dl=1" title="ScreenShot 2022-06-06 at 9.24.22 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0809c3a451b50c5f8477525a791be16f2440ef9e_2_446x375.jpeg" alt="ScreenShot 2022-06-06 at 9.24.22 PM" data-base62-sha1="196JQIFoPbnNDLuzYl3Uq3lm1Zk" width="446" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0809c3a451b50c5f8477525a791be16f2440ef9e_2_446x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0809c3a451b50c5f8477525a791be16f2440ef9e_2_669x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0809c3a451b50c5f8477525a791be16f2440ef9e_2_892x750.jpeg 2x" data-dominant-color="783388"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenShot 2022-06-06 at 9.24.22 PM</span><span class="informations">1920×1613 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any other ideas, folks?</p>

---

## Post #4 by @mau_igna_06 (2022-06-06 17:31 UTC)

<p>Maybe you can try some kind of lapalacian smoothing filter for polydata and then decimate<br>
Maybw try with rhe taubin one.</p>
<p>Hopw it helps</p>

---

## Post #5 by @pieper (2022-06-06 18:43 UTC)

<p>It looks like your input data was pixelated (binarized) before the original surface was generated.  Starting with an original continuous tone scan would be the normal way to generate a smooth isosurface.</p>

---

## Post #6 by @massisenergy (2022-06-07 15:48 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> Okay. Reducing the total number of triangles isn’t hard anymore, <code>Blender (v 3.1.2)</code> serves the purpose quite well. I tried with the <code>Taubin</code> option as well, that also removes volume while smoothing!</p>
<p><a class="mention" href="/u/pieper">@pieper</a> exactly. I got a binary pixelated tomography data and I have make smooth surface out of it. You’re absolutely in the right direction:</p>
<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="23722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Starting with an original continuous tone scan would be the normal way to generate a smooth isosurface.</p>
</blockquote>
</aside>
<p>I realise that even if Slicer offers sphere type (which is not available at the moment I guess?) dilation or erosion elements, <em>simply</em> working with those on <strong>square pixelated</strong> tomography data would inevitably result in the loss of some volume <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20">.</p>
<p>So my question now changes into – <em>Is it possible to get smooth surface out of binary pixelated data (negligible loss of volume)?</em></p>

---

## Post #7 by @pieper (2022-06-07 17:07 UTC)

<p>If the mesh-based smoothing is failing (which make some sense given that the data is basically aliased) then converting the mesh to an image, smoothing in image space, and re-isosurfacing may work better.  You will have options about kernel size, weights, and thresholds so you can see what works best for that data.</p>

---

## Post #8 by @massisenergy (2022-08-17 10:57 UTC)

<p>Thanks all. For now, I used the Blender provided smoothing tools, but generating the surface without any “voxelized segmentation” would be best if smoothing induced volume loss is unacceptable!</p>

---

## Post #9 by @lassoan (2023-03-21 02:13 UTC)



---
