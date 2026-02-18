# Question on marching cube algorithm

**Topic ID**: 39446
**Date**: 2024-09-30
**URL**: https://discourse.slicer.org/t/question-on-marching-cube-algorithm/39446

---

## Post #1 by @alientex (2024-09-30 06:45 UTC)

<p>Hello,</p>
<p>I have changed to the Marching Cube algorithm in the file <code>vtkBinaryLabelmapToClosedSurfaceConversionRule</code> at line 320 in Slicer source. Here’s the output of both algorithms: Marching Cube (green) and Flying Edges (yellow), respectively:</p>
<table> <tbody><tr> <th>Marching Cube</th> <th>Flying Edges</th> </tr> <tr> <td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/734e11b1242e8bf4e6c8fbaf5a13bfee4c53939c.jpeg" data-download-href="/uploads/short-url/gs2aCQDzbe0MNL1w0kllE5QnR1y.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/734e11b1242e8bf4e6c8fbaf5a13bfee4c53939c_2_644x500.jpeg" data-base62-sha1="gs2aCQDzbe0MNL1w0kllE5QnR1y" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/734e11b1242e8bf4e6c8fbaf5a13bfee4c53939c_2_644x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/734e11b1242e8bf4e6c8fbaf5a13bfee4c53939c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/734e11b1242e8bf4e6c8fbaf5a13bfee4c53939c.jpeg 2x" data-dominant-color="B3DCB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">827×642 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td> <td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/006bfd22b218b3ad53b7652b7e9fdae6f9feab90.jpeg" data-download-href="/uploads/short-url/3JmCU8H5YYplZiCV9WX2mhW6wU.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/006bfd22b218b3ad53b7652b7e9fdae6f9feab90_2_627x499.jpeg" data-base62-sha1="3JmCU8H5YYplZiCV9WX2mhW6wU" width="627" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/006bfd22b218b3ad53b7652b7e9fdae6f9feab90_2_627x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/006bfd22b218b3ad53b7652b7e9fdae6f9feab90.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/006bfd22b218b3ad53b7652b7e9fdae6f9feab90.jpeg 2x" data-dominant-color="D3D36A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">720×574 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td> </tr> <tr> <td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffd08837010add700634fbd8c0f010bd627bc0bf.jpeg" data-download-href="/uploads/short-url/Av2x2ufRxXrdvdkelCHucgjKV8H.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffd08837010add700634fbd8c0f010bd627bc0bf.jpeg" data-base62-sha1="Av2x2ufRxXrdvdkelCHucgjKV8H" width="569" height="500" data-dominant-color="54C654"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">862×757 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td> <td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87ec2fb3752fe10e39e44a9a122b580aaa5d775e.jpeg" data-download-href="/uploads/short-url/joqu5QOhvsEL9gEQ8M04sJf8xfE.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87ec2fb3752fe10e39e44a9a122b580aaa5d775e_2_639x500.jpeg" data-base62-sha1="joqu5QOhvsEL9gEQ8M04sJf8xfE" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87ec2fb3752fe10e39e44a9a122b580aaa5d775e_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87ec2fb3752fe10e39e44a9a122b580aaa5d775e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87ec2fb3752fe10e39e44a9a122b580aaa5d775e.jpeg 2x" data-dominant-color="D4D43B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">720×563 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td> </tr> </tbody></table>
<p>Why do I see cracks on the surface of the Marching Cube output?</p>
<p>Slicer version: 5.6.2 r32448 / f10cd8c</p>

---

## Post #2 by @alientex (2024-10-01 03:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> Any thoughts?</p>

---

## Post #3 by @lassoan (2024-10-01 04:34 UTC)

<p>Marching cubes seem to have trouble computing surface normals consistently.</p>
<p>Flying edges algorithm is a modernized, parallelized version of marching cubes. Why would you consider going back to the old algorithm?</p>

---

## Post #4 by @alientex (2024-10-03 03:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="39446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Why would you consider going back to the old algorithm?</p>
</blockquote>
</aside>
<p>I just wanted to see the results of both algorithms.</p>

---
