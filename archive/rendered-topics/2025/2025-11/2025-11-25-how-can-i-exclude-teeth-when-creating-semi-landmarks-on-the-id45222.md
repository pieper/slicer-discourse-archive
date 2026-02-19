---
topic_id: 45222
title: "How Can I Exclude Teeth When Creating Semi Landmarks On The"
date: 2025-11-25
url: https://discourse.slicer.org/t/45222
---

# How Can I Exclude Teeth When Creating Semi-Landmarks on the Mandible?

**Topic ID**: 45222
**Date**: 2025-11-25
**URL**: https://discourse.slicer.org/t/how-can-i-exclude-teeth-when-creating-semi-landmarks-on-the-mandible/45222

---

## Post #1 by @Esra_Karacan (2025-11-25 14:01 UTC)

<p>Dear all,</p>
<p>I am working on human mandibles. Most of my material has missing teeth. So, I would like to discard the teeth and put the semi-landmarks on just bone. I tried to delete the teeth, but the software put on the semi-landmark on the place of the teeth. So, it didn’t work. In article, I saw that they made a contour and put the semi-landmarks in this contour (The picture is attached). But they did it another software. Is it possible to do it in Slicer? Or do you have other suggestions to discard the teeth? Thank you very much in advance.<br>
Cheers,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7fc108c6097e47c16bf3b3b980369773897ea2.jpeg" data-download-href="/uploads/short-url/bcqXaXpy8m23tUb2eHD3XkTseFI.jpeg?dl=1" title="Ekran Resmi 2025-11-25 16.47.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7fc108c6097e47c16bf3b3b980369773897ea2_2_345x244.jpeg" alt="Ekran Resmi 2025-11-25 16.47.50" data-base62-sha1="bcqXaXpy8m23tUb2eHD3XkTseFI" width="345" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7fc108c6097e47c16bf3b3b980369773897ea2_2_345x244.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7fc108c6097e47c16bf3b3b980369773897ea2_2_517x366.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7fc108c6097e47c16bf3b3b980369773897ea2_2_690x488.jpeg 2x" data-dominant-color="A49DA6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Resmi 2025-11-25 16.47.50</span><span class="informations">1412×1000 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c918c3a3f4dd5dfd3ddd1ba2cdd9e9195a415bdc.jpeg" data-download-href="/uploads/short-url/sGZ1Ma0SxTIAebH97MXnCaegW3q.jpeg?dl=1" title="Ekran Resmi 2025-11-25 16.49.03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c918c3a3f4dd5dfd3ddd1ba2cdd9e9195a415bdc_2_244x250.jpeg" alt="Ekran Resmi 2025-11-25 16.49.03" data-base62-sha1="sGZ1Ma0SxTIAebH97MXnCaegW3q" width="244" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c918c3a3f4dd5dfd3ddd1ba2cdd9e9195a415bdc_2_244x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c918c3a3f4dd5dfd3ddd1ba2cdd9e9195a415bdc_2_366x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c918c3a3f4dd5dfd3ddd1ba2cdd9e9195a415bdc_2_488x500.jpeg 2x" data-dominant-color="D6DDD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Resmi 2025-11-25 16.49.03</span><span class="informations">520×532 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-11-25 18:00 UTC)

<p>You will remove them using the MarkupEditor, which allows you to select points by drawing curves. See the tutorial here; <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/MarkupsEditor at main · SlicerMorph/Tutorials · GitHub</a></p>

---
