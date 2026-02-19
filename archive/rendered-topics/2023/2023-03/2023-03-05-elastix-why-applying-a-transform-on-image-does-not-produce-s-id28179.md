---
topic_id: 28179
title: "Elastix Why Applying A Transform On Image Does Not Produce S"
date: 2023-03-05
url: https://discourse.slicer.org/t/28179
---

# Elastix, why applying a transform on image does not produce same image as the generated output at registration time?

**Topic ID**: 28179
**Date**: 2023-03-05
**URL**: https://discourse.slicer.org/t/elastix-why-applying-a-transform-on-image-does-not-produce-same-image-as-the-generated-output-at-registration-time/28179

---

## Post #1 by @S_Arbabi (2023-03-05 12:52 UTC)

<p>Hi,</p>
<p>I have two MR images (fixed, moving) and do the Elastix “rigid” registration in Slicer (5.0.2):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7c3607d3b375a80e62e3420cf701bd3713dab5.png" data-download-href="/uploads/short-url/mC1yNBReosc0FBWWIjONLiHlFkN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7c3607d3b375a80e62e3420cf701bd3713dab5.png" alt="image" data-base62-sha1="mC1yNBReosc0FBWWIjONLiHlFkN" width="612" height="500" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">809×660 22.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>after this process finishes, I have a generated (registered) moving image (called Volume_7) and a transformation (called Transform_1):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4427d1d5a834f1f44469a93bc0ced246d3491b53.png" data-download-href="/uploads/short-url/9IVMr3xrvDPUCS6MU31uZp96SFd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4427d1d5a834f1f44469a93bc0ced246d3491b53_2_690x111.png" alt="image" data-base62-sha1="9IVMr3xrvDPUCS6MU31uZp96SFd" width="690" height="111" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4427d1d5a834f1f44469a93bc0ced246d3491b53_2_690x111.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4427d1d5a834f1f44469a93bc0ced246d3491b53.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4427d1d5a834f1f44469a93bc0ced246d3491b53.png 2x" data-dominant-color="DCEAF3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×128 7.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>now I transform the moving image with the Transform_1 and expect its output should be the same as Volume_7. I thought it should be a valid assumption, unless I misunderstood a part or so?</p>
<p>this is moving after being transformed by this transformation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3202eb2c787fbde881c8d6e0c093bde3eb043ce.png" data-download-href="/uploads/short-url/yGMYv4IpMsjuObX7Dx9ttZO2n5c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3202eb2c787fbde881c8d6e0c093bde3eb043ce.png" alt="image" data-base62-sha1="yGMYv4IpMsjuObX7Dx9ttZO2n5c" width="690" height="251" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">794×289 7.22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and this is moving after being registered on fixed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebb0093a8e05e26fd60593c7b1c5445b618ac86.png" data-download-href="/uploads/short-url/26jkLZyH8LfTQMocVKL1f5mSA2G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebb0093a8e05e26fd60593c7b1c5445b618ac86.png" alt="image" data-base62-sha1="26jkLZyH8LfTQMocVKL1f5mSA2G" width="690" height="252" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×291 9.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>could you please help me in this?</p>

---

## Post #2 by @lassoan (2023-03-06 04:13 UTC)

<p>Both are correct and about the same in physical space, they just have different geometry (origin, spacing, axis directions).</p>
<p>Elastix is based on the ITK library. ITK cannot easily extrapolate transforms, so usually it only computes transformed moving image in the fixed volume’s geometry. It simply cuts off any parts of the transformed moving image that is outside of the fixed image.</p>
<p>Slicer uses both ITK and VTK, and it takes advantage of VTK’s more advanced transform infrastructure, which can smoothly extrapolate and invert any transforms on-the-fly. The result is that Slicer can harden the transform on the moving image without cutting off any part of the image. If harden a rigid transform then operation is lossless (the image is not resampled). If you prefer setting a specific geometry then you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">resample the image on a chosen reference image</a>.</p>

---
