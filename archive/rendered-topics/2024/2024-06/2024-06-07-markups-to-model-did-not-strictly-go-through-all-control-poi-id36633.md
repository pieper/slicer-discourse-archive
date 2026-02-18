# "Markups to model" did not strictly go through all control points of the markups, resulting in the surface not being what I expected. Unable to create complex surfaces

**Topic ID**: 36633
**Date**: 2024-06-07
**URL**: https://discourse.slicer.org/t/markups-to-model-did-not-strictly-go-through-all-control-points-of-the-markups-resulting-in-the-surface-not-being-what-i-expected-unable-to-create-complex-surfaces/36633

---

## Post #1 by @linhuanfeng (2024-06-07 02:23 UTC)

<p>“Markups to model” did not strictly go through all control points of the markups, resulting in the surface not being what I expected. Unable to create complex surfaces.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15e2501f943bfef8f40c53e84571e8e8aade2109.jpeg" data-download-href="/uploads/short-url/37ATOouRSqTU2UBcpVhlucpuRgR.jpeg?dl=1" title="409ce85116a44f02484a47d14807c60e_" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15e2501f943bfef8f40c53e84571e8e8aade2109_2_690x430.jpeg" alt="409ce85116a44f02484a47d14807c60e_" data-base62-sha1="37ATOouRSqTU2UBcpVhlucpuRgR" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15e2501f943bfef8f40c53e84571e8e8aade2109_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15e2501f943bfef8f40c53e84571e8e8aade2109_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15e2501f943bfef8f40c53e84571e8e8aade2109.jpeg 2x" data-dominant-color="7C7F6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">409ce85116a44f02484a47d14807c60e_</span><span class="informations">1244×776 96.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @linhuanfeng (2024-06-07 02:29 UTC)

<p>I found that all of the Slicer tools are based on the Markup module, but it is not possible to generate surfaces or inclusions that strictly follow the control points. Recurrence satisfies complex scenarios.<br>
The slicer has something similar to a bezier surface, but it is too simple and the operation is also very cumbersome. I hope to generate complex surfaces based on a set of control points (ensuring passing through all control points)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e92f946b60d0cede189cd034b68dfdb753e4862.png" alt="image" data-base62-sha1="i3J3af7SL1WjVdenH3ZImr9xgHg" width="232" height="66"></p>
<p>Here is an example of generating a surface from points and strictly passing through all control points。（minics）<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac25efefea01b2393a851135d42f429dbc904eaa.jpeg" data-download-href="/uploads/short-url/oyTp7f77ODEIoOWkSz52yBD0pZM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac25efefea01b2393a851135d42f429dbc904eaa_2_690x323.jpeg" alt="image" data-base62-sha1="oyTp7f77ODEIoOWkSz52yBD0pZM" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac25efefea01b2393a851135d42f429dbc904eaa_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac25efefea01b2393a851135d42f429dbc904eaa_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac25efefea01b2393a851135d42f429dbc904eaa_2_1380x646.jpeg 2x" data-dominant-color="686C6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×896 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @linhuanfeng (2024-06-07 02:36 UTC)

<p>I have achieved some results by adjusting the following parameters, but they cannot meet the requirements and are very troublesome</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f71c5c175f149bae19c72b6067b662a77df28c2.png" data-download-href="/uploads/short-url/ksY29mRUKpoudFgO8GXrB9U1rtU.png?dl=1" title="74b5614f8f0cae0cc2e3afa65ae8fc1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f71c5c175f149bae19c72b6067b662a77df28c2.png" alt="74b5614f8f0cae0cc2e3afa65ae8fc1" data-base62-sha1="ksY29mRUKpoudFgO8GXrB9U1rtU" width="690" height="131" data-dominant-color="F6F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">74b5614f8f0cae0cc2e3afa65ae8fc1</span><span class="informations">712×136 2.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @linhuanfeng (2024-06-07 02:39 UTC)

<p>If you have a good solution, please contact me（mail:2303814193@qq.com）. I am also very willing to pay the compensation.</p>

---

## Post #5 by @linhuanfeng (2024-06-07 06:04 UTC)

<p>I have found that “Grid Surface” can achieve precise surfaces, so can we use this in turn to generate surfaces from countless points. Just like the minics above</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40bfa36d3c967941c8741682463a0816b085befd.jpeg" data-download-href="/uploads/short-url/9eN8LKYO2oRBOdwI9lVrHfbu2jX.jpeg?dl=1" title="f9db0bcfaf3b34e6d4dd72a44d9e24f" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40bfa36d3c967941c8741682463a0816b085befd_2_690x392.jpeg" alt="f9db0bcfaf3b34e6d4dd72a44d9e24f" data-base62-sha1="9eN8LKYO2oRBOdwI9lVrHfbu2jX" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40bfa36d3c967941c8741682463a0816b085befd_2_690x392.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40bfa36d3c967941c8741682463a0816b085befd_2_1035x588.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40bfa36d3c967941c8741682463a0816b085befd_2_1380x784.jpeg 2x" data-dominant-color="BDBCDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">f9db0bcfaf3b34e6d4dd72a44d9e24f</span><span class="informations">1920×1091 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
