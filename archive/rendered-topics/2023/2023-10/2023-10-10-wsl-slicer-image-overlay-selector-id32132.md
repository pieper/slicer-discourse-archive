---
topic_id: 32132
title: "Wsl Slicer Image Overlay Selector"
date: 2023-10-10
url: https://discourse.slicer.org/t/32132
---

# WSL Slicer image overlay selector

**Topic ID**: 32132
**Date**: 2023-10-10
**URL**: https://discourse.slicer.org/t/wsl-slicer-image-overlay-selector/32132

---

## Post #1 by @IVarha (2023-10-10 10:35 UTC)

<p>I am trying to select overlay between images on WSL, hovewer the selector does not work for me<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d2ad55f6b2d9d3383e33f144ce141a29fb4872d.png" data-download-href="/uploads/short-url/4a1CfCjfMadGVwgb2lLWAO6hTvT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d2ad55f6b2d9d3383e33f144ce141a29fb4872d_2_690x127.png" alt="image" data-base62-sha1="4a1CfCjfMadGVwgb2lLWAO6hTvT" width="690" height="127" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d2ad55f6b2d9d3383e33f144ce141a29fb4872d_2_690x127.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d2ad55f6b2d9d3383e33f144ce141a29fb4872d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d2ad55f6b2d9d3383e33f144ce141a29fb4872d.png 2x" data-dominant-color="6F6466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">728×135 8.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system: Windows / WSL Fedora /WSL ubuntu<br>
Slicer version: 5.4<br>
Expected behavior: I am able to overlay two images in slicer<br>
Actual behavior: selector for second image don’t work</p>

---

## Post #2 by @lassoan (2023-10-10 10:36 UTC)

<p>You need to click the small double-arrow button in the popup to choose a foreground volume.</p>

---

## Post #3 by @IVarha (2023-10-10 10:37 UTC)

<p>The problem is that it is unclickable there</p>

---

## Post #4 by @lassoan (2023-10-10 10:39 UTC)

<p>You can use View Controllers module then.</p>

---

## Post #5 by @IVarha (2023-10-10 10:46 UTC)

<p>Thanks that solution works for my case</p>

---

## Post #6 by @lassoan (2023-10-10 10:54 UTC)

<p>Now that the error cause of this problem is most likely WSLg’s limited support for scaling - see for example <a href="https://github.com/microsoft/wslg/issues/388" class="inline-onebox">HiDPI Scaling · Issue #388 · microsoft/wslg · GitHub</a></p>
<p>Your may be able to fix it by enabling/disabling scaling in the operating system and/or in the application.</p>

---
