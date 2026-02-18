# Extension manager for the sake of deep learning

**Topic ID**: 12015
**Date**: 2020-06-14
**URL**: https://discourse.slicer.org/t/extension-manager-for-the-sake-of-deep-learning/12015

---

## Post #1 by @khikho (2020-06-14 09:57 UTC)

<p>hi<br>
Is there Extension manager for the sake of deep learning?</p>

---

## Post #2 by @lassoan (2020-06-14 14:58 UTC)

<p>3D Slicer (and its extensions) is a great tool for creating, evaluating, and deploying machine learning models for medical imaging applications, and can be used with any deep learning toolkits (Keras, PyTorch, TensorFlow, NVidia Clara, etc.).</p>
<p>You can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Segment Editor</a> and various segmentation extensions (such as <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">SegmentEditorExtraEffects</a>, <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrap</a>, …).for creating training data set. For segmenting hundreds of data sets, you may find <a href="https://github.com/JoostJM/SlicerCaseIterator">CaseIterator extension</a> (for all kinds of 3D volumes), <a href="https://github.com/SlicerIGT/aigt">AIGT modules</a> (mainly for ultrasound images) useful.</p>
<p>For training and quick review of results, you can use Jupyter notebooks in Slicer, using <a href="https://github.com/Slicer/SlicerJupyter">SlicerJupyter extension</a>. Slicer allows both qualitative visual assessment using its sophisticated 3D visualization features and computation of quantitative metrics.</p>
<p>For deployment - to make your deep learning models easily accessible to clinical end users - you can use <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin">NVidia AIAA extension</a>, which makes NVidia Clara models directly in Slicer’s Segment Editor. You may also learn from some previous efforts, such <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DeepInfer">DeepInfer</a> and <a href="https://github.com/faustomilletari/TOMAAT-Slicer">TOMAAT</a>.</p>

---
