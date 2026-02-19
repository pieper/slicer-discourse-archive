---
topic_id: 33729
title: "Problems In Subtracting 2 Segmentations"
date: 2024-01-11
url: https://discourse.slicer.org/t/33729
---

# Problems in subtracting 2 segmentations

**Topic ID**: 33729
**Date**: 2024-01-11
**URL**: https://discourse.slicer.org/t/problems-in-subtracting-2-segmentations/33729

---

## Post #1 by @Inka_Saraswati (2024-01-11 08:26 UTC)

<p>Hi, all. My case is a cleft lip and palate scan. My goal is to find volume of the bony defect by subtracting the original skull and its mirrored skull. My data looks as below. I know it’s confusing but what matters are just the 2 segmentations I marked yellow: Green (Bone cut) is from the original skull, and Red (Bone cut copy registered) is the mirrored skull.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f95b74fb3f4a87262ad32a10c6b0c7474fd50b0.jpeg" data-download-href="/uploads/short-url/94uQrjWRV9coXiXup0FPPMssjhC.jpeg?dl=1" title="Pic 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f95b74fb3f4a87262ad32a10c6b0c7474fd50b0_2_690x338.jpeg" alt="Pic 1" data-base62-sha1="94uQrjWRV9coXiXup0FPPMssjhC" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f95b74fb3f4a87262ad32a10c6b0c7474fd50b0_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f95b74fb3f4a87262ad32a10c6b0c7474fd50b0_2_1035x507.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f95b74fb3f4a87262ad32a10c6b0c7474fd50b0_2_1380x676.jpeg 2x" data-dominant-color="A2A09F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic 1</span><span class="informations">2878×1410 671 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(If you’re curious with my overall data, the top ones (CTVolume and Segmentation) are the original skull, the Copy ones are the mirror images, and anything below Registration Matrix are the mirror images that have been registered. All transforms are already hardened)</p>
<p>I tried to subtract with Logical Operators and when I click apply, nothing happens. And I want to know what I did wrong. My settings are as follows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/013878c95e0827514c26141e7762869540d24b04.jpeg" data-download-href="/uploads/short-url/aNt0c1SVm1MrC6hhdnSf41RK6M.jpeg?dl=1" title="Pic 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/013878c95e0827514c26141e7762869540d24b04_2_690x331.jpeg" alt="Pic 2" data-base62-sha1="aNt0c1SVm1MrC6hhdnSf41RK6M" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/013878c95e0827514c26141e7762869540d24b04_2_690x331.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/013878c95e0827514c26141e7762869540d24b04_2_1035x496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/013878c95e0827514c26141e7762869540d24b04_2_1380x662.jpeg 2x" data-dominant-color="A1A1A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic 2</span><span class="informations">2880×1384 786 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3feec4ca47dd14bccf398baa833d124bbe737cfa.png" data-download-href="/uploads/short-url/97zDH5XkPjQR0IbtnegAVR352pY.png?dl=1" title="Pic 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3feec4ca47dd14bccf398baa833d124bbe737cfa_2_690x450.png" alt="Pic 3" data-base62-sha1="97zDH5XkPjQR0IbtnegAVR352pY" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3feec4ca47dd14bccf398baa833d124bbe737cfa_2_690x450.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3feec4ca47dd14bccf398baa833d124bbe737cfa_2_1035x675.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3feec4ca47dd14bccf398baa833d124bbe737cfa.png 2x" data-dominant-color="F1F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic 3</span><span class="informations">1120×732 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Any help is appreciated!</p>

---
