---
topic_id: 47500
title: "Pyradiomics GLRLM crashing at native 100um resolution vs 250um"
date: 2026-06-29
url: https://discourse.slicer.org/t/47500
last_bumped: 2026-06-29T19:25:43.488Z
---

# Pyradiomics GLRLM crashing at native 100um resolution vs 250um

**Topic ID**: 47500
**Date**: 2026-06-29
**URL**: https://discourse.slicer.org/t/pyradiomics-glrlm-crashing-at-native-100um-resolution-vs-250um/47500

---

## Post #1 by @oviya (2026-06-29 17:10 UTC)

<p>Hello everyone! My name is Oviya, I’m an undergrad hoping to get a bit of help.</p>
<p>I have been trying extract features from MRI images via a compute cluster, and have been successful with downsampled (250um) images (41MB). However, I am unable to run the same script on the native 100um resolution (542 MB). On the 100um resolution, I’ve been able to extract GLCM, GLSZM, NGTDM, and GLDM, but <strong>not</strong> GLRLM.</p>
<p>Tech support from the compute cluster indicated that the job is failing with a segmentation fault (exit code 139), which indicates a low-level crash in compiled code (e.g., ITK/SimpleITK/PyRadiomics or NumPy C extensions), not a Python exception.</p>
<p>From the logs, PyRadiomics completes feature extraction successfully (“Reading feature maps: 100%”), and the crash occurs immediately afterward during post-processing. So the failure might be happening in the step where extracted feature maps are converted into arrays and assembled into a feature matrix, or during cleanup between chunks.</p>
<p>I’m unsure of how to resolve this. If anyone could take a peek at the code/offer advice, it would be appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad3ba1d2f6a2464d78eb94faedf43d9de6982651.png" data-download-href="/uploads/short-url/oIumxMtk5qUKq4aZyVJU7BCfr7H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad3ba1d2f6a2464d78eb94faedf43d9de6982651.png" alt="image" data-base62-sha1="oIumxMtk5qUKq4aZyVJU7BCfr7H" width="690" height="419" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1284×780 78.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f998cda4ab2c2f93185a805c47835048b3ebc347.png" data-download-href="/uploads/short-url/zC2gIGt6Un9OZwS0TijLjvOM8BN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f998cda4ab2c2f93185a805c47835048b3ebc347_2_690x125.png" alt="image" data-base62-sha1="zC2gIGt6Un9OZwS0TijLjvOM8BN" width="690" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f998cda4ab2c2f93185a805c47835048b3ebc347_2_690x125.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f998cda4ab2c2f93185a805c47835048b3ebc347_2_1035x187.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f998cda4ab2c2f93185a805c47835048b3ebc347_2_1380x250.png 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1468×268 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9257a33ce06ee3606cb56b3a2bf91bd368389cbc.png" data-download-href="/uploads/short-url/kSBtm3tgGRfO6ntXnPbBhYQSfjm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257a33ce06ee3606cb56b3a2bf91bd368389cbc_2_420x500.png" alt="image" data-base62-sha1="kSBtm3tgGRfO6ntXnPbBhYQSfjm" width="420" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257a33ce06ee3606cb56b3a2bf91bd368389cbc_2_420x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257a33ce06ee3606cb56b3a2bf91bd368389cbc_2_630x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257a33ce06ee3606cb56b3a2bf91bd368389cbc_2_840x1000.png 2x" data-dominant-color="201E20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1268×1506 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc9b40d152931aa586660bd0188404d5c8e47bcb.png" data-download-href="/uploads/short-url/vtzFEUq8XJAWaTh2pPyuAHtWd87.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc9b40d152931aa586660bd0188404d5c8e47bcb_2_433x500.png" alt="image" data-base62-sha1="vtzFEUq8XJAWaTh2pPyuAHtWd87" width="433" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc9b40d152931aa586660bd0188404d5c8e47bcb_2_433x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc9b40d152931aa586660bd0188404d5c8e47bcb_2_649x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc9b40d152931aa586660bd0188404d5c8e47bcb_2_866x1000.png 2x" data-dominant-color="1F1F20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1284×1482 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @PaoloZaffino (2026-06-29 17:39 UTC)

<p>Just out of curiosity, have you tried <a href="https://www.radiomicsjl.org/" rel="noopener nofollow ugc">Radiomics.jl</a>?</p>
<p>It’s written in Julia (so it is much more efficient) but it can be easily called from Python.</p>
<p>Of course, it is IBSI compliant!</p>

---

## Post #3 by @oviya (2026-06-29 19:25 UTC)

<p>I haven’t tried radiomics.jl, I/my colleagues haven’t used it before, so there is some unfamiliarity. However it can definitely be a next step I can try! In the meantime if there are PyRadiomics solutions, I’d love to hear.</p>
<p>Best,<br>
Oviya</p>

---
