---
topic_id: 40793
title: "Dentalsegmentator Does Not Complete On Slicer 5 7 0"
date: 2024-12-18
url: https://discourse.slicer.org/t/40793
---

# DentalSegmentator does not complete on Slicer 5.7.0

**Topic ID**: 40793
**Date**: 2024-12-18
**URL**: https://discourse.slicer.org/t/dentalsegmentator-does-not-complete-on-slicer-5-7-0/40793

---

## Post #1 by @dr_drcadcam (2024-12-18 22:31 UTC)

<p>Problem report for Slicer 5.7.0-2024-12-16 win-amd64: [please describe expected and actual behavior]</p>
<p>[DEBUG][Qt] 18.12.2024 10:51:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20241218_105123 [DEBUG][Qt] 18.12.2024 10:51:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.7.0-2024-12-16 (revision 33157 / f711b40) win-amd64 - installed release [DEBUG][Qt]</p>

---

## Post #2 by @lassoan (2024-12-19 06:10 UTC)

<p><a class="mention" href="/u/dr_drcadcam">@dr_drcadcam</a> Please describe what you did, what you expected to happen, and what happened instead.</p>

---

## Post #3 by @dr_drcadcam (2024-12-19 11:06 UTC)

<p>Good morning! I’m glad you informed me. I installed the latest version and even so the segmentation (DENTALSEGMENTATOR) didn’t work. It keeps running but doesn’t complete the segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe021c485dda930c149edc75c2a25778b0902716.png" data-download-href="/uploads/short-url/Af3Ny1LzCRMNiSriKcuQlo9xkFg.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe021c485dda930c149edc75c2a25778b0902716_2_562x298.png" data-base62-sha1="Af3Ny1LzCRMNiSriKcuQlo9xkFg" alt="image.png" width="562" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe021c485dda930c149edc75c2a25778b0902716_2_562x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe021c485dda930c149edc75c2a25778b0902716_2_843x447.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe021c485dda930c149edc75c2a25778b0902716_2_1124x596.png 2x" data-dominant-color="7B7E75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">2578×1366 496 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Fernanda_Palma (2025-10-10 17:17 UTC)

<p>i Have the same probllem</p>

---

## Post #5 by @lassoan (2025-10-16 12:33 UTC)

<p>Developers of AI segmentation models rely on Python packages that are kept being updated. These updates may break compatibility with old software. You may need to manually install older versions of nnnunet.</p>
<p>If you have problems running DentalSegmentator in the latest Slicer Stable Release or latest Slicer Preview Release then let us know.</p>

---
