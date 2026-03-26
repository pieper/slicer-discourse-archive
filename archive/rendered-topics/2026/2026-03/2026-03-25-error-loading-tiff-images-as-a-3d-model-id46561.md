---
topic_id: 46561
title: "Error Loading Tiff Images As A 3D Model"
date: 2026-03-25
url: https://discourse.slicer.org/t/46561
---

# Error loading tiff images as a 3D model

**Topic ID**: 46561
**Date**: 2026-03-25
**URL**: https://discourse.slicer.org/t/error-loading-tiff-images-as-a-3d-model/46561

---

## Post #1 by @Varsha (2026-03-25 15:00 UTC)

<p>I am trying to load 15 tiff images which are basically images taken at different z slices and create a 3D model out of it. When I try doing this using the Image Stack option under Slicer Morph, the load button remains de-activated. Could anyone advise on what I might be doing wrong? Alternatively, when I try to load it using the ‘Add Data’ option, even though I de-select ‘Single output/ file’ and select ‘Volume’ option, I keep getting error messages of the kind shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b.png" data-download-href="/uploads/short-url/icagqqzJJQuAfKXN7pqh28BLF0f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_352x500.png" alt="image" data-base62-sha1="icagqqzJJQuAfKXN7pqh28BLF0f" width="352" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_352x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_528x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f872e9a69b271cd0682459a53310100683dc08b_2_704x1000.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">864×1227 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf99477a5236dfba4a5305288c77c2e899b82085.png" data-download-href="/uploads/short-url/rkXAXdbVngcnv26BgiJzIUg98BT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf99477a5236dfba4a5305288c77c2e899b82085.png" alt="image" data-base62-sha1="rkXAXdbVngcnv26BgiJzIUg98BT" width="690" height="345" data-dominant-color="E2E0E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">930×466 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea why this might be happening?</p>

---

## Post #2 by @muratmaga (2026-03-25 15:38 UTC)

<ol>
<li>Upgrade to the latest stable (5.10), you are using and unmaintained version of Slicer.</li>
<li>Copy the files somewhere that’s not on Onedrive. Cloud synced folders can sometimes cause weird issues.</li>
</ol>
<p>If these don’t help, you need to share the dataset.</p>

---
