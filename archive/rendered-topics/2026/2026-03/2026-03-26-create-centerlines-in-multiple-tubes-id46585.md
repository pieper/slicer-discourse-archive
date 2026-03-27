---
topic_id: 46585
title: "Create Centerlines In Multiple Tubes"
date: 2026-03-26
url: https://discourse.slicer.org/t/46585
---

# Create centerlines in multiple tubes?

**Topic ID**: 46585
**Date**: 2026-03-26
**URL**: https://discourse.slicer.org/t/create-centerlines-in-multiple-tubes/46585

---

## Post #1 by @Morgenstern (2026-03-26 19:01 UTC)

<p>Hey, I have a structure consisting of many closed, not connected tubes. I would like to know if it is possible to detect the centerlines of multiple tubes at once. I was only able to create the centerline for one tube at a time, even when setting endpoints for multiple tubes manually since the auto detection wasn’t working on this structure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/035a662e9c2cd718e47ad37f4c416a48d272123c.jpeg" data-download-href="/uploads/short-url/tF6VlRpeXxsoppo5QOKNb1bD8o.jpeg?dl=1" title="Bildschirmfoto 2025-12-17 um 15.38.52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035a662e9c2cd718e47ad37f4c416a48d272123c_2_528x500.jpeg" alt="Bildschirmfoto 2025-12-17 um 15.38.52" data-base62-sha1="tF6VlRpeXxsoppo5QOKNb1bD8o" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035a662e9c2cd718e47ad37f4c416a48d272123c_2_528x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035a662e9c2cd718e47ad37f4c416a48d272123c_2_792x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/035a662e9c2cd718e47ad37f4c416a48d272123c_2_1056x1000.jpeg 2x" data-dominant-color="9C9BAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2025-12-17 um 15.38.52</span><span class="informations">1612×1526 586 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f9480a83f0acbbf99b75cc2b4421d4480f02693.jpeg" data-download-href="/uploads/short-url/mLI59nk46ktkXy6HVYuoGjp67wT.jpeg?dl=1" title="Screenshot 2026-03-23 172354" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f9480a83f0acbbf99b75cc2b4421d4480f02693_2_690x449.jpeg" alt="Screenshot 2026-03-23 172354" data-base62-sha1="mLI59nk46ktkXy6HVYuoGjp67wT" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f9480a83f0acbbf99b75cc2b4421d4480f02693_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f9480a83f0acbbf99b75cc2b4421d4480f02693_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f9480a83f0acbbf99b75cc2b4421d4480f02693_2_1380x898.jpeg 2x" data-dominant-color="9D998B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-03-23 172354</span><span class="informations">1920×1252 632 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2026-03-26 22:15 UTC)

<p>The ExtractCenterlines module auto detection of endpoints is designed for branching trees like vasculature or bronchial airway trees, not for multiple separate tubes.  For separate tubes, just find the centerline of each one serially.  You can automate this using python. You can split the each tube into a separate segment using the Islands tool, and then iterate over each segment, finding the centerline.</p>

---
