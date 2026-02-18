# Creation of a new module which contains a transparent adjustable overlay

**Topic ID**: 4183
**Date**: 2018-09-25
**URL**: https://discourse.slicer.org/t/creation-of-a-new-module-which-contains-a-transparent-adjustable-overlay/4183

---

## Post #1 by @katharina_hecker (2018-09-25 09:14 UTC)

<p>Hi everyone,<br>
I was wondering if it is possible to create a new module, which can load in the coronal window an transparent overlay, which is adjustable (stretchable…).</p>
<p>This overlay consists of several images which you could scroll through, when it is adjusted and locked in its position to the volume underneath.</p>
<p>To give you a more specific idea: This is for the purpose if you have f.ex.  fMRI images of the brain (which you load normally as a volume in the Slicer) and you want to lay an atlas as transparent overlay on it so that you can segment specific parts of the brain volume underneath with the aid of the atlas… you could scroll through the atlas and find the right slice and adjust it to the brain slice underneath).</p>
<p>I´m very curious if it would be technically possible in the 3D Slicer or whether some of you know a similar feature.<br>
Thanks a lot for all your inputs and your help!</p>

---

## Post #2 by @cpinter (2018-09-25 13:16 UTC)

<p>Instead of the overlay, I’d use the foreground layer for this. For scrolling through, you could put the atlas images into a sequence node (you’ll need the Sequences extension). To position the atlas you can add a parent transform to the atlas image and change the transform to align it.<br>
Just one thing that occurred to me because you want to use overlay: the atlas images are also 3D not 2D right?</p>

---

## Post #3 by @katharina_hecker (2018-09-25 13:18 UTC)

<p>Hi. thanks for the quick reply, the atlas is like the brain image stack in 2D Slices…</p>

---

## Post #4 by @lassoan (2018-09-25 20:37 UTC)

<p>This all sounds standard atlas-based segmentation.</p>
<p>Normally you register the atlas image to the anatomical image automatically, using intensity-based registration (for example, using SlicerElastix extension). If that does not work well (you only have segmentation and don’t have the corresponding atlas image that was segmented; or the atlas image is too different from your anatomical image) then you can register the atlas manually, by defining corresponding landmarks on the two volumes (for example using SlicerIGT extension’s Fiducial registration wizard module) - it supports, rigid, affine, and warping transform.</p>
<p>Once the global alignment of the images are done, you apply the transform to the segmentation. You can further tune the segmentation in Segment Editor module.</p>

---

## Post #5 by @katharina_hecker (2018-09-26 06:04 UTC)

<p>Thanks a lot for these information!<br>
I will try them out.</p>
<p>Just out of curiosity: is there a tool available or in progress, which can add buttons at the edges of a volumes so that you can dragg/stretch/adjust them faster than with the transforms module?<br>
Thank you for your understanding</p>

---

## Post #6 by @katharina_hecker (2018-09-26 08:27 UTC)

<p>quick update: I tried it with the foreground layer, but this volume is than not visible at all even when the visibility is changed. When I put the visibility of the atlas to 100% the other volume underneath is also not visible do you know  what could be the problem? the size I already adjusted with Fiji…</p>

---

## Post #7 by @katharina_hecker (2018-09-26 09:49 UTC)

<p>never mind i just managed it. there was a problem with the brightness and size…</p>

---

## Post #8 by @cpinter (2018-09-26 11:47 UTC)

<p>You can edit a transform in the 3D view by turning on “Visible in 3D view” in the Interaction subsection of the Display section in the Transforms module.</p>
<p>Can you please explain the project more? Answering to these individual questions is a bit like shooting in the dark. What exactly comprises the atlas? You said stack of 2D images, so OK, a 3D image. But is it only segmentation? Or what? If you attach screenshots that could also be helpful.</p>

---
