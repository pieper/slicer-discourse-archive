# How to create a new volume from pre-segmented slices?

**Topic ID**: 33750
**Date**: 2024-01-12
**URL**: https://discourse.slicer.org/t/how-to-create-a-new-volume-from-pre-segmented-slices/33750

---

## Post #1 by @andrade.pha (2024-01-12 12:03 UTC)

<p>Hello,</p>
<p>I performed segmentation on a volume of 100 DICOM images (CT), and now I would like to select and export only 25 specific slices that have already been segmented. Essentially, I want to have a new volume consisting of these 25 pre-segmented slices. The alternative (which I would prefer not to do) would be to select the ROI and then perform the entire segmentation process again. </p>
<p>Could someone help me with this? I appreciate it in advance.</p>

---

## Post #2 by @muratmaga (2024-01-12 19:34 UTC)

<p>You may want to try SplitVolume (part of the SegmentEditorExtraEffects extension) or MaskVolume. Split volume will reduce the volume to the minimum extend of the segmentation, whereas will keep the original sizes of the volume. But will contain only the contents of the segmentations.</p>

---

## Post #3 by @andrade.pha (2024-01-26 09:44 UTC)

<p>Hello, first of all, I would like to thank <a class="mention" href="/u/muratmaga">@muratmaga</a> for the quick response.<br>
I ended up not being able to use the paths you suggested.<br>
Nevertheless, I found a solution to do exactly what I wanted here: <a href="https://discourse.slicer.org/t/how-to-crop-a-segmented-volume/28742/2" class="inline-onebox">How to crop a segmented volume? - #2 by lassoan</a></p>
<p>Perhaps I didn’t express myself well regarding what I initially wanted to do.<br>
Once again, thank you for the response.</p>

---
