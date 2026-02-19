---
topic_id: 26457
title: "Slicer 5 3 Preview Warnings And Error Messages"
date: 2022-11-27
url: https://discourse.slicer.org/t/26457
---

# Slicer 5.3 Preview warnings and error messages

**Topic ID**: 26457
**Date**: 2022-11-27
**URL**: https://discourse.slicer.org/t/slicer-5-3-preview-warnings-and-error-messages/26457

---

## Post #1 by @rbumm (2022-11-27 10:14 UTC)

<p>Testing the Lung CT Segmenter on Slicer 5.3 Preview (5.3.0-2022-11-25 r31426 / 0e36f10)<br>
I get all kinds of errors and warnings and the extension is practically unusable overnight.</p>
<p>My question is: How should we handle these errors and messages, many of them QT / VTK related? Should we work on this at all?</p>
<p>Manual lung segmentation (creating segmentation in the end):</p>
<pre><code class="lang-auto">Python 3.9.10 (main, Nov 25 2022, 23:30:04) [MSC v.1930 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
[Qt] QLayout::addChildLayout: layout "" already has a parent
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 1000 1
[Qt] qMRMLSegmentEditorWidget::setMasterVolumeNode is deprecated, use setSourceVolumeNode method instead.
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Segmentations\MRML\vtkMRMLSegmentEditorNode.h, line 175
[VTK] vtkMRMLSegmentEditorNode (000001E79EDC4EF0): vtkMRMLSegmentEditorNode::SetMasterVolumeIntensityMaskRange() method is deprecated, use SetSourceVolumeIntensityMaskRange method instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.h, line 355
[VTK] vtkSlicerMarkupsLogic (000001E78A8EF920): vtkSlicerMarkupsLogic::SetAllMarkupsLocked method is deprecated, please use SetAllControlPointsLocked instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 107
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A325C40): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A325C40): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A325C40): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A325C40): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A325C40): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A325C40): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A325C40): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 107
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A326EC0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 107
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A327EF0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialNode.h, line 126
[VTK] vtkMRMLMarkupsFiducialNode (000001E78A327EF0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead
self.extentGrowthRatio = 0.5
masterImageExtent = (0, 194, 0, 194, 0, 173)
labelsEffectiveExtent = (49, 156, 57, 132, 63, 141)
labelsExpandedExtent = [0, 194, 20, 169, 24, 173]
[VTK] Warning: In D:\D\P\S-0\Modules\Loadable\Segmentations\MRML\vtkMRMLSegmentEditorNode.h, line 175
[VTK] vtkMRMLSegmentEditorNode (000001E79EDC4EF0): vtkMRMLSegmentEditorNode::SetMasterVolumeIntensityMaskRange() method is deprecated, use SetSourceVolumeIntensityMaskRange method instead

</code></pre>

---

## Post #6 by @lassoan (2022-11-27 16:15 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="26457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I get all kinds of errors and warnings and the extension is practically unusable overnight.</p>
<p>My question is: How should we handle these errors and messages, many of them QT / VTK related? Should we work on this at all?</p>
</blockquote>
</aside>
<p>These are all warnings, not errors. You can ignore them, but since they are all deprecation warnings, at some points (within a few years) the deprecated methods will be removed and so it is recommended to fix them. It is also nice to fix these warnings to make other errors/warnings (that may indicate actual problems) easier to see.</p>
<p>Since I think the new methods are not available in Slicer-5.0.x, you can wait for the fix until Slicer-5.2 is released (in a few days). You can then create a 5.0 branch in your repository to archive the current module version of the code (that works with Slicer-5.0), and fix the deprecation warnings in your main branch (that works with Slicer-5.2 and later).</p>

---

## Post #7 by @rbumm (2022-11-27 18:35 UTC)

<p>How would I define the different branches to appear in the stores of 5.0 (archive) and 5.2 (stable) and 5.3 (preview)? I would like to support both stable and preview versions.</p>
<p>The 5.3 version already supports the SlicerTotalSegmentator call, which works great.</p>

---

## Post #8 by @lassoan (2022-11-27 19:08 UTC)

<p>ExtensionsIndex repository stores the branch (or tag) name for each Slicer version</p>
<ol>
<li>Create a 5.0 branch in your repository</li>
<li>Change the branch name in your s4ext file in the ExtensionsIndex repository’s 5.0 branch. (send a pull request or just write us here to change it for you)</li>
</ol>

---

## Post #9 by @rbumm (2022-11-27 19:42 UTC)

<p>“Lungmask” segmentation throws:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/rudol/Documents/MySlicerExtensions/SlicerLungCTAnalyzer/LungCTSegmenter/LungCTSegmenter.py", line 605, in runProcessing
    self.logic.applySegmentation()
  File "C:/Users/rudol/Documents/MySlicerExtensions/SlicerLungCTAnalyzer/LungCTSegmenter/LungCTSegmenter.py", line 1688, in applySegmentation
    inputVolumeSitk = sitkUtils.PullVolumeFromSlicer(self.inputVolume)
  File "C:\Users\rudol\AppData\Local\NA-MIC\Slicer 5.3.0-2022-11-26\bin\Python\sitkUtils.py", line 36, in PullVolumeFromSlicer
    sitkimage = sitk.ReadImage(myNodeFullITKAddress)
  File "C:\Users\rudol\AppData\Local\NA-MIC\Slicer 5.3.0-2022-11-26\lib\Python\Lib\site-packages\SimpleITK\extra.py", line 346, in ReadImage
    return reader.Execute()
  File "C:\Users\rudol\AppData\Local\NA-MIC\Slicer 5.3.0-2022-11-26\lib\Python\Lib\site-packages\SimpleITK\SimpleITK.py", line 5779, in Execute
    return _SimpleITK.ImageFileReader_Execute(self)
RuntimeError: Exception thrown in SimpleITK ImageFileReader_Execute: D:\a\1\sitk\Code\IO\src\sitkImageReaderBase.cxx:97:
sitk::ERROR: The file "slicer:000001B2EC1A8B20#vtkMRMLScalarVolumeNode1" does not exist.
</code></pre>
<p>in 5.3</p>

---

## Post #10 by @lassoan (2022-11-27 20:29 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> is this expected?</p>
<p>Can it be due to this extension using TotalSegmentator Python package, which uses SimpleITK, and TotalSegmentator is pip_installed with <code>--upgrade</code> option? Can we prevent pip to replace Slicer’s SimpleITK?</p>

---

## Post #11 by @jamesobutler (2022-11-28 03:06 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="26457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>My question is: How should we handle these errors and messages, many of them QT / VTK related? Should we work on this at all?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> There appears to be some confusion about where the log message originates. Where these aren’t all warnings in the core Qt or VTK toolkits, but rather in Qt and VTK based Slicer classes. So for example below the warning is not from QWidget, but qMRMLSegmentEditorWidget which is source contained in the Slicer repo. Should this log message be instead listed as <code>[Slicer]</code> or <code>[Slicer Qt]</code>? The example below is warning about a deprecated usage of Slicer code rather than pure Qt code.</p>
<blockquote>
<p>[Qt] qMRMLSegmentEditorWidget::setMasterVolumeNode is deprecated, use setSourceVolumeNode method instead.</p>
</blockquote>

---
