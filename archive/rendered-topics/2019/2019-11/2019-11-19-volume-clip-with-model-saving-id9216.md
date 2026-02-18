# Volume clip with model saving

**Topic ID**: 9216
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/volume-clip-with-model-saving/9216

---

## Post #1 by @keesh (2019-11-19 13:19 UTC)

<p>Hello,<br>
I using 3D Slicer 4.10.2 to crop a CT abdominal Nifti volume for testing a deep learning model.<br>
I have downloaded and installed the VolumeClip extension.<br>
I select some options like Outside fill value = -1000, etc.<br>
After clipping my input Nifti volume, to my heart’s content, I now wish to save it.<br>
I then save 6 files, including the Nifti volume.<br>
However, after I import the clipped Nifti volume into Fiji (Image/J),<br>
the volume appears to be the original Nifti volume?<br>
Is there any method to save the actual clipped volume in Nifti format?<br>
thx e.-</p>

---

## Post #2 by @lassoan (2019-11-19 13:28 UTC)

<p>Saved files contain what you see on screen. Normally you would have two volumes saved: the original and the clipped (same extents as the original, just some area blanked out).</p>
<p>If you want more elaborate tools for blanking out image regions, you can use Segment Editor module and “Surface cut” and “Mask volume” effects (provided by SegmentEditorExtraEffects extension).</p>
<p>If you want to reduce the image extents instead of blanking out regions then you can use Crop Volume module.</p>

---
