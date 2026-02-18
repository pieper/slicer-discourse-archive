# Creating .nrrd/.mha files from the sequence of tracked raw images for 3D reconstruction

**Topic ID**: 36316
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/creating-nrrd-mha-files-from-the-sequence-of-tracked-raw-images-for-3d-reconstruction/36316

---

## Post #1 by @Viktor_Sokolov (2024-05-22 10:20 UTC)

<p>Hi everyone,<br>
I want to do offline 3D reconstruction from parallel  ultrasound slices tracked by robotic arm encoders using <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationVolumeReconstructor.html" rel="noopener nofollow ugc">volume reconstructor application</a>. It requires the input sequence either in  .nrrd or .mha format, but I only have, for example, 1000 raw images (each image is an array 512x512) and corresponding  1000 positions of those slices in my world frame (array of doubles). Does anybody know any python library or other software which can help with such a task? I am a complete newbie in ultrasound acquisition and these file formats; so some links on how the data is organized in these file formats would also be helpful.</p>

---
