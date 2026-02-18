# Volumes registration takes too long

**Topic ID**: 20068
**Date**: 2021-10-08
**URL**: https://discourse.slicer.org/t/volumes-registration-takes-too-long/20068

---

## Post #1 by @lolamartinalonso (2021-10-08 11:50 UTC)

<p>Operating system: 64 bit<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Volume registration taking 5 min not more<br>
Actual behavior:<br>
I am performing a volume registration of two volumes of 1700x1700x1737 slices with Rigid 6 DOF and it is taking too much time. Maybe it is normal but I haven´t worked with 3D Slicer before.</p>
<p>Can I change some values for the registration to make it faster?</p>
<p>This is a screenshot of my running status.</p>
<p>Thanks in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b139e2da5c3ea89a33e5c8b218d7e94d51b3472a.jpeg" data-download-href="/uploads/short-url/phOx1W52zz77NthHuITpV3lsNYe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b139e2da5c3ea89a33e5c8b218d7e94d51b3472a_2_690x374.jpeg" alt="image" data-base62-sha1="phOx1W52zz77NthHuITpV3lsNYe" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b139e2da5c3ea89a33e5c8b218d7e94d51b3472a_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b139e2da5c3ea89a33e5c8b218d7e94d51b3472a_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b139e2da5c3ea89a33e5c8b218d7e94d51b3472a_2_1380x748.jpeg 2x" data-dominant-color="9C9DA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1043 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-10-08 12:19 UTC)

<p>Rigid registration can be typically computed in 15-30 seconds.</p>
<p>The image is relatively high resolution, which may slow down the registration. If you just want to align the white spots then you can probably downsample the image by at least a factor of 4 along each axis (resulting in 64x smaller volume) without impacting registration result. The easiest is to use “Crop volume” and specify “Spacing scale” of 4.0x.</p>
<p>Also make sure to try <a href="https://github.com/lassoan/SlicerElastix#slicerelastix">SlicerElastix</a> and <a href="https://github.com/simonoxen/SlicerANTs#slicerants">SlicerANTs</a> extensions, as they may converge faster than the BRAINS algorithm.</p>
<p>Registration may also take longer (or may not converge at all) if it is started from the optimum. Make sure your images are sufficiently aligned (shifted less than about 5-10% of the image size and rotated by less than 5-10 degrees) by <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">using manual or semi-automatic registration methods</a> as needed.</p>

---
