# Annotations in 3D slicer to prepare training datasets

**Topic ID**: 13528
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/annotations-in-3d-slicer-to-prepare-training-datasets/13528

---

## Post #1 by @Jigabytes (2020-09-17 13:57 UTC)

<p>Hi,Can we use 3D Slicer to do annotation on medical image slices and then prepare annotated data to build training data sets to build neural network from scratch? Can you point me to tutorial or example of it?</p>

---

## Post #2 by @lassoan (2020-09-18 00:21 UTC)

<p>This is probably one of the most common use cases of Slicer nowadays. See an overview of basic segmentation concepts <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a> and step-by-step tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>.</p>
<p>If you need to segment hundreds or thousands of data sets then it is probably worth setting up <a href="https://github.com/JoostJM/SlicerCaseIterator">Case iterator</a> (for single-click switch between data sets).</p>

---
