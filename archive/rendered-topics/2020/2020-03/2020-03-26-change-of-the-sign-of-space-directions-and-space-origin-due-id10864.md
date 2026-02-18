# Change of the sign of space directions and space origin due to interpolation / cropping

**Topic ID**: 10864
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/change-of-the-sign-of-space-directions-and-space-origin-due-to-interpolation-cropping/10864

---

## Post #1 by @MMMPPPMMM (2020-03-26 22:51 UTC)

<p>Hello</p>
<p>Is it intended that the sign of space directions and space origin change due to interpolated cropping?</p>
<p>From the header files of the volumes:</p>
<p>Before interpolation / cropping:</p>
<blockquote>
<p>type: float<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 59 69 162<br>
space directions: <strong>(1.26953125,0,0) (0,1.26953125,0)</strong> (0,0,0.5)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: gzip<br>
space origin: <strong>(262.79296875,250.09765625000003</strong>,54.000000000000007)</p>
</blockquote>
<p>After interpolation / cropping:</p>
<blockquote>
<p>type: float<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 150 177 162<br>
space directions: <strong>(-0.5,0,0) (0,-0.5,0)</strong> (0,0,0.5)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: gzip<br>
space origin: <strong>(336.75900268554688,337.75399780273438</strong>,53.922901153564453)</p>
</blockquote>
<p>Example scene: <a href="https://gigamove.rz.rwth-aachen.de/d/id/XjfDBwn6fC5RKF" rel="noopener nofollow ugc">https://gigamove.rz.rwth-aachen.de/d/id/XjfDBwn6fC5RKF</a></p>
<p>Is it possible to avoid this?</p>
<p>Kind regards</p>

---

## Post #2 by @lassoan (2020-03-26 23:14 UTC)

<aside class="quote no-group" data-username="MMMPPPMMM" data-post="1" data-topic="10864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>Is it intended that the sign of space directions and space origin change due to interpolated cropping?</p>
</blockquote>
</aside>
<p>Interpolated cropping axes are not attempted to be matched to axes of the original volume, as it is not feasible in general (only when the ROI axes happen to be parallel to the original volume axes). If the image geometry is correct in physical space, it should not matter what is internal voxel coordinate system.</p>
<p>If you need a specific image geometry then you can create an empty reference volume with that geometry and crop&amp;resample by using an image resample module.</p>

---
