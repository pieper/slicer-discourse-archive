---
topic_id: 3543
title: "Dose Volume Histogram Comparison"
date: 2018-07-20
url: https://discourse.slicer.org/t/3543
---

# Dose Volume Histogram Comparison

**Topic ID**: 3543
**Date**: 2018-07-20
**URL**: https://discourse.slicer.org/t/dose-volume-histogram-comparison/3543

---

## Post #1 by @aseman (2018-07-20 18:44 UTC)

<p>Hi 3D slicer experts:<br>
I want to compare two DVH curves in one diagram .I created DVHs with Dose Volume Histogram module , then   I used  the DVH Comparison module , but it doesn’t show the second DVH for me. how I can see them simultaneously in one diagrame?<br>
thanks</p>

---

## Post #2 by @cpinter (2018-07-20 19:12 UTC)

<p>Dose Comparison only gives you quantitative comparison results. If you want to see DVHs in the same graph, then you need to do it in the Dose Volume Histogram module. Just calculate one set of DVHs (DoseVolume1 with StructureSet), then the second set (DoseVolume2 with StructureSet), and click the Show all button. All DVHs should show up, the ones belonging to DoseVolume2 with dashed lines to be able to differentiate.</p>
<p>Hope this helps!</p>

---

## Post #3 by @PaoloZaffino (2019-02-20 21:44 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>, can I ask how the DVHs are compared?<br>
What is that percentage I get?</p>
<p>Thank you!<br>
Paolo</p>

---

## Post #4 by @cpinter (2019-02-20 23:04 UTC)

<p>The percentage is the pass rate of the 1D gamma comparison algorithm, which is the same as the gamma you use to compare dosimetry measurements on films (2D) or gels (3D).</p>
<p>There is a detailed description in the documentation of the function, see <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/Logic/vtkSlicerDoseVolumeHistogramComparisonLogic.h#L48-L55" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/Logic/vtkSlicerDoseVolumeHistogramComparisonLogic.h#L48-L55</a><br>
It references a paper (Ebert et al. 2010) that you can read if you want more details.</p>

---
