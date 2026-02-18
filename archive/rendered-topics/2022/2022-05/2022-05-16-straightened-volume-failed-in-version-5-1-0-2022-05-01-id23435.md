# Straightened volume failed in version 5.1.0-2022-05-01

**Topic ID**: 23435
**Date**: 2022-05-16
**URL**: https://discourse.slicer.org/t/straightened-volume-failed-in-version-5-1-0-2022-05-01/23435

---

## Post #1 by @chendong9416 (2022-05-16 06:21 UTC)

<p>Recently, i made an update for 3D slicer to version 5.1.0-2022-05-01, and used open curve module to for a center line for the aorta, then i used curved planar reformat to form a straightened volume base on the open curve, but it turned with grey without any true imaging, is there a bug for the module in this new version? how can i deal with it ? thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/297f6be953de17c5a1eefbba5fed1ee8adc31c6d.png" data-download-href="/uploads/short-url/5V6zGOMDCQDcbTCXfmD9Grk2jGB.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/297f6be953de17c5a1eefbba5fed1ee8adc31c6d_2_690x359.png" alt="1" data-base62-sha1="5V6zGOMDCQDcbTCXfmD9Grk2jGB" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/297f6be953de17c5a1eefbba5fed1ee8adc31c6d_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/297f6be953de17c5a1eefbba5fed1ee8adc31c6d_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/297f6be953de17c5a1eefbba5fed1ee8adc31c6d_2_1380x718.png 2x" data-dominant-color="9F9FA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1919×1001 66.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-05-16 21:22 UTC)

<p>I’ve just tested this on an aortic arch CT using Slicer-5.1.0-2022-05-08 on Windows and everything worked well.</p>
<p>Maybe you just need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level">adjust the window/level setting</a>.</p>

---

## Post #3 by @chendong9416 (2022-05-16 22:28 UTC)

<p>it not the window/setting issue, another thing different is the resolution of tgis CTA is 1.25mm, i usually works with 0.625mm, it this a potential problem?</p>

---

## Post #4 by @lassoan (2022-05-17 00:10 UTC)

<p>That spacing difference is not that big, it should not cause any problem. Do you find that the module works with most CTs but not with a specific one?</p>
<p>Maybe the problematic CT has non-uniform spacing and so an acquisition transform is applied on import. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">Hardening the transform on the volume</a> will resolve this problem.</p>

---

## Post #5 by @chendong9416 (2022-05-17 03:15 UTC)

<p>The module does not work with other CTA, but these problems solved automaticly when i made an update to version 5.1.0-2022-05-14, thanks for your advice anyway.</p>

---
