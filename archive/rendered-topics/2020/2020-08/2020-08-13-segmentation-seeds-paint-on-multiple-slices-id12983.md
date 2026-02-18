# Segmentation seeds paint on multiple slices

**Topic ID**: 12983
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/segmentation-seeds-paint-on-multiple-slices/12983

---

## Post #1 by @epearlstone (2020-08-13 18:05 UTC)

<p>Operating system: mac<br>
Slicer version: 4.11<br>
Expected behavior: When using paint to mark a segment in segment editor only one slice should have that painted. That mark will appear only on the edited slice until ‘grow from seed’ is initialized and all slices containing the painted object are highlighted.<br>
Actual behavior: Seed bleeds through to other slices (before pressing grow from seed).</p>
<p>The same also applies for erasing part of a segmentation. So erasing part of a segment on one slice will affect other slices.</p>
<p>Can someone please help me fix this?</p>

---

## Post #2 by @lassoan (2020-08-13 18:06 UTC)

<p>Probably you paint on oblique slices. See more information and solutions here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---

## Post #3 by @epearlstone (2020-08-13 18:17 UTC)

<p>I’ve been using the same DICOM files / slices that I’ve used to make other models. Something has changed but I’m not sure.</p>

---

## Post #4 by @lassoan (2020-08-13 18:24 UTC)

<p>Can you post a screenshot?</p>

---

## Post #5 by @epearlstone (2020-08-13 18:32 UTC)

<p>It seems to have stopped but I’m not sure why.<br>
My problem was this: I paint a segment on one slice. That colored painted segment appears on the next slice, following (changing in size and position) the threshold of the object it was painted on in the original slide. My segmentation settings were all set to default.</p>

---

## Post #6 by @lassoan (2020-08-13 18:40 UTC)

<p>If slice view is aligned with volume axes then the only reason you may not paint on the currently visible slice is that you are exactly at the border between two slices (you can confirm this if you enable slice intersection display, disable image interpolation, and you zoom in the slice view a lot).</p>
<p>Solution: You can easily reposition slice views by moving the mouse in a slice view while holding down Shift key.</p>
<p>In previous Slicer versions, when you moved the slice offset slier all the way to one direction then it positioned the slice view at the border between two slices, so you could end up with not seeing what you were drawing. We have changed this behavior a couple of days ago - now if you move the slice offset slider to min/max value then you’ll be centered on the slice, so you should not have such issues.</p>

---

## Post #7 by @epearlstone (2020-08-13 19:00 UTC)

<p>My slice view was not aligned with my volume axes. Aligning them stopped the problem. Thank you for your help!</p>

---
