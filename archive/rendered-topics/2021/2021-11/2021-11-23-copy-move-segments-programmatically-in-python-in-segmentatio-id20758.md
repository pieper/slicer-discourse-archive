# Copy/move segments programmatically in Python in Segmentations module

**Topic ID**: 20758
**Date**: 2021-11-23
**URL**: https://discourse.slicer.org/t/copy-move-segments-programmatically-in-python-in-segmentations-module/20758

---

## Post #1 by @nthach17 (2021-11-23 18:15 UTC)

<p>Slicer version: 4.11.20210226</p>
<p>Hello,</p>
<p>I’m writing a Python script for moving segments from a segmentation node to another. I looked up the source code and found that the function in C++ is <code>qSlicerSegmentationsModuleWidget::copySegmentBetweenSegmentations()</code>. However, the equivalent function in Python, i.e. <code>slicer.modules.segmentations.widgetRepresentation().CopySegmentBetweenSegmentations()</code> does not exist. Am I missing something?</p>

---

## Post #2 by @lassoan (2021-11-23 18:39 UTC)

<p>Module widget methods are not to be called from other modules or scripts. You need to <a href="https://github.com/Slicer/Slicer/blob/56ebd8ee84557fe0c67e9db8fe0ddd771d799751/Modules/Loadable/Segmentations/qSlicerSegmentationsModuleWidget.cxx#L799">dig one level deeper</a> and call <a href="http://apidocs.slicer.org/master/classvtkSegmentation.html#a001c13d90bea679cb7697e33e56b59e5">vtkSegmentation::CopySegmentFromSegmentation method</a> from Python.</p>

---

## Post #3 by @nthach17 (2021-11-23 18:58 UTC)

<p>It works now! Thank you for the quick response!</p>

---
