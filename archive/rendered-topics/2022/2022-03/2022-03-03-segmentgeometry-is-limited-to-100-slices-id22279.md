---
topic_id: 22279
title: "Segmentgeometry Is Limited To 100 Slices"
date: 2022-03-03
url: https://discourse.slicer.org/t/22279
---

# SegmentGeometry is limited to 100 slices

**Topic ID**: 22279
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/segmentgeometry-is-limited-to-100-slices/22279

---

## Post #1 by @Michel_Atieh (2022-03-03 10:05 UTC)

<p>Hello, I noticed that when segmenting large organs like the uterus which consisted of ~150 slices in one case, when I wanted to get the information (mean HU, area, etc.) for each slice, the table always printed only 100 values, which seemed to take every other slice’s information.<br>
When the number of slices is less than 100, the table displays all the slices correctly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f81a186a3a0186969116ce42b114e5bd28b1edab.png" data-download-href="/uploads/short-url/zoOjWMZKYRDPJ6FUE57MKLaOL11.png?dl=1" title="Screenshot from 2022-03-03 11-05-17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81a186a3a0186969116ce42b114e5bd28b1edab_2_690x408.png" alt="Screenshot from 2022-03-03 11-05-17" data-base62-sha1="zoOjWMZKYRDPJ6FUE57MKLaOL11" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81a186a3a0186969116ce42b114e5bd28b1edab_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f81a186a3a0186969116ce42b114e5bd28b1edab_2_1035x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f81a186a3a0186969116ce42b114e5bd28b1edab.png 2x" data-dominant-color="41423E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-03-03 11-05-17</span><span class="informations">1298×768 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you.</p>

---

## Post #2 by @jmhuie (2022-03-03 20:48 UTC)

<p>Change the Percent Interval to 0 to compute on every slice. It’s set to 1 because for the initial intent of the module, folks often have way more than 100 slices to compute on.</p>
<p>If any other questions come up, I’d recommend checking the github documentation first. <a href="https://github.com/jmhuie/Slicer-SegmentGeometry" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jmhuie/Slicer-SegmentGeometry: Extension to calculate second moment of area and other cross-sectional properties in 3D Slicer</a></p>

---

## Post #3 by @Michel_Atieh (2022-03-03 22:18 UTC)

<p>Thanks a lot for your help!</p>

---
