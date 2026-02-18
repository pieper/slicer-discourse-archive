# Can we edit multiple segments at once?

**Topic ID**: 41101
**Date**: 2025-01-15
**URL**: https://discourse.slicer.org/t/can-we-edit-multiple-segments-at-once/41101

---

## Post #1 by @Dr_Akshaya_S_R1 (2025-01-15 23:25 UTC)

<p>Im working on a oroject that involves more than 35 to 40 segments and each representing anatomy with similar threshold. So im thinking on working on them simultaneously. Is that possible?</p>

---

## Post #2 by @lassoan (2025-01-15 23:26 UTC)

<p>Yes, sure, there are many ways to achieve this. What exactly would you like to do?</p>

---

## Post #3 by @Dr_Akshaya_S_R1 (2025-01-16 09:06 UTC)

<p>I would like to know if there is any way to segment multiple teeth at once or smooth them out. I’m currently segmenting teeth manually, and all of them fall under the same threshold. If I segment all the teeth as one segment, is there a way that I can then divide them into individual segments?</p>

---

## Post #4 by @Matteboo (2025-01-16 15:30 UTC)

<p>You can use the island module and split island to segment.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad08dda30d838a491fd7f9e52bf562e5ea9568bd.png" data-download-href="/uploads/short-url/oGJB1G1Bxknw31pj18p34H5rUOF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad08dda30d838a491fd7f9e52bf562e5ea9568bd_2_452x500.png" alt="image" data-base62-sha1="oGJB1G1Bxknw31pj18p34H5rUOF" width="452" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad08dda30d838a491fd7f9e52bf562e5ea9568bd_2_452x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad08dda30d838a491fd7f9e52bf562e5ea9568bd_2_678x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad08dda30d838a491fd7f9e52bf562e5ea9568bd.png 2x" data-dominant-color="36393A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×786 40.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2025-01-16 16:35 UTC)

<p>You can use DentalSegmentator and other extension for fully automatic teeth segmentation. You can separate teeth using Scissors effect and then smooth all visible segments at once using the Smoothing effect with “joint smoothing” method.</p>

---

## Post #6 by @Dr_Akshaya_S_R1 (2025-01-17 17:55 UTC)

<p>Thank you for your response. However, I am experiencing issues with the dental segmentation module. Every time I try to use it, I encounter an error. How can I resolve this?</p>

---

## Post #7 by @Dr_Akshaya_S_R1 (2025-01-17 18:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e7135f46049a42dce3b4d27bf2320a619b4be0e.png" data-download-href="/uploads/short-url/i2yIhqBt4zS87KStSwIZ3MN3f2u.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e7135f46049a42dce3b4d27bf2320a619b4be0e.png" data-base62-sha1="i2yIhqBt4zS87KStSwIZ3MN3f2u" alt="image.png" width="523" height="84" data-dominant-color="362828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1332×214 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2025-01-20 14:51 UTC)

<p>Please use the latest Slicer Preview Release. If you still experience any difficulties with DentalSegmentator then review <a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#troubleshooting">documentation</a>, posts related to this topic on this forum, and if you still have unanswered questions then post it as a new topic (do not post further question on DentalSegmentator in this topic, which is about editing multiple segments at once).</p>

---
