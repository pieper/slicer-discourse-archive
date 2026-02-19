---
topic_id: 14374
title: "Sequence Of Pngs Getting Interlaced Artifact"
date: 2020-11-02
url: https://discourse.slicer.org/t/14374
---

# Sequence of PNGs, getting interlaced artifact

**Topic ID**: 14374
**Date**: 2020-11-02
**URL**: https://discourse.slicer.org/t/sequence-of-pngs-getting-interlaced-artifact/14374

---

## Post #1 by @tomasb (2020-11-02 06:24 UTC)

<p>Operating system: win10<br>
Slicer version: 4.11.20200930</p>
<p>Expected behavior:<br>
I follow this one minute tutorial (<a href="https://www.youtube.com/watch?v=BcnpzYE8VO8" class="inline-onebox" rel="noopener nofollow ugc">Load sequence of PNG files as a 3D volume into 3D Slicer - YouTube</a>)<br>
and expect the 3d model.</p>
<p>Actual behavior:<br>
one of the slices gets an interlaced artifact as you can see here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1e4c859eaea95102a9d5d4dd78ea118896547ef.jpeg" data-download-href="/uploads/short-url/yvTeyTKlBnVpV0guFtNliw16Q11.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1e4c859eaea95102a9d5d4dd78ea118896547ef_2_690x423.jpeg" alt="error" data-base62-sha1="yvTeyTKlBnVpV0guFtNliw16Q11" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1e4c859eaea95102a9d5d4dd78ea118896547ef_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1e4c859eaea95102a9d5d4dd78ea118896547ef_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1e4c859eaea95102a9d5d4dd78ea118896547ef_2_1380x846.jpeg 2x" data-dominant-color="8A8A97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">2303×1413 461 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I don’t understand why the image (10) generates that pattern,<br>
give that it’s not particularly different than the rest.</p>
<p>you can check my 20 pngs dataset here:<br>
<a href="https://drive.google.com/drive/folders/1vRMPralT98ORdev-24qxff-Uzt0747LJ?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1vRMPralT98ORdev-24qxff-Uzt0747LJ?usp=sharing</a></p>
<p>I’m just a random guy who got an MRI of my head, I’m sorry if this is too basic. Thank you.</p>

---

## Post #2 by @Alex_Vergara (2020-11-02 10:17 UTC)

<p>png are stored in RGB color space (3 images one for each color), when you load the png you need to convert to grayscale first. How did you plan to import your png in the first place?</p>

---

## Post #3 by @tomasb (2020-11-02 10:33 UTC)

<p>I follow this one minute video, step by step (<a href="https://www.youtube.com/watch?v=BcnpzYE8VO8" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=BcnpzYE8VO8</a>)</p>
<p>I get the 3D model but just one slice in particular gets this weird interlaced repetition pattern that you can see on the screenshot at the red panel (bottom left) and on the 3D model.</p>
<p>I tried with diferent segments of the sequence and it always happen at the same image, and there’s  nothing particularly different about it.</p>

---

## Post #4 by @lassoan (2020-11-02 14:54 UTC)

<p>All images in the stack must be the same. <code>image (12).png</code> has only 3 components (RGB) while all the others have 4 components (RGBA). It would have been nicer if ITK (image processing library that Slicer uses for image reading) rejected this data set instead of showing a corrupted image - I’ve filed a bug report for you (see <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/2086">here</a>).</p>
<p>To fix this problem, you need to save all the screenshots with the same settings (either RGB or RGBA works fine).</p>
<p>Note that 8-bit screenshots are not suitable for capturing CT data sets, as in the image that you get the noise is either magnitudes higher compared to the original 12-bit image, and/or details in high and/or low intensity regions are lost. You don’t have very accurate information on pixel size either.</p>
<p>Many of the web DICOM viewers do not allow export of the actual data set to “prevent” leaking of patient data without permission, but the study protocol should allow you to obtain properly anonymized data sets that are not compromised in image quality. It is worth going through the process of getting proper images, as any results that you get from such low-quality 8-bit screenshots will not be representative of the results that you could get from the actual clinical images. If you don’t have a study protocol set up for this project then you are probably better off with using data from open image databases.</p>

---
