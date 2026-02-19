---
topic_id: 8002
title: "Help With Segment Editor Sphere Brush"
date: 2019-08-13
url: https://discourse.slicer.org/t/8002
---

# Help with segment editor sphere brush

**Topic ID**: 8002
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/help-with-segment-editor-sphere-brush/8002

---

## Post #1 by @Roni (2019-08-13 15:05 UTC)

<p>Hi There,</p>
<p>I am trying to use the spere brush option for thresholded segmentation in “segment editor” module.<br>
specifications:</p>
<p>Slicer version: 4.10.2<br>
OS: windows<br>
Data : 3D (dicom2nii converted)<br>
Expected behaviour: using one step of paint along with sphere brush, to segment a structure from all slices.(Expect volume filled with label number in Y and G view panel)<br>
Actual behaviour: sphere brush functanality does not work for entire volume. Paint is only applied on single slice.(check Y and G view panel)</p>
<p>Any guidance or help is really helpful. I have tried to follow the youtube tutorial<br>
<a href="https://www.youtube.com/watch?v=55cqpl8_b8c" rel="noopener nofollow ugc">segment editor Tutorial</a><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eee553fab12c414a85dcb21a562a0094fa834959.png" data-download-href="/uploads/short-url/y5mYcERKoY0SBTaRngWopGXjbkZ.png?dl=1" title="3d%20slicer%20brush" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee553fab12c414a85dcb21a562a0094fa834959_2_690x419.png" alt="3d%20slicer%20brush" data-base62-sha1="y5mYcERKoY0SBTaRngWopGXjbkZ" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee553fab12c414a85dcb21a562a0094fa834959_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee553fab12c414a85dcb21a562a0094fa834959_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eee553fab12c414a85dcb21a562a0094fa834959_2_1380x838.png 2x" data-dominant-color="6B6C72"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d%20slicer%20brush</span><span class="informations">1915×1164 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-08-13 15:19 UTC)

<p>Looks like the brush radius is smaller than the slice spacing.  What happens if you use a bigger radius?</p>

---
