# Segmentation Comparsion

**Topic ID**: 9467
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/segmentation-comparsion/9467

---

## Post #1 by @fkr (2019-12-10 19:59 UTC)

<p>Hi,</p>
<p>I need some help with the Segmentation Comparsion Module of SlicerRT. I have some dicoms with segmentations (10 per Dicom), that I want to compare to each other. The results I get from the Dice and Hausdorff tables are perfect for me, but due to the mass of data I need to automate it.</p>
<p>Is there a simple way in Python to do this? Similar to: <a href="https://discourse.slicer.org/t/hausdorff-distance-calculation-in-segmentcomparison-module/4300" class="inline-onebox">Hausdorff distance calculation in SegmentComparison module</a> maybe?</p>
<p>I just need to get the values of the dice score and hausdorff distance, so I can save them to a variable. The rest of the script should be no problem.</p>
<p>Maybe <a class="mention" href="/u/cpinter">@cpinter</a> can help?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @fkr (2019-12-10 22:09 UTC)

<p>Sorry, i meant this thread: <a href="https://discourse.slicer.org/t/distance-between-two-segments/4910/5" class="inline-onebox">Distance between two segments</a></p>

---

## Post #3 by @fedorov (2019-12-11 02:00 UTC)

<p><a href="https://plastimatch.org/plastimatch.html"><code>plastimatch dice</code></a> can be one way to batch it:</p>
<blockquote>
<p>The plastimatch  <em>dice</em>  compares binary label images using Dice coefficient, Hausdorff distance, or contour mean distance. The input images are treated as boolean, where non-zero values mean that voxel is inside of the structure and zero values mean that the voxel is outside of the structure.</p>
</blockquote>

---
