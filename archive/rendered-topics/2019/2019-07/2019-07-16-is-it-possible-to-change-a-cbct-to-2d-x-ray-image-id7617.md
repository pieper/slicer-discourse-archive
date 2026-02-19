---
topic_id: 7617
title: "Is It Possible To Change A Cbct To 2D X Ray Image"
date: 2019-07-16
url: https://discourse.slicer.org/t/7617
---

# Is it possible to change a CBCT to 2D X-ray image?

**Topic ID**: 7617
**Date**: 2019-07-16
**URL**: https://discourse.slicer.org/t/is-it-possible-to-change-a-cbct-to-2d-x-ray-image/7617

---

## Post #1 by @Jmarcs (2019-07-16 19:48 UTC)

<p>Is it possible to change a cbct to a 2d Radiography sagital for orthodontics <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6f2930f0c75f500f6962f560a23f2dde21c9aca.jpeg" data-download-href="/uploads/short-url/wX3wXk7c5jyQYrSzpG2FFBVXcQG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6f2930f0c75f500f6962f560a23f2dde21c9aca_2_375x500.jpeg" alt="image" data-base62-sha1="wX3wXk7c5jyQYrSzpG2FFBVXcQG" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6f2930f0c75f500f6962f560a23f2dde21c9aca_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6f2930f0c75f500f6962f560a23f2dde21c9aca_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6f2930f0c75f500f6962f560a23f2dde21c9aca_2_750x1000.jpeg 2x" data-dominant-color="62605F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3024×4032 2.18 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thanks</p>

---

## Post #2 by @lassoan (2019-07-16 22:03 UTC)

<p>Yes, you can generate a 2D x-ray image by volume rendering module: disable shading, use a liner ramp-shape opacity transfer function (maximum opacity around 0.1 or lower), plain white color map, and set the 3D view background to black.</p>
<p>Volume rendering with a default bone preset:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f19a76a503fc38223cd3f440e6a5716c1d9dbb7e.jpeg" data-download-href="/uploads/short-url/ytk0q9SqTZg5DnnqyXucMVu4pem.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f19a76a503fc38223cd3f440e6a5716c1d9dbb7e_2_690x438.jpeg" alt="image" data-base62-sha1="ytk0q9SqTZg5DnnqyXucMVu4pem" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f19a76a503fc38223cd3f440e6a5716c1d9dbb7e_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f19a76a503fc38223cd3f440e6a5716c1d9dbb7e_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f19a76a503fc38223cd3f440e6a5716c1d9dbb7e_2_1380x876.jpeg 2x" data-dominant-color="D4CFD6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1434 870 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Volume rendering with X-ray settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3d34c55b9b1a7632345fc77f186376e695d9333.jpeg" data-download-href="/uploads/short-url/yMYJexmDigDNLOS98LNyRsvbRBh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3d34c55b9b1a7632345fc77f186376e695d9333_2_690x417.jpeg" alt="image" data-base62-sha1="yMYJexmDigDNLOS98LNyRsvbRBh" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3d34c55b9b1a7632345fc77f186376e695d9333_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3d34c55b9b1a7632345fc77f186376e695d9333_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3d34c55b9b1a7632345fc77f186376e695d9333_2_1380x834.jpeg 2x" data-dominant-color="A29798"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1366 450 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @jcfr (2019-09-11 13:29 UTC)

<p>I wonder if adding a “X-ray” volume rendering preset would be helpful ?</p>
<p>Ideally, switching to this preset would also change the background to black but I am not sure it is the right place to do this.</p>

---

## Post #4 by @burnhamd (2019-09-11 14:57 UTC)

<p>I think it would be nice to have.  Maybe in a separate module? I have basically written the same thing that generates DRRs using different methods.  I have found it helpful in presenting the information to clinicians in a way that they are used to visualizing from standard practice.</p>

---

## Post #5 by @lassoan (2019-09-11 16:43 UTC)

<p>I’ve added an X-ray VR preset - see pull request here: <a href="https://github.com/Slicer/Slicer/pull/1209" class="inline-onebox">qSlicerTractographyFiducialSeedingModuleTest1 failure · Issue #1209 · Slicer/Slicer · GitHub</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73044084067dac5e07b7c6721c991d399e203605.jpeg" data-download-href="/uploads/short-url/gpu1b2q6XtAMsIL7mWcuEyADZlP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73044084067dac5e07b7c6721c991d399e203605_2_690x238.jpeg" alt="image" data-base62-sha1="gpu1b2q6XtAMsIL7mWcuEyADZlP" width="690" height="238" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73044084067dac5e07b7c6721c991d399e203605_2_690x238.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73044084067dac5e07b7c6721c991d399e203605_2_1035x357.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73044084067dac5e07b7c6721c991d399e203605_2_1380x476.jpeg 2x" data-dominant-color="777676"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1867×645 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Lorensen (2019-09-11 21:12 UTC)

<p>I’m not sure a  transfer function can represent an X-Ray. I think you need a digitally reconstructed radiograph. The is an ITK example that <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Examples/Filtering/DigitallyReconstructedRadiograph1.cxx" rel="nofollow noopener">implements the DRR</a>.</p>
<p>Also, as part of a DARPA-Sponsored Virtual Autopsy Project we generated hundreds of DRR’s of soldiers. I could probably resurrect the ITK code. Here is a<br>
<a href="http://marchingcubes.org/images/c/c2/MMVR2006Poster.pdf" rel="nofollow noopener">poster of some of that work</a></p>
<p>.</p>

---

## Post #7 by @lassoan (2019-09-12 00:46 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="6" data-topic="7617">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>I’m not sure a transfer function can represent an X-Ray</p>
</blockquote>
</aside>
<p>If shading is disabled and scalar opacity transfer function is a linear ramp then volume raycast mapper computes DRR.</p>
<p>Assuming monoergetic radiation and linear attenuation, gray level of an image pixel in an X-ray image (after calibration and logarithmic processing) is proportional to the sum of linear attenuation coefficient integrated over the entire ray. Voxels in a CT volume are specified in Hounsfield units, which can be converted to/from linear attenuation coefficient using linear scaling and offset. Therefore, as long as the transfer function is linear and the ray integration is set up reasonably (there is no saturation, step size is not too small or large to numerical inaccuracies become significant, etc.), then volume raycast mapper computes a DRR image (with some linear scaling/offset).</p>

---
