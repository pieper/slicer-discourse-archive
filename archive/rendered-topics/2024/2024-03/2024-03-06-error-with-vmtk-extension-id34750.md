# Error with vmtk extension

**Topic ID**: 34750
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/error-with-vmtk-extension/34750

---

## Post #1 by @Paula_Feldman (2024-03-06 20:10 UTC)

<p>the following shows up in the python interactor and I cannot use the extension from there, only through the GUI. I´m using the latest stable release</p>
<p>Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
[Qt]   Error(s):<br>
[Qt]     CLI executable: C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules/vtkvmtk.py<br>
[Qt]     The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[Qt] Fail to instantiate module  “vtkvmtk”<br>
[Qt] The following modules failed to be instantiated:<br>
[Qt]    vtkvmtk</p>

---

## Post #2 by @chir.set (2024-03-06 22:26 UTC)

<aside class="quote no-group" data-username="Paula_Feldman" data-post="1" data-topic="34750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paula_feldman/48/69587_2.png" class="avatar"> Paula_Feldman:</div>
<blockquote>
<p>[Qt] Fail to instantiate module “vtkvmtk”</p>
</blockquote>
</aside>
<p>This will persist in any Slicer version for now. It is harmless, don’t look at it.</p>
<aside class="quote no-group quote-modified" data-username="Paula_Feldman" data-post="1" data-topic="34750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paula_feldman/48/69587_2.png" class="avatar"> Paula_Feldman:</div>
<blockquote>
<p>Failed to load … …</p>
</blockquote>
</aside>
<p>This has been <a href="https://github.com/Slicer/Slicer/commit/9c875033632aea198791c0960310c165cad487c4" rel="noopener nofollow ugc">fixed</a>. These messages do not appear in the Slicer Preview download. They are are harmless too.</p>

---
