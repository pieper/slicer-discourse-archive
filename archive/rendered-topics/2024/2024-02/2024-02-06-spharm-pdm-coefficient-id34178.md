# Spharm PDM Coefficient

**Topic ID**: 34178
**Date**: 2024-02-06
**URL**: https://discourse.slicer.org/t/spharm-pdm-coefficient/34178

---

## Post #1 by @Golriz (2024-02-06 19:28 UTC)

<p>I have a concern regarding the reconstruction of the 3D mesh from the coefficients using the provided scripts, namely “SphericalHarmonicPolynomial.txx” and “SphericalHarmonicMeshSource.cxx”. The resulting mesh appears to be compressed and does not match our expectations or the real case.</p>
<p>We would like to explore the possibility of adjusting the coefficients to observe their effect on the reconstructed mesh. Our goal is to understand how different coefficients impact the final mesh output.<br>
I will be attaching both the reconstructed mesh and the expected outcome for comparison. Could you please review this issue and provide any insights or suggestions for improvement?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d731b77dc238c666e3c85831e47c1c80d61f668.png" data-download-href="/uploads/short-url/1UYP30CNkfRoqXWyHyT6F9vJme4.png?dl=1" title="Real" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d731b77dc238c666e3c85831e47c1c80d61f668_2_360x500.png" alt="Real" data-base62-sha1="1UYP30CNkfRoqXWyHyT6F9vJme4" width="360" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d731b77dc238c666e3c85831e47c1c80d61f668_2_360x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d731b77dc238c666e3c85831e47c1c80d61f668_2_540x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d731b77dc238c666e3c85831e47c1c80d61f668.png 2x" data-dominant-color="989A99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Real</span><span class="informations">696×966 81.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f11fcf53ab2e799c0b2d52b1b3fc1534cbd2b1cb.png" data-download-href="/uploads/short-url/yp5dO6l7Tgr38MMncKLu1vtbXRN.png?dl=1" title="Reconstructed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11fcf53ab2e799c0b2d52b1b3fc1534cbd2b1cb_2_638x500.png" alt="Reconstructed" data-base62-sha1="yp5dO6l7Tgr38MMncKLu1vtbXRN" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11fcf53ab2e799c0b2d52b1b3fc1534cbd2b1cb_2_638x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11fcf53ab2e799c0b2d52b1b3fc1534cbd2b1cb_2_957x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f11fcf53ab2e799c0b2d52b1b3fc1534cbd2b1cb.png 2x" data-dominant-color="9D9EB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Reconstructed</span><span class="informations">1165×913 62.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @styner (2024-02-12 22:43 UTC)

<p>Hi Golriz, are these surfaces open on one end, or are these closed surfaces.<br>
This is likely not an issue of the degree of the coefficients, but rather that the surface reconstruction failed as some preconditions are not met (e.g. that the surfaces need to be closed).</p>
<p>Please provide more details on how you did the surface reconstruction?<br>
Best<br>
Martin</p>

---

## Post #3 by @Golriz (2024-02-13 19:29 UTC)

<p>Hello Martin,<br>
thank you for your response.<br>
Yes the coefficiants are for the closed mesh. We did the same procedure as you explained in one answer: “we sample the spherical parametrization space and then evaluate the spherical harmonic series at those sample”. we use SlicerSALT to first calculate the coefficients of our groundtruth tooth , then change a little bit the coeff (std of 0.2) to see what we will get as reconstructed tooth. Then we do spherical sampling scheme based on an icosahedron subdivision.</p>
<p>Best regards,</p>
<p>Golriz</p>

---
