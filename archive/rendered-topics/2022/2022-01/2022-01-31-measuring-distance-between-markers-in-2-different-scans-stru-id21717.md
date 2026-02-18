# Measuring distance between markers in 2 different scans, struggling with transform because of unknown segment origins?

**Topic ID**: 21717
**Date**: 2022-01-31
**URL**: https://discourse.slicer.org/t/measuring-distance-between-markers-in-2-different-scans-struggling-with-transform-because-of-unknown-segment-origins/21717

---

## Post #1 by @tbmeier (2022-01-31 19:01 UTC)

<p>I have MRI scans of the knee (femur and tibia) and I am looking to compare the position of fiducials on the skin  with respect to the bone between 2 different scans. I have segmented each bone in both scans, and then I start a new Slicer scene, upload 2 segmentation (ex. tibia1(before movement) and tibia2(after movement). I manually align the tibia’s using the Transforms module, then I need to measure the distance (3D) between the skin fiducials before movement and after movement. But when I try to export the transforms, and the fiducial positions from each respective scan, the results don’t match the visuals. It seems like the global coordinate system in each original scan, is not the same at the segment coordinate system after I upload it separately. Is there something I am missing? Should I approach this problem differently? This seems like it should be a straight forward measurement!</p>

---

## Post #2 by @pieper (2022-01-31 22:27 UTC)

<p>It sounds like you didn’t export the transformed point.  You can use <code>Harden transform</code> in the context menu of the Transform hierarchy tab of the Data module. Or the button at the bottom of the Transforms module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d359f6d18aab61e8ecea7f0e75f9f15ad410b7d.png" alt="image" data-base62-sha1="6rWn5vpOCpbTr60IBXs3raZd0cJ" width="212" height="227"></p>

---

## Post #3 by @tbmeier (2022-02-02 14:37 UTC)

<p>The point/marker/fiducial that I want to transform is not saved with the segment, I think when I save the segment from the original scan I need to save it with the original as the same as the original scan. That would solve my problem!</p>

---

## Post #4 by @tbmeier (2022-02-02 17:32 UTC)

<p>I meant to say I need the segment coordinate system/origin to be the same in the original scan and when I export the segment and bring back only the segment.</p>

---

## Post #5 by @tbmeier (2022-02-02 17:51 UTC)

<p>I think I found the answer here !! <a href="https://discourse.slicer.org/t/how-to-provide-global-coordinate-system-after-crop-volume-segment/1199/2" class="inline-onebox">How to provide global coordinate system after crop volume segment? - #2 by lassoan</a></p>

---
