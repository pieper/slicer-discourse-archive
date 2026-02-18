# Changing image spacing of image segmentations

**Topic ID**: 42385
**Date**: 2025-03-31
**URL**: https://discourse.slicer.org/t/changing-image-spacing-of-image-segmentations/42385

---

## Post #1 by @jps (2025-03-31 18:13 UTC)

<p>Hello!</p>
<p>I mistakenly began segmenting on volumes without specifying the correct image spacing. Currently they are set to 1 mm and I learned how to change them to 0.002 mm by editing the volume properties.</p>
<p>How do I apply this to my segmentations? I have messed around with the specify geometry option with little success. Thank you!</p>

---

## Post #2 by @pieper (2025-03-31 18:29 UTC)

<p>Probably easiest is to export to labelmap, change the spacing, and then re-convert to segmentation.</p>

---

## Post #3 by @lassoan (2025-03-31 20:15 UTC)

<p>You can also apply and harden a scaling transform (linear transform with scaling factors in the first 3 values of the diagonal) to both your image and the segmentation.</p>
<p>Or, save the segmentation as .nhdr file and edit the spacing in the header using a text editor. The .nrrd file is not suitable for modification in a text editor, because it also contains binary data, which is often corrupted by text editors.</p>

---
