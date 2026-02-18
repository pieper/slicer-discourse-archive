# Registration MRI

**Topic ID**: 6775
**Date**: 2019-05-13
**URL**: https://discourse.slicer.org/t/registration-mri/6775

---

## Post #1 by @MSpindler (2019-05-13 12:54 UTC)

<p>Dear Slicer-Community,</p>
<p>I want to register a T2 MRI-image (showing only a middle part of the head) to a skullstripped T1 image of the whole brain of the same participant.<br>
I tried using General Registration (BRAINS) and Elastix, both without success.<br>
Maybe it doesnt work because Slicer cant find correct landmarks due to the skullstripping and the missing head parts?<br>
Do you know of another way to align these images?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/024336812da51c460061ff2574a5bd3f541a02a7.png" alt="alignment" data-base62-sha1="k0XoimuZwpP4cMVuQPNTGU2s7l" width="384" height="374"></p>
<p>Cheers<br>
Melanie</p>

---

## Post #2 by @lassoan (2019-05-13 16:14 UTC)

<p>Probably you need to crop the T1 image of the whole brain image (e.g., using Crop volume module) to contain approximately the same region as the partial T2 image.</p>

---

## Post #3 by @MSpindler (2019-05-20 09:16 UTC)

<p>Hmm, that doesnt work so well either, but thanks for the idea!<br>
I can align the images correctly using Coregistration in SPM12. However, I need to reslice the image for 3DSlicer to accept the reorientation. Without reslicing, the image is displayed as before. Do you know why that happens?<br>
I only want to register my images, without reslicing/resampling them.</p>

---

## Post #4 by @mangotee (2019-05-20 12:01 UTC)

<p>From my experience, if you use BRAINS registration, a cropped region of the head does not register well to a volume the overall head. By the way, this does not work well in ANTs either (both methods are ITK based). I have had success with BRAINS if you switch the role of “moving” and “fixed”, i.e. if you set the cropped volume to be the “fixed” volume and the whole head is the “moving” volume, it often works (not always though). Afterwards, you have to invert the resulting transform.<br>
I haven’t tried it in Elastix (also ITK-based), and it’s interesting to hear that it doesn’t work there either. I think that the problem lies in the base ITK classes that all these registration frameworks rely on - I assume that the moving volume gets resampled to the fixed volume (i.e. the cropped volume gets resampled into the whole-head fixed voxel-space) and there are a lot of “black regions” (all zeros) in the non-overlap regions. That would throw off the similarity functions if they wrongly assume those zero-voxels to be image intensities. The reason may be more complex though, I’m not familiar with the source-code of ITK.<br>
I also know that SPM (not ITK-based) handles this case gracefully. It would be interesting if this could be fixed in ITK eventually. It’s a limitation, especially because cropped volumes with limited overlap are a very common scenario in image registration. Sometimes, the inverse-transform trick (see above) works, but often enough, I need to solve this with a cumbersome workaround.</p>

---
