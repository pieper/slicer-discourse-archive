---
topic_id: 26118
title: "Thresholding In Drr Image Computation Module"
date: 2022-11-07
url: https://discourse.slicer.org/t/26118
---

# Thresholding in DRR Image Computation module

**Topic ID**: 26118
**Date**: 2022-11-07
**URL**: https://discourse.slicer.org/t/thresholding-in-drr-image-computation-module/26118

---

## Post #1 by @fieldr4 (2022-11-07 19:23 UTC)

<p>Hi Slicer community,</p>
<p>Is the “Hounsfield unit threshold” applied in the “Plastimatch DRR image processing” submenu in the <code>DRR Image Computation</code> module represented in the “Plastimatch DRR command arguments (read only)” field?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6456fc477182deb2367f1bca6c7d75b20caf0af.png" data-download-href="/uploads/short-url/q0rFliZnxSNrtm9MQKMkwTwWuAL.png?dl=1" title="Thresholding in DRR Image Computation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6456fc477182deb2367f1bca6c7d75b20caf0af_2_183x250.png" alt="Thresholding in DRR Image Computation" data-base62-sha1="q0rFliZnxSNrtm9MQKMkwTwWuAL" width="183" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6456fc477182deb2367f1bca6c7d75b20caf0af_2_183x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6456fc477182deb2367f1bca6c7d75b20caf0af_2_274x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6456fc477182deb2367f1bca6c7d75b20caf0af_2_366x500.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Thresholding in DRR Image Computation</span><span class="informations">586×797 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is a great functionality and it seems to be missing from the <a href="http://plastimatch.org/drr.html" rel="noopener nofollow ugc">Plastimatch DRR documentation</a>.</p>

---

## Post #2 by @Mik (2022-11-08 09:47 UTC)

<p>No, it isn’t. It’s not a plastimatch feature, so it’s absent in the docs. It’s a part of “DRR generation” CLI module. The threshold filter is applied before any <code>plastimatch drr</code> functionality, some sort of preprocessing of original CT data if needed. May be something like than can be done with <code>plastimatch adjust</code> command, but i have never tried.</p>

---

## Post #3 by @fieldr4 (2022-11-09 03:01 UTC)

<p>Plastimatch adjust worked perfectly! Thank you for the recommendation (and to Greg Sharp in the Plastimatch Google group).</p>
<p>For all those interested, --pw-linear “-inf,0,66,-1000,67,67,inf,1” maps all input intensities below 66 to -1000 and maps all values above 66 to themselves. Basically, like setting the thresholder slider in 3D Slicer to 66.</p>

---
