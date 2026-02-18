# converting model to binary label map creates artifacts 

**Topic ID**: 29879
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/converting-model-to-binary-label-map-creates-artifacts/29879

---

## Post #1 by @NahomKidane (2023-06-06 23:00 UTC)

<p>Hello,</p>
<p>I am trying to use the convert model to segmentation node but I get artifacts.  Any idea on how to correct this issue?<br>
Thank you!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6ae630d636dab5a722fdd8e8a47c1805a0a09db.png" alt="image" data-base62-sha1="wUHrj8BSj7rLQ9q0inMnH0QMi2n" width="168" height="164"></p>

---

## Post #2 by @lassoan (2023-06-06 23:04 UTC)

<p>Was the input model a closed surface?</p>
<p>There have been several projects using Slicer for orbital bone segmentation. You can find more information by <a href="https://discourse.slicer.org/search?expanded=true&amp;q=orbital%20bone">searching on this forum</a>. What is the approach that you are trying to implement?</p>

---

## Post #3 by @NahomKidane (2023-06-07 12:30 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> . Yes, the input was a closed surface of the orbital. I am trying to use the wrap solidify tool to create a closed surface after patching a fractured area with small patch surface. Hence combine two segmentations into one and then run the wrap tool to create a smooth surface.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bc66918dd453ffea9433fe97d53d4d635c1575f.png" alt="image" data-base62-sha1="6ffCG2SCp4xhku5ffveW16aETvx" width="476" height="302"></p>

---

## Post #4 by @lassoan (2023-06-07 13:03 UTC)

<p>You may be able to reconstruct the entire eye socket with wrap solidify effect, but if that is too hard then adding a patch manually could make sense. A segmentation’s binary labelmap representation may not be able to represent arbitrarily thin surface, so may you need to either make the surface thicker or <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">change the segmentation to have smaller voxel size</a>.</p>

---
