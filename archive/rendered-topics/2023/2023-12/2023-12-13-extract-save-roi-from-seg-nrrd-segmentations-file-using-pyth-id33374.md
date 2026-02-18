# Extract/Save ROI from seg.nrrd (segmentations file) using Python packages SimpleITK or Slicerio

**Topic ID**: 33374
**Date**: 2023-12-13
**URL**: https://discourse.slicer.org/t/extract-save-roi-from-seg-nrrd-segmentations-file-using-python-packages-simpleitk-or-slicerio/33374

---

## Post #1 by @Vishal_P (2023-12-13 00:40 UTC)

<p>Hello!</p>
<p>I have a .nii scan file and have successfully created segments, saving them in a .seg.nrrd file. My goal now is to extract ROIs based on label names and save them as new .nii files. To achieve this, I am exploring the use of SimpleITK and the SlicerIO package.</p>
<p>i want to perform the multiplication between an ROI mask (based on Label Name) and the original scan file, resulting in an extracted ROI region. without broadcast error or shape mismatch error.</p>
<p>and does the seg.nrrd file contain the voxels from scan file for each ROI or just ROI masks?</p>
<p>Thank You!</p>

---

## Post #2 by @muratmaga (2023-12-13 05:37 UTC)

<p>You mean you want to save the contents of each segment as a separate volume? If that’s the case, it is already available as part of the SegmentEditorExtraEffects extension It is called SplitVolume.</p>
<p>Once your subvolumes are added to your scene, you can save them in nifti or nrrd format…</p>

---

## Post #3 by @cpinter (2023-12-13 09:58 UTC)

<aside class="quote no-group" data-username="Vishal_P" data-post="1" data-topic="33374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vishal_p/48/6438_2.png" class="avatar"> Vishal_P:</div>
<blockquote>
<p>does the seg.nrrd file contain the voxels from scan file for each ROI or just ROI masks?</p>
</blockquote>
</aside>
<p>Just the masks. The files .seg.nrrd are labelmaps, 3D or 4D depending on whether there are overlapping segments. The content is only the segment binary labelmaps.</p>

---

## Post #4 by @Vishal_P (2023-12-27 23:42 UTC)

<p>should I utilize the SegmentEditorExtraEffects from the slicer API and use SplitVolume or is it included in the segment editor interface in the 3D Slicer application? is there a way to add SplitVolume to the effects section of the Segment Editor using 3D slicer startup code?</p>
<p>Thanks!</p>

---

## Post #6 by @Vishal_P (2023-12-27 23:44 UTC)

<p>my bad <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">, found SegmentEditorExtraEffects  in extensions manager.</p>
<p>Thank you!</p>

---
