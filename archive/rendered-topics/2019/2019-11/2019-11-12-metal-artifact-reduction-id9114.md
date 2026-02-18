# Metal artifact reduction

**Topic ID**: 9114
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/metal-artifact-reduction/9114

---

## Post #1 by @labixin (2019-11-12 14:02 UTC)

<p>Hi all,</p>
<p>I want to register these two images. But the metal artifact is a bit heavy in the right one. (It’s because that patients had lead wire attached to their skin in order to mark the range of the breast.) Could I use any slicer module to reduce the artifact? Or are there any methods?</p>
<p>Hope for some suggestions. Thank a lot!</p>
<p>Crayon</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcc7e6402f8047df7108d0f42e804e0e540edfa7.jpeg" data-download-href="/uploads/short-url/vv7kdeI8DqIfdrFpZm28mvMEso7.jpeg?dl=1" title="artifact" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcc7e6402f8047df7108d0f42e804e0e540edfa7_2_690x463.jpeg" alt="artifact" data-base62-sha1="vv7kdeI8DqIfdrFpZm28mvMEso7" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcc7e6402f8047df7108d0f42e804e0e540edfa7_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcc7e6402f8047df7108d0f42e804e0e540edfa7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcc7e6402f8047df7108d0f42e804e0e540edfa7.jpeg 2x" data-dominant-color="403E3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">artifact</span><span class="informations">818×550 92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-11-12 18:46 UTC)

<p>Most registration algorithms can take optional image mask(s) as input to specify which regions of the image they can take into account for the registration. You can create a mask using Segment editor module where the additional wires are excluded. You may need to export your segment to a labelmap volume (right-click in Data module) to be able to use it as a mask in a registration module.</p>

---
