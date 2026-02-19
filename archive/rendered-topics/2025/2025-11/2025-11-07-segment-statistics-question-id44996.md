---
topic_id: 44996
title: "Segment Statistics Question"
date: 2025-11-07
url: https://discourse.slicer.org/t/44996
---

# Segment Statistics Question

**Topic ID**: 44996
**Date**: 2025-11-07
**URL**: https://discourse.slicer.org/t/segment-statistics-question/44996

---

## Post #1 by @BennyShoe (2025-11-07 21:05 UTC)

<p>Hello,</p>
<p>I have a question about the Segment Statistics module. I am calculating volumes for multiple segments, but I am getting different sets of output values depending on the segment.</p>
<p>For some segments, I get the full set of values:</p>
<ul>
<li>
<p>Voxel Count</p>
</li>
<li>
<p>Volume (LM) [mm³]</p>
</li>
<li>
<p>Volume (LM) [cm³]</p>
</li>
<li>
<p>Surface Area (mm²)</p>
</li>
<li>
<p>Volume (CS) [mm³]</p>
</li>
<li>
<p>Volume (CS) [cm³]</p>
</li>
</ul>
<p>But for other segments, I only get:</p>
<ul>
<li>
<p>Voxel Count</p>
</li>
<li>
<p>Volume (mm³)</p>
</li>
<li>
<p>Volume (cm³)</p>
</li>
</ul>
<p>Is this normal? What determines whether the Surface Area and Closed Surface measurements appear? Does this mean that the volume values could be inaccurate? All of the data is processed the same way, so I am unsure why the output varies between segments.</p>
<p>Thank you!</p>

---

## Post #2 by @ebrahim (2025-11-09 21:28 UTC)

<p>Could it be that for some segments it fails to create a closed surface representation?</p>

---

## Post #3 by @BennyShoe (2025-11-12 16:11 UTC)

<p>I think that might be the case! Can you still create one after a segmentation has been made?</p>

---

## Post #4 by @Deep_Learning (2025-11-12 16:53 UTC)

<p>Are they really tiny?  Segmentation and closed surface representation are not related.</p>

---

## Post #5 by @BennyShoe (2025-11-12 17:19 UTC)

<p>Yes some some are very tiny while a few others are medium in size</p>

---

## Post #6 by @lassoan (2025-11-12 17:32 UTC)

<p>Very tiny segments (few voxels) may not be suitable to be reconstructed as a smooth 3D surface. These  segments will not have a closed surface representation and therefore <code>Volume (CS)</code> and <code>Surface Area</code> metrics sill not be computed.</p>
<p>Turning off surface smoothing will probably generate some blocky 3D objects, so you will see all the metrics. However, without surface smoothing the results are not meaningful, because you then don’t reconstruct the actual surface of the object but you just draw a brick at each sample point.</p>

---

## Post #7 by @pieper (2025-11-12 17:37 UTC)

<p>Note that if you really want to measure very small objects you should resample the segmentation so that you can represent them well.</p>

---

## Post #8 by @BennyShoe (2025-11-12 23:22 UTC)

<p>Is it possible to resample a segmentation that’s already been created, without having to redo the entire segmentation manually?</p>
<p>Thank you all for all the helpful responses!</p>

---

## Post #9 by @pieper (2025-11-12 23:40 UTC)

<p>Yes, you can resample after segmenting, but you won’t get the benefit since you’ve already lost the resolution.</p>

---

## Post #10 by @BennyShoe (2025-11-13 00:42 UTC)

<p>That makes sense! For my case, I’m not as concerned about recovering high resolution detail. I mainly care about getting an accurate volume measurement from the segmentation I already created. As long as resampling won’t meaningfully affect the volume values, I’m okay with the loss of fine resolution.</p>

---

## Post #11 by @pieper (2025-11-13 13:46 UTC)

<p>I think that’s the key point: the high resolution detail isn’t just to make the image look better, it’s a more faithful representation of the source object, so capturing the detail correlates with the accuracy of the volume measurement.</p>

---

## Post #12 by @Deep_Learning (2025-11-13 16:09 UTC)

<p>Segment Stats works!!! But, Fitting a surface to very small structures, such as coronary calcium, is not really feasible or worthwhile.  Voxel based methods are more appropriate.</p>

---
