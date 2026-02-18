# Add labels/ inscription in the created segmentation/model

**Topic ID**: 4372
**Date**: 2018-10-12
**URL**: https://discourse.slicer.org/t/add-labels-inscription-in-the-created-segmentation-model/4372

---

## Post #1 by @katharina_hecker (2018-10-12 11:01 UTC)

<p>Hello everyone,<br>
I wanted to ask, if it is possible to create labels/inscriptions in the 3D view at the created models/ volume renderings? That would be really great!</p>
<p>Thanks for all your suggestions!</p>

---

## Post #2 by @lassoan (2018-10-12 13:05 UTC)

<p>You can export segmentation to labelmap (in Segmentations node), then go to Colors module to show color legend in 3D view:</p>
<ul>
<li>find the colormap generated for the exported labelmap node - it should be at the top, inside Segmentations section</li>
<li>scroll down to Scalar bar section and open it</li>
<li>enable “Use color names for labels”,</li>
<li>enable “Display scalar bar”</li>
<li>set “Format” to <code>%s</code>
</li>
<li>set “Maximum number of colors” and “Number of labels” to the number of segments + 1 (if you have 7 segments, set it to 8)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b32a43c8b44adfc5d2cd7e7fdf63a82d0db0d8.png" data-download-href="/uploads/short-url/sDtlV0ku3jSrrx7KUXdVi2bSSpO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8b32a43c8b44adfc5d2cd7e7fdf63a82d0db0d8_2_690x419.png" alt="image" data-base62-sha1="sDtlV0ku3jSrrx7KUXdVi2bSSpO" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8b32a43c8b44adfc5d2cd7e7fdf63a82d0db0d8_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8b32a43c8b44adfc5d2cd7e7fdf63a82d0db0d8_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8b32a43c8b44adfc5d2cd7e7fdf63a82d0db0d8_2_1380x838.png 2x" data-dominant-color="C7C7DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you want to mark place labels on segments then currently your only option is to add markup fiducials and edit their labels manually (in Markups module).</p>

---

## Post #3 by @katharina_hecker (2018-10-13 14:08 UTC)

<p>Thanks a lot Sir, this is a great option!</p>

---

## Post #4 by @lassoan (2018-10-13 14:27 UTC)

<p>I’ve also added an option to improve label placement, it’ll be available in nightly version from tomorrow. If you click “Center labels” checkbox then labels will be placed in the middle of each color swatch.</p>

---

## Post #5 by @katharina_hecker (2018-10-13 16:18 UTC)

<p>Thank you very much!!!</p>

---

## Post #6 by @katharina_hecker (2018-10-16 09:49 UTC)

<p>Hello again,<br>
quick question: would it be possible to integrate the Screen Capture module in the nightly version, were the “Center labels” checkbox is now integrated? That would be nice so that you can create a video…</p>

---

## Post #7 by @lassoan (2018-10-16 14:05 UTC)

<p>There has been a <a href="https://discourse.slicer.org/t/2018-10-15-windows-nightly-build-unable-to-import-vtk/4403/3">temporary issue</a> in the nightly build. Screen Capture module should be available in tomorrow’s nightly build.</p>

---

## Post #8 by @katharina_hecker (2018-10-16 15:19 UTC)

<p>Thank you very much!</p>

---
