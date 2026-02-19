---
topic_id: 2447
title: "Color Module Continuous Display Is Greyed Out"
date: 2018-03-27
url: https://discourse.slicer.org/t/2447
---

# Color module: Continuous display is greyed out

**Topic ID**: 2447
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/color-module-continuous-display-is-greyed-out/2447

---

## Post #1 by @Matt (2018-03-27 22:06 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.90<br>
Expected behavior: Continuous display allows for direct manual manipulation/re-weighting of color maps<br>
Actual behavior: Functionality is inaccessible and tab is grey in the color module.</p>

---

## Post #2 by @lassoan (2018-03-27 22:08 UTC)

<p>Built-in colormaps are not editable. Click on “Copy” button to create an editable copy.</p>

---

## Post #3 by @Matt (2018-03-28 00:49 UTC)

<p>Hi Andras,</p>
<p>I agree with you, however, your description of functionality doesn’t seem to work either.</p>
<p>Please see attached.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/6/665978d4b0d53e05c3468472684319cfa4d42e01.jpg" data-download-href="/uploads/short-url/eBqotOg0ltg9jkZC2lrKiunNIf7.jpg?dl=1" title="slicerdisplayexample.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/665978d4b0d53e05c3468472684319cfa4d42e01_2_690x371.jpg" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/665978d4b0d53e05c3468472684319cfa4d42e01_2_690x371.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/665978d4b0d53e05c3468472684319cfa4d42e01_2_1035x556.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/665978d4b0d53e05c3468472684319cfa4d42e01_2_1380x742.jpg 2x" data-dominant-color="696870"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerdisplayexample.jpg</span><span class="informations">1921×1035 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-03-28 01:34 UTC)

<p>I’ve just tested and it works well for me. To change a color, double-click the small colored square in Color column of the table.</p>

---

## Post #5 by @Matt (2018-03-28 02:34 UTC)

<p>Is there a way to help me to use the continuous display to change the colours? Changing them box by box is not very practical.</p>
<p>I’ve installed the nightly build, the stable build and even done this on another machine. Continuous display does not work.</p>
<p>What’s the new catch? I’ve used this lots in the past.</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2018-03-28 03:35 UTC)

<p>If you want to place points to arbitrary locations then you need to select a procedural color node as a basis, such as “RedGreenBlue”.</p>
<p>In the latest nightly builds, the displayed range is smaller than the full range of the colormap by default. This will be fixed in the release that you download Thursday or later. Until then you need to adjust the sliders below the colormap to see the full range.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a8a749a413b00899e15460e6e52b98eb0474016.png" data-download-href="/uploads/short-url/3MN3kwB8ypiaiKHmp3G44zpEDv8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8a749a413b00899e15460e6e52b98eb0474016_2_439x500.png" alt="image" data-base62-sha1="3MN3kwB8ypiaiKHmp3G44zpEDv8" width="439" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8a749a413b00899e15460e6e52b98eb0474016_2_439x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8a749a413b00899e15460e6e52b98eb0474016_2_658x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8a749a413b00899e15460e6e52b98eb0474016_2_878x1000.png 2x" data-dominant-color="C6E1D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">911×1036 41.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2018-03-29 03:56 UTC)

<p>3 posts were split to a new topic: <a href="/t/discourse-members-getting-unexpected-amount-of-email-notifications/2463">Discourse members getting unexpected amount of email notifications</a></p>

---
