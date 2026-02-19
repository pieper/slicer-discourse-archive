---
topic_id: 42235
title: "Imported Volumes Are Not Aligned"
date: 2025-03-20
url: https://discourse.slicer.org/t/42235
---

# Imported volumes are not aligned

**Topic ID**: 42235
**Date**: 2025-03-20
**URL**: https://discourse.slicer.org/t/imported-volumes-are-not-aligned/42235

---

## Post #1 by @Aidan (2025-03-20 18:57 UTC)

<p>Hi, I have a very basic issue that I can’t seem to figure out. When I import 2 different NIFTI volumes of the same subject from the same session in Slicer (one is an anatomical 3D MR volume and the other is a function EPI time series) they appear in completely different orientations to each other.</p>
<p>However, they were acquired with the same bounding box parameters and orientations on the scanner, converted from DICOM to NIFTI the same way (dcm2niix), and indeed they appear correctly and perfectly aligned when imported into any neuroimaging software (AFNI, FSL, SPM).</p>
<p>How can I make Slicer behave in the same was as these other (RAS-based) software when importing volumes?</p>
<p>I did search the forum and found this (<a href="https://discourse.slicer.org/t/slice-view-orientation-of-oblique-rotated-volumes-aligned-to-volume-or-anatomical-axes/20092" class="inline-onebox">Slice view orientation of oblique/rotated volumes - aligned to volume or anatomical axes?</a>), but it doesn’t seem to resolve my issue.</p>

---

## Post #2 by @Aidan (2025-03-24 15:36 UTC)

<p>To illustrate, here are the same 2 scans (anatomy in grey and functional overlay in color) loaded in Slicer (misaligned):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22670f77a2440975e919f01ebd85aab2cc9c2ecf.jpeg" data-download-href="/uploads/short-url/4Ul2ttgCYu6mRauCJH1iLK9dl1l.jpeg?dl=1" title="FuncAnatMisalign" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22670f77a2440975e919f01ebd85aab2cc9c2ecf_2_606x499.jpeg" alt="FuncAnatMisalign" data-base62-sha1="4Ul2ttgCYu6mRauCJH1iLK9dl1l" width="606" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22670f77a2440975e919f01ebd85aab2cc9c2ecf_2_606x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22670f77a2440975e919f01ebd85aab2cc9c2ecf_2_909x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22670f77a2440975e919f01ebd85aab2cc9c2ecf_2_1212x998.jpeg 2x" data-dominant-color="35363E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">FuncAnatMisalign</span><span class="informations">1920×1584 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And FSLeyes (correctly aligned):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b73dbd3179bb1cefd27c07645fd503ba4ae1831.jpeg" data-download-href="/uploads/short-url/jTEARdIhKMzwDrYXu4y2670XEIx.jpeg?dl=1" title="Screenshot 2025-03-24 at 11.24.59 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b73dbd3179bb1cefd27c07645fd503ba4ae1831_2_690x448.jpeg" alt="Screenshot 2025-03-24 at 11.24.59 AM" data-base62-sha1="jTEARdIhKMzwDrYXu4y2670XEIx" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b73dbd3179bb1cefd27c07645fd503ba4ae1831_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b73dbd3179bb1cefd27c07645fd503ba4ae1831_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b73dbd3179bb1cefd27c07645fd503ba4ae1831_2_1380x896.jpeg 2x" data-dominant-color="473D3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-24 at 11.24.59 AM</span><span class="informations">3450×2240 680 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any ideas what these software are doing differently to yield this discrepancy?</p>

---

## Post #3 by @cpinter (2025-03-25 12:28 UTC)

<p>This indeed seems like LPS-RAS issue. When you load the Nifti file, there is a checkbox to show options. Can you set some option that allows keeping (or converting) the orientation? Or if you have the original DICOM files they would probably load properly.</p>

---

## Post #4 by @Aidan (2025-03-26 21:11 UTC)

<p>Thanks Csaba. I assume you mean the “Ignore Orientation” checkbox?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45afe50ec895791aefffbe142f7d997809d0de29.jpeg" data-download-href="/uploads/short-url/9WtNuqOwIjJl6u74CGsGbdhTSsh.jpeg?dl=1" title="Screenshot 2025-03-25 at 1.01.32 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45afe50ec895791aefffbe142f7d997809d0de29_2_690x310.jpeg" alt="Screenshot 2025-03-25 at 1.01.32 PM" data-base62-sha1="9WtNuqOwIjJl6u74CGsGbdhTSsh" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45afe50ec895791aefffbe142f7d997809d0de29_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45afe50ec895791aefffbe142f7d997809d0de29_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45afe50ec895791aefffbe142f7d997809d0de29_2_1380x620.jpeg 2x" data-dominant-color="525152"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-25 at 1.01.32 PM</span><span class="informations">2416×1088 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I select that for either or both scans, then at least both volumes now load in approximately the same orientation! However, they’re still not aligned in the same was as they appear in neuroimaging software…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/754eb3625d5170acbe50451375909227ba3fa4a2.jpeg" data-download-href="/uploads/short-url/gJKtJpOj9hWfGxNH2QURdguQRnY.jpeg?dl=1" title="Screenshot 2025-03-25 at 1.04.14 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/754eb3625d5170acbe50451375909227ba3fa4a2_2_577x500.jpeg" alt="Screenshot 2025-03-25 at 1.04.14 PM" data-base62-sha1="gJKtJpOj9hWfGxNH2QURdguQRnY" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/754eb3625d5170acbe50451375909227ba3fa4a2_2_577x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/754eb3625d5170acbe50451375909227ba3fa4a2_2_865x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/754eb3625d5170acbe50451375909227ba3fa4a2_2_1154x1000.jpeg 2x" data-dominant-color="3D4042"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-25 at 1.04.14 PM</span><span class="informations">1920×1661 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2025-03-26 22:10 UTC)

<aside class="quote no-group" data-username="Aidan" data-post="4" data-topic="42235">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c5a1d2/48.png" class="avatar"> Aidan:</div>
<blockquote>
<p>ation! However, they’re still not aligned in the same was as they appear in neuroimaging software…</p>
</blockquote>
</aside>
<p>To test whether this is LPS/RAS issue, load both volumes normally into Slicer (don’t use the option above). Go to transforms module and create a transform in which the first two diagonal values are -1. Then assign one of the volumes to this transform. See if they line up.</p>

---
