# Cross-section analysis ImportError on Mac

**Topic ID**: 32849
**Date**: 2023-11-15
**URL**: https://discourse.slicer.org/t/cross-section-analysis-importerror-on-mac/32849

---

## Post #1 by @urethralking (2023-11-15 22:51 UTC)

<p>Hi everyone, I installed Slicer VMTK using the extensions module on my Mac M1 and successfully extracted a centerline of a urethra using the module. However, when I try to use Cross-section Analysis, I keep getting the following error:</p>
<p>“File “/Applications/Slicer.app/Contents/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-scripted-modules/CrossSectionAnalysis.py”, line 995, in updateOutputTable<br>
import vtkSlicerCrossSectionAnalysisModuleLogicPython as vtkSlicerCrossSectionAnalysisModuleLogic<br>
ImportError: Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython”</p>
<p>Under “Browse cross-sections”, for cross-section area I keep seeing 'N/A (input lumen not specified) even though I entered my segmentation as the input lumen surface.</p>
<p>I’ve successfully run Cross-section analysis on a Windows PC before and would appreciate help understanding why this error is occurring now. Thank you!</p>

---

## Post #2 by @lassoan (2023-11-15 22:52 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> can you help with this?</p>

---

## Post #3 by @chir.set (2023-11-16 09:59 UTC)

<aside class="quote no-group" data-username="urethralking" data-post="1" data-topic="32849">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/u/f04885/48.png" class="avatar"> urethralking:</div>
<blockquote>
<p>No module named vtkSlicerShapeModuleMRMLPython</p>
</blockquote>
</aside>
<p>The library ‘vtkSlicerShapeModuleMRMLPython’ is not being found while importing ‘vtkSlicerCrossSectionAnalysisModuleLogicPython’.</p>
<p>This means that your must install the ‘ExtraMarkups’ extension using the extensions manager; this extension provides the ‘vtkSlicerShapeModuleMRMLPython’ library.</p>
<p>It’s weird because ‘ExtraMarkups’ is a dependency of ‘SlicerVMTK’ and it is installed together with ‘SlicerVMTK’. Are you using an old version of ‘SlicerVMTK’ or an old version of Slicer itself? Try with the latest stable or preview versions.</p>

---

## Post #4 by @urethralking (2023-11-16 13:06 UTC)

<p>Thank you both so much! I was running the latest stable release (5.4.0) but the issue resolved when I switched to the preview (5.5.0).</p>

---
