# Filling up MRI missing voxels in cortical region

**Topic ID**: 8408
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/filling-up-mri-missing-voxels-in-cortical-region/8408

---

## Post #1 by @banikr (2019-09-12 17:26 UTC)

<p>Hello, I am using some MRI data that were used in Deep Brain Stimulation study. Now due to electrodes there are gaps in cortical section/skull in the images. Now for my purpose I would like to fill those missing skull sections and tissues with nearest/adjacent ones.<br>
How can I do that in slicer 3D?<br>
I am a beginner in 3D Slicer, would really appreciate the help.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2019-09-12 17:39 UTC)

<p>Normally you don’t need to create such “fake” images. Instead, you can check that the image processing operation that you use can accept a mask as input (e.g., it is very common for registration algorithms to allow mask images to constrain where image samples are taken from).</p>
<p>If you are sure you must create such modified images you can do the followings: Change voxel values in the electrodes area to some extremely low values (e.g., using Mask Volume effect provided by segmentEditorExtraEffects) then apply Median Image Filter with large enough neighborhood to fill all the blanks. After that, you can combine the original and hole-filled image using numpy as described <a href="https://discourse.slicer.org/t/how-to-stitch-together-two-sets-of-ct-slices-to-make-one-file/1197/11">here</a>.</p>

---
