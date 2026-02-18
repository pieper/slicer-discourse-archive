# Register MRI with CT by Elastix

**Topic ID**: 42624
**Date**: 2025-04-19
**URL**: https://discourse.slicer.org/t/register-mri-with-ct-by-elastix/42624

---

## Post #1 by @Asparagine (2025-04-19 13:01 UTC)

<p>Hello everyone. I’m new to slicer and now using elastix to register the MRI to CT (about temporomandibular joint), but I found it is not that accurate using presets <strong>generic (all)</strong> and <strong>generic rigid (all)</strong>.</p>
<p>I read the paper <em>elastix: A Toolbox for Intensity-Based Medical Image Registration</em>, which mentioned that elastix support different metrics like MSD, NC, MI, etc., but I don’t know how to adjust that in slicer. Is this included in the preset or other options? How should I adjust for a better preformance for MRI and CT registration?</p>
<p>By the way, we have tried cropping the data to cover approximately the same anatomical region, it is better, but still not as what we want.</p>
<p>P.S. the figure shows the problem we met, where the red and blue curve shows the structure we are interested in, and we want them to overlap each other.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be1f07428bb93bc6df2ef0238e4ba0cd90553c4.jpeg" data-download-href="/uploads/short-url/aPhSK1TfzIYuHkigUORRQRVXG6g.jpeg?dl=1" title="sample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4be1f07428bb93bc6df2ef0238e4ba0cd90553c4.jpeg" alt="sample" data-base62-sha1="aPhSK1TfzIYuHkigUORRQRVXG6g" width="668" height="452"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample</span><span class="informations">668×452 46.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-04-19 13:05 UTC)

<p>You can edit the configuration files. It is easier in latest Slicer Preview Release, which contains a built-in preset editor for Elastix.</p>
<p>I would not expect that changing the similarity metric from the default MI to something else will significantly improve the results. Cropping the region of interest more tightly to the region of interest and improve initial position will probably have bigger impact.</p>
<p>You can also try ANTs, which uses somewhat different registration algorithms.</p>

---

## Post #3 by @Asparagine (2025-04-21 05:36 UTC)

<p>Thank you for your reply, I’ll try as you say.</p>

---
