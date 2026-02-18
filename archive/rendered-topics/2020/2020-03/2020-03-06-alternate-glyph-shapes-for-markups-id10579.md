# Alternate glyph shapes for Markups?

**Topic ID**: 10579
**Date**: 2020-03-06
**URL**: https://discourse.slicer.org/t/alternate-glyph-shapes-for-markups/10579

---

## Post #1 by @stl (2020-03-06 23:31 UTC)

<p>Hi,</p>
<p>Right now in Slicer 4.11, there are two options for 3D Glyph Types: Sphere3D and Diamond3D.</p>
<p>Can someone point me in the right direction for how to add or for code that I could use to add more 3D shapes?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-03-07 22:01 UTC)

<p>Actually, there are many other shapes and they all show up in 3D. I agree that as of now they are not optimal, as their normal is set to a fixed RAS=(0,0,1) direction. It would make more sense if the normal would be set when the point is placed (e.g., it could be the slice, surface, or camera plane normal), or there could be a mode to orient the glyphs to always face the camera. Rather than just add some new sources Would you be interested in working on this? What would be the glyph shapes that you would like to have in 2D and 3D views?</p>

---

## Post #3 by @stl (2020-03-14 21:32 UTC)

<p>Sure, what would that involve?</p>
<p>I don’t need any particular shapes but would like to have a variety in one scene to represent different data sets.</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2020-03-16 16:11 UTC)

<p>I’ve checked VTK’s glyph filter, which is used for displaying the markers in 3D views and found that it is quite easy to add a new display mode, which orients glyphs to always face the camera. This will allow using all the “2D” shapes in 3D views, too. I’ll start the integration now, it will probably take 1-2 weeks (as this has to be merged into VTK first and then into Slicer).</p>
<p>VTK pull request: <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6586">https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6586</a><br>
Slicer pull request: <a href="https://github.com/Slicer/Slicer/pull/4736">https://github.com/Slicer/Slicer/pull/4736</a></p>

---

## Post #5 by @lassoan (2020-03-18 03:53 UTC)

<p>The changes have been merged and will be available in Slicer Preview Releases downloaded March 19 or later.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/987917ea16ce58a209b80d6f6d96f91f9cd6cd8e.jpeg" data-download-href="/uploads/short-url/lKQ13aNF8xmA467BDCPWJEDi99s.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/987917ea16ce58a209b80d6f6d96f91f9cd6cd8e_2_690x441.jpeg" alt="image" data-base62-sha1="lKQ13aNF8xmA467BDCPWJEDi99s" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/987917ea16ce58a209b80d6f6d96f91f9cd6cd8e_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/987917ea16ce58a209b80d6f6d96f91f9cd6cd8e_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/987917ea16ce58a209b80d6f6d96f91f9cd6cd8e_2_1380x882.jpeg 2x" data-dominant-color="9A9A9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 586 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @stl (2020-03-27 04:14 UTC)

<p>thank you! this worked well</p>

---

## Post #7 by @stl (2020-03-28 02:05 UTC)

<p>I did notice one thing that fix might have changed. Now the markups are present on every slice on the 2D views instead of only where they exist (i.e.: if you scroll through the dicom, the markups are on every slice). Would this be easy to fix?</p>

---

## Post #8 by @lassoan (2020-03-28 14:27 UTC)

<p>Nothing has changed related to visibility of markups in slice views. Maybe you have enabled “projection” in advanced display settings.</p>

---
