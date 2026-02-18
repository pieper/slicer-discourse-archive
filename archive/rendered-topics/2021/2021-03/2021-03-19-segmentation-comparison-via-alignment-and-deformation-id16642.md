# Segmentation Comparison via alignment and deformation

**Topic ID**: 16642
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/segmentation-comparison-via-alignment-and-deformation/16642

---

## Post #1 by @reddington.15 (2021-03-19 15:25 UTC)

<p>Hi,</p>
<p>I have been working on segmenting the pelvis from a pre-CT scan and then a post CT scan with a fracture. I have both of the segmentations in the same window in Slicer and I have been able to transform the pre-CT on top of the post CT by using the IGT-Fiducials Registration Wizard. However, I want to measure how well these 2 structures are aligning and if there is any deformation/rotation in the axis of these 2. Is there any way that I can easily measure the deformation between these 2 segmentations now that I have them overlapping each other? I hope this makes sense that you are able to help.</p>
<p>Thanks!</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-03-21 12:56 UTC)

<p>One option is to use SegmentComparison module in the SlicerRT extension</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison</a></p>

---

## Post #3 by @reddington.15 (2021-03-22 12:53 UTC)

<p>Yes I have used that. Is there anyway I can measure deformation between the points I have selected on the pre CT vs. the post CT?</p>

---

## Post #4 by @reddington.15 (2021-03-22 12:55 UTC)

<p>I want to measure how the orientation could be different from the pre to post CT, if that makes sense.</p>

---

## Post #5 by @reddington.15 (2021-03-22 13:57 UTC)

<p>I know you aren’t a math professor, but how would one calculate the the translation magnitude or total rotation in degrees from the transformation matrix using linear algebra?</p>

---

## Post #6 by @lassoan (2021-03-24 17:39 UTC)

<p>Translation is not uniform across the image. You can convert the transform to a a displacement magnitude image (using Transforms module Convert section) and compute all the displacement statistics that you need from there. You can use Segment statistics module or get the voxels as a numpy array and compute anything you need using standard numpy functions.</p>
<p>You can compute rotation from the computed 4x4 homogeneous transformation matrix that is displayed in Transforms module. There are many parametrizations, such as variants of Euler angles.</p>

---

## Post #7 by @reddington.15 (2021-08-31 15:08 UTC)

<p>Hi Andras,</p>
<p>I am trying to use the convert section in the transforms module to compute the displacement statistics. Where can I access the data after I press convert? Nothing new pops up in the data window.</p>

---

## Post #8 by @lassoan (2021-08-31 19:25 UTC)

<p>A new volume or transform node should be generated that shows up in Data module. If you don’t see a new node then reason for the error is probably described in the application log.</p>

---
