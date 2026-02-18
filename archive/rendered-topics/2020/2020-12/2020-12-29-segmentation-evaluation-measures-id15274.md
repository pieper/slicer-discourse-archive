# Segmentation Evaluation Measures

**Topic ID**: 15274
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/segmentation-evaluation-measures/15274

---

## Post #1 by @Ester_RG (2020-12-29 15:18 UTC)

<p>Hi there! I’m an university student and I’m struggling with the following topic.<br>
I’m triying to compare Otsu’s method segmentation and Watershed algorithm segmentation results to a ground thruth as reference (in this case, I will consider the one obtained with GrowCut algorithm) made on CT images… The measures that I would like to know for the evaluation framework mainly are: accuracy, precision and efficiency.</p>
<p>Does anyone know some extension which can calculate these? In negative case, I would like to know other alternatives with examples, if it’s possible, for a better understanding.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-12-29 19:17 UTC)

<p>Global thresholding (Otsu or any other method) is so much worse than seed-based methods (Grow from seeds, Watershed, Fast marching) that it is not even a fair comparison.</p>
<p>How do you define “accuracy, precision, and efficiency” for segmentations?</p>
<p>If you don’t have a clinical evaluation criteria then you may use 95% Hausdorff distance for comparing segmentations. Dice coefficient is also commonly used because it is easy to compute, but it does not provide generally meaningful values (as the metric value highly depends on segment shape and can grossly over/underestimate the error). You can compute these using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison">Segment Comparison module</a> in SlicerRT extension.</p>

---
